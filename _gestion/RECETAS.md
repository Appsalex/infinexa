# RECETAS · INFINEXA

> Prompts e instrucciones reutilizables, organizados por tipo de actividad. Cuando necesites repetir algo que ya funcionó antes, copia el prompt de aquí y ajusta lo que esté entre [corchetes].
>
> Cómo agregar una receta nueva: cuando algo te funcione bien en una conversación con Claude, pide "agrégalo a RECETAS.md" y se documenta aquí mismo, en la sección que corresponda.

---

## 1. Páginas web (estructura tipo scroll, estilo Infinexa)

**Cuándo usar:** para crear una página nueva de contenido largo (educativa, narrativa, de ventas) que siga el mismo sistema visual que la carta, la infografía y Diversifica.

**Prompt:**
```
Quiero crear una página nueva llamada [NOMBRE] en infinexa.app/[ruta]. 
Sigue exactamente el mismo sistema visual que ya usamos: fondo grafito 
(#0F1720 a #1F2A33), acento cobre (#C8682E), texto en plata clara 
(#EDF1F2), tipografía Inter, formato de scroll vertical normal (NO 
carrusel de pantalla completa — eso ya lo intentamos y falla en móvil 
porque bloquea el zoom nativo).

Estructura: header con logo lockup horizontal + badge superior + 
titular grande, luego secciones de contenido alternando fondo grafito 
para los momentos de mayor peso narrativo, acordeones para el 
contenido más largo/expositivo, y cierre con botón de WhatsApp.

El tema de la página es: [DESCRIBE EL TEMA Y MENSAJE CENTRAL]
```

**Notas importantes que ya aprendimos:**
- Los media queries SIEMPRE van al final del bloque `<style>`, después de todas las reglas base (si van antes, las reglas base las sobreescriben silenciosamente por la cascada CSS).
- No olvidar los meta tags de Open Graph (`og:title`, `og:description`, `og:image`, `og:url`) y el `apple-touch-icon` desde el primer borrador — agregarlos después es fácil de olvidar.
- Usar siempre `https://infinexa.app/infinexa-assets/files/...` (ruta absoluta) para imágenes de marca, nunca rutas relativas (`../`) — los crawlers de redes sociales no siempre las resuelven bien.

---

## 2. Infografías para WhatsApp (estado o grupo)

**Cuándo usar:** para crear una pieza visual tipo infografía, con un dato como gancho, para compartir en estados o grupos de WhatsApp.

**Prompt:**
```
Necesito una infografía de WhatsApp sobre [TEMA]. Formato vertical 
(proporción aproximada 420x860 o 1080x1920 para estado). 

Estructura: eyebrow pequeño arriba, titular grande de impacto, una 
tarjeta destacada con un dato estadístico verificado como gancho 
principal, 3 tarjetas comparativas o de progresión, una sección de 
barras de datos si aplica, pregunta de cierre directa, y logo de 
Infinexa al pie.

Paleta: fondo grafito (#0F1720/#1F2A33), acento cobre (#C8682E), 
texto en plata clara (#EDF1F2). Tipografía Inter.

IMPORTANTE: si el dato estadístico que voy a usar no está verificado, 
investígalo primero con fuentes reales antes de usarlo.
```

**Cómo exportar a PNG con bajo peso (ya resuelto, usar este método):**
```
Genera el HTML/CSS de la infografía con Playwright (sync_playwright), 
viewport del tamaño exacto de la pieza, screenshot del elemento 
específico (no de toda la página), formato PNG. Esto da archivos de 
~60KB, ideal para WhatsApp sin pérdida de calidad.
```

**Ejemplo de referencia:** `infinexa-diversifica.png` (62.8 KB) — infografía "¿Cuántas fuentes de ingreso tienes tú?" con el dato del 65%, generada el 19 jun 2026.

---

## 3. Favicons e íconos (favicon, apple-touch-icon, og-image)

**Cuándo usar:** cuando necesites regenerar o verificar los íconos de una página — para la pestaña del navegador, para anclar a pantalla de inicio en iOS, o para la vista previa al compartir en redes/WhatsApp.

