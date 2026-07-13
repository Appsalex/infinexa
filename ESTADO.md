# ESTADO · INFINEXA

> Este archivo es la fuente única de verdad del proyecto. Se actualiza después de cada sesión de trabajo, sin importar en qué conversación de Claude se realizó. No se crean archivos nuevos por conversación — siempre se edita este mismo documento.

**Última actualización:** 13 de julio, 2026 — 🔴 **Decisión estratégica: reposicionamiento total de Infinexa, desvinculación completa de Hand4Hand.** Infinexa deja de ser un funnel de prospección hacia Hand4Hand y pasa a ser una plataforma independiente de educación, criterio y conexión sobre la evolución del dinero, blockchain, Web3, IA y nuevos modelos de creación de valor. **Fase 1** (eliminación de Hand4Hand de `index.html`, commit `06747d6`), **Fase 2** (nueva home de 13 secciones + navegación unificada, commit `51caf8a`), **Fase 3** (reposicionamiento de contenido de Diversifica, Infografía y Servicios → Infinexa Digital, commits `2520362`/`47285b5`), **Fase 4** (páginas de Transparencia/Riesgos/Privacidad/Términos + sitemap, commit `07a8512`), **Fase 5** (auditoría de claims del blog, commit `80528bd`) y **Fase 6** (auditoría de accesibilidad, commit `ececf51`) ejecutadas y publicadas — ver sección 1.1–1.7 y `_gestion/BITACORA.md`. Alejandro confirmó dejar `builders/carlos` sin tocar por ahora (1.6) y mantener Diversifica/Infografía como páginas standalone enlazadas desde el home (no fusionarlas al nav). Pendiente: analítica real (falta ID de GA4/GTM) e informe final consolidado.

---

## 1. Resumen del proyecto

Infinexa es una plataforma de educación, análisis y conexión para personas y empresas que quieren entender cómo evolucionan el dinero, blockchain, Web3, la inteligencia artificial y los nuevos modelos de creación de valor — para llevar ese conocimiento a decisiones y proyectos concretos. **Ya no es un funnel de prospección hacia Hand4Hand** (decisión del 13 jul 2026, ver 1.1). El proyecto se construyó desde cero usando Claude Code, con sitio web propio e identidad de marca completa.

### 1.1 Reposicionamiento y desvinculación de Hand4Hand (13 jul 2026)

Alejandro decidió pivotar Infinexa de "funnel de prospección hacia Hand4Hand" a "plataforma independiente de educación financiera/tecnológica". Motivo directo: el propio hallazgo de cumplimiento del 23 jun (sección 4.0 original, ver abajo) ya había marcado la mecánica "Ciclo 2×2" de la carta como estructuralmente similar a un esquema Ponzi/piramidal ante los detectores automáticos de Meta/WhatsApp — nunca se había ejecutado la corrección.

**Ejecutado en esta sesión (Fase 1, commit `06747d6`):**
- Eliminado el Escalón 4 completo de `index.html` (mecánica Ciclo 2×2, los 3 "pilares" de Hand4Hand, tabla comparativa de custodia, tech badges USDT/Polygon/wallet) y el Escalón 5 (SI/NO — describía en su totalidad el producto de Hand4Hand).
- Eliminado el roadmap de onboarding de Hand4Hand del CTA final (Génesis, Human Wallet, Sprint 72h, trayectoria Insider→Maker).
- Reescritos el Bridge y el CTA para invitar a una conversación genérica sobre Infinexa, sin nombrar Hand4Hand ni presuponer ningún producto específico.
- Reescrito el disclaimer final: ahora describe a Infinexa como plataforma educativa (no a Hand4Hand como producto de aportaciones).
- Limpiado el CSS huérfano de todos los bloques eliminados.
- `_config.yml`: la descripción del sitio ya no dice "prospección"; ahora describe la propuesta educativa. Se agregó también `ESTADO.md` a `exclude:` — este archivo se estaba subiendo sin querer como archivo estático descargable en GitHub Pages (no tenía front matter, Jekyll lo copiaba tal cual), exponiendo públicamente hallazgos internos de cumplimiento y estrategia de negocio.
- Verificado: cero menciones de "Hand4Hand"/"H4H" en cualquier página, post o layout publicado (servicios, diversifica, infografía y los 15 posts del blog ya estaban limpios desde antes — solo la carta y el sistema de builders tenían el contenido).

**Pendiente de decisión explícita — NO tocado en esta sesión:** `builders/carlos/`, `builders/_template/` y `carlos/` en la raíz son landings completas de Hand4Hand para el sistema de subdominios "Builder Edition", con `carlos.infinexa.app` **en vivo para un tercero real** (un builder real de Hand4Hand). Eliminarlas o reescribirlas apaga su página sin aviso — requiere que Alejandro decida primero qué pasa con esa relación/subdominio antes de tocar el código. Ver sección 6 (sistema de builders) y "Próximos pasos" abajo.

### 1.2 Fase 2 — nueva home y navegación unificada (13 jul 2026, commit `51caf8a`)

`index.html` se reconstruyó por completo como la nueva home (13 secciones: hero, "el cambio ya comenzó", "el verdadero problema", qué puedes aprender —10 tarjetas enlazadas a posts/páginas reales—, tres rutas Comprender/Evaluar/Aplicar, Método Infinexa de 5 pasos, Diagnóstico funcional con quiz de 3 preguntas sin backend que genera un mensaje de WhatsApp, "del conocimiento a la práctica", Talleres con formulario funcional, Infinexa Digital, Quién está detrás con el perfil de Alejandro, Principios, CTA final).

Se agregó una nav compartida (Inicio · Aprender · Diagnóstico · Talleres · Servicios · Nosotros + botón "Hablemos") a **todas** las páginas del sitio: `index.html`, `servicios/`, `diversifica/`, `infografia/`, `donativo/`, y `_layouts/default.html` (blog — reemplaza el nav anterior de Inicio/Diversifica/El Patrón/Blog). "Diagnóstico"/"Talleres"/"Nosotros" son anclas dentro de la home (`/#diagnostico`, `/#talleres`, `/#nosotros`), no páginas separadas todavía — funcionan desde cualquier página del sitio.

Se agregó un helper `trackEvent()` en la home, instrumentado en los CTA principales, pero **no hace nada todavía**: no hay GA4/GTM instalado en el sitio (se verificó, cero rastro de analítica previa). Pendiente: Alejandro debe proporcionar un ID de medición de GA4 o un contenedor de GTM para activarlo de verdad.

Contenido de Diversifica, Infografía y Servicios no se tocó en esta fase (solo se les agregó la nav) — su reposicionamiento de contenido se ejecutó en la Fase 3 (ver 1.3).

### 1.3 Fase 3 — reposicionamiento de Diversifica, Infografía y Servicios (13 jul 2026, commits `2520362`/`47285b5`)

**Diversifica:** nueva tesis ("Diversificar no significa acumular opciones. Significa reducir dependencias sin perder claridad, liquidez ni control."), fuente citada explícitamente para el dato del 65% (Tom Corley, "Rich Habits"), la "2ª fuente" ya no se prescribe como exclusivamente "Descentralizada" sino como "Nueva" (habilidad monetizada, negocio digital o modelo descentralizado — sin imponer una sola ruta), eliminado el determinismo de "cuando algo mejor llega, el mundo avanza y no regresa" y la urgencia artificial de "ventana que se cierra" (aparecía dos veces). CTA cambiado a "Evaluar mi nivel de diversificación" → enlaza al diagnóstico de la home, con opción secundaria de WhatsApp.

