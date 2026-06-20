# BITÁCORA · INFINEXA

> Registro cronológico de sesiones de trabajo. Solo se agrega, nunca se borra ni se reescribe lo ya registrado — así siempre puedes reconstruir el orden exacto de lo que pasó. Las entradas más recientes van arriba.
>
> Para una visión del estado actual del proyecto (no histórico), ver `ESTADO.md`. Para prompts reutilizables, ver `RECETAS.md`. Este archivo es solo el "qué pasó y cuándo".

---

## 2026-06-19 (sesión separada, Claude.ai — plan de marketing orgánico)

- Verificado, mediante el HTML real de `index.html` e `infografia/index.html`, que los tres ajustes de contraste de color (borde blanco transparente en íconos de acordeón `rgba(255,255,255,0.65)`, fondo petróleo denso en badges `rgba(27,77,92,0.35)`, cobre brillante en cursivas `#D97B3C`) ya estaban aplicados en producción — no se trataba de un pendiente real, solo de una duda a resolver. Confirmado: sin acción necesaria.
- Creada carpeta `_marketing/` en el repo, separada de `_gestion/`, para contenido de marketing de atracción (planes de contenido, copys de publicación) — distinto del estado técnico (`ESTADO.md`) y los prompts reutilizables (`RECETAS.md`).
- Generado `_marketing/PLAN-ORGANICO.md`: plan de 4 semanas / 12 publicaciones para Facebook, dirigido a la red personal de Alejandro (2,000+ contactos, audiencia tibia, sin contenido previo publicado sobre economía digital o Hand4Hand).
- Estructura del plan en escalera de convicción de 4 fases: Despertar (semana 1, sin mencionar H4H) → Educación (semana 2, sigue sin vender) → Revelación (semana 3, primera mención de H4H + primer CTA suave) → Conversión (semana 4, experiencia propia + CTA directo).
- Copiadas a `_marketing/assets/` las 4 imágenes generadas para WhatsApp en la conversación de Claude.ai: `arte_infinexa_wa.png`, `arte_infinexa_estado.jpg`, `infinexa_whatsapp.png`, `infinexa_estado.jpg`.
- Agregada receta nueva (sección 10) a `RECETAS.md`: patrón reutilizable de "plan de contenido orgánico por escalera de convicción", aplicable a cualquier red social a futuro, no solo Facebook.
- Agregado enlace desde `ESTADO.md` §7 (Estrategia de prospección) hacia `_marketing/PLAN-ORGANICO.md`, sin modificar el resto de esa sección.
- Subido a GitHub en el commit `f1046dc`: `_marketing/PLAN-ORGANICO.md`, las 4 imágenes en `_marketing/assets/`, y el addendum de `RECETAS.md`.
- **Nota de proceso:** esta sesión se trabajó en una conversación distinta (Claude.ai, no Claude Code), por lo que se siguió un protocolo de verificación antes de escribir: se pidió el contenido real de `ESTADO.md`, `RECETAS.md`, `BITACORA.md` y el HTML en vivo de ambas páginas antes de asumir qué información era nueva, cuál ya existía, y cuál podía contradecir decisiones más recientes tomadas en otras sesiones (Claude Code).

## 2026-06-19