**Prompt:**
```
Necesito generar/verificar los íconos de marca para [PÁGINA]:
- favicon.png (32x32px, para la pestaña del navegador)
- apple-touch-icon.png (180x180px, esquinas CUADRADAS sin redondear 
  — iOS las redondea automáticamente, así que si el archivo ya viene 
  redondeado se ve doble-recortado)
- og-image.png (1200x630px, para vista previa al compartir)

CRÍTICO: ninguno de los tres debe tener canal alfa/transparencia 
(modo RGBA). Deben ser RGB puro con fondo sólido real, porque iOS 
renderiza mal la transparencia en el apple-touch-icon (queda 
distorsionado al anclar a pantalla de inicio).

Genera todos desde el SVG vectorial fuente (infinexa-icono.svg o 
infinexa-logo-negativo.svg), no desde un PNG ya exportado, para 
garantizar nitidez perfecta.
```

**Cómo verificar si un archivo tiene transparencia (diagnóstico):**
```python
from PIL import Image
img = Image.open('archivo.png')
print(img.mode)  # Si dice "RGBA" tiene transparencia — ese es el problema
```

**Bug ya resuelto (19 jun 2026):** el `apple-touch-icon.png` de Diversifica tenía `mode=RGBA` y por eso se veía distorsionado al anclar en iPhone, aunque la imagen de Open Graph (que sí era RGB) se veía perfecta. Se regeneraron los tres archivos desde el SVG vectorial, confirmando RGB puro antes de subirlos.

**Bug raíz más importante (19 jun 2026):** el problema real no era solo la transparencia — era que existían DOS carpetas de assets paralelas (`assets/` y `infinexa-assets/files/`), y Diversifica apuntaba a la equivocada (la huérfana, sin uso real, con la versión vieja). **Antes de crear cualquier carpeta nueva de assets/imágenes de marca, verificar primero si ya existe una con `grep -rn "assets" --include="*.html" .` desde la raíz del repo** — evita crear duplicados que generan inconsistencias silenciosas entre páginas.

---

## 4. Investigación de datos para usar en copy/marketing

**Cuándo usar:** antes de usar cualquier estadística o dato como gancho en una pieza de marketing — nunca usar un dato "que se escucha por ahí" sin verificarlo primero.

**Prompt:**
```
Antes de usar este dato en una pieza de marketing, investiga si tiene 
respaldo real: "[EL DATO QUE QUIERES VERIFICAR]". Quiero saber: 
¿de dónde viene?, ¿qué estudio o fuente lo respalda?, ¿hay matices 
importantes que deba conocer antes de usarlo?
```

**Ejemplo ya resuelto:** la idea de "5 a 7 fuentes de ingreso recomendadas" no tenía buen respaldo. Lo que sí está documentado: 65% de millonarios hechos a sí mismos tienen al menos 3 fuentes de ingreso (45% tienen 4, 30% tienen 5+). Se usó "libertad financiera" en vez de "millonarios" para sonar más alcanzable al avatar de Infinexa.

---

## 5. Revisión de copy para claridad (auditoría de frases confusas)

**Cuándo usar:** cuando una página o pieza ya está escrita pero sientes que alguna frase es confusa o requiere demasiado esfuerzo para entenderse.

**Prompt:**
```
Lee toda la página/pieza completa con ojo crítico de claridad. Para 
cada frase que sea ambigua, abstracta, o requiera esfuerzo extra para 
entenderse, dame: (1) la frase original, (2) por qué es confusa, 
(3) una propuesta de reemplazo más simple y directa. El objetivo es 
que cualquier persona, sin esfuerzo, entienda la idea a la primera 
lectura — sin ser infantil, solo claro.

No cambies nada todavía — primero dame el informe completo para que 
yo apruebe los cambios.
```

---

## 6. Git — flujo de subida de archivos (recordatorio rápido)

**El flujo de siempre:**
```bash
cd ~/Downloads/infinexa-repo
git add [carpeta o archivo]
git commit -m "[descripción del cambio]"
git push
```

**Si aparece error de "rejected" / "diverged":**
```bash
git pull
git push
```

**Configuración ya aplicada una vez (no repetir):** `git config pull.rebase false` — ya se configuró para que `git pull` no vuelva a preguntar por estrategia de merge.

---

## 7. SEO e indexación de páginas nuevas

**Cuándo usar:** cada vez que publiques una página nueva, para que Google la indexe rápido.

**Pasos:**
1. Agregar la URL nueva a `sitemap.xml` (en la raíz del repo)
2. Ir a Google Search Console → Sitemaps → reenviar `sitemap.xml` (si ya está enviado, Google la detecta solo en el siguiente rastreo)
3. Ir a Inspección de URLs → pegar la URL nueva → "Solicitar indexación"
4. No es necesario repetir la verificación del dominio — ya quedó configurada una sola vez para todo `infinexa.app`

