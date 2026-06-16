#!/bin/bash
# Script para agregar favicon y Open Graph a infinexa
# Ejecutar desde: bash ~/Downloads/aplicar-og.sh

REPO="$HOME/Downloads/infinexa-repo"
ASSETS_DIR="$HOME/Downloads/infinexa-assets"

echo "→ Copiando assets al repo..."
mkdir -p "$REPO/assets"
cp "$ASSETS_DIR/favicon.png" "$REPO/assets/favicon.png"
cp "$ASSETS_DIR/favicon.svg" "$REPO/assets/favicon.svg"
cp "$ASSETS_DIR/og-image.png" "$REPO/assets/og-image.png"

echo "→ Actualizando index.html (carta)..."
python3 << 'PYEOF'
import re

META_TAGS = """
  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
  <link rel="icon" type="image/png" href="/assets/favicon.png">
  <link rel="shortcut icon" href="/assets/favicon.png">

  <!-- Open Graph / WhatsApp -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://infinexa.app/">
  <meta property="og:title" content="infinexa · Una conversación que cambia el chip">
  <meta property="og:description" content="Connecting value with purpose. Una forma distinta de ver el dinero, la tecnología y el futuro.">
  <meta property="og:image" content="https://infinexa.app/assets/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="https://infinexa.app/assets/og-image.png">
"""

import os
path = os.path.expanduser("~/Downloads/infinexa-repo/index.html")
with open(path, "r") as f:
    content = f.read()

if "og:title" not in content:
    content = content.replace("<title>infinexa · Una conversación que cambia el chip</title>",
        "<title>infinexa · Una conversación que cambia el chip</title>" + META_TAGS)
    with open(path, "w") as f:
        f.write(content)
    print("  ✓ index.html actualizado")
else:
    print("  ℹ index.html ya tiene OG tags")
PYEOF

echo "→ Actualizando infografia/index.html..."
python3 << 'PYEOF'
import re, os

META_TAGS = """
  <!-- Favicon -->
  <link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
  <link rel="icon" type="image/png" href="/assets/favicon.png">
  <link rel="shortcut icon" href="/assets/favicon.png">

  <!-- Open Graph / WhatsApp -->
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://infinexa.app/infografia">
  <meta property="og:title" content="infinexa · El patrón que nunca falla">
  <meta property="og:description" content="La infografía que revela el patrón detrás del crecimiento real. Connecting value with purpose.">
  <meta property="og:image" content="https://infinexa.app/assets/og-image.png">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="https://infinexa.app/assets/og-image.png">
"""

path = os.path.expanduser("~/Downloads/infinexa-repo/infografia/index.html")
with open(path, "r") as f:
    content = f.read()

if "og:title" not in content:
    content = content.replace("<title>infinexa · El patrón que nunca falla</title>",
        "<title>infinexa · El patrón que nunca falla</title>" + META_TAGS)
    with open(path, "w") as f:
        f.write(content)
    print("  ✓ infografia/index.html actualizado")
else:
    print("  ℹ infografia/index.html ya tiene OG tags")
PYEOF

echo "→ Haciendo commit y push..."
cd "$REPO"
git add .
git commit -m "Agregar favicon y Open Graph tags"
git push origin main

echo ""
echo "✅ Listo. En 1-2 minutos estará en vivo en infinexa.app"
echo "   Favicon: infinexa.app/assets/favicon.svg"
echo "   OG image: infinexa.app/assets/og-image.png"
