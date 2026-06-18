# ESTADO · INFINEXA

> Este archivo es la fuente única de verdad del proyecto. Se actualiza después de cada sesión de trabajo, sin importar en qué conversación de Claude se realizó. No se crean archivos nuevos por conversación — siempre se edita este mismo documento.

**Última actualización:** 17 de junio, 2026 (sesión: construcción y publicación de Diversifica)

---

## 1. Resumen del proyecto

Infinexa es una marca digital que conecta personas con conceptos de finanzas descentralizadas (DeFi) y sirve como funnel de prospección hacia Hand4Hand. El proyecto se construyó desde cero usando Claude Code, con sitio web propio, identidad de marca completa, y un modelo de negocio de dos capas: venta del servicio completo a terceros, y venta de subdominios bajo la marca Infinexa ("Builder Edition") a otros builders de Hand4Hand.

---

## 2. Infraestructura técnica

- **Repositorio:** `github.com/Appsalex/infinexa` (público, autodeploy vía GitHub Pages)
- **Dominio:** `infinexa.app`, gestionado en Cloudflare
- **DNS:** 4 registros A apuntando a IPs de GitHub Pages (185.199.108–111.153) en modo DNS only; CNAME `www` → `appsalex.github.io`
- **Wildcard para builders:** CNAME `*.infinexa.app` → `appsalex.github.io` en modo **Proxied** (nube naranja)
- **SSL/TLS:** modo **Full** activado en Cloudflare para generar certificados automáticos en subdominios wildcard
- **Cloudflare Worker:** `infinexa-builders` — hace proxy transparente de cualquier subdominio (excepto `www`, `infinexa`, `app`) hacia la carpeta correspondiente en `infinexa.app/{subdominio}`
- **Workers Route:** `*.infinexa.app/*` → Worker `infinexa-builders`
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
| `infinexa-brand-brief.docx` | DOCX | Brief técnico completo: historia del nombre, especificaciones del símbolo (paths SVG, propiedades de trazo), paleta con muestras, tipografía, lockups, zonas de exclusión, usos incorrectos, tabla de entregables |

**Pendiente:** importar los SVG a Figma/Illustrator y convertir textos a outlines; exportar PNG en 1x/2x/3x; instalar Inter como fuente del sistema; aplicar el símbolo actualizado al sitio web en vivo (actualmente el sitio puede tener la versión visual anterior).

---

## 4. Páginas publicadas

| Página | URL | Estado |
|---|---|---|
| La carta | `infinexa.app` | ✅ Publicada |
| La infografía | `infinexa.app/infografia` | ✅ Publicada — gradiente corregido hasta DeFi, tipografía igualada con la carta |
| Servicios | `infinexa.app/servicios` | ✅ Publicada — con precios USDT y wallet (sin QR) |
| Diversifica | `infinexa.app/diversifica` | ✅ Publicada — ver detalles abajo |

**Detalles técnicos resueltos en la infografía:**
- Gradiente de la barra histórica corregido para terminar exactamente en el marcador "DeFi"
- Cursivas y texto de cuerpo corregidos de `--plata` a `--cobre`/`--plata-cl` para igualar el brillo de la carta

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
8. Línea divisoria — sistema tradicional vs. descentralizado, con el matiz de "terreno apenas en construcción" y ventana de oportunidad temprana — en acordeón
9. El legado — "a veces alguien tiene que dar el primer paso" (visible siempre, fondo grafito)
10. Cierre/CTA — "Conoce. Explora. Empieza a construir." + botón WhatsApp con mensaje prellenado

**Decisión de formato — de carrusel a scroll:** la primera versión se construyó como carrusel de pantalla completa (un slide por pantalla, navegación por swipe/flechas). Se abandonó por completo porque en móvil bloqueaba el zoom nativo del navegador (el gesto de pinch-zoom hacía avanzar al siguiente slide en vez de ampliar el texto), y los tamaños de fuente quedaban forzadamente pequeños para que todo el contenido cupiera en una sola pantalla. Se reconstruyó como página de scroll vertical normal, replicando el mismo sistema visual de la infografía (`card` centrada con `box-shadow`, header con lockup horizontal, badge superior, tipografía en clamps generosos, secciones con fondo `--grafito` para los momentos de mayor peso narrativo).

