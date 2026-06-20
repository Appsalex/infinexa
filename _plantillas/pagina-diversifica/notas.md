# Plantilla: Página educativa tipo "Diversifica"

## ¿Qué es esto?

Página web de scroll largo, estilo editorial oscuro, para presentar un argumento educativo/persuasivo en varios bloques narrativos progresivos, terminando en un CTA de WhatsApp. Construida originalmente para Infinexa como pieza de prospección sobre diversificación de ingresos.

## Decisiones que NO deben cambiarse a la ligera (ya se probaron y funcionan)

- **Formato scroll vertical, NUNCA carrusel de pantalla completa.** Se intentó primero como carrusel (un slide por pantalla, swipe para avanzar) y se abandonó por completo: en móvil bloqueaba el zoom nativo del navegador (el gesto de pinch-zoom avanzaba al siguiente slide en vez de ampliar texto), y forzaba tamaños de fuente artificialmente pequeños.
- **Los media queries SIEMPRE van al final del bloque `<style>`**, después de todas las reglas base. Si van antes, la cascada CSS hace que las reglas base (más abajo en el código) sobreescriban silenciosamente las correcciones de móvil, sin importar el ancho real de pantalla — esto pasó y costó varias rondas de debugging detectarlo.
- **Acordeones para contenido expositivo largo, contenido emocional/persuasivo siempre visible.** No todos los bloques necesitan estar abiertos por defecto — los más largos y argumentativos van en acordeón (colapsados), los de mayor peso emocional/de cierre se dejan siempre visibles.
- **Las imágenes de marca SIEMPRE con ruta absoluta** (`https://tudominio.com/assets/...`), nunca relativa (`../assets/...`). Los crawlers de redes sociales (Facebook/WhatsApp) no siempre resuelven bien las rutas relativas al leer el HTML para generar la vista previa.
- **El `apple-touch-icon.png` (180×180) y `favicon.png` NUNCA deben tener canal alfa/transparencia** (modo debe ser RGB, no RGBA). Si lo tienen, iOS lo renderiza distorsionado al anclar la página a pantalla de inicio, aunque la imagen de Open Graph se vea perfecta. Generar siempre desde el SVG vectorial fuente, no desde un PNG ya exportado.
- **Una sola carpeta de assets por proyecto, verificada antes de crear cualquier carpeta nueva.** Usar `grep -rn "assets" --include="*.html" .` desde la raíz del repo para confirmar la convención existente antes de subir cualquier imagen nueva — evita crear carpetas duplicadas con el mismo propósito.

## Qué SÍ hay que cambiar al reutilizar en un proyecto nuevo

- Todo el copy es específico de Infinexa/diversificación de ingresos — reemplazar por el argumento/tema del proyecto nuevo, manteniendo la estructura de: apertura → contexto/problema → giro emocional → argumento central → objeción resuelta → cierre con CTA.
- Paleta de colores (variables CSS `--grafito-oscuro`, `--cobre`, `--plata-clara`, etc.) — ajustar a la paleta de marca del proyecto nuevo.
- Logo y wordmark en el header — reemplazar el SVG inline del símbolo de Infinexa por el del proyecto nuevo.
- Número de WhatsApp y mensaje prellenado del botón de CTA final.
- Meta tags de Open Graph (título, descripción, URL, imagen) — todos específicos del dominio nuevo.
- Las rutas de favicon/apple-touch-icon/og-image — ajustar a la carpeta de assets real del proyecto nuevo (confirmar primero cuál es esa carpeta, siguiendo la lección de arriba).

## Decisión de diseño que vale la pena recordar (no técnica, sino de redacción)

Si el avatar/audiencia es sensible a sonar "demasiado de venta" o "demasiado cripto-bro", el patrón que funcionó fue: nombrar el problema sin alarmismo → dar un dato verificado y citable (no un rumor sin respaldo) → presentar la solución como una opción adicional, nunca como reemplazo de lo que la persona ya tiene → cerrar con invitación, no con presión.
