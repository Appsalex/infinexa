# AGENTS.md — Infinexa

Instrucciones para cualquier agente de IA (Claude Code, Antigravity, ChatGPT/Codex, Cowork, u otro) que trabaje sobre este repositorio. Léelo antes de modificar cualquier archivo.

## Qué es este proyecto

Infinexa (`infinexa.app`) es una plataforma educativa independiente sobre la evolución del dinero, blockchain, Web3, IA y nuevos modelos de creación de valor. Sitio estático Jekyll, desplegado vía GitHub Pages, dominio gestionado en Cloudflare. Repo público: `github.com/Appsalex/infinexa`.

## Antes de tocar nada — lee en este orden

1. `ESTADO.md` (raíz del repo) — **fuente única de verdad** del proyecto completo: historia, decisiones, fases ejecutadas, pendientes reales.
2. `_gestion/BITACORA.md` — registro cronológico de qué se hizo en cada sesión.
3. `_gestion/RECETAS.md` — prompts, reglas y checklists reutilizables (incluye reglas de prevención de bugs ya encontrados antes).
4. `_gestion/PROMPT_BLOG.md` y `_gestion/BLOG_GUIA.md`, si vas a tocar el blog.

No asumas nada del estado del proyecto sin confirmarlo en `ESTADO.md` primero — puede haber cambiado desde tu último contexto.

## Antes de empezar a trabajar

Corre y revisa:

```bash
git status
git log --oneline -10
git branch --show-current
```

Confirma árbol limpio, rama `main`, y que los últimos commits coinciden con lo que dice `ESTADO.md`. Si hay cambios sin commitear que no son tuyos, detente y confirma con Alejandro antes de continuar.

## Regla crítica — un solo agente escribe a la vez

Este repo puede estar conectado simultáneamente a varias herramientas (Claude Code, Antigravity, Cowork, ChatGPT/Codex). Para evitar sobrescribir cambios o trabajar sobre un estado intermedio:

- Nunca asumas que eres el único agente con acceso en vivo a este repo en este momento.
- Antes de cada commit, corre `git status`/`git diff` y revisa que los cambios son coherentes con lo que tú hiciste.
- Al terminar una tarea: commit + push a `main`, y actualiza `ESTADO.md`/`BITACORA.md` con lo que se hizo. Esa actualización es la que permite que la siguiente herramienta (sin importar cuál sea) retome el contexto sin repetir trabajo ni perderlo.

## ⚠️ Infraestructura — no tocar sin releer `ESTADO.md` sección 2

- El dominio raíz (`infinexa.app`, `www.infinexa.app`) debe quedarse siempre en **DNS only** en Cloudflare (nube gris). Nunca "Proxied".
- Solo el registro `*.infinexa.app` debe estar Proxied (nube naranja).
- El Worker `infinexa-builders` debe tener únicamente la ruta `*.infinexa.app/*`. Si aparece también `infinexa.app/*`, bórrala de inmediato — esa combinación tumbó el sitio completo el 12 de julio de 2026.

## Convenciones técnicas ya establecidas

- Includes compartidos en `_includes/`: `nav.html`, `footer.html`, `design-tokens.html`, `ga4.html`, `analytics.html`, `qr-share.html`, `reduced-motion.html`, `form-handler.html`. Usa estos en vez de duplicar código inline.
- Tokens de diseño (ancho, tipografía, espaciado) viven en `_includes/design-tokens.html` como variables CSS — no hardcodear anchos nuevos.
- No hay build local de Jekyll disponible en entornos sandbox con red restringida (`gem install` suele bloquearse) — la verificación se hace por balance de `<div>`/`<script>`/Liquid antes de commit, y por fetch en vivo post-deploy.
- Antes de dar por bueno un cambio de navegación/diseño, verifica que no se dupliquen elementos ya presentes en `nav.html` (ej. logo) al migrar una página al include compartido — ver checklist en `_gestion/RECETAS.md`.

## Al terminar tu sesión

Actualiza `ESTADO.md` (sección correspondiente) y agrega una entrada nueva en `_gestion/BITACORA.md` con fecha, qué se hizo, y qué queda pendiente — sin inflar ni maquillar lo que no se pudo verificar.
