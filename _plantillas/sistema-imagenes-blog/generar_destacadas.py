from playwright.sync_api import sync_playwright
import random

W, H = 1200, 630

ICONS = {
    "carta": '''<g transform="translate(90,330)">
        <rect x="0" y="14" width="34" height="26" rx="5" fill="none" stroke="#C8682E" stroke-width="2.5"/>
        <path d="M 7 14 V 6 C 7 -1 27 -1 27 6 V 14" fill="none" stroke="#C8682E" stroke-width="2.5"/>
        <circle cx="17" cy="27" r="2.6" fill="#C8682E"/>
    </g>''',
    "diversifica": '''<g transform="translate(90,330)">
        <path d="M 17 40 V 20" stroke="#C8682E" stroke-width="2.5" fill="none" stroke-linecap="round"/>
        <path d="M 17 20 L 2 0" stroke="#C8682E" stroke-width="2.5" fill="none" stroke-linecap="round"/>
        <path d="M 17 20 L 17 0" stroke="#C8682E" stroke-width="2.5" fill="none" stroke-linecap="round"/>
        <path d="M 17 20 L 32 0" stroke="#C8682E" stroke-width="2.5" fill="none" stroke-linecap="round"/>
        <circle cx="2" cy="0" r="2.4" fill="#C8682E"/>
        <circle cx="17" cy="0" r="2.4" fill="#C8682E"/>
        <circle cx="32" cy="0" r="2.4" fill="#C8682E"/>
    </g>''',
    "patron": '''<g transform="translate(107,347)">
        <path d="M 14 -7 A 14 14 0 1 1 -7 14" stroke="#C8682E" stroke-width="2.5" fill="none" stroke-linecap="round"/>
        <path d="M -7 14 L -7 6 M -7 14 L 1 14" stroke="#C8682E" stroke-width="2.5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
    </g>'''
}

def in_exclusion_zone(x, y):
    # zona reservada para el texto (columna izquierda, donde van logo/categoría/título/subtítulo)
    return 50 < x < 850 and 20 < y < 430

def build_focal_cluster(seed):
    # grupo de nodos más grandes en el lado derecho, para balancear el peso visual
    # del bloque de texto en la izquierda — sin esto, el lado derecho queda vacío.
    import math
    rnd = random.Random(seed + 500)
    cx, cy = rnd.uniform(870, 970), rnd.uniform(240, 360)
    nodes = [(cx, cy)]
    for _ in range(4):
        ang = rnd.uniform(0, 2*math.pi)
        dist = rnd.uniform(60, 110)
        nx = max(820, min(W-50, cx + dist*math.cos(ang)))
        ny = max(60, min(H-60, cy + dist*math.sin(ang)))
        nodes.append((nx, ny))
    svg = ""
    for i in range(len(nodes)-1):
        x1,y1 = nodes[i]
        x2,y2 = nodes[i+1]
        svg += f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#2E6E80" stroke-width="1.2" opacity="0.6"/>\n'
    svg += f'<line x1="{nodes[0][0]:.1f}" y1="{nodes[0][1]:.1f}" x2="{nodes[2][0]:.1f}" y2="{nodes[2][1]:.1f}" stroke="#2E6E80" stroke-width="1.2" opacity="0.6"/>\n'
    for i, (x,y) in enumerate(nodes):
        r = 7 if i == 0 else rnd.choice([4,5,6])
        color = "#C8682E" if i == 0 else "#C9D2D6"
        op = 0.95 if i == 0 else rnd.uniform(0.45,0.8)
        svg += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{color}" opacity="{op:.2f}"/>\n'
        if i == 0:
            svg += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r+9}" fill="none" stroke="#C8682E" stroke-width="1" opacity="0.35"/>\n'
    # anillo orbital grande detrás del cluster, para dar peso incluso donde no hay nodos
    svg += f'<circle cx="{cx-20:.1f}" cy="{cy+10:.1f}" r="160" fill="none" stroke="#2E6E80" stroke-width="1" opacity="0.18"/>\n'
    svg += f'<circle cx="{cx-20:.1f}" cy="{cy+10:.1f}" r="215" fill="none" stroke="#2E6E80" stroke-width="1" opacity="0.1"/>\n'
    return svg

