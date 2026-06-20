from playwright.sync_api import sync_playwright
import pathlib

svg_content = pathlib.Path('/home/claude/favicons/icono.svg').read_text()

def render_png(size, output_path, square_no_radius=False):
    """Renderiza el SVG a PNG en el tamaño exacto especificado."""
    svg = svg_content
    if square_no_radius:
        # Apple ya redondea las esquinas automáticamente — exportamos cuadrado sin rx
        svg = svg.replace('rx="44"', 'rx="0"')
    html = f'''<!DOCTYPE html>
<html><head><style>
* {{ margin:0; padding:0; }}
body {{ width:{size}px; height:{size}px; }}
svg {{ display:block; width:{size}px; height:{size}px; }}
</style></head>
<body>{svg}</body></html>'''
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": size, "height": size}, device_scale_factor=1)
        page.set_content(html)
        page.wait_for_timeout(300)
        page.screenshot(path=output_path, type='png')
        browser.close()

# Favicon estándar (con esquinas redondeadas del diseño original)
render_png(32, '/home/claude/favicons/favicon-32.png')
render_png(16, '/home/claude/favicons/favicon-16.png')

# Apple touch icon — 180x180, esquinas cuadradas (iOS las redondea solo)
render_png(180, '/home/claude/favicons/apple-touch-icon-180.png', square_no_radius=True)

print("Favicons generados")