---

## 8. Verificación de vista previa al compartir (Meta Debugger)

**Cuándo usar:** cada vez que publiques o actualices una página, para confirmar que la vista previa de WhatsApp/Facebook se ve bien.

**Pasos:**
1. Ir a `developers.facebook.com/tools/debug/`
2. Pegar la URL de la página
3. Clic en "Depurar"
4. Si la imagen sale vieja o no aparece, clic en "Volver a extraer" para forzar que Facebook vuelva a leer el HTML
5. La advertencia de "Faltan las siguientes propiedades obligatorias: fb:app_id" es normal y no bloqueante — no afecta la vista previa real, solo es necesaria para integraciones avanzadas de Facebook que no usamos

---

## 9. Sincronizar conversaciones viejas con ESTADO/RECETAS/BITÁCORA (19 jun 2026)

**Cuándo usar:** cuando tengas conversaciones distintas y separadas sobre Infinexa (por ejemplo, porque una ya llegó a su límite de longitud y abriste una nueva) y quieras rescatar de ahí solo lo que realmente aporte valor — sin duplicar lo que ya está documentado, y sin reintroducir por accidente algo que ya se descartó o corrigió después.

**Por qué importa este proceso y no uno más simple:** una conversación vieja puede tener decisiones que después cambiaron. Si se le pide a Claude que "agregue todo lo que encuentre" sin comparar primero contra los archivos reales y vigentes, el riesgo no es solo duplicar — es deshacer correcciones sin darte cuenta.

**Prompt (pegar completo en la conversación vieja antes de pedir cualquier actualización):**
```
Estoy trabajando en el proyecto Infinexa (infinexa.app), documentado en tres 
archivos en mi repositorio de GitHub (github.com/Appsalex/infinexa): 
ESTADO.md, _gestion/RECETAS.md y _gestion/BITACORA.md.

Esta conversación en la que te estoy hablando ahora puede contener 
información VIEJA — decisiones que después cambiaron, ideas que se 
descartaron, o pasos que ya se completaron de otra forma en otra 
conversación distinta. Por eso, antes de actualizar cualquiera de los tres 
archivos con algo de esta conversación, necesito que actúes como un FILTRO 
DE CALIDAD, no solo como alguien que agrega información. Sigue este proceso 
exacto, sin excepción:

PASO 1 — Pide la versión real antes de asumir nada.
No uses tu memoria de esta conversación como fuente de verdad. Pídeme que 
te comparta el contenido actual y real de los archivos desde GitHub:
cat ~/Downloads/infinexa-repo/ESTADO.md
cat ~/Downloads/infinexa-repo/_gestion/RECETAS.md
cat ~/Downloads/infinexa-repo/_gestion/BITACORA.md

PASO 2 — Compara, no asumas.
Revisa todo lo que se discutió en esta conversación contra lo que ya existe 
en los archivos reales. Para cada elemento de esta conversación, clasifícalo 
en una de tres categorías:
  (a) YA ESTÁ documentado en los archivos reales → ignóralo, no lo dupliques.
  (b) CONTRADICE algo que ya está documentado y es más reciente → ignóralo, 
      y dime explícitamente qué contradicción encontraste, por si quiero 
      revisarlo yo mismo antes de descartarlo del todo.
  (c) Es información NUEVA, real, y no está en ningún archivo → esto es lo 
      único que se agrega.

PASO 3 — Dame un resumen ANTES de tocar nada.
Antes de escribir cualquier cambio, dame una lista corta de qué vas a 
agregar (solo la categoría c) y qué vas a descartar (categorías a y b, con 
el motivo). Espera mi confirmación antes de generar el archivo actualizado.

PASO 4 — Solo entonces, actualiza.
Una vez que confirme, edita el archivo correspondiente integrando solo lo 
aprobado. Para BITACORA.md: nunca reescribas entradas viejas, solo agrega 
una entrada nueva. Para ESTADO.md y RECETAS.md: si una sección existente 
quedó desactualizada, corrígela en su lugar — no crees una sección 
duplicada diciendo lo mismo de otra forma.

PASO 5 — Valida antes de entregar.
Confirma que la numeración de secciones sigue consecutiva y que no quedó 
ningún encabezado roto o duplicado por la edición.

Confirma que entendiste este proceso de 5 pasos antes de que te pida 
cualquier actualización.
```