**Infografía / El Patrón:** título cambiado de "El patrón que nunca falla" a "El Patrón — cómo evaluar una innovación". Eliminados los absolutismos ("nunca falla", "siempre es el mismo", "sin excepción", "siempre ha tenido el mismo final"). Agregado un acordeón nuevo completo — "Cómo evaluar una innovación" — con los 11 criterios (problema real, adopción, infraestructura, incentivos, regulación, seguridad, utilidad, escalabilidad, sostenibilidad, riesgo, evidencia): la página deja de ser solo narrativa histórica y se convierte también en herramienta de evaluación. Cierre reescrito sin "la ventana está abierta". CTA principal ahora "Aprender a evaluar una innovación" (ancla al nuevo acordeón).

**Servicios → Infinexa Digital:** branding actualizado en title/OG a "Infinexa Digital" manteniendo la URL `/servicios/` (sin romper SEO). Eliminado el lenguaje de "materiales/textos de prospección" (herencia directa del modelo Hand4Hand) → ahora "materiales comerciales". Precios ($2,000 implementación / $97 mensual / $797 anual) ahora expresados en USD en vez de solo USDT, con nota de equivalencia en USDT/MXN — **ya no se obliga el pago exclusivo en cripto**: se agregó transferencia bancaria tradicional como alternativa igualmente válida (sección de pago y FAQ reescritas). Aclarado que implementación y mantenimiento se facturan por separado. Metodología alineada al método Infinexa (analizar → definir → construir → publicar → medir → mejorar).

Verificado tras el push: balance de HTML correcto en los 3 archivos, cero menciones de Hand4Hand, cero menciones de "prospección".

### 1.4 Fase 4 — páginas legales y sitemap (13 jul 2026, commit `07a8512`)

Creadas 4 páginas nuevas, todas con el sistema visual del sitio (nav compartida, footer, QR compartible):

- **`/transparencia/`** — qué es/no es Infinexa, quién la dirige, cómo se genera y verifica el contenido, cómo se presentan proyectos de terceros y relaciones comerciales (con revelación explícita si Alejandro tiene una relación comercial con algo mencionado en una conversación 1:1), diferencia entre educación y promoción, qué implica solicitar una conversación.
- **`/riesgos/`** — 10 categorías (mercado, tecnológico, custodia, contraparte, liquidez, regulatorio, operativo, fraude, proyectos productivos, pérdida), con nota de que no sustituye asesoría legal profesional.
- **`/privacidad/`** — qué datos se recopilan (solo los que el usuario envía activamente por el diagnóstico, el formulario de talleres o WhatsApp — no hay cuentas de usuario ni analítica activa hoy), qué no se hace con ellos, y cómo ejercer derechos de acceso/corrección/eliminación.
- **`/terminos/`** — naturaleza educativa del contenido, sin garantías de resultados, condiciones de Infinexa Digital, propiedad intelectual, ley aplicable (México).

Enlazadas desde el footer de las 6 superficies del sitio (home, servicios, diversifica, infografía, donativo, blog) — antes no existían y no estaban enlazadas desde ningún lado. `sitemap.xml` actualizado con las 4 rutas nuevas (prioridad baja, `changefreq: yearly`, acorde a contenido legal/informativo estable).

**Qué falta de la visión completa de reposicionamiento (fases futuras, no ejecutadas):** auditoría de claims sensibles en los 15 posts del blog, analítica real (falta ID de GA4/GTM — Alejandro debe proporcionarlo), accesibilidad, decisión sobre `builders/carlos` (ver "Próximos pasos" ítem 1b). El detalle completo de esta visión vive en el prompt maestro que Alejandro proporcionó el 13 jul 2026 (no se guardó como archivo aparte — si se retoma, pedir a Alejandro que lo vuelva a compartir o consultar el historial de esta conversación).

### 1.5 Fase 5 — auditoría de claims del blog (13 jul 2026, commit `80528bd`)

Sweep con grep sobre los 15 posts de `_posts/` buscando lenguaje absolutista, garantías de rendimiento, urgencia artificial y superlativos sin fuente. Resultado: la gran mayoría de coincidencias de "siempre"/"nunca" eran usos narrativos normales (ej. "nunca fue realmente a la máquina en sí", en `piezas-rompecabezas.md`), no claims financieros problemáticos. Dos hallazgos reales, corregidos:

- **`stablecoin-vs-bitcoin.md`** describía la paridad de USDT como absoluta ("está diseñada para valer siempre exactamente un dólar", "siempre hay con qué [canjear]", "el valor es siempre el mismo"). Reescrito para presentarlo como objetivo de diseño, no garantía — se agregó una frase explícita sobre el riesgo de de-peg y el escrutinio público que han recibido las reservas de Tether en distintos momentos.
- **Referencias obsoletas a "la carta"** en 4 posts (`wallet-no-custodial`, `stablecoin-vs-bitcoin`, `bloque-genesis-bitcoin`, `whitepaper-bitcoin`): tanto el `pillar_label` del front matter ("Ver la carta") como enlaces en el cuerpo del texto apuntaban a `/` describiéndolo como "la carta de Infinexa" — una narrativa que ya no existe ahí desde la Fase 2 (la home se reconstruyó por completo). Corregido a "Ver Infinexa" / "[Infinexa](/)" en los 4 posts, y la misma referencia en `donativo/index.html`.

Verificado además: sin lenguaje de "rendimiento garantizado" ni urgencia artificial ("ventana que se cierra", "cupos limitados", etc.) en ninguna página publicada. La estadística del 65% (tres fuentes de ingreso) no aparece sin fuente en el blog — los posts que la mencionan (`ingreso-vs-activo.md`) remiten a Diversifica, donde ya está citada (Tom Corley / *Rich Habits*, corregido en Fase 3). `historia-del-dinero.md` y `piezas-rompecabezas.md` tenían coincidencias de "garantiza"/"aseguran" que en contexto son correctas (la primera niega explícitamente una garantía; la segunda es "cómo se aseguran de coordinarse", no una promesa financiera) — no requerían cambio. `sitemap.xml` actualizado con `lastmod: 2026-07-13` en los 4 posts editados.

**Pendiente:** decisión sobre `builders/carlos`, analítica real (GA4/GTM), accesibilidad, informe final consolidado de cumplimiento (sección 31 del prompt maestro).

### 1.6 Decisión sobre `builders/carlos` (13 jul 2026)

Alejandro confirmó explícitamente: dejarlo como está por ahora. No se avisó a Carlos, no se dio de baja el subdominio, no se tocó código de `builders/carlos/`, `builders/_template/` ni `carlos/`. Sigue siendo una decisión abierta para el futuro, no resuelta — solo se confirmó que por ahora no se actúa.

### 1.7 Auditoría de accesibilidad (13 jul 2026, commit `ececf51`)

Revisión de navegación por teclado, foco, contraste de color, aria-labels y labels de formulario en las 6 superficies del sitio + las 4 páginas legales. La mayoría ya estaba en buen estado: `lang="es"` presente en todas las páginas, inputs del diagnóstico y de talleres con `<label for="">` correctamente asociado, acordeones con `aria-expanded` actualizado por JS, sin `outline:none` sin reemplazo visible.

**Hallazgo real (medido con fórmula de contraste WCAG):** el párrafo del disclaimer de cumplimiento ("No es asesoría financiera...") se renderizaba a ~2.1:1 de contraste (`rgba(200,210,214,.3)` sobre el fondo oscuro) en 8 páginas (`index.html`, `_layouts/default.html`, `diversifica`, `infografia`, `transparencia`, `riesgos`, `privacidad`, `terminos`) — muy por debajo del mínimo 4.5:1 de WCAG AA para texto normal. Era, irónicamente, el párrafo que más necesitaba ser legible. Corregido subiendo la opacidad a .6 (contraste resultante ~4.9–5.0:1) en las 8 páginas.