- Diagnosticado y corregido bug del `apple-touch-icon` de Diversifica: el archivo tenía canal alfa (RGBA/transparencia), lo que causaba distorsión visual al anclar la página a la pantalla de inicio en iOS (aunque la imagen de Open Graph, que sí era RGB sin transparencia, se veía perfecta).
- Regenerados desde cero los tres archivos de íconos de marca (`favicon.png` 32×32, `apple-touch-icon.png` 180×180, `og-image.png` 1200×630) directamente desde el SVG vectorial fuente (`infinexa-icono.svg` / `infinexa-logo-negativo.svg`), confirmando en cada uno modo RGB sin transparencia antes de subirlos.
- **Descubierta la causa raíz real:** existían dos carpetas paralelas de assets — `assets/` (la que de verdad usan la carta, infografía, servicios y el builder `carlos`) y `infinexa-assets/files/` (carpeta huérfana, sin ninguna referencia real, creada por error en una sesión anterior). Diversifica apuntaba a la carpeta huérfana, que tenía una versión vieja con transparencia — por eso se veía mal mientras las demás páginas (que ya usaban `assets/`, correcto desde antes) se veían bien.
- Verificado con `grep -rn "infinexa-assets" --include="*.html" .` que ninguna página dependía de la carpeta huérfana antes de eliminarla.
- Corregidas las rutas de `diversifica/index.html` para usar `/assets/` (consistente con el resto del sitio) en lugar de `infinexa-assets/files/`.
- Eliminada por completo la carpeta `infinexa-assets/` (8 archivos, incluyendo `.DS_Store` y el script `aplicar-og.sh` que ya no se usaba). Commit `872c0c0`.
- **Lección para futuras sesiones:** antes de crear una carpeta nueva de assets, verificar primero con `grep -rn "assets" --include="*.html" .` si ya existe una convención establecida en el repo — evita duplicar carpetas con el mismo propósito.
- Confirmado con captura de WhatsApp que la vista previa de Diversifica ya se ve idéntica en calidad a la de la carta principal, y confirmado por el usuario que el ancla a pantalla de inicio en iPhone ya se ve nítida.
- Iniciada esta bitácora y `RECETAS.md` como sistema de organización para futuras sesiones.
- **(Sesión separada, mismo día) Auditoría y optimización del sistema de documentos de marca:** se comparó el `Manual de Marca` (PDF v1.0) contra el `Brand Identity Brief` (DOCX) para determinar si debían fusionarse. Se concluyó que no — cubren audiencias distintas (estrategia/voz vs. especificación técnica/visual) — pero sí debían optimizarse como sistema conectado.
- Reconstruidos ambos documentos en formato DOCX, v1.1, cada uno con una sección inicial "cómo usar este sistema de dos documentos", eliminando la duplicación de la paleta de color y la tipografía (que ahora vive completa solo en el Brief, con referencia desde el Manual), agregando cajas de referencia cruzada entre ambos, y numerándolos como "Documento 1 de 2" / "Documento 2 de 2".
- Investigadas con búsqueda web las políticas vigentes (2026) de Meta Ads, Google Ads y WhatsApp Business para contenido financiero/cripto, además del contexto regulatorio de CONDUSEF/CNBV en México sobre esquemas piramidales disfrazados de "red de marketing" o "academia de inversión".
- Agregada al `Manual de Marca` una sección nueva — "07 — Cumplimiento y políticas de plataformas" — con lineamientos prácticos para evitar baneos/spam en cada plataforma, y dos ítems nuevos en el checklist de coherencia (anuncios pagados y mensajería de WhatsApp). Sección renumerada consecutivamente (Coherencia pasó de sección 06 a 08).
- **Corregida la paleta de color de ambos documentos:** faltaban 2 colores que ya estaban documentados en `ESTADO.md` §3.4 (Grafito oscuro `#0F1720`, fondo principal negativo; Blanco marca `#F8F8F6`, fondo principal positivo) — se detectó la discrepancia comparando contra el `ESTADO.md` real antes de tocar los documentos, y se agregaron a ambos.
- Agregada nueva receta a `RECETAS.md` (sección 9): cómo auditar/optimizar un sistema de documentos de marca en dos capas, y cómo agregar secciones de cumplimiento legal/políticas investigando primero la información vigente.
- **Pendiente para la próxima sesión:** subir `Infinexa_Manual_de_Marca.docx` e `Infinexa_Brand_Identity_Brief.docx` al repositorio, y eliminar las versiones anteriores (PDF del Manual v1.0 y el `infinexa-brand-brief.docx` viejo) una vez confirmado que el contenido fue migrado completo.

## 2026-06-17 (sesión larga — Diversifica completa)

- Construida página Diversifica desde cero: 10 bloques narrativos sobre diversificación de ingresos, con enfoque progresivo hacia la economía descentralizada.
- Primera versión en formato carrusel de pantalla completa — **abandonada por completo** tras detectar que bloqueaba el zoom nativo del navegador en móvil (el gesto de pinch-zoom avanzaba al siguiente slide en vez de ampliar texto).
- Reconstruida completa en formato scroll vertical normal, replicando el sistema visual ya validado de la infografía (header con lockup, badge superior, acordeones, tipografía en clamps).
- Resuelto bug de CSS: un media query de `max-width:720px` estaba posicionado *antes* de las reglas base de tipografía — en la cascada CSS, eso hacía que las reglas base (más abajo) sobreescribieran silenciosamente las correcciones de móvil. **Lección permanente: los media queries siempre van al final del bloque `<style>`.**
- Agregado el set completo de Open Graph y Twitter Card (la primera versión no tenía ninguno, por lo que no se generaba vista previa al compartir).
- Auditoría completa de copy para claridad: 9 frases identificadas como confusas o ambiguas, todas reescritas (incluyendo la frase del trueque/efectivo que generó la auditoría completa).
- Investigado y verificado el dato de "fuentes de ingreso de millonarios": 65% de millonarios hechos a sí mismos tienen al menos 3 fuentes de ingreso (no el rumor de "5 a 7 fuentes" que no tenía buen respaldo). Usado en la página y en la infografía de WhatsApp, con el término "libertad financiera" en vez de "millonarios" para sonar más alcanzable.
- Reforzado en tres puntos de la página el enfoque específico hacia la economía descentralizada como el terreno concreto donde se construye la "siguiente fuente de ingreso" — incluyendo la idea de velocidad/ventana de oportunidad temprana.
- Página publicada en `infinexa.app/diversifica`.
- Agregados `sitemap.xml` y `robots.txt` en la raíz del repo; verificado dominio en Google Search Console (método archivo HTML); indexadas la carta, la infografía y Diversifica (servicios quedó pendiente por decisión propia).
- Confirmado en Meta Debugger que la vista previa de Diversifica funciona correctamente (advertencia menor no bloqueante de `fb:app_id`, decidido no resolver).
- Generada infografía para WhatsApp ("¿Cuántas fuentes de ingreso tienes tú?") con el dato del 65%, exportada a PNG vía Playwright (62.8 KB).
- `ESTADO.md` actualizado dos veces durante la sesión (sección 4.1 Diversifica, sección 4.2 SEO e indexación), verificando contra la versión real del repo antes de cada actualización para no perder ediciones manuales.

---

## Cómo seguir esta bitácora

- Cada sesión de trabajo nueva, pide a Claude: "agrega una entrada a la bitácora de hoy" al final de la conversación.
- Si una sesión se extiende por varios días, usa la fecha de inicio como encabezado y ve agregando viñetas conforme avanza.
- No reescribas entradas viejas — si algo cambió después, se documenta como una entrada nueva que referencia a la anterior (ej. "corregido el bug de X que se reportó el [fecha]").