**Cómo usarlo paso a paso:**
1. Ábrelo en cualquier conversación vieja sobre Infinexa.
2. Pega el prompt completo y espera la confirmación de Claude.
3. Pide: "revisa toda esta conversación y dime qué valdría la pena llevar a ESTADO.md / RECETAS.md / BITACORA.md".
4. Comparte el `cat` de los tres archivos reales cuando Claude lo pida.
5. **Espera el resumen antes de aprobar nada** — revisa con calma qué se agregaría y qué se descartaría, y corrige a Claude si algo no te parece correcto.
6. Solo después de tu confirmación, sube el archivo final con el flujo de siempre.

---

## 10. Prompts de apertura para conversaciones especializadas por tema (19 jun 2026)

**Cuándo usar:** cuando el proyecto crece y conviene separar el trabajo en conversaciones distintas por área, en vez de seguir todo en una sola conversación gigante. Categorías recomendadas: páginas web, marketing de atracción/contenido, identidad de marca, infraestructura técnica, negocio/builders, y SEO (orgánico y pagado).

**Por qué separar por tema:** cada conversación se mantiene enfocada, tarda más en llegar a su límite de longitud, y es más fácil retomarla después sabiendo exactamente de qué trata. El riesgo de dispersión que esto podría generar se controla con el mismo proceso de verificación de la sección 9 — nunca asumir, siempre comparar contra los archivos reales antes de editar.

**Regla práctica para evitar conflictos:** evitar tener dos conversaciones actualizando los archivos de control (`ESTADO.md`, `RECETAS.md`, `BITACORA.md`) el mismo día al mismo tiempo — cerrar y subir los cambios de una antes de empezar a actualizar desde otra.

### 1. Páginas web (construcción y código)
```
Estoy trabajando en el proyecto Infinexa (infinexa.app). Esta conversación 
es específicamente para construir y modificar páginas web del sitio 
(estructura HTML/CSS, nuevas páginas, ajustes de diseño).

Antes de cualquier cosa, voy a compartirte el ESTADO.md actual del proyecto 
para que tengas contexto. Si en algún momento necesitas actualizar 
ESTADO.md, _gestion/RECETAS.md o _gestion/BITACORA.md con algo de esta 
conversación, sigue este proceso: (1) pídeme el contenido real y actual de 
esos archivos vía 'cat' antes de asumir nada, (2) compara contra lo que se 
habló aquí, (3) dame un resumen de qué agregarías y qué descartarías ANTES 
de tocar nada, (4) solo edita después de mi confirmación.

También revisa si en _plantillas/ ya existe una pieza similar a lo que 
vamos a construir — ahí guardo las versiones finales ya probadas, para 
partir de eso en vez de empezar de cero. Lee también _plantillas/README.md 
si necesitas saber qué hay disponible.
```

### 2. Marketing de atracción / contenido
```
Estoy trabajando en el proyecto Infinexa (infinexa.app). Esta conversación 
es específicamente para marketing de atracción: copy persuasivo, 
infografías para WhatsApp, estrategia de prospección, textos para redes 
sociales y grupos.

Tono de marca que SIEMPRE debe respetarse: sobrio, educativo, sin promesas 
de rendimiento ni lenguaje de "ciclo alcista" o "multiplica tus ahorros". 
La diferenciación de Infinexa frente a la competencia del espacio DeFi es 
precisamente NO sonar como venta agresiva — presentar datos verificados, 
nunca rumores, y dar opciones, nunca presionar.

Antes de cualquier cosa, voy a compartirte el ESTADO.md actual para que 
tengas contexto. Si necesitas actualizar ESTADO.md, _gestion/RECETAS.md o 
_gestion/BITACORA.md, sigue el proceso de verificación de siempre: pide el 
contenido real vía 'cat', compara, dame un resumen antes de tocar nada, 
edita solo después de mi confirmación.
```

