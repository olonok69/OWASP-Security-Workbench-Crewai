# OWASP Security Workbench — Guía de Presentación (1 hora)

Audiencia: Mixta (técnica + no técnica)  
Duración: máximo 60 minutos  
Formato: presentación en vivo + demo guiada

---

## 0) Objetivo de la sesión (qué debe llevarse la audiencia)

Al finalizar, la audiencia debe entender:
- Qué hace la aplicación y por qué existe
- Qué tecnologías la soportan
- Cómo contribuye cada módulo principal al flujo completo
- Cómo ejecutar y usar las funcionalidades clave (incluyendo review workflows)

---

## 1) Agenda (60 minutos)

- 0:00–0:05 — Apertura y contexto
- 0:05–0:12 — Qué hace la aplicación, propósito y valor
- 0:12–0:20 — Technology stack y overview de arquitectura
- 0:20–0:43 — Explicación módulo por módulo
- 0:43–0:56 — Demo en vivo de funcionalidades
- 0:56–1:00 — Cierre + Q&A

---

## 2) Script de apertura (0:00–0:05)

Talking points sugeridos:
- “Hoy voy a mostrar un OWASP Security Workbench construido con Streamlit y CrewAI.”
- “Centraliza exploración de guidance de seguridad y AI-assisted code review.”
- “Veremos propósito, arquitectura, módulos y una demo end-to-end.”

Contenido recomendado de slide:
- Nombre del proyecto
- Misión en una frase
- Agenda

---

## 3) Introducción: qué hace, propósito y tecnologías (0:05–0:20)

### 3.1 Qué hace la aplicación (0:05–0:09)

Capacidades principales:
- Explorar OWASP Cheat Sheets (live o local JSON)
- Explorar fuentes OWASP Top 10 (static/web/local)
- Ejecutar AI-assisted code reviews contra contexto OWASP seleccionado
- Generar reportes Markdown descargables

Value statement simple:
- “Reduce la fricción entre conocimiento de seguridad y decisiones de código seguro.”

### 3.2 Propósito y usuarios objetivo (0:09–0:12)

Propósito:
- Hacer guidance OWASP más accesible y operativo
- Soportar checks de seguridad pre-review más rápidos y consistentes

Usuarios principales:
- Developers y tech leads
- AppSec/security engineers
- Equipos que ejecutan workshops de secure SDLC

### 3.3 Tecnologías usadas (0:12–0:20)

Resumen de stack para presentación:
- UI: Streamlit
- Data/modeling: Pydantic, pandas, PyYAML
- Parsing: BeautifulSoup + lxml
- HTTP/reliability: httpx + tenacity
- Scraping source: Firecrawl API
- AI orchestration: CrewAI + tools
- Storage: local JSON + disk cache

Referencia visual:
- Architecture diagram en `docs/images/architecture.svg`

Visual de interacción de Agents/Crews:

![Interacción de Agents y Crews](docs/images/agents-crews-interaction.svg)

---

## 4) Explicación Módulo por Módulo (0:20–0:43)

Usa esta sección como walkthrough central. Mantén cada módulo en ~2–4 minutos.

### 4.1 UI y orquestación principal (`app.py`) (0:20–0:24)

Explica:
- Entry point único de Streamlit para todos los flujos de usuario
- Dos secciones principales: Cheat Sheets y Top 10
- Code Review panel compartido + viewer de reportes

Demo cue:
- Mostrar navegación por sidebar y cambio de secciones

### 4.2 Configuration Layer (`config.yaml`, `src/config_manager.py`) (0:24–0:27)

Explica:
- Carga de environment + YAML config
- API keys, comportamiento de cache, logging, rate limits
- Por qué importa: portabilidad y operación segura

Mensaje clave:
- “La config controla el comportamiento sin cambiar código.”

### 4.3 Data Acquisition (`src/firecrawl_client.py`) (0:27–0:30)

Explica:
- Integración con Firecrawl para live content scraping
- Retries y rate limiting
- Manejo de fallos

Mensaje clave:
- “El contenido externo se obtiene de forma confiable.”

### 4.4 Parsing y Domain Modeling (`src/cheatsheet_parser.py`, `src/models.py`) (0:30–0:34)

Explica:
- Transformación de contenido raw a modelos estructurados
- Risks, sections, mitigations, examples, metadata
- Schema consistente para rendering y local data interchange

Mensaje clave:
- “La estructura habilita automatización y consistencia.”

### 4.5 Caching Layer (`src/cache_manager.py`) (0:34–0:36)

Explica:
- Disk cache con TTL y límites de tamaño
- Mejor experiencia y menor consumo de API

Mensaje clave:
- “El cache es crítico para performance y estabilidad.”

### 4.6 Top 10 Data Handling (`owasp_llm/config.yaml`, `src/top10_data.py`) (0:36–0:38)

