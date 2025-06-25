#!/bin/bash

# Script para executar o projeto Click-Food

# Mudar para o diretório raiz do projeto
cd "$(dirname "$0")/.."

echo "🚀 Iniciando Click-Food..."

# Verificar se o ambiente virtual existe
if [ ! -d ".venv" ]; then
    echo "❌ Ambiente virtual não encontrado!"
    echo "📦 Criando ambiente virtual..."
    python3 -m venv .venv
fi

# Ativar ambiente virtual
echo "🔧 Ativando ambiente virtual..."
source .venv/bin/activate

# Verificar se as dependências estão instaladas
if [ ! -f ".venv/lib/python*/site-packages/flask" ]; then
    echo "📦 Instalando dependências..."
    pip install -r requirements.txt
fi

# Executar o servidor
echo "🌐 Iniciando servidor Flask..."
echo "📍 URL: http://localhost:5000"
echo "🛑 Para parar: Ctrl + C"
echo ""

python run.py 