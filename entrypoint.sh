#!/bin/bash
set -e

# Atualiza pacotes e instala zsh
apt update
apt install -y zsh sudo

# Cria usuário
useradd -m -s /usr/bin/zsh sites || true
usermod -aG sudo sites || true

# Ajusta permissões
chmod -R 777 /app/

# Banco SQLite
rm -f /app/database/database.sqlite
touch /app/database/database.sqlite
chmod -R 777 /app/database/database.sqlite

# Dependências Laravel
cd /app/
composer install
[ ! -f .env ] && cp .env.example .env
php artisan key:generate || true
chmod -R 777 /app

# Ativa módulos Apache
a2enmod rewrite
a2enmod ssl

# Diretório de certificados montado pelo docker-compose
CERT_DIR=/etc/apache2/certs

# Se os certificados do mkcert não existirem, gera fallback self-signed
if [ ! -f "$CERT_DIR/pryamoy.test.pem" ] || [ ! -f "$CERT_DIR/pryamoy.test-key.pem" ]; then
    echo "⚠️ Nenhum certificado encontrado em $CERT_DIR. Gerando self-signed..."
    mkdir -p $CERT_DIR
    openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
        -keyout $CERT_DIR/pryamoy.test-key.pem \
        -out $CERT_DIR/pryamoy.test.pem \
        -subj "/C=BR/ST=SP/L=SaoPaulo/O=Dev/OU=IT/CN=pryamoy.test"
else
    echo "✅ Usando certificados existentes em $CERT_DIR"
fi

# Habilita site SSL
a2ensite 000-default.conf || true

# Inicia Apache
service apache2 restart
service ssh start

# Mantém container vivo
tail -f /dev/null