### 3. Identidad de marca
```
Estoy trabajando en el proyecto Infinexa (infinexa.app). Esta conversación 
es específicamente para identidad visual: logo, manual de marca, paleta de 
colores, tipografía, exportación de assets (SVG, PNG, favicons).

Antes de cualquier cosa, voy a compartirte el ESTADO.md actual (sección 3, 
Marca e identidad visual) para que tengas contexto completo: historia del 
nombre, sistema del símbolo, paleta exacta, lockups, archivos ya entregados.

Si necesitas actualizar ESTADO.md, _gestion/RECETAS.md o _gestion/BITACORA.md, 
sigue el proceso de verificación de siempre: pide el contenido real vía 
'cat', compara, dame un resumen antes de tocar nada, edita solo después de 
mi confirmación.

Revisa también si en _plantillas/ ya existe algo reutilizable (por ejemplo, 
el sistema de generación de favicons sin transparencia, ya resuelto y 
documentado ahí).
```

### 4. Infraestructura técnica
```
Estoy trabajando en el proyecto Infinexa (infinexa.app). Esta conversación 
es específicamente para infraestructura técnica: Cloudflare, DNS, GitHub 
Pages, Workers, configuración del dominio, bugs técnicos de despliegue.

Antes de cualquier cosa, voy a compartirte el ESTADO.md actual (sección 2, 
Infraestructura técnica) para que tengas contexto completo del setup actual.

Si necesitas actualizar ESTADO.md, _gestion/RECETAS.md o _gestion/BITACORA.md, 
sigue el proceso de verificación de siempre: pide el contenido real vía 
'cat', compara, dame un resumen antes de tocar nada, edita solo después de 
mi confirmación.

Nota importante: en este proyecto ya existe una sola carpeta de assets 
real, llamada `assets/` en la raíz del repo (no crear ninguna carpeta 
nueva con el mismo propósito — esto ya causó un bug confirmado y resuelto, 
documentado en RECETAS.md sección 9 / BITACORA.md 19 jun 2026).
```

### 5. Negocio / builders
```
Estoy trabajando en el proyecto Infinexa (infinexa.app). Esta conversación 
es específicamente para el modelo de negocio: precios, sistema de builders 
("Builder Edition"), prospección de clientes, evaluación de oportunidades.

Antes de cualquier cosa, voy a compartirte el ESTADO.md actual (secciones 
5, 6 y 7: Servicios y precios, Sistema de builders, Estrategia de 
prospección) para que tengas contexto completo.

Si necesitas actualizar ESTADO.md, _gestion/RECETAS.md o _gestion/BITACORA.md, 
sigue el proceso de verificación de siempre: pide el contenido real vía 
'cat', compara, dame un resumen antes de tocar nada, edita solo después de 
mi confirmación.
```

### 6. SEO — orgánico y pagado
```
Estoy trabajando en el proyecto Infinexa (infinexa.app). Esta conversación 
es específicamente para SEO: posicionamiento orgánico en buscadores 
(prioridad actual) y, más adelante, estrategias de SEO pagado. Incluye 
investigación de palabras clave, optimización de metadatos, estructura de 
contenido para buscadores, Google Search Console, y cumplimiento de 
políticas de publicidad relevantes (Google Ads / Meta Ads tienen 
restricciones específicas para contenido financiero/cripto que hay que 
respetar siempre).

Contexto ya investigado (sesión del 19 jun 2026, sin acceso directo a 
Google Trends — investigación cualitativa por búsqueda web):
- Términos de alto interés en el espacio: "diversificar ingresos", 
  "ingresos pasivos", "finanzas descentralizadas", "libertad financiera" 
  (este último ya se usa en el copy actual de Diversifica).
- Riesgo identificado: competidores del espacio DeFi se posicionan con 
  lenguaje de "ciclo alcista" y "multiplica tus ahorros" — Infinexa se 
  diferencia deliberadamente NO usando ese tono, lo cual también ayuda a 
  cumplir políticas de publicidad más estrictas para este tipo de contenido.
- Pendiente real: entrar directamente a trends.google.com y comparar 
  volumen de búsqueda real de los términos candidatos antes de priorizar 
  cuáles trabajar en contenido — la búsqueda web no sustituye los datos 
  reales de Trends.

Estado actual de SEO ya resuelto (ver ESTADO.md sección 4.2): sitemap.xml 
y robots.txt en la raíz del repo, dominio verificado en Search Console, 
3 de 4 páginas ya indexadas (servicios pendiente por decisión propia).

Antes de cualquier cosa, voy a compartirte el ESTADO.md actual completo. 
Si necesitas actualizarlo (o RECETAS.md / BITACORA.md), sigue el proceso 
de verificación de siempre: pide el contenido real vía 'cat', compara, 
dame un resumen antes de tocar nada, edita solo después de mi confirmación.
```