También corregido: `donativo/index.html` tenía el mismo disclaimer al 4.2:1 (opacity .7 sobre `--tmuted`) — subido a .9 (6.2:1). Y se descubrió que **`servicios/index.html` era la única página pública sin ninguna frase de disclaimer** — se agregó una en el footer, y se subió el contraste de los enlaces del footer de esa página (.7 → .85, de 4.2:1 a 5.1:1).

Verificado balance de HTML en las 10 páginas tocadas antes de publicar. Sin cambios de estructura ni de contenido más allá del color/opacidad y la frase nueva en servicios.

**Pendiente:** analítica real (GA4/GTM — falta ID de Alejandro), informe final consolidado (sección 31 del prompt maestro). `builders/carlos` no se toca (ver 1.6).

---

## 2. Infraestructura técnica

- **Repositorio:** `github.com/Appsalex/infinexa` (público, autodeploy vía GitHub Pages)
- **Dominio:** `infinexa.app`, gestionado en Cloudflare
- **DNS:** 4 registros A apuntando a IPs de GitHub Pages (185.199.108–111.153) en modo DNS only; CNAME `www` → `appsalex.github.io`
- **Wildcard para builders:** CNAME `*.infinexa.app` → `appsalex.github.io` en modo **Proxied** (nube naranja)
- **SSL/TLS:** modo **Full** activado en Cloudflare para generar certificados automáticos en subdominios wildcard
- **Cloudflare Worker:** `infinexa-builders` — hace proxy transparente de cualquier subdominio (excepto `www`, `infinexa`, `app`) hacia la carpeta correspondiente en `infinexa.app/{subdominio}`
- **Workers Route:** `*.infinexa.app/*` → Worker `infinexa-builders`

⚠️ **Regla crítica de infraestructura (incidente 12 jul 2026):** el dominio raíz (`infinexa.app`) DEBE quedarse en modo **DNS only** (nube gris) — NUNCA en Proxied. Si se activa el proxy en el dominio raíz por error, y el Worker `infinexa-builders` llega a tener una ruta que también matchee `infinexa.app/*` (además de `*.infinexa.app/*`), el sitio principal completo deja de cargar (timeout / certificado inválido) sin ningún error visible en los builds de GitHub Pages, que siguen mostrándose exitosos. Antes de tocar cualquier configuración de DNS o Workers Routes, confirmar que:
  1. Los 4 registros A de `infinexa.app` y el CNAME de `www` están en DNS only.
  2. Solo el CNAME `*.infinexa.app` está en Proxied.
  3. El Worker `infinexa-builders` tiene ÚNICAMENTE la ruta `*.infinexa.app/*` — nunca `infinexa.app/*`.
  Detalle completo del incidente en `_gestion/BITACORA.md`, entrada del 12 jul 2026.
- **GitHub:** autenticación con 2FA vía Google Authenticator
- **Entorno local:** MacBook Air, terminal Ghostty, Claude Code instalado (`curl -fsSL https://claude.ai/install.sh | sh`)
- **Carpeta de trabajo local:** `~/Downloads/infinexa-repo`

---

## 3. Marca e identidad visual

### 3.1 Historia y significado del nombre

Infinexa nace de la fusión de dos raíces: **Infinite** (expansión sin límites, escalabilidad, visión de largo plazo) + **Nexus** (conexión, punto de encuentro, nodo de unión). Se descartaron alternativas como InfinityWealth (demasiado financiero), InfinityAccess (demasiado descriptivo) e InfinityAlliance (demasiado comunitario) por quedar atrapadas en una sola categoría.

**Significado oficial:** *"Infinexa es el punto de conexión donde las posibilidades infinitas se transforman en valor con propósito."*

**Por qué trasciende el tiempo:** no promete riqueza, no depende de blockchain ni de ninguna moda tecnológica, funciona igual en español e inglés, y puede seguir vigente dentro de 20 años — no describe lo que hace hoy, representa la visión de lo que puede llegar a ser mañana.

### 3.2 Sistema de símbolo

- **Símbolo:** lemniscata (∞) orgánica, trazada como un único gesto continuo (no dos loops cerrados). Asimetría intencional: loop izquierdo más horizontal y abierto (comunidad, amplitud), loop derecho más vertical y tenso (precisión, arquitectura digital).
- **Acento cobre — "el nexo":** dos micro-arcos en cobre que abrazan un punto central exactamente en el cruce del símbolo. Representa literalmente el momento donde dos mundos se tocan — no es decoración, es significado.

### 3.3 Wordmark

- **Texto:** `infinexa` en minúsculas (decisión deliberada — más humano y accesible sin perder autoridad, siguiendo el patrón de marcas globales como Apple o Spotify)
- **Tipografía:** Inter, peso 300 (Light), letter-spacing amplio (18px en canvas de referencia 800×480)
- **Tagline:** `connecting value with purpose` en minúsculas, opacidad 50%, casi imperceptible — "el lujo no se anuncia, se descubre"

### 3.4 Paleta de color

| Color | Hex | Uso |
|---|---|---|
| Grafito oscuro | `#0F1720` | Fondo principal negativo |
| Grafito | `#1F2A33` | Fondo alterno, stroke en positivo |
| Petróleo | `#1B4D5C` | Subtítulos, separadores, tagline en positivo |
| Petróleo claro | `#2E6E80` | Labels secundarios, detalles |
| Cobre (acento) | `#C8682E` | Único acento cálido — nunca como fondo |
| Plata | `#C9D2D6` | Stroke del símbolo en negativo |
| Plata clara | `#EDF1F2` | Wordmark en negativo |
| Blanco marca | `#F8F8F6` | Fondo positivo |

**Colores de conexión (solo al presentar Hand4Hand):** Navy `#0D1B3E`, Naranja `#E8450A` — nunca como colores propios de Infinexa.

### 3.5 Sistema de lockups

- **Vertical** (principal): símbolo arriba centrado, aire generoso, wordmark, separador cobre, tagline. Uso: redes sociales, presentaciones, hero web.
- **Horizontal:** símbolo izquierda, separador vertical en petróleo, wordmark + tagline apilados a la derecha. Uso: firmas de correo, headers, banners.
- **Solo símbolo:** favicon, avatar, marca de agua.
- **Solo wordmark:** espacios mínimos donde el símbolo no renderiza bien.

**Zona de exclusión:** equivalente a la altura de la "i" del wordmark en todos los lados. **Tamaño mínimo digital:** 32px de alto para el lockup vertical completo.

### 3.6 Archivos de marca entregados

| Archivo | Formato | Contenido |
|---|---|---|
| `infinexa-logo-negativo.svg` | SVG | Logo vertical completo sobre fondo oscuro — master |
| `infinexa-logo-positivo.svg` | SVG | Logo vertical completo sobre fondo claro — master |
| `infinexa-logo-horizontal.svg` | SVG | Lockup horizontal — firmas, headers |
| `infinexa-icono.svg` | SVG | Solo símbolo — favicon, avatar |
| `infinexa-portada-linkedin.svg` | SVG | Banner LinkedIn/Twitter, 1584×396px |
| `Infinexa_Manual_de_Marca.docx` (v1.1) | DOCX | Documento 1 de 2 del sistema de marca. Estrategia, posicionamiento, tono de voz, bios, sección de cumplimiento de políticas de plataformas (Meta Ads, Google Ads, WhatsApp Business, contexto regulatorio CONDUSEF/CNBV en México), checklist de coherencia. Reemplaza el PDF "Manual de Marca v1.0" anterior. |
| `Infinexa_Brand_Identity_Brief.docx` (v1.1) | DOCX | Documento 2 de 2 del sistema de marca. Especificaciones técnicas: historia del nombre, símbolo (paths SVG), wordmark, paleta completa de 8 colores, tipografía, lockups, zonas de exclusión, usos incorrectos. Reemplaza la versión `infinexa-brand-brief.docx` anterior. |

