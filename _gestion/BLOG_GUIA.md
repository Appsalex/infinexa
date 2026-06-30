# GUÍA DEL BLOG · INFINEXA

> Fuente única de verdad para el blog de Infinexa. Consolida el Prompt
> Maestro, las reglas de unicidad, y las ampliaciones posteriores —
> todo lo que se ha definido en sesiones de trabajo sobre el blog.
>
> Cómo usar este archivo: al iniciar una conversación nueva sobre el
> blog, pide a Claude que lea esta guía desde:
> `https://raw.githubusercontent.com/Appsalex/infinexa/main/_gestion/BLOG_GUIA.md`
> Esto trae el contenido completo y exacto, sin depender de memoria
> entre conversaciones ni de tener que repegar el documento.

---

## 1. Principio rector

Información informa, conocimiento forma, pero solo la sabiduría
transforma. Cada post de Infinexa debe apuntar a lo tercero — el
lector debe sentir que se le ayudó a pensar distinto, no solo que se
le entregaron datos.

**Sello editorial:** cada post debe ayudar al lector a incrementar
alguno de sus activos más importantes: su conocimiento, su criterio,
su carácter, sus relaciones, o su capacidad para generar valor. Si un
post no contribuye de forma tangible al crecimiento de alguno de
estos, se revisa hasta lograrlo.

*Nota: se excluye deliberadamente "patrimonio" de esta lista —
enmarcar el valor del blog como "hace crecer tu patrimonio" es el tipo
de promesa de resultado financiero que la guía de cumplimiento
Meta/WhatsApp (ver `RECETAS.md`) ya identificó como riesgo real, no
solo de tono.*

---

## 2. Tono de marca (no negociable)

- Sobrio, educativo, sin promesas de rendimiento
- Sin lenguaje de "ciclo alcista", "multiplica tus ahorros", urgencia
  artificial o FOMO
- Datos verificados, nunca rumores — siempre con fuente citada
- Siempre presentar opciones, nunca presionar
- Comparte el "qué" (información completa y valiosa por sí misma) y
  reserva el "cómo" específico para conversación 1:1 — nunca como
  gancho oculto, siempre explicado con honestidad

---

## 3. Proceso obligatorio antes de escribir (en este orden)