---

## Cumplimiento de envío y diseño — WhatsApp / Meta (lección 23 jun 2026)

### Por qué funciona esto (base técnica)

WhatsApp cifra el **contenido** de los mensajes de extremo a extremo — nadie puede leerlos en tránsito. Pero detecta spam SIN necesidad de leer el contenido, usando:
- **Metadatos:** a cuántos contactos distintos escribes, frecuencia, horario, si son contactos nuevos o existentes.
- **Hash del mensaje:** huella digital matemática del texto. Mensajes idénticos enviados a muchas personas generan el mismo hash — detectable sin descifrar nada.
- **Reportes de usuarios:** quien te bloquea o reporta le envía a Meta una copia legible del mensaje (porque es destinataria). Solo ahí Meta "ve" contenido — y solo lo reportado.
- **Comportamiento de cuenta:** velocidad de envío, tasa de bloqueo, chats nuevos abiertos.
- **Reputación de URL/dominio:** Meta también evalúa el link que compartes (infinexa.app) contra listas de reputación. Si el mismo dominio se reporta mucho, el link puede quedar marcado como sospechoso independientemente del número que lo envíe — esto afecta a TODOS los builders que comparten subdominios de infinexa.app, no solo a quien envía.

**Conclusión:** no te marcan por lo que dices en el sentido de que alguien lo lea — te marcan por cómo lo dices y lo repites. El texto y el patrón de envío pesan igual.

### ✅ Qué SÍ hacer

1. Anclar cifras a una fuente con nombre ("según el estudio de Tom Corley...") en vez de presentarlas como promesa de resultado
2. Variar el saludo o una frase entre contacto y contacto — nunca copy-paste idéntico a muchos números
3. Espaciar los envíos a lo largo del día, nunca en ráfaga
4. Priorizar contactos con conversación previa sobre contactos en frío
5. Mantener tono educativo, sin urgencia artificial
6. Acompañar siempre el link con contexto/storytelling, nunca un link "pelón"

### ❌ Qué NO hacer

1. Usar frases-gatillo de spam financiero: "libertad financiera", "ingresos pasivos", "oportunidad única", "no te lo pierdas"
2. Enviar el mismo mensaje exacto a muchos contactos consecutivos en poco tiempo
3. Mandar mensajes en frío a números sin contacto previo, en volumen
4. Presionar o crear urgencia artificial
5. Enviar solo un link sin texto que lo sustente

### Extensión a páginas web y diseños (no solo WhatsApp)

- Evitar las mismas frases-gatillo también en el copy de las páginas (carta, diversifica, servicios) — si en algún momento se corren Meta Ads o Google Ads hacia estas páginas, la categoría "servicios financieros" recibe revisión extra, y el mismo lenguaje que dispara spam en WhatsApp dispara rechazo de anuncios.
- El dominio infinexa.app es un activo compartido (carta, builders, subdominios) — su reputación afecta a todos. Mantenerlo siempre con lenguaje sobrio protege la entregabilidad de TODO el ecosistema, no solo de un mensaje individual.
- Los meta tags (og:title, og:description) y cualquier texto que se previsualice al compartir un link también deben evitar las mismas frases-gatillo, porque son lo primero que un sistema automático escanea antes de que alguien abra el link.
- Más allá del lenguaje: cuidado especial con cualquier sección que describa mecánica de aportaciones/ciclos con cifras específicas de cómo se activa o escala un sistema — esto pattern-matchea con esquemas piramidales independientemente del lenguaje usado alrededor, y es un riesgo de cumplimiento mayor que cualquier frase-gatillo individual. Ese tipo de "cómo" se reserva para conversación 1:1, nunca para la página pública.

**Nota honesta:** esto es la mejor práctica defensiva derivada de cómo se comportó la cuenta + investigación general de políticas de Meta — no es la lista oficial exhaustiva del algoritmo (Meta no la publica), reduce el riesgo, no lo elimina por completo.

---

## Blog de Infinexa

La guía completa del blog (estructura narrativa, SEO, reglas de
unicidad, especificaciones de imagen, y sus ampliaciones) vive en
`_gestion/BLOG_GUIA.md` — no se duplica aquí. Para cualquier
conversación sobre el blog, pedir a Claude que lea ese archivo
directamente (vía raw.githubusercontent.com o `cat` local).