Ambos documentos quedaron optimizados como un sistema de dos capas con referencias cruzadas entre sí (estrategia/voz vs. especificación técnica/visual), evitando duplicar contenido entre ellos.

**Pendiente:** importar los SVG a Figma/Illustrator y convertir textos a outlines; exportar PNG en 1x/2x/3x; instalar Inter como fuente del sistema; aplicar el símbolo actualizado al sitio web en vivo (actualmente el sitio puede tener la versión visual anterior); subir ambos docx nuevos al repositorio y eliminar las versiones anteriores (PDF del Manual y `infinexa-brand-brief.docx` viejo) una vez confirmado que el contenido fue migrado completo.

### 3.7 Pipeline de generación de imágenes de marketing (nuevo, 23 jun 2026)

**Problema detectado:** las piezas generadas con `wkhtmltoimage` (motor basado en WebKit antiguo) mostraban artefactos visibles en curvas finas del logo — específicamente, el cruce central de la lemniscata se veía "cortado"/discontinuo, especialmente al aplicar después un filtro de nitidez (unsharp mask), que exageraba el defecto en vez de corregirlo.

**Solución adoptada — nuevo estándar:** renderizar con **Playwright + Chromium nativo** en vez de `wkhtmltoimage`.

- Chromium real disponible en el entorno de Claude vía `playwright` (`from playwright.sync_api import sync_playwright`)
- Proceso: HTML/CSS con el **path SVG real** del logo embebido directamente (extraído de `infinexa-icono.svg` / `infinexa-logo-negativo.svg`, nunca aproximado a mano)
- Captura con `device_scale_factor=2` (supersampling nativo — 2x resolución real, no un escalado falso)
- Reescalar el resultado a la mitad con Lanczos (`PIL.Image.LANCZOS`) para nitidez final sin artefactos
- Recortar al contenido real (`full_page` o crop manual) antes de entregar

**Resultado:** líneas continuas y limpias en el cruce del símbolo, sin necesidad de parches de nitidez posteriores que antes degradaban la calidad.

**Lección para futuras piezas:** siempre usar el path SVG real de los archivos de marca entregados (sección 3.6), nunca redibujar el símbolo a mano — y usar Chromium/Playwright como motor de render por defecto para cualquier infografía o pieza visual nueva.

---

## 4. Páginas publicadas

| Página | URL | Estado |
|---|---|---|
| La carta | `infinexa.app` | ✅ Publicada — ⚠️ ver sección 4.0, hallazgo de cumplimiento pendiente de ejecutar |
| La infografía | `infinexa.app/infografia` | ✅ Publicada — gradiente corregido hasta DeFi, tipografía igualada con la carta |
| Servicios | `infinexa.app/servicios` | ✅ Publicada — con precios USDT y wallet (sin QR) |
| Diversifica | `infinexa.app/diversifica` | ✅ Publicada — ver detalles abajo |
| Blog | `infinexa.app/blog` | ✅ Publicado — 15 posts, ver sección 4.4 |
| Donativo | `infinexa.app/donativo` | ✅ Publicada — USDT (Polygon) + Bitcoin, QR verificados |

**Detalles técnicos resueltos en la infografía:**
- Gradiente de la barra histórica corregido para terminar exactamente en el marcador "DeFi"
- Cursivas y texto de cuerpo corregidos de `--plata` a `--cobre`/`--plata-cl` para igualar el brillo de la carta

### 4.0 La carta — refuerzo del hilo de Carlos, resolución de duplicación, y hallazgo de cumplimiento (22-23 jun 2026)

**Refuerzo del hilo narrativo (22 jun 2026):** se detectó que Carlos (el personaje del hook inicial) desaparecía después del header y no volvía a aparecer en el resto de la página, perdiendo la calidez emocional abierta al inicio. Se agregaron tres apariciones breves de Carlos en puntos clave:
- **Escalón 3** (eras económicas): pull-quote al final — "Carlos está justo en ese punto ahora mismo..."
- **Escalón 4** (Hand4Hand): línea en cursiva al inicio del panel — "Carlos no decidió en automático..."
- **Bridge** (antes de las 3 razones): línea agregada después del bridge-body — "Carlos hizo exactamente esta pregunta antes de decidir..."

✅ Publicado (commit `51ccee0`).

**Resolución de duplicación de contenido con "El Patrón"/infografía (22 jun 2026):** se identificó que el Escalón 3 de la carta (tabla completa de 5 eras económicas + analogía de internet) repetía, casi palabra por palabra, contenido que también vive en la infografía (`/infografia`, nombre de trabajo "El Patrón"). Se decidió que **cada página profundiza en un ángulo distinto sin repetirse**, mismo principio que ya rige los assets compartidos: solo una página mantiene la versión completa de un tema, las demás resumen y enlazan hacia ella.

Se aligeró el Escalón 3 de la carta:
- La tabla se redujo de 5 eras a solo 2 (Digital vs. Descentralización — el contraste inmediato relevante)
- Se eliminó la analogía completa de internet (ya cubierta con más profundidad en El Patrón)
- Se agregó un enlace explícito: *"Esto es solo el panorama general. Si quieres ver los 200 años de este patrón completo... revisa El Patrón →"* apuntando a `/infografia`
- El Escalón 2 (escépticos históricos, 3 ejemplos) se dejó intacto — es suficiente para el propósito de la carta y no se consideró duplicación relevante

✅ Publicado (commit `a258cef`).

**Lección para futuras páginas:** cuando dos piezas cubren el mismo tema histórico/educativo, decidir desde el inicio cuál es la versión "autorizada" y completa, y cuál resume con enlace — evita inconsistencias futuras si se actualiza un dato en una sola página y no en la otra (mismo riesgo ya identificado con los assets duplicados de Diversifica, sección 4.3).

**⚠️ Hallazgo de cumplimiento — mecánica de Ciclos 2×2 (23 jun 2026, sesión Claude.ai, conversación de marketing):**

Al revisar el contenido completo de la carta en el contexto de una guía de cumplimiento Meta/WhatsApp (ver sección 10 / RECETAS.md), se detectó que el **Escalón 4 (Hand4Hand)** describe la mecánica de "Ciclo 2×2" con cifras específicas de activación y escalamiento: una aportación de 100 USDT que activa simultáneamente "Ciclo 10 + Ciclo 25 + Ciclo 50", escalando — según participación de la comunidad — hasta "Ciclo 5,000" sin aportación externa adicional. Incluye también un diagrama visual de ese flujo de escalamiento.

**Por qué es un riesgo:** independientemente de la legitimidad real del modelo y de los disclaimers ya presentes en la página ("no es una inversión", "no garantiza resultados"), esta estructura — una aportación fija que se multiplica en función de que se sumen más participantes, sin generar valor de un producto/servicio independiente — es **estructuralmente el mismo patrón que los esquemas Ponzi/piramidales**. Los sistemas automáticos de detección de Meta y WhatsApp evalúan patrón estructural, no solo intención ni disclaimers, así que este tipo de contenido es de alto riesgo de cumplimiento — más que cualquier frase-gatillo de copy.

