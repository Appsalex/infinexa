# _PLANTILLAS · INFINEXA

> Esta carpeta guarda SOLO la versión final y ganadora de cada pieza del proyecto — nunca versiones intermedias, descartadas, o de prueba. El objetivo es que cuando inicies un proyecto nuevo (otra marca, otro negocio, otro builder), puedas partir directamente de aquí en vez de reconstruir desde cero todo el proceso de iteración que ya costó tiempo resolver.
>
> Diferencia con los otros archivos de `_gestion/`:
> - `ESTADO.md` → qué existe y en qué estado está (snapshot del proyecto Infinexa específicamente)
> - `RECETAS.md` → cómo PEDIR que se genere algo (el prompt)
> - `BITACORA.md` → qué pasó y cuándo (historia)
> - **`_plantillas/` (esta carpeta)** → el RESULTADO final ya pulido, listo para copiar y adaptar

---

## Estructura de cada pieza

Cada pieza terminada vive en su propia subcarpeta, con siempre el mismo patrón de 2 archivos mínimo:

```
_plantillas/
  [nombre-de-la-pieza]/
    codigo-final.[html|docx|svg|...]   ← el archivo final, listo para copiar
    notas.md                            ← qué es, qué decisiones clave se tomaron, 
                                           qué cambiar si se reutiliza en otro proyecto
```

El archivo `notas.md` de cada pieza siempre responde 3 preguntas cortas:
1. **¿Qué es esto?** (una línea)
2. **¿Qué decisiones de diseño/copy NO deben cambiarse a la ligera?** (lo que ya se probó y funciona)
3. **¿Qué SÍ hay que cambiar si se reutiliza en un proyecto nuevo?** (nombres, colores, datos específicos de Infinexa que no aplican a otra marca)

---

## Índice de piezas guardadas

| Pieza | Carpeta | Última actualización |
|---|---|---|
| Página educativa tipo scroll con CTA WhatsApp | `pagina-diversifica/` | 19 jun 2026 |
| Sistema de generación de favicons/íconos sin transparencia | `sistema-favicons/` | 19 jun 2026 |

**Pendiente de agregar (mencionadas pero no confirmadas como versión final en esta conversación):**
- La carta principal (`infinexa.app`) — no se trabajó su código en esta conversación, solo se mencionó como referencia. Si quieres guardarla aquí, comparte el HTML final actual y la agregamos.
- El manual de marca / brand brief — se compartieron los archivos .docx en esta conversación, pero no se confirmó cuál es la versión definitiva si hubo varias iteraciones. Si ya sabes cuál es la final, dímelo y la agregamos.
- La infografía (`infinexa.app/infografia`) — mencionada como referencia de estilo varias veces, pero no se trabajó su código aquí.
- Los SVG de marca (logo negativo/positivo/horizontal, ícono) — ya los tengo de esta conversación, se pueden agregar como plantilla de "identidad visual" si quieres.

---

## Cómo agregar una pieza nueva a esta carpeta

Cuando una pieza llegue a su versión final (ya no se va a seguir iterando), pide a Claude:

> "Guarda la versión final de [pieza] en _plantillas/, con su notas.md correspondiente"

Claude debe:
1. Confirmar contigo que efectivamente es la versión final y no una intermedia.
2. Crear la subcarpeta con el nombre de la pieza.
3. Guardar el código/archivo final tal cual.
4. Escribir el `notas.md` respondiendo las 3 preguntas de arriba.
5. Actualizar la tabla de índice en este mismo README.

## Cómo reutilizar una pieza en un proyecto nuevo

1. Copia la subcarpeta completa de `_plantillas/[pieza]/` a tu proyecto nuevo.
2. Lee primero `notas.md` — ahí está explicado qué es seguro cambiar y qué no.
3. Pide a Claude: "toma esta plantilla de [pieza] y adáptala para [nuevo proyecto/marca]" — comparte el código final y el notas.md correspondiente.