Explica:
- Opciones múltiples de data source (static/web/local)
- Fallback estático para LLM Top 10 y soporte local JSON

Mensaje clave:
- “Fuentes flexibles para demos, workshops y entornos con restricciones.”

### 4.7 AI Workflows (`agents/*`) (0:38–0:43)

Explica por función:
- `agents/checksheet_crew`: genera checksheet JSON desde URL
- `agents/top10_crew`: genera Top 10 JSON desde URL
- `agents/code_review_crew`: pipeline de review multi-agent
- `agents/code_review_flow`: routing SIMPLE vs COMPLEX

Mensaje clave:
- “Los crews convierten guidance en outputs accionables.”

---

## 5) Script de Demo en Vivo (0:43–0:56)

Objetivo: mostrar valor end-to-end sin exceder tiempo.

### Checklist de preparación (antes de la sesión)

- Virtual env activo y dependencias instaladas
- `.env` configurado con keys necesarias (`FIRECRAWL_API_KEY`, opcionalmente `OPENAI_API_KEY`, `SERPER_API_KEY`)
- App inicia correctamente con:

```bash
streamlit run app.py
```

- Tener lista una cheat sheet URL conocida
- Tener listo un sample diff

### Flujo de demo

#### Paso 1 — Abrir app y orientar audiencia (2 min)
- Mostrar sección Cheat Sheets vs Top 10
- Explicar navegación y opciones de data source

#### Paso 2 — Exploración Cheat Sheets (3 min)
- Seleccionar `Live OWASP (Firecrawl)`
- Abrir una cheat sheet
- Mostrar Overview + Risk Details + Risk Matrix

#### Paso 3 — Exploración Top 10 (2 min)
- Cambiar a sección Top 10
- Mostrar risks list y resources

#### Paso 4 — Ejecutar Code Review panel (4 min)
- Subir archivos o pegar PR diff
- Agregar prompt opcional
- Ejecutar review y mostrar reporte generado

#### Paso 5 — Mostrar lifecycle de reportes (2 min)
- Ir a Reports
- Abrir y descargar reporte Markdown

### Extensión opcional (si queda tiempo)

Mostrar generación de local JSON:

```powershell
$env:CHEATSHEET_URL="https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html"
python agents/checksheet_crew/main.py

$env:TOP10_URL="https://owasp.org/Top10/2025/"
python agents/top10_crew/main.py
```

Luego cambiar data source en la app a local JSON y cargar los archivos generados.

---

## 6) Speaker Notes para audiencia mixta

Estrategia de lenguaje:
- Primero framing de negocio, después detalle técnico
- Evitar detalles de implementación profunda salvo que pregunten
- Traducir términos técnicos a outcomes (velocidad, consistencia, trazabilidad)

Ejemplos:
- En vez de “Pydantic schemas”, decir “formato de datos estructurado y validado”.
- En vez de “tenacity retries”, decir “resiliencia automática ante fallos temporales”.

---

## 7) Preguntas comunes + respuestas sugeridas

### Q1: ¿Esto reemplaza el human code review?
R: No. Es decision support y aceleración de triage; no reemplaza criterio humano.

### Q2: ¿Qué pasa si fallan servicios externos?
R: La app soporta cache y local JSON workflows para seguir operando.

### Q3: ¿Esto es salida oficial de OWASP?
R: OWASP es la fuente autoritativa; la app facilita navegación y operacionalización.

### Q4: ¿Podemos customizarlo para nuestra política interna?
R: Sí, mediante config, lógica de parser y definición de agents/tasks en CrewAI.

---

## 8) Guardrails de tiempo (para no pasar de 1 hora)

Si te quedas sin tiempo:
- Omite internals de parser/cache
- Ejecuta un único camino completo: Cheat Sheets + Code Review
- Mueve comandos de generación local a Q&A

Si te sobra tiempo:
- Muestra el architecture SVG y mapea una acción de usuario end-to-end
- Muestra un archivo de config de Crew (`agents/*/config/*.yaml`) para explicar extensibilidad

---

## 9) Script de cierre (0:56–1:00)

Cierre sugerido:
- “Vimos cómo el workbench conecta guidance OWASP con workflows de review prácticos.”
- “El valor principal es acelerar decisiones de desarrollo con mayor consistencia de seguridad.”
- “El siguiente paso es un piloto con un equipo durante un sprint.”

Call to action:
- Seleccionar equipo piloto y ejecutar este flujo en un sprint.

---

## 10) Enlaces rápidos para el presentador

- Guía principal EN: `PRESENTATION_GUIDE.md`
- Documentación ES: `README.es.md`
- Architecture diagram: `docs/images/architecture.svg`
- App principal: `app.py`
- Módulos core: `src/`
- AI workflows: `agents/`