**Decisión tomada:** eliminar de la página pública toda la mecánica numérica de ciclos (el "cómo" se activa y escala el sistema), reservando esa explicación exclusivamente para conversación 1:1 (llamada/WhatsApp), donde sí hay contexto y diálogo real. Se conserva intacto el resto de la página: historia de Carlos, Escalones 1-3, los 3 pilares (Educación/Comunidad/Participación voluntaria, reescribiendo el Pilar 3 sin cifras), el bloque de transparencia "Qué es/no es" (en lo que describe tecnología — USDT, Polygon, wallet no custodial — no mecánica de ciclos), y el cierre invitando a la conversación de 20 minutos.

**Estado: 🔧 Pendiente de ejecutar.** Se generó un prompt completo con el detalle de qué eliminar, qué conservar, y una propuesta de reescritura del Escalón 4, destinado a llevarse a la conversación de Claude dedicada a páginas web (esta sesión se mantuvo enfocada en marketing). El cambio NO se ha aplicado todavía al archivo real `index.html`.

### 4.1 Diversifica — narrativa y decisiones de diseño

**Propósito:** página educativa sobre diversificación de ingresos, con enfoque progresivo hacia la economía descentralizada como terreno de oportunidad temprana (no como producto a vender directamente).

**Estructura narrativa final (10 bloques de contenido):**
1. Apertura — "cada generación ha tenido que reaprender cómo generar ingresos"
2. Línea de tiempo de crisis históricas (1929, 1994, 2008, 2020) — en acordeón
3. Automatización dentro de las profesiones (ejemplos supermercado/contador) — en acordeón
4. Panorama completo: IA + automatización + descentralización convergiendo — en acordeón
5. El giro — "¿quiero seguir creciendo desde donde estoy hoy?" (visible siempre, fondo grafito)
6. Diversificar no es abandonar — introduce la distinción ingreso (depende del tiempo) vs. activo (genera valor sin presencia directa) (visible siempre)
7. Tendencia, no moda — analogías históricas (trueque→dinero, discos duros→nube) para argumentar que la descentralización es tendencia irreversible, no moda pasajera — en acordeón
8. Lo nuevo no reemplaza lo de siempre — lo amplía (antes "Línea divisoria") — sistema tradicional vs. descentralizado, con el matiz de segmentación natural de mercado y "terreno apenas en construcción" — en acordeón
9. El legado — "a veces alguien tiene que dar el primer paso" (visible siempre, fondo grafito)
10. Cierre/CTA — "Conoce. Explora. Empieza a construir." + botón WhatsApp con mensaje prellenado

**Decisión de formato — de carrusel a scroll:** la primera versión se construyó como carrusel de pantalla completa (un slide por pantalla, navegación por swipe/flechas). Se abandonó por completo porque en móvil bloqueaba el zoom nativo del navegador (el gesto de pinch-zoom hacía avanzar al siguiente slide en vez de ampliar el texto), y los tamaños de fuente quedaban forzadamente pequeños para que todo el contenido cupiera en una sola pantalla. Se reconstruyó como página de scroll vertical normal, replicando el mismo sistema visual de la infografía (`card` centrada con `box-shadow`, header con lockup horizontal, badge superior, tipografía en clamps generosos, secciones con fondo `--grafito` para los momentos de mayor peso narrativo).

**Sistema de acordeones:** 5 de los 10 bloques de contenido (los más largos/expositivos) están colapsados por defecto, replicando el patrón ya usado en la infografía (`acord-section`, `acord-trigger`, `acord-panel` con `max-height` animado). Los bloques de mayor peso emocional/persuasivo (apertura, "el giro", "diversificar no es abandonar", "el legado", cierre) se dejaron siempre visibles sin acordeón.

**Open Graph corregido:** se agregó el set completo de meta tags (`og:title`, `og:description`, `og:image`, `og:url`, Twitter Card) apuntando a los assets oficiales en `infinexa-assets/files/og-image.png` y `favicon.png`/`favicon.svg` — la primera versión no tenía ningún tag Open Graph, por lo que no se generaba vista previa al compartir en WhatsApp.

**Bug de CSS resuelto (relevante para futuras páginas):** en la versión carrusel, un media query de `max-width:720px` estaba posicionado *antes* de las reglas base de tipografía en el archivo. En CSS, con igual especificidad, la regla que aparece después en el código gana — así que las reglas base (más abajo) sobreescribían silenciosamente todas las correcciones de móvil, sin importar el ancho de pantalla real. Lección para futuras páginas: los media queries siempre deben ir *al final* del bloque `<style>`, después de todas las reglas base que pretenden sobreescribir.

**Pendiente:** ~~verificar en Meta Debugger que `og:image` ya no muestra advertencias~~ — ✅ **Resuelto.** Vista previa funcionando correctamente en Meta Debugger (logo, título y descripción se muestran bien). Queda una advertencia menor no bloqueante: "Faltan las siguientes propiedades obligatorias: fb:app_id" — solo es necesaria para integraciones avanzadas (login con Facebook, analíticas nativas de Facebook), no afecta la vista previa al compartir por WhatsApp/redes. Se decidió no agregarla por ahora.

**Refinamiento de copy (19 jun 2026):** se ajustó toda la página para alinear el mensaje con un dato estadístico verificado y con un enfoque más explícito hacia la economía descentralizada como vehículo concreto:
- **Dato central verificado:** 65% de quienes alcanzaron libertad financiera tenían al menos 3 fuentes de ingreso (se descartó el rumor sin respaldo de "5 a 7 fuentes recomendadas"; se usó "libertad financiera" en vez de "millonarios" para sonar más alcanzable al avatar).
- **Badge superior y pregunta de cierre** cambiados de "una conversación honesta sobre el dinero" (genérico) a "una conversación sobre tu siguiente fuente de ingreso" / "¿Cuál es tu siguiente fuente?" — mismo lenguaje usado en la infografía de WhatsApp, creando hilo narrativo entre ambas piezas.
- **Las tres tarjetas de progresión** (1ª/2ª/3ª fuente) ahora nombran explícitamente el destino: la 2ª fuente se llama "Descentralizada" (un negocio en la nueva economía digital) y la 3ª "Activo digital" — antes eran genéricas ("Construye", "Activo") sin decir dónde encontrar esa fuente.
- **Agregado el argumento de velocidad/ventana de oportunidad temprana:** la economía descentralizada se presenta como un terreno en etapas tempranas (analogía con internet "antes de que todo el mundo tuviera correo electrónico"), donde quien entra hoy lo hace antes de que el terreno "se llene" — sin caer en presión de ventas agresiva.
- **Auditoría completa de claridad de copy:** se revisaron las 9 frases más abstractas o ambiguas de toda la página (ej. "el efectivo no eliminó el trueque... pero el mundo nunca volvió atrás" generaba confusión lógica) y se reescribieron para que sean entendibles a la primera lectura, sin perder profundidad.

**Ajuste de balance narrativo (21 jun 2026):** se detectó que la página presentaba el "activo final" como exclusivamente digital/descentralizado, lo cual estrechaba el mensaje. Se corrigió para que la idea central sea: toda fuente de ingreso bien trabajada termina convirtiéndose en un activo — tradicional o descentralizado — sin restarle protagonismo a la economía descentralizada como la puerta nueva que la página invita a explorar. Se incorporó también el argumento de segmentación natural de mercado (la tecnología no inventa la actividad, se monta sobre algo que ya existía; quien prefiere lo de siempre y quien prefiere lo nuevo conviven, sin que uno elimine al otro), evitando que el mensaje suene fatalista hacia lo tradicional.

