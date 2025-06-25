#!/bin/bash

# Script para instalar dependências do Click-Food

# Mudar para o diretório raiz do projeto
cd "$(dirname "$0")/.."

echo "📦 Instalando dependências do Click-Food..."

# Verificar se o ambiente virtual existe
if [ ! -d ".venv" ]; then
    echo "🔧 Criando ambiente virtual..."
    python3 -m venv .venv
fi

# Ativar ambiente virtual
echo "🔧 Ativando ambiente virtual..."
source .venv/bin/activate

# Instalar dependências
echo "📦 Instalando pacotes do requirements.txt..."
pip install -r requirements.txt

echo "✅ Dependências instaladas com sucesso!"
echo "🚀 Para executar o projeto: ./scripts/run.sh" 