**PASO 1 — Elegir el tema con demanda comprobada** ("Skyscraper
Technique"). Elegir temas que la gente ya busca activamente — no
inventar temas desde cero. Validar con búsqueda real antes de
continuar.

**PASO 2 — Validar palabras clave y frases de cola larga.**
- Identificar la frase exacta que la gente busca en español (puede no
  coincidir con el marco conceptual o metáfora que se quiere usar —
  detectar ese desajuste ANTES de escribir, no después).
- Si existen dos marcos relacionados pero distintos, usar el marco
  propio como eje central, pero agregar UNA frase puente que conecte
  con el término más buscado sin generar confusión semántica.
- Evaluar el nivel de competencia real del término más buscado — si
  lo dominan sitios con mucha autoridad, no competir de frente;
  identificar en su lugar 4-6 frases de cola larga más específicas y
  con menos competencia.
- Documentar las palabras clave elegidas en el campo `keywords` del
  front matter, para que dos posts no compitan por la misma frase.

**PASO 3 — Verificar que el tema no duplica una página existente.** Si
el tema se solapa con la carta, El Patrón o Diversifica, el post debe
profundizar donde esas páginas NO lo hacen, y enlazar hacia la página
pilar relevante en vez de repetir su contenido. El contenido duplicado
no es una "penalización" de Google — es competencia interna dañina:
dos páginas compitiendo por la misma información se debilitan
mutuamente en vez de fortalecerse.

**PASO 4 — Definir el cluster.** Identificar a qué página pilar
existente se enlaza (Diversifica, El Patrón, la carta), para construir
autoridad temática concentrada en vez de fragmentada.

**PASO 5 — Verificar la idea central.** Antes de dar por terminado el
post, resumir su mensaje en una sola frase clara y específica. Si no
se puede resumir así, es señal de que el post tiene varios mensajes
débiles en vez de uno fuerte — hay que enfocarlo antes de publicar.

---

## 4. Estructura narrativa de cada post

1. **Gancho de pregunta** — algo que el lector ya se preguntó, pero
   formulada de forma que provoque, no que sea obvia o retórica.
   Evitar preguntas genéricas tipo "¿sabías que el dinero está
   cambiando?" (cualquiera respondería que sí) — buscar la versión
   específica que incomoda un poco porque toca algo real (ej. "¿por
   qué dos personas con el mismo sueldo durante veinte años terminan
   en lugares tan distintos?").
2. **Historia breve / epifanía** — mi duda real o la de "Carlos"
   (personaje recurrente, ya establecido en la carta), nunca "yo el
   experto te enseño".
3. **El panorama** — el "qué", con datos verificados y fuente citada,
   completo y valioso por sí mismo.
4. **Línea transparente entre el "qué" y el "cómo"** — honesta sobre
   por qué esa parte requiere conversación 1:1, sin sonar a gancho
   oculto y SIN etiquetar visiblemente la estructura (nunca escribir
   "esto es el qué, esto es el cómo" literal — debe sentirse en el
   tono, no anunciarse como fórmula).
5. **Cierre con 2-3 opciones, nunca presión** — afirmando lo que el
   lector ya se lleva (no describiendo el propio artículo como
   "genérico" o "básico", eso resta valor justo al final) e invitando
   a compartirlo con alguien más, cuando aplique.

---

## 4.1 Ritmo visual tipográfico (evitar la "tira sin respiro")

**Diagnóstico (27 jun 2026):** con solo encabezados H2/H3 como respiro,
un post largo se siente como una sola tira de texto idéntico de
principio a fin — el CSS ya tenía un estilo de `blockquote` (fondo
tintado, borde cobre) pero nunca se usaba porque las citas de Carlos
se escribían en cursiva inline, no como bloque markdown real.

**Tres herramientas tipográficas, ya disponibles en `_layouts/post.html`,
para usar en cada post nuevo:**

- **`{: .lead}`** — en el párrafo de apertura (el gancho), justo
  después del título. Texto más grande y más ligero, marca de entrada
  distinta al cuerpo. Una sola vez por post.
- **Blockquote real (`>`)** — para toda cita textual hablada (Carlos,
  un amigo, un primo, una fuente). Nunca escribir el diálogo en cursiva
  inline con asteriscos — siempre como bloque `>` para que se vea
  visualmente distinto del resto del párrafo. Normalmente aparece 1-2
  veces por post.
- **`{: .insight}`** — para LA frase que resume el giro central del
  post (el "ajá"). Texto centrado, grande, con línea divisoria arriba
  y abajo — el equivalente en HTML de lo que antes era la imagen
  "frase grande". Una sola vez por post, nunca más — si se usa seguido
  pierde el efecto de pausa.

Igual que con la regla de unicidad: variar EN QUÉ PUNTO del post cae
cada elemento (no siempre el insight justo antes del cierre) para que
la pausa se sienta orgánica, no como fórmula repetida.

---

## 4.2 Enfoque de promoción, no de prevención (27 jun 2026)

**El principio:** existen dos formas de motivar a alguien hacia la
misma acción — partir de un miedo a evitar (prevención: "no le temas",
"protégete de", "sin presión", "no te quedes fuera") o partir de una
posibilidad a alcanzar (promoción: "ve la puerta", "descubre",
"construye", "entiende antes que los demás"). Ambas son honestas, pero
la de prevención hace que el lector sienta primero el miedo y después
el alivio; la de promoción lo hace sentir que avanza, no que se
defiende. Esto es lo mismo que ya vive en tu filosofía de faro, no
cazador — el faro no advierte de un peligro, simplemente está ahí.

**Regla práctica para todo lo que se escriba (blog, carta, cualquier
página):**
- Evitar arrancar una frase central con una negación que plante la
  duda que intenta resolver ("no es una pirámide", "sin presión", "no
  le temas al cambio") —mejor describir el estado positivo directo.
- **La línea con "promesas falsas" — dónde está exactamente:**
  lenguaje de posibilidad describe que algo se puede VER o ENTENDER
  antes que otros (percepción, conocimiento) — eso está bien.
  Lenguaje de promesa describe un RESULTADO financiero garantizado
  ("vas a multiplicar", "asegura tus ganancias") — eso sigue
  prohibido, sin excepción, sin importar qué tan optimista sea el
  tono. **Se promete claridad y perspectiva, nunca resultado.**
- Antes de publicar cualquier frase de gancho, cierre, o título:
  preguntarse "¿esto parte de un miedo o de una posibilidad?" — si
  parte de un miedo, reescribir en positivo antes de revisar cualquier
  otra cosa.

**Cómo se descubrió:** el subtítulo original del blog ("sin presión,
con datos verificados") partía de prevención. Se corrigió dos veces —
primero a una versión que seguía partiendo de negación ("no le teme al
cambio"), luego a la versión correcta de promoción ("ve la puerta
antes que los demás"). Dos rondas que se hubieran evitado si esta
sección ya existiera desde antes.

**Excepción importante — auditoría del 27 jun 2026:** "sin presión"
aparece 8 veces en el sitio (la carta, servicios, plantillas de
Builder, plan de marketing), siempre junto a una invitación a llamada/
conversación de WhatsApp. **Esos 8 casos NO se cambian** — ahí la
prevención es legítima porque responde a una objeción real y nombrada
("¿esta llamada va a ser un pitch de venta agresivo?"), no a un miedo
inventado. La regla completa es: **prevención está bien cuando nombra
una objeción específica que el lector de verdad tiene en ese momento
(ej. justo antes de pedirle que agende una llamada); está mal cuando
es atmósfera general sin objeción concreta detrás (ej. el subtítulo de
una página de blog, donde nadie temía nada).** Antes de "corregir" una
frase de prevención, preguntar primero: ¿a qué objeción específica
responde? Si la respuesta es "a ninguna en particular", ahí sí se
reescribe en positivo.

---

## 5. Regla de unicidad (crítica — leer con cuidado)

**Regla general:** cada post del blog debe ser una pieza única de
principio a fin — no solo distinta en el tema que trata, sino distinta
en cómo está escrita: su gancho, su metáfora, su forma de presentar el
panorama, y su cierre. Que dos posts compartan la misma estructura
narrativa base (la sección 4 de esta guía) está bien y es intencional
— lo que NO está bien es que compartan las mismas palabras, los mismos
encabezados, o la misma forma exacta de construir cada sección.

**Reglas concretas:**

1. PROHIBIDO repetir, palabra por palabra, cualquier encabezado o
   frase entre posts distintos — no solo en el cierre, en cualquier
   parte del post (el gancho inicial, las transiciones, los nombres de
   sección). Antes de dar por terminado un post nuevo, comparar TODOS
   sus encabezados contra los de todos los posts ya publicados — si
   alguno coincide o se parece demasiado, reescribir.
2. Variar activamente, de post a post: el encabezado de cierre, si las
   opciones van en lista numerada o en prosa corrida, cuántas opciones
   se ofrecen (2 o 3), en qué parte del post aparece el callback al
   personaje recurrente (Carlos) — al inicio, en medio, o al final — y
   el tipo de gancho inicial (pregunta directa, anécdota, dato
   sorprendente).
3. El objetivo de fondo: que el lector sienta que cada pieza fue
   escrita para él específicamente en ese momento — no que reconozca
   un molde reciclado. Eso es lo que hace que alguien regrese,
   comparta, y trate el blog como una fuente de consulta real — una
   biblioteca, no contenido desechable.

---

## 6. Extensión y formato de lectura

- Mínimo: 1,200 palabras / Rango ideal: 1,500–2,200 / Máximo: 2,500
  (excepto páginas pilar, 3,000+)
- Nunca alargar artificialmente — la extensión es consecuencia de la
  profundidad real del tema
- Mínimo 6 horas de trabajo real por pieza antes de publicar
- Encabezados H2/H3 cada 250–350 palabras; al menos 1-2 con la frase
  clave de forma natural
- Párrafos de máximo 3-4 líneas; viñetas para listas de 3+
- Valor real en los primeros 100 palabras

---

## 7. Enfoque editorial y cadencia

- **"Biblioteca", no "publicación"** — contenido evergreen, sin fechas
  prominentes en el diseño, pensado para tráfico de búsqueda durante
  años, no para lectores que vuelven a diario
- Calidad sobre frecuencia — 1 post excelente cada 2 semanas, sostenido
  durante meses/años
- **E-E-A-T:** nombre real, bio breve con experiencia genuina, fuentes
  reales y verificables — nunca contenido anónimo

---

## 8. Uso de IA en la redacción

No hay penalización de Google por usar IA en sí; se penaliza contenido
de baja calidad sin revisión humana.

- NO buscar formas de "ocultar" el uso de IA — esfuerzo desperdiciado,
  los detectores de terceros son poco confiables
- SÍ aplicar siempre revisión humana real: verificar cada dato, agregar
  experiencia/ejemplos propios, checklist de calidad por capas antes
  de publicar

---

## 9. Imágenes — cantidad, especificaciones y metadatos

**Cantidad:** 1 imagen destacada por post. Las tarjetas de comparación,
listas y líneas de tiempo dentro del cuerpo **ya NO son imagen** — se
construyen en HTML/CSS nativo (ver sección 9.1). Solo se usa imagen de
apoyo para el estilo "frase grande" (una sola declaración visual, sin
columnas de texto pequeño, como `crisis-insight.webp`).

**Por qué cambió (27 jun 2026):** las tarjetas con texto pequeño en
columnas (3-4 por imagen) se volvían illegible en celular — el texto
nace a 1200px y se escala junto con la imagen hasta ~345px reales en
pantalla, cayendo a 4-5px de altura. Además, el texto horneado en una
imagen es invisible para Google (no se indexa, no cuenta como
contenido). Pasarlo a HTML real resuelve ambos problemas a la vez:
texto siempre legible (controlado con `clamp()`, igual que el resto
del post) y contenido indexable. Las imágenes destacadas y la de
"frase grande" se quedan como imagen porque ahí sí funcionan: poco
texto, grande, sin necesidad de escalar columnas.

**Dimensiones y peso (imagen destacada y "frase grande"):**
- Destacada/portada: 1200 × 630 px (ratio 1.91:1), máx 250 KB
- Apoyo tipo "frase grande": ~1200 px de ancho, 150–250 KB
- Logo/iconos de pilar: SVG, integrados en el mismo lienzo Playwright
- Peso total de imágenes por página: bajo 2.5 MB

**Formato:** WebP para la imagen destacada y la de "frase grande", SVG
para logo/iconos, 72 DPI siempre.

**Estilo visual de la imagen destacada (vigente desde 27 jun 2026):**
fondo de constelación (puntos y líneas finas conectando nodos, color
Petróleo claro para las líneas, Plata/Cobre para los nodos) sobre
Grafito — no degradado difuso genérico. Texto reducido a la idea
central (no el título SEO completo) + ícono fijo por pilar:
- **La carta** (economía descentralizada): candado abstracto
- **Diversifica** (diversificación/historia económica): bifurcación/rama
- **El Patrón** (historia y tecnología): ciclo/flecha circular
Los puntos de la constelación nunca se generan dentro de la zona de
texto (columna izquierda) para no cruzar encima del título.

**Metadatos:**
- Alt text descriptivo y específico (nunca relleno de palabras clave)
- Nombre de archivo descriptivo, en español, con guiones, sin espacios
  ni "Captura_de_pantalla"
- EXIF: irrelevante para SEO

**Detalles técnicos:**
- Ancho y alto explícitos en el HTML
- Imagen destacada carga inmediata (sin lazy load)
- Nunca subir al tamaño nativo del pipeline — siempre reescalar antes

**Flujo por imagen:** generar con Chromium/Playwright a 2x → reescalar
al tamaño final → convertir a WebP comprimido → verificar peso →
nombrar descriptivamente → escribir alt text.

---

## 9.1 Tarjetas de comparación, listas y líneas de tiempo (HTML nativo)

Reemplazan lo que antes eran imágenes de apoyo con columnas de texto.
Se escriben directo en el `.md` del post, en HTML crudo (Jekyll/kramdown
lo permite sin problema). Clases ya definidas en `_layouts/post.html`:

- **`.cards-row` + `.card-box`** — 2 o 3 columnas (se apilan solas en
  celular). Variantes: `.card-box.accent` (borde cobre, para resaltar
  la opción "buena" en una comparación), `.card-num` (círculo numerado),
  `.card-label` (etiqueta pequeña en mayúsculas), `.card-title`,
  `.card-quote` (cita en cursiva), `.card-text`, `.card-bullets` (viñetas;
  `.muted` para la columna que no se quiere resaltar).
- **`.timeline-row` + `.timeline-item`** — línea de tiempo horizontal
  con línea conectora; se apila vertical en celular con borde lateral
  en vez de línea horizontal. `.timeline-dot.accent` para resaltar un
  punto. Sirve tanto para años (con `.timeline-year`) como para etapas
  sin año (solo `.timeline-label` + `.timeline-text`).
- **`.section-label-inline`** — encabezado pequeño centrado en mayúsculas,
  reemplaza el texto que antes iba horneado arriba de la imagen.

Antes de usar estas clases en un post nuevo: copiar la estructura de
un bloque ya existente en los posts publicados, no inventar HTML desde
cero, para no romper el espaciado ya calibrado.

---

## 9.2 Reglas de oro para evitar retrabajo (27 jun 2026)

Esta sesión nos costó varias rondas de corrección que se pudieron
evitar. Quedan como regla fija, no como sugerencia:

**1. El logo y cualquier elemento de marca SIEMPRE se copian del activo
original — nunca se redibujan a mano ni se aproximan a otra escala.**
El logo del infinito vive en
`_plantillas/sistema-favicons/codigo-final-render-og-image.py` con sus
coordenadas SVG exactas. Si se necesita en otro tamaño, se envuelve el
mismo `<path>` en un `<g transform="translate(X,Y) scale(S)">` y se
calcula la matemática — nunca se vuelve a trazar la curva a ojo. Redibujar
a mano fue exactamente el error que causó dos rondas de corrección del
logo en esta sesión.

**2. Checklist obligatorio antes de entregar cualquier imagen o cambio
visual — los cuatro puntos, no solo los que parezcan obvios:**
1. Legibilidad del texto a tamaño real de uso (no solo a tamaño completo)
2. Cumplimiento de marca y paleta
3. **Balance compositivo** — ¿el peso visual se reparte entre ambos
   lados del lienzo, o se amontona en uno? Verificar visualmente, no
   asumir.
4. Simulación a ancho de celular (~390px) antes de dar por buena
   cualquier imagen — redimensionar y ver, no solo calcular en teoría.

**3. Centrado de contenedores: todo bloque con `max-width` fijo debe
llevar `margin: 0 auto` junto con él.** `max-width` sin `margin:auto`
deja el contenido pegado a la izquierda en pantallas anchas — fue la
causa real de "se ve cargado a un lado", no la imagen.

**Reincidencia confirmada (30 jun 2026):** este mismo error se repitió
en la página `/donativo/`, una página nueva escrita desde cero — es
decir, la regla ya estaba documentada arriba, pero no se aplicó como
paso activo al escribir CSS nuevo, solo se recordó cuando ya estaba en
producción y alguien lo reportó. **Por eso, de aquí en adelante, antes
de entregar cualquier HTML/CSS nuevo (no solo posts del blog — cualquier
página del sitio), correr expresamente:**
```
grep -n "max-width" archivo.html
```
y confirmar, línea por línea, que cada resultado tenga también
`margin:0 auto` (o esté dentro de un contenedor que ya lo tenga). Este
chequeo se vuelve parte obligatoria del checklist de la sección 9.2,
punto 3 — no opcional, no "si se acuerda".

**Nota de cierre de este incidente (30 jun 2026):** tras aplicar el fix
y confirmarlo publicado byte por byte en GitHub, el usuario seguía
viendo la versión vieja incluso en ventana de incógnito con parámetro
de caché forzado (`?v=2`). Se resolvió solo, minutos después, sin
ningún cambio adicional — la propagación del CDN de GitHub Pages
ocasionalmente tarda más de lo normal (más allá de los 1-2 minutos
típicos). **Antes de seguir diagnosticando un "bug fantasma" después
de confirmar que el código está bien publicado, esperar unos minutos
más primero** — no asumir que la verificación de código fue
insuficiente solo porque el navegador todavía no refleja el cambio.

**4. Caché al actualizar una imagen con el mismo nombre de archivo:**
GitHub Pages (vía CDN) y los navegadores cachean imágenes agresivamente.
Si se sobrescribe un `.webp` con el mismo nombre, puede tardar en
reflejarse o no reflejarse hasta forzar recarga (`Cmd+Shift+R`) o abrir
en ventana privada. Antes de asumir que "la corrección no funcionó",
descartar caché primero — comparar el archivo real publicado en GitHub
contra el que se generó, no solo lo que se ve en pantalla.

**5. Tamaño mínimo legible del detalle fino del logo (corregido 27 jun
2026):** el logo del infinito lleva un detalle pequeño en el cruce (dos
trazos cobre + un punto). Ese detalle mide ~10% del ancho total del
ícono, sin importar la escala — así que el tamaño mínimo del ÍCONO
COMPLETO para que el detalle se siga viendo (no se vuelva mancha) es de
~110-130px de ancho. Por debajo de eso, usar la versión simplificada
(solo el punto cobre, sin los dos trazos) — no es un error, es la
decisión correcta a ese tamaño. El logo de las imágenes destacadas
quedó a 130px de ancho, fiel al original en desktop; en celular, donde
la imagen completa se reduce a ~350-390px, el ícono vuelve a quedar
por debajo del umbral y el detalle se suaviza — esto es una limitación
física del tamaño, no un bug, y se decidió aceptarlo (27 jun 2026)
porque forzarlo más grande para que se viera en celular lo haría
desproporcionado en el resto de la composición.

---

## 9.3 Audio de los posts (texto a voz) — protocolo de verificación (29 jun 2026)

**Herramienta:** ElevenLabs, modelo Multilingual v2, voz de categoría
"Narración" en español latinoamericano (no Conversacional, Anuncio, ni
Redes Sociales — esas no calzan con el tono "sin presión" de la marca).

**Por qué existe este protocolo:** en la primera implementación (post
de Ingreso vs. activo), partes del texto no se escucharon en el audio
final, aunque el resultado sonaba bien — el error pasó desapercibido
hasta que el usuario lo notó escuchando con atención. Causa más
probable: el límite de 5,000 caracteres por generación de ElevenLabs
se acercó demasiado sin margen de seguridad, y/o la unión de los clips
en QuickTime perdió contenido en el corte entre partes.

**Protocolo obligatorio para cada audio nuevo, sin excepción:**

1. **Margen de seguridad de caracteres:** cada parte del script debe
   quedar claramente por debajo de 4,500 caracteres (no 5,000) al
   dividir un post largo en dos o más partes.
2. **Verificación del contador en ElevenLabs:** antes de generar,
   confirmar que el contador en pantalla (ej. "2,887 / 5,000")
   coincide con el conteo de caracteres que se entregó en el script —
   si no coincide, algo se perdió al copiar/pegar y no se debe generar
   todavía.
3. **Puntos de control en la unión de clips:** al combinar partes en
   QuickTime (Edición → Agregar clip al final), escuchar con atención
   los últimos 10 segundos de cada parte y los primeros 10 segundos de
   la siguiente — es el punto más común donde se pierde contenido.
4. **Lectura cruzada del cierre/apertura:** al entregar un script
   dividido en partes, se debe marcar explícitamente la última frase
   de la Parte 1 y la primera frase de la Parte 2, para que sea fácil
   confirmar de oído que ninguna se saltó en la unión.
5. **Este mismo protocolo aplica a cualquier página del sitio que
   reciba audio en el futuro** (la carta, Diversifica, El Patrón), no
   solo al blog — el riesgo de truncado es del mismo origen (límite de
   caracteres de la herramienta) sin importar qué página sea.

**Carpeta de trabajo local recomendada:** `~/Downloads/infinexa-audio/`
para los MP3 ya convertidos, antes de subirlos a `assets/audio/` en el
repo — evita perderlos entre las descargas de otros archivos.

---

## 10. Plantilla técnica (front matter de cada post)

```yaml
---
title: "Título del post"
author: "Alejandro García, MBA"
category: "categoría"
pillar: "/diversifica"          # o "/" (la carta), o "/infografia" (El Patrón)
pillar_label: "Ver Diversifica" # debe coincidir con el destino real del botón
keywords: ["frase 1", "frase 2", "frase 3", "frase 4", "frase 5"]
description: "Meta descripción con la frase clave cerca del inicio."
image: "/assets/blog/nombre-imagen.webp"
image_alt: "Descripción específica de lo que muestra la imagen"
---
```

**Importante sobre `pillar_label`:** el botón de CTA al final de cada
post (en `_layouts/post.html`) usa este campo para mostrar el texto
correcto según a dónde apunte realmente el post — nunca debe quedar un
texto fijo tipo "Ver Diversifica" si el post en realidad enlaza a otra
página. Verificar siempre que `pillar`, `pillar_label`, y los enlaces
dentro del cuerpo del texto (incluyendo el cierre) apunten al mismo
destino y usen el mismo nombre.

**Importante sobre la fecha del archivo:** usar siempre la fecha real
del día de publicación (o anterior), nunca una fecha proyectada a
futuro — Jekyll no publica posts con fecha futura en el nombre del
archivo, los trata como programados.

---

## 11. Contexto técnico del sitio

- Sitio: 4 páginas (carta en infinexa.app, infografía en /infografia,
  Diversifica en /diversifica, Servicios en /servicios) + blog en /blog
- Paleta: Grafito #0F1720, Petróleo #1B4D5C, Cobre #C8682E, Plata
  #C9D2D6
- Plataforma: Jekyll sobre GitHub Pages
- Permalinks del blog sin fecha en la URL (`/blog/:title/`) — consistente
  con el enfoque "biblioteca"

---

## 12. Objetivo de negocio detrás del blog

- Posicionamiento SEO orgánico de largo plazo (3-6 meses)
- Pilares conectados a páginas existentes:
  1. Historia económica/tecnológica → El Patrón
  2. Educación financiera/diversificación → Diversifica
  3. Explicadores DeFi/Web3 → la carta
  4. Storytelling sin nombrar negocios específicos

---

## 13. Lo que se evaluó y se descartó explícitamente, con motivo

Para que esto no se vuelva a proponer sin recordar por qué — se evaluó
un prompt externo de estilo "editor de pensamiento/mentor
transformacional" y se descartaron estos elementos:

- **Las "9 secciones de análisis"** (Principios universales,
  Aplicación práctica, Errores, Beneficios, etc.) como subtítulos
  visibles fijos en cada post — violaría directamente la regla de
  Unicidad (sección 5); el lector reconocería el molde en 3-4 posts.
- **"Explicar el cómo" / "proponer acciones concretas paso a paso"** —
  va contra la regla central (sección 4, punto 4) de dar el qué
  completo y reservar el cómo personalizado para conversación 1:1.
- **Lenguaje de "mejora tus finanzas/tu patrimonio"** como beneficio
  prometido — riesgo de cumplimiento real (ver guía Meta/WhatsApp en
  `RECETAS.md`), no solo de tono.
- **Tono de "mentor con todas las respuestas"** — choca con la voz ya
  construida (Carlos, Epiphany Bridge), que parte de la duda
  compartida, no de la autoridad absoluta.

---

## Historial de posts publicados

| # | Título | Pilar | Fecha |
|---|---|---|---|
| 1 | Ingreso vs. activo: la diferencia que cambia cómo ves tu dinero | Diversifica | 2026-06-25 |
| 2 | 1929, 1994, 2008, 2020: por qué la misma crisis se repite distinto cada vez | Diversifica | 2026-06-26 |
| 3 | ¿Por qué una wallet no custodial no tiene botón de "olvidé mi contraseña"? | La carta | 2026-06-26 |
| 4 | ¿Por qué rechazamos lo nuevo antes de entenderlo? | El Patrón | 2026-06-26 |