Tres bloques se reescribieron con este balance:
- **"Diversificar no es abandonar":** el párrafo de apertura ahora nombra la economía descentralizada como "presente y futuro de las finanzas"; la 3ª tarjeta de progresión cambió de "Activo digital" a solo "Activo", aclarando que puede ser tradicional o descentralizado.
- **Acordeón 5** (antes "Línea divisoria", ahora **"Lo nuevo no reemplaza lo de siempre — lo amplía"**): se agregó un párrafo de apertura con la analogía de transporte (sin marcas) para introducir la segmentación natural; el lado "descentralizado" del split ahora dice explícitamente que no reemplaza lo de siempre, es la nueva opción dentro de la misma necesidad.
- **Cierre/CTA:** se agregó la frase "Toda fuente bien trabajada termina convirtiéndose en un activo — tradicional o descentralizado" para que el CTA cierre con la idea central completa.

✅ Publicado en `infinexa.app/diversifica` (commit `121f741`).

**Infografía de WhatsApp actualizada (23 jun 2026, sesión Claude.ai):** se regeneró la pieza visual de Diversifica para WhatsApp (gancho "¿Y si una sola fuente de ingreso ya no es suficiente?") con tres ajustes:
- **Datos verificados y atribuidos:** las tres cifras (65% / 45% / 29% de quienes alcanzaron libertad financiera, por número de fuentes de ingreso) fueron confirmadas vía investigación web — provienen del estudio de **Tom Corley, "Rich Habits"**. Se corrigió un dato impreciso de una versión anterior de la pieza (decía 30% en vez de 29% para "5 o más fuentes"). Se agregó atribución explícita de la fuente en la pieza, reforzando la regla de marca de "nunca rumores, solo datos verificados".
- **Nombres de las 3 tarjetas de progresión alineados con el copy actual de la página:** 1ª Activa / 2ª **Descentralizada** (antes decía "Construye" en la versión vieja de la infografía) / 3ª Activo.
- **Gancho de 3 segundos + storytelling:** se rediseñó para que lo primero visible sea la pregunta de apertura de la página (no el logo), se agregó una banda compacta con los años de crisis históricas (1929·1994·2008·2020) como guiño narrativo, y el cierre usa pregunta abierta + dos opciones suaves ("Conoce"/"Explora") en vez de un CTA de presión.
- Generada con el nuevo pipeline de render (sección 3.7) — logo real, sin artefactos.

Archivo: `infinexa-diversifica-actualizada.png`.

### 4.1b La infografía / "El Patrón" — optimización de hilo conductor (22 jun 2026)

**Nota de nombres:** la página vive en `/infografia` en el repo; durante esta sesión se usó el nombre de trabajo "El Patrón" (referencia a su tesis central: el patrón histórico de Ignoran → Ridiculizan → Adoptan repetido en 6 revoluciones tecnológicas, 1837–hoy).

Se revisó el hilo de storyselling y se identificaron 3 ajustes, todos aplicados:

1. **Gancho de apertura:** la página entraba directo a la tesis sin ningún gancho emocional o de curiosidad antes de los datos. Se agregó un párrafo breve después del logo, antes del badge educativo: *"Quizás te ha pasado: alguien te habla de algo nuevo, y tu primera reacción es dudar..."* — apela a la experiencia del lector sin nombrar a Carlos (tono más documental/analítico que la carta, decisión intencional para esta pieza).

2. **Bridge antes del CTA:** el cierre inspiracional saltaba directo al botón de WhatsApp sin explicar qué obtiene la persona al escribir. Se agregó una línea entre el cierre y el botón: *"Si esto resuena, no te pedimos que decidas nada todavía. Te pedimos una conversación..."*

3. **CTA más abierto:** el botón decía "Quiero la llamada de 20 minutos" — presuponía el mismo formato que usa la carta para Hand4Hand, cuando esta página es más temprana en el embudo y no presupone si la persona terminará como builder o en otro tipo de colaboración. Cambiado a **"Quiero la conversación"**.

✅ Publicado (commit `e515b12`).

Ver sección 4.0 para la resolución de duplicación de contenido con esta página (tabla de eras económicas, antes repetida completa en la carta).

### 4.2 SEO e indexación en buscadores

**Archivos técnicos agregados en la raíz del repo:**
- `sitemap.xml` — lista las 4 páginas del sitio (carta, infografía, diversifica, servicios) con prioridad y frecuencia de cambio
- `robots.txt` — permite el rastreo completo del sitio y apunta a `sitemap.xml`
- Archivo de verificación de Google (`google4faf14065532c62d.html`) — no eliminar, mantiene la verificación de propiedad activa en Search Console

**Google Search Console:**
- ✅ Propiedad `infinexa.app` verificada (método: archivo HTML)
- ✅ Sitemap enviado
- ✅ Indexación solicitada y confirmada para: la carta (`infinexa.app`), la infografía (`infinexa.app/infografia`), Diversifica (`infinexa.app/diversifica`)
- ⏸️ Servicios (`infinexa.app/servicios`) — indexación pendiente, en pausa por decisión propia (la página aún no está lista para recibir tráfico de búsqueda directa)

**Flujo para indexar páginas nuevas a futuro:** Search Console → Inspección de URLs → pegar la URL nueva → "Solicitar indexación". No es necesario repetir la verificación del dominio, ya quedó configurada una sola vez para todo `infinexa.app`. Recordar también agregar cada página nueva a `sitemap.xml` cuando se publique.

### 4.3 Corrección de assets duplicados e íconos (19 jun 2026)

**Síntoma reportado:** Diversifica se veía distorsionada al anclar a pantalla de inicio en iPhone (logo pixelado/deformado), mientras que las demás páginas se veían nítidas. La vista previa de Open Graph al compartir por WhatsApp, en cambio, sí se veía bien en todas.

**Causa raíz real (no era solo transparencia):** existían dos carpetas de assets paralelas en el repo:
- `assets/` — la carpeta real y activa, usada por la carta, infografía, servicios y el builder `carlos`
- `infinexa-assets/files/` — carpeta huérfana, creada por error en una sesión anterior, sin ninguna referencia real en ninguna página

Diversifica apuntaba a la carpeta huérfana, que tenía una versión vieja del `apple-touch-icon.png` con canal alfa (RGBA/transparencia) — formato que iOS no renderiza bien para este uso específico, causando la distorsión visual.

**Resolución:**
1. Regenerados `favicon.png` (32×32), `apple-touch-icon.png` (180×180, esquinas cuadradas sin redondear — iOS las redondea automáticamente) y `og-image.png` (1200×630) directamente desde el SVG vectorial fuente, confirmando modo RGB sin transparencia en los tres.
2. Verificado con `grep -rn "assets" --include="*.html" .` qué carpeta usaba cada página antes de tocar nada.
3. Reemplazados los tres archivos en `assets/` (la carpeta correcta) para las páginas existentes.
4. Corregidas las rutas de `diversifica/index.html` para usar `/assets/` en lugar de `infinexa-assets/files/`, dejando las 5 páginas/builders consistentes.
5. Eliminada por completo la carpeta `infinexa-assets/` tras confirmar que ninguna página la referenciaba.

**Lección para futuras sesiones:** antes de crear cualquier carpeta nueva de assets/imágenes de marca, verificar primero con `grep -rn "assets" --include="*.html" .` desde la raíz del repo si ya existe una convención establecida — evita crear carpetas duplicadas que generan inconsistencias silenciosas entre páginas.