def build_svg(category, titulo_lineas, subtitulo, icon_key, seed, extra_chips=None):
    random.seed(seed)
    points = []
    tries = 0
    while len(points) < 10 and tries < 200:
        tries += 1
        x, y = random.uniform(60, W-60), random.uniform(30, H-30)
        if in_exclusion_zone(x, y):
            continue
        points.append((x, y))
    lines, circles = "", ""
    for i, (x, y) in enumerate(points):
        if i < len(points) - 1:
            x2, y2 = points[i+1]
            if ((x2-x)**2 + (y2-y)**2) ** 0.5 < 250:
                lines += f'<line x1="{x:.1f}" y1="{y:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="#2E6E80" stroke-width="1" opacity="0.5"/>\n'
        r = random.choice([2, 2, 3, 4.5])
        color = "#C8682E" if random.random() < 0.2 else "#C9D2D6"
        op = 0.9 if color == "#C8682E" else random.uniform(0.25, 0.65)
        circles += f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{color}" opacity="{op:.2f}"/>\n'
    circles += build_focal_cluster(seed)

    title_y_start = 225
    title_svg = ""
    for i, linea in enumerate(titulo_lineas):
        title_svg += f'<text x="90" y="{title_y_start + i*56}" font-size="46" font-weight="800" fill="#EDF1F2" font-family="Inter,Arial,sans-serif">{linea}</text>\n'

    sub_y = title_y_start + len(titulo_lineas)*56 + 40
    sub_svg = f'<text x="90" y="{sub_y}" font-size="20" font-weight="400" fill="#C9D2D6" opacity="0.85" font-family="Inter,Arial,sans-serif">{subtitulo}</text>' if subtitulo else ""

    # punto de anclaje del ícono: siempre con margen fijo debajo del último elemento de texto real
    contenido_bottom = sub_y + (12 if subtitulo else -28)
    icon_anchor_y = contenido_bottom + 55

    chips_svg = ""
    if extra_chips:
        cx = 90
        chip_y = contenido_bottom + 28
        for chip in extra_chips:
            w = 18 * len(chip) + 40
            chips_svg += f'''<rect x="{cx}" y="{chip_y}" width="{w}" height="40" rx="20" fill="none" stroke="#C8682E" stroke-width="1.5"/>
            <text x="{cx+w/2}" y="{chip_y+26}" font-size="18" font-weight="700" fill="#C8682E" text-anchor="middle" font-family="Inter,Arial,sans-serif">{chip}</text>'''
            cx += w + 14

    icon_svg = ""
    if not extra_chips:
        icon_svg = ICONS[icon_key].replace('translate(90,330)', f'translate(90,{icon_anchor_y})').replace('translate(107,347)', f'translate(107,{icon_anchor_y+17})')

    return f'''<!DOCTYPE html><html><head><style>
    *{{margin:0;padding:0;}} body{{width:{W}px;height:{H}px;background:#0F1720;}}
    </style></head><body>
    <svg width="{W}" height="{H}" viewBox="0 0 {W} {H}">
      <rect width="{W}" height="{H}" fill="#0F1720"/>
      <defs><radialGradient id="fade" cx="78%" cy="28%" r="65%">
        <stop offset="0%" stop-color="#1B4D5C" stop-opacity="0.35"/>
        <stop offset="100%" stop-color="#0F1720" stop-opacity="0"/>
      </radialGradient></defs>
      <rect width="{W}" height="{H}" fill="url(#fade)"/>
      {lines}{circles}
      <g transform="translate(1.18,-36.52) scale(0.4037)">
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
        " fill="none" stroke="#BDC8CC" stroke-width="4.95" stroke-linecap="round" stroke-linejoin="round"/>
        <path d="M 384 198 Q 392 210 384 222" fill="none" stroke="#C8682E" stroke-width="3.22" stroke-linecap="round"/>
        <path d="M 416 198 Q 408 210 416 222" fill="none" stroke="#C8682E" stroke-width="3.22" stroke-linecap="round"/>
        <circle cx="400" cy="210" r="4.46" fill="#C8682E"/>
      </g>
      <text x="235" y="55" font-size="20" font-weight="300" fill="#EDF1F2" font-family="Inter,Arial,sans-serif" letter-spacing="3">infinexa</text>
      <text x="90" y="170" font-size="16" font-weight="600" letter-spacing="3" fill="#C8682E" font-family="Inter,Arial,sans-serif">{category}</text>
      {title_svg}
      {sub_svg}
      {chips_svg}
      {icon_svg}
    </svg></body></html>'''

