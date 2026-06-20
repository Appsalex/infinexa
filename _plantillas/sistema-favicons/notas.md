# Plantilla: Sistema de generación de favicons/íconos sin transparencia

## ¿Qué es esto?

Dos scripts de Python (usando Playwright) que generan, desde un SVG vectorial fuente, los tres archivos de íconos estándar que necesita cualquier sitio web: `favicon.png` (32×32), `apple-touch-icon.png` (180×180), y `og-image.png` (1200×630) para vista previa al compartir en redes/WhatsApp.

## Decisiones que NO deben cambiarse a la ligera

- **Renderizar siempre desde el SVG vectorial fuente, nunca desde un PNG ya exportado.** Garantiza nitidez perfecta en cada tamaño sin artefactos de reescalado.
- **El `apple-touch-icon.png` se exporta con esquinas CUADRADAS (sin `border-radius`/`rx`), nunca redondeadas.** iOS aplica su propio redondeo automáticamente al mostrarlo en pantalla de inicio — si el archivo ya viene redondeado, se ve doble-recortado o con artefactos en las esquinas.
- **Ninguno de los tres archivos debe tener canal alfa/transparencia (modo RGBA).** Deben exportarse en modo RGB puro con fondo sólido real. La transparencia en el apple-touch-icon específicamente causa distorsión visual al anclar en iOS — bug confirmado y resuelto en este proyecto (19 jun 2026).
- **Verificación obligatoria antes de subir cualquier ícono nuevo:**
  ```python
  from PIL import Image
  img = Image.open('archivo.png')
  print(img.mode)  # Debe decir "RGB", nunca "RGBA"
  ```
- **La imagen de Open Graph se renderiza a doble resolución (`device_scale_factor=2`) y luego se reescala** con `Image.LANCZOS` al tamaño final exacto — esto da nitidez en pantallas de alta densidad sin que el archivo pese de más.

## Qué SÍ hay que cambiar al reutilizar en un proyecto nuevo

- La ruta del SVG fuente (`icono.svg` en el script) — apuntar al símbolo/logo del proyecto nuevo.
- Los colores hardcodeados dentro del SVG inline en `render_og.py` (actualmente usa la paleta de Infinexa: `#0F1720`, `#BDC8CC`, `#C8682E`, `#EDF1F2`, `#C9D2D6`).
- El texto del wordmark y tagline dentro del SVG de `render_og.py`.
- Confirmar primero cuál es la carpeta de assets real del proyecto (ver lección en la plantilla de "pagina-diversifica") antes de decidir dónde guardar los archivos generados.

## Cómo correrlo (requiere Playwright instalado)

```bash
pip install playwright --break-system-packages
python3 -m playwright install chromium
python3 codigo-final-render-favicons.py
python3 codigo-final-render-og-image.py
```
