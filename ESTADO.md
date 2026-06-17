# ESTADO · INFINEXA

> Este archivo es la fuente única de verdad del proyecto. Se actualiza después de cada sesión de trabajo, sin importar en qué conversación de Claude se realizó. No se crean archivos nuevos por conversación — siempre se edita este mismo documento.

**Última actualización:** 17 de junio, 2026

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

- **Símbolo:** lemniscata (∞)
- **Slogan:** "connecting value with purpose"
- **Colores:**
  - Grafito: `#1F2A33`
  - Grafito oscuro: `#0F1720`
  - Petróleo: `#1B4D5C`
  - Petróleo claro: `#2E6E80`
  - Cobre (único acento cálido, nunca fondo): `#C8682E`
  - Plata: `#C9D2D6`
  - Plata clara: `#EDF1F2`
- **Tipografía:** Inter (300 light para wordmark con tracking amplio, 400 cuerpo, 500 subtítulos, 800 titulares), cargada desde Google Fonts
- **Archivos de marca:** infinexa-icono.svg, infinexa-logo-horizontal.svg, infinexa-logo-negativo.svg, infinexa-logo-positivo.svg, infinexa-portada-linkedin.svg, infinexa-brand-brief.docx

---

## 4. Páginas publicadas

| Página | URL | Estado |
|---|---|---|
| La carta | `infinexa.app` | ✅ Publicada |
| La infografía | `infinexa.app/infografia` | ✅ Publicada — gradiente corregido hasta DeFi, tipografía igualada con la carta |
| Servicios | `infinexa.app/servicios` | ✅ Publicada — con precios USDT y wallet (sin QR) |

**Detalles técnicos resueltos en la infografía:**
- Gradiente de la barra histórica corregido para terminar exactamente en el marcador "DeFi"
- Cursivas y texto de cuerpo corregidos de `--plata` a `--cobre`/`--plata-cl` para igualar el brillo de la carta

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

1. Generar HTML completo de `carta.html` e `infografia.html` para el sistema de builders (templates con variables)
2. Terminar de personalizar y publicar el builder de prueba `carlos`
3. Decidir si se generan los 4 textos de prospección semanal para grupos de WhatsApp
4. Evaluar primer cliente real para el servicio completo o para Builder Edition

---

## 9. Datos clave de referencia

- **Repo:** `github.com/Appsalex/infinexa`
- **Dominio:** `infinexa.app`
- **Wallet USDT (Polygon):** `0xb20f9ed762b3d11c6c293d6271b7024cfd888951`
- **WhatsApp Alejandro:** +52 646 117 3209
- **Carpeta local:** `~/Downloads/infinexa-repo`
- **Worker Cloudflare:** `infinexa-builders`

---

## Cómo usar este archivo

- Antes de cerrar una sesión de trabajo, actualiza las secciones correspondientes con lo que se completó o lo que quedó pendiente.
- No crear archivos nuevos por conversación — todo se integra aquí.
- Al iniciar una nueva conversación con Claude, comparte el contenido relevante de este archivo (o el archivo completo) para dar contexto inmediato sin tener que reconstruir el historial.
