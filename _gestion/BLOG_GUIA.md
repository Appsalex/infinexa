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
