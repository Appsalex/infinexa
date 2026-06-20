from playwright.sync_api import sync_playwright

# Lienzo 1200x630 (estándar Open Graph), con el logo de 800x480 centrado
# Mantenemos el fondo grafito en todo el lienzo, sin distorsionar el logo
html = '''<!DOCTYPE html>
<html><head><style>
* { margin:0; padding:0; }
body { width:1200px; height:630px; background:#0F1720; display:flex; align-items:center; justify-content:center; }
svg { display:block; }
</style></head>
<body>
<svg xmlns="http://www.w3.org/2000/svg" width="900" height="540" viewBox="0 0 800 480">
  <rect width="800" height="480" fill="#0F1720"/>
  <path d="
    M 400 210
    C 388 178, 344 140, 296 142
    C 242 144, 216 178, 220 206
    C 224 238, 258 256, 306 252
    C 348 248, 382 222, 400 210
    C 418 198, 442 162, 476 156
    C 514 150, 542 174, 542 202
    C 542 234, 516 254, 480 254
    C 444 254, 416 230, 400 210
  " fill="none" stroke="#BDC8CC" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M 384 198 Q 392 210 384 222" fill="none" stroke="#C8682E" stroke-width="2.6" stroke-linecap="round"/>
  <path d="M 416 198 Q 408 210 416 222" fill="none" stroke="#C8682E" stroke-width="2.6" stroke-linecap="round"/>
  <circle cx="400" cy="210" r="2.8" fill="#C8682E"/>
  <text x="400" y="340" font-family="'Inter','SF Pro Display','Helvetica Neue',Arial,sans-serif" font-size="36" font-weight="300" fill="#EDF1F2" text-anchor="middle" letter-spacing="18">infinexa</text>
  <line x1="378" y1="356" x2="422" y2="356" stroke="#C8682E" stroke-width="0.8" opacity="0.85"/>
  <text x="400" y="382" font-family="'Inter','SF Pro Text','Helvetica Neue',Arial,sans-serif" font-size="11" font-weight="300" fill="#C9D2D6" text-anchor="middle" letter-spacing="5.5" opacity="0.5">connecting value with purpose</text>
</svg>
</body></html>'''

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page(viewport={"width": 1200, "height": 630}, device_scale_factor=2)
    page.set_content(html)
    page.wait_for_timeout(500)
    page.screenshot(path='/home/claude/favicons/og-image-1200x630.png', type='png')
    browser.close()

print("OG image generada")
