#!/usr/bin/env bash
set -e
sudo apt update && sudo apt install -y mkcert

PROJECT_NAME="pryamoy"
DOMAIN="${PROJECT_NAME}.test"
CERTS_DIR="./docker/certs"

echo "🚀 Iniciando setup para ${PROJECT_NAME}..."

# 1. Criar pastas necessárias
mkdir -p ${CERTS_DIR}

# 2. Gerar certificados TLS no host
cd ${CERTS_DIR}
if [ ! -f "${DOMAIN}.pem" ] || [ ! -f "${DOMAIN}-key.pem" ]; then
    if command -v mkcert >/dev/null 2>&1; then
        echo "🔐 Gerando certificados TLS confiáveis com mkcert..."
        mkcert -key-file ${DOMAIN}-key.pem -cert-file ${DOMAIN}.pem ${DOMAIN}
    else
        echo "⚠️ mkcert não encontrado, gerando certificado self-signed com OpenSSL..."
        openssl req -x509 -nodes -days 365 \
            -newkey rsa:2048 \
            -keyout ${DOMAIN}-key.pem \
            -out ${DOMAIN}.pem \
            -subj "/C=US/ST=Denial/L=Springfield/O=Dis/CN=${DOMAIN}"
    fi
else
    echo "🔐 Certificados já existem, pulando..."
fi
cd -

# 3. Atualizar /etc/hosts
if ! grep -q "${DOMAIN}" /etc/hosts; then
    echo "📝 Adicionando ${DOMAIN} em /etc/hosts (pode pedir senha sudo)..."
    echo "127.0.0.1 ${DOMAIN}" | sudo tee -a /etc/hosts
else
    echo "📝 ${DOMAIN} já está em /etc/hosts"
fi

# 4. Subir containers
echo "🚢 Subindo containers..."
docker compose up --build

echo "🎉 Setup concluído!"
echo "👉 Acesse: https://${DOMAIN}"