CONFIGS = [
    dict(out="wallet-no-custodial", category="ECONOMÍA DESCENTRALIZADA",
         titulo=["Wallet no custodial:", "tus llaves, tu control"], subtitulo=None,
         icon="carta", seed=7),
    dict(out="ingreso-vs-activo", category="DIVERSIFICACIÓN",
         titulo=["Ingreso vs. activo"], subtitulo="La diferencia que cambia cómo ves tu dinero",
         icon="diversifica", seed=3),
    dict(out="crisis-1929-2020", category="HISTORIA ECONÓMICA",
         titulo=["Por qué la misma crisis", "se repite distinto cada vez"], subtitulo=None,
         icon="diversifica", seed=11, chips=["1929","1994","2008","2020"]),
    dict(out="por-que-rechazamos-lo-nuevo", category="HISTORIA Y TECNOLOGÍA",
         titulo=["¿Por qué rechazamos lo nuevo", "antes de entenderlo?"], subtitulo=None,
         icon="patron", seed=19),
    dict(out="cajero-automatico-wallet", category="HISTORIA Y TECNOLOGÍA",
         titulo=["El cajero automático y", "la misma desconfianza de hoy"], subtitulo=None,
         icon="patron", seed=31),
    dict(out="stablecoin-vs-bitcoin", category="ECONOMÍA DESCENTRALIZADA",
         titulo=["Stablecoin vs. Bitcoin:", "no son lo mismo"], subtitulo=None,
         icon="carta", seed=43),
    dict(out="historia-del-dinero", category="HISTORIA ECONÓMICA",
         titulo=["Del trueque al", "dólar digital"], subtitulo=None,
         icon="patron", seed=67),
    dict(out="dinero-e-inflacion", category="DIVERSIFICACIÓN",
         titulo=["El impuesto", "silencioso"], subtitulo=None,
         icon="diversifica", seed=53),
    dict(out="ingreso-pasivo", category="DIVERSIFICACIÓN",
         titulo=["Ingreso pasivo:", "lo que sí es"], subtitulo=None,
         icon="diversifica", seed=77),
    dict(out="piezas-rompecabezas", category="HISTORIA Y TECNOLOGÍA",
         titulo=["30 años de", "piezas sueltas"], subtitulo=None,
         icon="patron", seed=89),
    dict(out="ecash-digicash", category="HISTORIA Y TECNOLOGÍA",
         titulo=["La idea que", "fracasó primero"], subtitulo=None,
         icon="patron", seed=97),
    dict(out="whitepaper-bitcoin", category="ECONOMÍA DESCENTRALIZADA",
         titulo=["Nueve páginas,", "un cambio total"], subtitulo=None,
         icon="carta", seed=101),
    dict(out="bloque-genesis-bitcoin", category="ECONOMÍA DESCENTRALIZADA",
         titulo=["El mensaje del", "primer bloque"], subtitulo=None,
         icon="carta", seed=103),
    dict(out="nodos-y-mineros", category="HISTORIA Y TECNOLOGÍA",
         titulo=["Quién guarda", "la verdad"], subtitulo=None,
         icon="patron", seed=107),
    dict(out="infraestructura-del-dinero-hoy", category="DIVERSIFICACIÓN",
         titulo=["Quince años", "después"], subtitulo=None,
         icon="diversifica", seed=109),
    dict(out="inflacion-en-profundidad", category="DIVERSIFICACIÓN",
         titulo=["Cuando el dinero", "pierde el control"], subtitulo=None,
         icon="diversifica", seed=113),
    dict(out="remesas-usdt", category="ECONOMÍA DESCENTRALIZADA",
         titulo=["Enviar dinero sin", "la comisión de siempre"], subtitulo=None,
         icon="carta", seed=127),
    dict(out="defi-en-la-practica", category="ECONOMÍA DESCENTRALIZADA",
         titulo=["Prestar y pedir", "prestado sin bancos"], subtitulo=None,
         icon="carta", seed=131),
    dict(out="seguridad-digital-llaves", category="ECONOMÍA DESCENTRALIZADA",
         titulo=["Proteger tus llaves", "antes de que sea tarde"], subtitulo=None,
         icon="carta", seed=137),
]

with sync_playwright() as p:
    browser = p.chromium.launch()
    for cfg in CONFIGS:
        html = build_svg(cfg["category"], cfg["titulo"], cfg.get("subtitulo"), cfg["icon"], cfg["seed"], cfg.get("chips"))
        page = browser.new_page(viewport={"width": W, "height": H}, device_scale_factor=2)
        page.set_content(html)
        page.wait_for_timeout(200)
        page.screenshot(path=f'/home/claude/mockup/{cfg["out"]}.png', type='png')
        page.close()
        print(f'{cfg["out"]} listo')
    browser.close()