**Sistema de acordeones:** 5 de los 10 bloques de contenido (los más largos/expositivos) están colapsados por defecto, replicando el patrón ya usado en la infografía (`acord-section`, `acord-trigger`, `acord-panel` con `max-height` animado). Los bloques de mayor peso emocional/persuasivo (apertura, "el giro", "diversificar no es abandonar", "el legado", cierre) se dejaron siempre visibles sin acordeón.

**Open Graph corregido:** se agregó el set completo de meta tags (`og:title`, `og:description`, `og:image`, `og:url`, Twitter Card) apuntando a los assets oficiales en `infinexa-assets/files/og-image.png` y `favicon.png`/`favicon.svg` — la primera versión no tenía ningún tag Open Graph, por lo que no se generaba vista previa al compartir en WhatsApp.

**Bug de CSS resuelto (relevante para futuras páginas):** en la versión carrusel, un media query de `max-width:720px` estaba posicionado *antes* de las reglas base de tipografía en el archivo. En CSS, con igual especificidad, la regla que aparece después en el código gana — así que las reglas base (más abajo) sobreescribían silenciosamente todas las correcciones de móvil, sin importar el ancho de pantalla real. Lección para futuras páginas: los media queries siempre deben ir *al final* del bloque `<style>`, después de todas las reglas base que pretenden sobreescribir.

**Pendiente:** verificar en Meta Debugger (`developers.facebook.com/tools/debug/`) que la advertencia de `og:image` faltante ya no aparezca con la versión final desplegada (la última verificación fue con una versión anterior a la corrección de Open Graph).

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

---

## 7. Estrategia de prospección

**Materiales listos:**
- Imagen para estado de WhatsApp ("¿En cuál etapa estás tú?") diseñada en Claude Design — calidad superior a generación por código
- Imagen alternativa sin CTA "Escríbeme" para envío directo
- Mensajes de WhatsApp redactados (enfoque "cercano y directo" y "profesional y considerado")

**Estrategia para grupos abiertos de WhatsApp:**
1. Enviar la imagen sola primero (sin texto)
2. 3 segundos después, enviar texto corto con el link a la infografía
3. Responder personalizadamente a quien reaccione o escriba
4. Rotar contenido en ciclos de 4 semanas para no sonar repetitivo
5. Mejor horario: 8–9am y 8–9pm; domingos en la noche también funcionan bien
6. No publicar más de 1 vez por semana en el mismo grupo

**Pendiente:** generar los 4 textos de las 4 semanas de rotación de contenido (ofrecido, no confirmado aún por el usuario)

---

## 8. Próximos pasos inmediatos

1. Verificar en Meta Debugger que `infinexa.app/diversifica` ya muestra correctamente el `og:image` sin advertencias (forzar "Volver a extraer")
2. Generar HTML completo de `carta.html` e `infografia.html` para el sistema de builders (templates con variables)
3. Terminar de personalizar y publicar el builder de prueba `carlos`
4. Aplicar el nuevo logo al sitio web en vivo (`infinexa.app`)
5. Importar los SVG de marca a Figma/Illustrator y generar exportaciones PNG
6. Decidir si se generan los 4 textos de prospección semanal para grupos de WhatsApp
7. Evaluar primer cliente real para el servicio completo o para Builder Edition
8. Considerar agregar Diversifica al pipeline de prospección por WhatsApp (mensaje + link, mismo patrón que la infografía)

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

## Cómo usar este archivo

- Antes de cerrar una sesión de trabajo, actualiza las secciones correspondientes con lo que se completó o lo que quedó pendiente.
- No crear archivos nuevos por conversación — todo se integra aquí.
- Al iniciar una nueva conversación con Claude, comparte el contenido relevante de este archivo (o el archivo completo) para dar contexto inmediato sin tener que reconstruir el historial.
