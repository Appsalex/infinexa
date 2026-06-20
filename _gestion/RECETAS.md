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

## 9. Auditoría y optimización de documentos de marca en dos capas

**Cuándo usar:** cuando tengas dos o más documentos de marca (ej. un manual de tono/estrategia y un brief técnico/visual) y quieras saber si se solapan, si deben fusionarse, o si conviene mantenerlos separados pero mejor conectados entre sí.

**Prompt:**
```
Tengo estos documentos de marca: [LISTA LOS ARCHIVOS]. Quiero saber:
¿cuál es la diferencia real entre ellos?, ¿hay contenido duplicado?,
¿deberían fusionarse en uno solo o mantenerse separados? Si conviene
mantenerlos separados, optimízalos para que:

1. Cada uno tenga una sección breve al inicio ("cómo usar este
   sistema de documentos") que explique cuándo consultar cuál.
2. Se elimine cualquier duplicación de contenido técnico (paleta de
   color, tipografía, especificaciones) — que viva en un solo lugar
   y el otro documento solo lo referencie.
3. Se agreguen cajas de referencia cruzada en los puntos exactos
   donde un documento necesita información del otro.
4. Queden numerados como "Documento X de Y del sistema de marca".

No fusiones los documentos salvo que la duplicación sea tan grande
que ya no se justifique mantenerlos separados.
```

**Cómo agregar una sección nueva a un documento de marca ya existente (ej. políticas de cumplimiento, lineamientos legales):**
```
Antes de escribir nada, investiga la información vigente y actual
sobre [TEMA — ej. políticas de anuncios de Meta/Google para
contenido financiero o cripto, políticas de WhatsApp Business contra
spam, regulación local relevante]. No uses solo tu conocimiento
general — las políticas de estas plataformas cambian seguido.

Una vez investigado, agrega una sección nueva al documento [NOMBRE],
manteniendo la numeración consecutiva de las secciones existentes
(si insertas en medio, renumera lo que sigue). Incluye una nota
aclarando que esto no sustituye asesoría legal y que las políticas
deben verificarse en la fuente oficial antes de cualquier campaña
pagada.
```

**Ejemplo ya resuelto (19 jun 2026):** se comparó el `Manual de Marca` (PDF v1.0, capa estratégica/verbal) contra el `Brand Identity Brief` (DOCX, capa técnica/visual). Se determinó que no debían fusionarse — cubren audiencias distintas (quien escribe un post vs. quien produce un logo) — pero sí debían optimizarse: se eliminó la duplicación de la paleta de color, se agregaron referencias cruzadas, y se renumeraron como "Documento 1 de 2" / "Documento 2 de 2". Después se agregó al Manual una sección nueva de cumplimiento de políticas de plataforma (Meta Ads, Google Ads, WhatsApp Business, contexto regulatorio CONDUSEF/CNBV en México), investigada con búsqueda web antes de escribirse. Ambos quedaron en formato DOCX (`Infinexa_Manual_de_Marca.docx`, `Infinexa_Brand_Identity_Brief.docx`), versión 1.1.

**Nota técnica (si generas los documentos con la librería `docx` de Node.js):** al usar bordes de párrafo en los cuatro lados (`top`/`left`/`bottom`/`right`), la librería puede emitir el XML en un orden que no pasa la validación OOXML estricta, sin importar el orden en que se declaren las propiedades en el código. Si la validación falla con un error de tipo "Element left/right not expected", hay que desempacar el `.docx`, corregir manualmente el orden de las etiquetas (`top`, `left`, `bottom`, `right`, en ese orden exacto) en `word/document.xml`, y volver a empacar.
