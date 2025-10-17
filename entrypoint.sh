#!/bin/bash
set -e

# === CORES ===
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
BLUE='\033[1;34m'
NC='\033[0m' # Sem cor

echo -e "${BLUE}📦 Instalando dependências Python...${NC}"
pip install requests yt-dlp --break-system-packages

echo -e "${BLUE}📦 Atualizando pacotes e instalando zsh e sudo...${NC}"
apt update
apt install -y zsh sudo

echo -e "${BLUE}👤 Verificando/criando usuário 'sites'...${NC}"
if ! id sites >/dev/null 2>&1; then
    useradd -m -s /usr/bin/zsh sites || true
    usermod -aG sudo sites || true
else
    echo -e "${GREEN}✅ Usuário 'sites' já existe.${NC}"
fi

echo -e "${BLUE}🧾 Ajustando permissões de /app...${NC}"
chmod -R 777 /app/

cd /app/

echo -e "${BLUE}🎵 Instalando dependências Laravel...${NC}"
composer install --no-interaction --prefer-dist

echo -e "${BLUE}⚙️ Configurando ambiente Laravel (.env)...${NC}"
if [ ! -f .env ]; then
    echo -e "${YELLOW}📄 Copiando .env.example...${NC}"
    cp .env.example .env
    sed -i 's/^APP_ENV=.*/APP_ENV=local/' .env
    sed -i 's/^APP_DEBUG=.*/APP_DEBUG=true/' .env
    php artisan key:generate || true
else
    cp .env.example .env
    echo -e "${GREEN}✅ .env já existe.${NC}"
fi

chmod -R 777 /app

echo -e "${BLUE}💾 Preparando banco SQLite...${NC}"
rm -f /app/database/database.sqlite
touch /app/database/database.sqlite

echo -e "${BLUE}🚀 Rodando migrations e seeders...${NC}"
php artisan migrate:fresh --seed --force || {
    echo -e "${RED}❌ Erro ao rodar migrations.${NC}"
    exit 1
}

chmod -R 777 /app/database/database.sqlite

echo -e "${BLUE}🔌 Ativando módulos Apache...${NC}"
a2enmod rewrite
a2enmod ssl

CERT_DIR=/etc/apache2/certs

echo -e "${BLUE}🔏 Verificando certificados SSL...${NC}"
if [ ! -f "$CERT_DIR/pryamoy.test.pem" ] || [ ! -f "$CERT_DIR/pryamoy.test-key.pem" ]; then
    echo -e "${YELLOW}⚠️ Nenhum certificado encontrado em $CERT_DIR. Gerando self-signed...${NC}"
    mkdir -p $CERT_DIR
    openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
        -keyout $CERT_DIR/pryamoy.test-key.pem \
        -out $CERT_DIR/pryamoy.test.pem \
        -subj "/C=BR/ST=SP/L=SaoPaulo/O=Dev/OU=IT/CN=pryamoy.test"
else
    echo -e "${GREEN}✅ Usando certificados existentes em $CERT_DIR${NC}"
fi

echo -e "${BLUE}🔐 Habilitando site SSL...${NC}"
a2ensite 000-default.conf || true

echo -e "${BLUE}🚀 Reiniciando serviços...${NC}"
service apache2 restart
service ssh start

echo -e "${GREEN}🟢 Container iniciado com sucesso — mantendo ativo...${NC}"
tail -f /dev/null