### 4.4 Blog de Infinexa

**Estado:** ✅ Publicado en `infinexa.app/blog`, **15 posts activos** con
sistema de principios visuales numerados, QR compartible dinámico,
enlace discreto a `/donativo/`, y audio en el post #1. Cada post tiene
campo `date:` explícito con hora (ver regla de orden en `_gestion/PROMPT_BLOG.md`).

**Arco Bitcoin (6 posts, historia de blockchain): completo ✅ (#10–#15).**
Detalle completo en `_gestion/PROMPT_BLOG.md`.

**Posts publicados:**

| # | Título | Pilar | Principios |
|---|---|---|---|
| 1 | Ingreso vs. activo | Diversifica | 2 |
| 2 | Por qué la misma crisis se repite | Historia económica | 1 |
| 3 | ¿Por qué rechazamos lo nuevo? | El Patrón | 1 |
| 4 | Wallet no custodial | La carta | 1 |
| 5 | El cajero automático y la desconfianza | El Patrón | 1 |
| 6 | Stablecoin vs. Bitcoin | La carta | 3 |
| 7 | Historia del dinero: del trueque al dólar digital | Historia económica | 3 |
| 8 | El impuesto silencioso (inflación) | Diversifica | 3 |
| 9 | Ingreso pasivo: lo que sí es | Diversifica | 3 |
| 10 | Las piezas sueltas de un rompecabezas de 30 años | El Patrón | 3 |
| 11 | Una idea que fracasó antes de tener éxito (eCash/DigiCash) | El Patrón | 3 |
| 12 | El documento de nueve páginas que cambió todo (whitepaper) | La carta | 2 |
| 13 | El mensaje escondido en el primer bloque de la historia (bloque génesis) | La carta | 2 |
| 14 | Quién guarda la verdad cuando nadie está a cargo (nodos/mineros) | El Patrón | 2 |
| 15 | De un experimento de nueve páginas a la infraestructura del dinero de hoy (cierre) | Diversifica | 2 |
| 13 | El mensaje escondido en el primer bloque de la historia (bloque génesis) | La carta | 2 |

**Sistemas activos en todos los posts:**
- Bloque `.principio` — tarjeta con círculo numerado cobre, línea lateral,
  número translúcido de fondo. CSS en `_layouts/post.html`.
- QR compartible dinámico — generado con `window.location.href` al cargar.
- Enlace discreto a `/donativo/` — después del CTA de pilar.
- Audio en post #1 (ElevenLabs, Narración, español mexicano).

**QR compartible también instalado en todas las páginas standalone:**
carta, servicios, diversifica, infografía, donativo.

La guía completa vive en `_gestion/BLOG_GUIA.md`. El detalle por sesión
en `_gestion/BITACORA.md`.

---

## 5. Servicios y precios (servicio completo, marca propia)

**"Presencia digital lista en 48 horas"**

| Concepto | Precio |
|---|---|
| Setup inicial | $2,000 USDT |
| Mensualidad | $97 USDT/mes |
| Anualidad (con descuento) | $797 USDT/año (~$66/mes, ahorro de $367) |

**Incluye:** identidad de marca, sitio web, dominio configurado, materiales de prospección, capacitación en vivo, 7 días de soporte post-entrega.

**Pago:** USDT en red Polygon. Wallet: `0xb20f9ed762b3d11c6c293d6271b7024cfd888951`

**LTV estimado:** ~15 meses de retención promedio = ~$3,455 USD por cliente total (setup + mensualidades)

---

## 6. Sistema de builders ("Builder Edition")

**Modelo:** venta de subdominios bajo la marca Infinexa a otros builders de Hand4Hand, sin necesidad de marca propia.

- Formato de subdominio: apodo o marca personal del builder (ej. `carlos.infinexa.app`)
- Páginas incluidas: carta + infografía (2 páginas)
- Precio sugerido: Setup $300–500 USDT + $47 USDT/mes (o $397 USDT/año)

**Estado actual:**
- ✅ Infraestructura técnica funcionando — `carlos.infinexa.app` resuelve correctamente con SSL
- ✅ Worker de redirección configurado y desplegado
- 🔧 **Pendiente:** generar el HTML personalizado del builder de prueba (`carlos`) — la carta y la infografía deben ser réplicas exactas del diseño principal, usando variables:
  - `{{NOMBRE}}` — nombre completo del builder
  - `{{APODO}}` — subdominio
  - `{{ROL}}` — rol o ciudad
  - `{{WHATSAPP}}` — número con código de país

**Flujo para agregar un nuevo builder:**
1. Reemplazar variables en los templates (`carta.html` e `infografia.html`)
2. Colocar en `builders/{apodo}/index.html` y `builders/{apodo}/infografia/index.html` (o directamente en `{apodo}/` en la raíz del repo)
3. `git add`, `git commit`, `git push`
4. El subdominio queda vivo automáticamente en 1–2 minutos

**Nota de cumplimiento (23 jun 2026):** dado que el hallazgo de la sección 4.0 (mecánica de Ciclos 2×2) afecta a la carta que usan los builders, una vez se ejecute la corrección en la página principal, replicar el mismo cambio en los templates de builders para mantener consistencia.

---

## 7. Estrategia de prospección

**Materiales listos:**
- Imagen para estado de WhatsApp ("¿En cuál etapa estás tú?") diseñada en Claude Design — calidad superior a generación por código
- Imagen alternativa sin CTA "Escríbeme" para envío directo
- Mensajes de WhatsApp redactados (enfoque "cercano y directo" y "profesional y considerado")
- **Infografía de Diversifica actualizada** (23 jun 2026)
- **Arte + texto WhatsApp para post #1 — Ingreso vs. activo (6 jul 2026):** primera pieza de la serie de artes por post del blog. Arte PNG 680×920px, paleta Infinexa completa, texto bajo framework PAS + Gancho Deslizante (5 líneas + firma). URL verificada: `infinexa.app/blog/ingreso-vs-activo/`. Proceso completo documentado en RECETAS.md sección 11. — ver sección 4.1, datos verificados 65%/45%/29% con fuente citada (Tom Corley)
- **Pieza de Día del Padre** (23 jun 2026) — ejercicio de buena voluntad de marca, no prospección directa, con logo real y nuevo pipeline de render

**Estrategia para grupos abiertos de WhatsApp:**
1. Enviar la imagen sola primero (sin texto)
2. 3 segundos después, enviar texto corto con el link a la infografía
3. Responder personalizadamente a quien reaccione o escriba
4. Rotar contenido en ciclos de 4 semanas para no sonar repetitivo
5. Mejor horario: 8–9am y 8–9pm; domingos en la noche también funcionan bien
6. No publicar más de 1 vez por semana en el mismo grupo

**Pendiente:** generar los 4 textos de las 4 semanas de rotación de contenido (ofrecido, no confirmado aún por el usuario)

**Plan de contenido orgánico para Facebook (19 jun 2026, sesión Claude.ai):** ver `_marketing/PLAN-ORGANICO.md` para el plan de contenido orgánico de 4 semanas en Facebook (12 publicaciones completas, listo para usar). Dirigido a la red personal de Alejandro (2,000+ contactos, audiencia tibia, sin contenido previo publicado). Sigue una escalera de convicción de 4 fases — Despertar → Educación → Revelación → Conversión — donde Hand4Hand no se menciona hasta la semana 3. El plan completo, sus reglas de cumplimiento y las imágenes de apoyo viven en la carpeta `_marketing/`, separada de `_gestion/` porque es contenido de marketing (cambia seguido, es desechable) y no estado técnico del proyecto.

**Incidente de cuenta de WhatsApp Business y guía de cumplimiento (23 jun 2026):** la cuenta de WhatsApp Business de Alejandro tuvo una restricción temporal (bloqueo, luego envío lento al reactivarse). Se investigó la causa probable y se generó una guía completa de cumplimiento — ver sección 10 para dónde vive (`_gestion/RECETAS.md`). Resumen: no es solo el texto lo que dispara restricciones, sino también el patrón de envío (mensajes idénticos masivos, hashes repetidos, reputación del dominio compartido). Mensaje ajustado se envió sin problema tras aplicar la guía.

---

## 8. Próximos pasos inmediatos

1. ~~🔴 Prioritario — Ejecutar la eliminación de la mecánica de Ciclos 2×2 del Escalón 4 de la carta~~ — ✅ **Resuelto el 13 jul 2026**, ver sección 1.1. Superado además por la decisión de eliminar Hand4Hand por completo, no solo la mecánica de ciclos.
1b. **🔴 Nuevo prioritario — Decidir qué pasa con `builders/carlos/`, `builders/_template/` y `carlos/`** (landings de Hand4Hand del sistema Builder Edition, `carlos.infinexa.app` en vivo para un tercero real). No se tocaron en la sesión del 13 jul — requiere que Alejandro decida primero (¿avisar a Carlos? ¿dar de baja el subdominio? ¿migrar a una landing propia de Hand4Hand fuera de Infinexa, backlog Fase 3?) antes de que el código se modifique.
1c. ~~Continuar las fases del reposicionamiento de Infinexa (auditoría de claims del blog)~~ — ✅ **Resuelto el 13 jul 2026**, ver sección 1.5. Quedan pendientes de sesión(es) futuras: SEO técnico más amplio (títulos/canonicals/structured data), analítica real y accesibilidad.
2. **Blog — próximos posts identificados (no escritos todavía):** Remesas y USDT (cómo enviar dinero sin banco, datos reales de comisiones, pilar la carta) · El dinero y la inflación en profundidad (tema escrito como post #8, puede ampliarse con más datos) · Posts futuros sobre DeFi en práctica.
3. **Audio pendiente para posts #2–#9** — flujo documentado en sección 9.3 de `BLOG_GUIA.md`. Scripts de ElevenLabs pendientes de generar para cada post.
3b. ⚠️ *Posiblemente obsoleto tras el pivote del 13 jul — confirmar con Alejandro antes de ejecutar:* generar HTML completo de `carta.html` e `infografia.html` para el sistema de builders (templates con variables).
4. ⚠️ *Posiblemente obsoleto tras el pivote:* terminar de personalizar y publicar el builder de prueba `carlos` — ver 1b, depende de la decisión sobre Builder Edition.
5. Aplicar el nuevo logo al sitio web en vivo (`infinexa.app`)
6. Importar los SVG de marca a Figma/Illustrator y generar exportaciones PNG
7. ⚠️ *Posiblemente obsoleto tras el pivote:* decidir si se generan los 4 textos de prospección semanal para grupos de WhatsApp (prospección apuntaba a Hand4Hand).
8. ⚠️ *Posiblemente obsoleto tras el pivote:* evaluar primer cliente real para Builder Edition (Hand4Hand). El servicio completo de Infinexa Digital/Servicios sigue vigente.
9. Compartir la infografía de Diversifica actualizada (65%/45%/29%, fuente Tom Corley) en estados/grupos, enlazando a `infinexa.app/diversifica/`
10. Cuando la página de Servicios esté lista para tráfico de búsqueda directa, solicitar su indexación en Google Search Console (mismo proceso ya usado para las otras 3 páginas)
11. Agregar cada página nueva que se publique a futuro tanto al `sitemap.xml` como a la solicitud de indexación en Search Console
12. Subir los dos documentos de marca actualizados (`Infinexa_Manual_de_Marca.docx`, `Infinexa_Brand_Identity_Brief.docx`) al repositorio, y eliminar las versiones anteriores (PDF del Manual y `infinexa-brand-brief.docx` viejo) una vez confirmado que el contenido fue migrado completo
13. Ejecutar la semana 1 del plan de contenido orgánico en Facebook (`_marketing/PLAN-ORGANICO.md`) y registrar resultados reales (DMs recibidos, llamadas agendadas) en `BITACORA.md` para ajustar las semanas siguientes con datos, no con intuición
14. ~~Revisar si la infografía de WhatsApp tiene el mismo desbalance detectado en Diversifica~~ — ✅ **Resuelto.** Revisión completa hecha en sesión del 22 jun 2026 (ver sección 4.1b).
15. Aplicar la guía de cumplimiento Meta/WhatsApp (sección 10 / RECETAS.md) a futuras revisiones de copy en todas las páginas, especialmente antes de correr cualquier campaña de Meta Ads o Google Ads

---

## 9. Datos clave de referencia

- **Repo:** `github.com/Appsalex/infinexa`
- **Dominio:** `infinexa.app`
- **Wallet USDT (Polygon):** `0xb20f9ed762b3d11c6c293d6271b7024cfd888951`
- **WhatsApp Alejandro:** +52 646 117 3209
- **Carpeta local:** `~/Downloads/infinexa-repo`
- **Worker Cloudflare:** `infinexa-builders`
- **Significado del nombre:** Infinite + Nexus = Infinexa — "el punto de conexión donde las posibilidades infinitas se transforman en valor con propósito"

---

## 10. Sistema de gestión de trabajo

Para complementar este archivo (que documenta el *estado* del proyecto), se crearon archivos adicionales en `_gestion/` y `_marketing/` dentro del mismo repo:

- **`_gestion/RECETAS.md`** — prompts e instrucciones reutilizables por tipo de actividad (páginas web, infografías para WhatsApp, generación de favicons, investigación de datos, auditoría de copy, flujo de git, SEO, Meta Debugger, auditoría de documentos de marca, planes de contenido orgánico). Se consulta cuando se quiere repetir algo que ya funcionó antes, sin tener que redactar el prompt desde cero. **Actualizado 23 jun 2026:** se agregó la sección "Cumplimiento de envío y diseño — WhatsApp/Meta" — guía consolidada sobre cómo WhatsApp detecta spam sin leer el contenido cifrado (metadatos, hash del mensaje, reportes, reputación de dominio), checklist de qué sí/qué no hacer en envíos, y extensión de los mismos principios a páginas web y diseños (confirmado: una sola copia en el archivo, sin duplicados).
- **`_gestion/BITACORA.md`** — registro cronológico append-only (solo se agrega, nunca se reescribe lo viejo) de qué se hizo en cada sesión y cuándo. Sirve para reconstruir el hilo de decisiones sin tener que leer transcripciones completas.
- **`_marketing/`** — contenido de marketing de atracción (planes de publicación, copys, imágenes de campaña). Separado de `_gestion/` porque este contenido es desechable/rotativo, a diferencia de los prompts reutilizables y el registro histórico.

**Cuándo actualizar cada uno:** al cierre de una sesión, pedir a Claude "agrega esto a la bitácora" o "guarda este prompt en recetas" — igual que se hace con este `ESTADO.md`.

---

## Cómo usar este archivo

- Antes de cerrar una sesión de trabajo, actualiza las secciones correspondientes con lo que se completó o lo que quedó pendiente.
- No crear archivos nuevos por conversación — todo se integra aquí.
- Al iniciar una nueva conversación con Claude, comparte el contenido relevante de este archivo (o el archivo completo) para dar contexto inmediato sin tener que reconstruir el historial.
