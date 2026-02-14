# OWASP Security Workbench — Speaker Cheat Sheet (1 Page)

Duration: 60 min  
Audience: Mixed (technical + non-technical)

---

## 1) Talk Track (time-boxed)

- **0:00–0:05** — Opening
  - “This is an OWASP Security Workbench built with Streamlit + CrewAI.”
  - “Goal: make security guidance usable during real code review workflows.”

- **0:05–0:12** — What it does + purpose
  - Browse OWASP Cheat Sheets and Top 10
  - Run AI-assisted code reviews with selected OWASP context
  - Generate Markdown reports for team workflows

- **0:12–0:20** — Tech + architecture
  - Streamlit UI, Firecrawl, parsing/modeling, cache, CrewAI workflows
  - Show architecture SVG

- **0:20–0:43** — Module walkthrough
  - `app.py` (UI/orchestration)
  - `src/config_manager.py` + `config.yaml`
  - `src/firecrawl_client.py`
  - `src/cheatsheet_parser.py` + `src/models.py`
  - `src/cache_manager.py`
  - `agents/*` workflows

- **0:43–0:56** — Live demo
- **0:56–1:00** — Close + Q&A

---

## 2) Key Message by Audience Type

- **Business/management:** faster and more consistent security-aware decisions
- **Developers:** practical OWASP context while reviewing PR diffs/files
- **Security/AppSec:** reusable guidance + structured outputs + traceable reports

---

## 3) Demo Script (quick commands + flow)

Start app:

```bash
streamlit run app.py
```

Demo flow:
1. Open Cheat Sheets section and select `Live OWASP (Firecrawl)`.
2. Show Overview + Risk Details + Risk Matrix.
3. Switch to Top 10 and show All Risks.
4. Open Code Review panel, upload/paste diff, run review.
5. Open Reports page and download generated report.

Optional local JSON generation:

```powershell
$env:CHEATSHEET_URL="https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html"
python agents/checksheet_crew/main.py

$env:TOP10_URL="https://owasp.org/Top10/2025/"
python agents/top10_crew/main.py
```

---

## 4) Must-Say Disclaimers

- AI review is **decision support**, not a guaranteed security audit.
- OWASP is the authoritative source; this app operationalizes it.
- Local JSON + cache support resilience when external services are slow/failing.

---

## 5) If You’re Running Late

- Skip parser internals and flow internals.
- Keep one full path: Cheat Sheets → Code Review → Reports.
- Move local generation commands to Q&A.

---

## 6) Common Q&A (short answers)

- **Does this replace human review?** No.
- **Can this be customized?** Yes, via configs/parsers/crew tasks.
- **What if APIs fail?** Use cache and local JSON modes.

---

## 7) Presenter Pointers

- Main guide: `PRESENTATION_GUIDE.md`
- Architecture image: `docs/images/architecture.svg`
- Main docs: `README.md` / `README.es.md`
