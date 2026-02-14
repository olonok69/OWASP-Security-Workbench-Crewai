def _normalize_risk_level(value):
    if value is None:
        return None

    text = str(value).strip().lower()
    if not text:
        return None

    # Common variants returned by LLMs
    if text in {"critical", "severe", "very high"}:
        return "high"
    if text in {"moderate", "med"}:
        return "medium"
    if text in {"minor"}:
        return "low"
    if text in {"none", "n/a", "na", "not_applicable", "not applicable", "unknown"}:
        return "low"

    if text in {"low", "medium", "high"}:
        return text

    return None


def security_review_output_guardrail(output):
    try:
        json_output = output if isinstance(output, dict) else output.json_dict
    except Exception as e:
        return (False, ("Error retrieving the `json_dict` argument: "
                        f"\n{str(e)}\n"
                        "Make sure you set the output_json parameter in the Task."
                        ))

    if json_output is None:
        return (False, "Guardrail received empty output JSON.")

    valid_risk_levels = ['low', 'medium', 'high']

    vulnerabilities = json_output.get('security_vulnerabilities', [])
    if vulnerabilities is None:
        vulnerabilities = []

    # Normalize each vulnerability risk level in-place
    risk_levels = []
    for vuln in vulnerabilities:
        risk_level = _normalize_risk_level(vuln.get('risk_level'))
        if risk_level is None:
            error_message = f"Invalid risk level: {vuln.get('risk_level')}"
            return (False, error_message)
        vuln['risk_level'] = risk_level
        risk_levels.append(risk_level)

    # Derive highest risk from vulnerabilities and auto-correct model output if needed
    derived_highest = 'low'
    if 'high' in risk_levels:
        derived_highest = 'high'
    elif 'medium' in risk_levels:
        derived_highest = 'medium'

    normalized_highest = _normalize_risk_level(json_output.get("highest_risk"))
    if normalized_highest is None:
        normalized_highest = derived_highest

    if normalized_highest not in valid_risk_levels:
        return (False, "Invalid highest risk level.")

    # Keep output consistent for downstream tasks
    json_output["highest_risk"] = derived_highest

    # If there are no vulnerabilities, keep a safe default
    if not vulnerabilities:
        json_output["highest_risk"] = "low"

    return (True, json_output)
