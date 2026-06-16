#!/bin/bash
# Script para crear un nuevo builder en Infinexa
# Uso: bash builder-setup.sh

REPO="$HOME/Downloads/infinexa-repo"

echo ""
echo "═══════════════════════════════════════"
echo "  INFINEXA · Nuevo Builder Edition"
echo "═══════════════════════════════════════"
echo ""

read -p "Apodo/subdominio (ej: carlos): " APODO
read -p "Nombre completo del builder: " NOMBRE
read -p "Rol o ciudad (ej: Builder · Monterrey): " ROL
read -p "Número WhatsApp con código de país (ej: 526461234567): " WHATSAPP

NOMBRE_URL=$(echo "$NOMBRE" | sed 's/ /%20/g')
BUILDER_DIR="$REPO/builders/$APODO"

echo ""
echo "→ Creando estructura para $APODO.infinexa.app ..."

mkdir -p "$BUILDER_DIR/infografia"

# Carta personalizada
sed "s/{{NOMBRE}}/$NOMBRE/g; s/{{APODO}}/$APODO/g; s/{{ROL}}/$ROL/g; s/{{WHATSAPP}}/$WHATSAPP/g; s/{{NOMBRE_URL}}/$NOMBRE_URL/g" \
  "$REPO/builders/_template/carta.html" > "$BUILDER_DIR/index.html"

# Infografía personalizada  
sed "s/{{NOMBRE}}/$NOMBRE/g; s/{{APODO}}/$APODO/g; s/{{ROL}}/$ROL/g; s/{{WHATSAPP}}/$WHATSAPP/g; s/{{NOMBRE_URL}}/$NOMBRE_URL/g" \
  "$REPO/builders/_template/infografia.html" > "$BUILDER_DIR/infografia/index.html"

cd "$REPO"
git add "builders/$APODO/"
git commit -m "Agregar builder: $APODO ($NOMBRE)"
git push origin main

echo ""
echo "✅ Listo. En 2 minutos estará en:"
echo "   https://$APODO.infinexa.app"
echo "   https://$APODO.infinexa.app/infografia"
echo ""
