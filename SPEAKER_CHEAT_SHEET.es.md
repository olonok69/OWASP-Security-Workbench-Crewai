# OWASP Security Workbench — Speaker Cheat Sheet (1 Página)

Duración: 60 min  
Audiencia: Mixta (técnica + no técnica)

---

## 1) Talk Track (con tiempo)

- **0:00–0:05** — Apertura
  - “Este es un OWASP Security Workbench construido con Streamlit + CrewAI.”
  - “Objetivo: usar guidance de seguridad en workflows reales de code review.”

- **0:05–0:12** — Qué hace + propósito
  - Explorar OWASP Cheat Sheets y Top 10
  - Ejecutar AI-assisted code reviews con contexto OWASP
  - Generar reportes Markdown para equipos

- **0:12–0:20** — Tech + arquitectura
  - Streamlit UI, Firecrawl, parsing/modeling, cache, CrewAI workflows
  - Mostrar architecture SVG

- **0:20–0:43** — Walkthrough por módulos
  - `app.py` (UI/orchestration)
  - `src/config_manager.py` + `config.yaml`
  - `src/firecrawl_client.py`
  - `src/cheatsheet_parser.py` + `src/models.py`
  - `src/cache_manager.py`
  - `agents/*` workflows

- **0:43–0:56** — Demo en vivo
- **0:56–1:00** — Cierre + Q&A

---

## 2) Mensaje clave por tipo de audiencia

- **Negocio/management:** decisiones más rápidas y consistentes con enfoque de seguridad
- **Developers:** contexto OWASP práctico durante review de PR diffs/files
- **Seguridad/AppSec:** guidance reutilizable + outputs estructurados + trazabilidad

---

## 3) Script de demo (rápido)

Iniciar app:

```bash
streamlit run app.py
```

Flujo de demo:
1. Abrir sección Cheat Sheets y elegir `Live OWASP (Firecrawl)`.
2. Mostrar Overview + Risk Details + Risk Matrix.
3. Cambiar a Top 10 y mostrar All Risks.
4. Abrir Code Review panel, subir/pegar diff y ejecutar review.
5. Ir a Reports y descargar reporte generado.

Opcional local JSON generation:

```powershell
$env:CHEATSHEET_URL="https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html"
python agents/checksheet_crew/main.py

$env:TOP10_URL="https://owasp.org/Top10/2025/"
python agents/top10_crew/main.py
```

---

## 4) Disclaimers obligatorios

- AI review es **decision support**, no una auditoría de seguridad garantizada.
- OWASP es la fuente autoritativa; la app operacionaliza ese contenido.
- Local JSON + cache aportan resiliencia cuando servicios externos fallan o son lentos.

---

## 5) Si vas tarde

- Omite internals de parser/flow.
- Mantén un único camino completo: Cheat Sheets → Code Review → Reports.
- Pasa comandos de generación local a Q&A.

---

## 6) Q&A común (respuestas cortas)

- **¿Reemplaza review humano?** No.
- **¿Se puede customizar?** Sí, con config/parsers/crew tasks.
- **¿Qué pasa si fallan APIs?** Se puede operar con cache y local JSON.

---

## 7) Referencias rápidas del presentador

- Guía completa EN: `PRESENTATION_GUIDE.md`
- Guía completa ES: `PRESENTATION_GUIDE.es.md`
- Architecture image: `docs/images/architecture.svg`
- Documentación base: `README.md` / `README.es.md`
