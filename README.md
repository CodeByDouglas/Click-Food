# 🍕 Click-Food

Sistema de pedidos online para restaurantes desenvolvido em Flask.

## 🚀 Instalação Rápida

### Pré-requisitos
- Python 3.8 ou superior
- Git

### Passos para instalar

1. **Clone o repositório**
```bash
git clone <url-do-repositorio>
cd Click-Food
```

2. **Execute o script de instalação**
```bash
./scripts/install.sh
```

3. **Execute o projeto**
```bash
./scripts/run.sh
```

4. **Acesse a aplicação**
- Abra o navegador e acesse: http://localhost:5000

## 📋 Comandos Disponíveis

### Scripts Automatizados
```bash
# Instalar dependências
./scripts/install.sh

# Executar servidor
./scripts/run.sh
```

### Comandos Manuais
```bash
# Criar ambiente virtual
python3 -m venv .venv

# Ativar ambiente virtual
source .venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Executar servidor
python run.py
```

## 🛑 Parar o Servidor
Pressione `Ctrl + C` no terminal onde o servidor está rodando.

## 📁 Estrutura do Projeto
```
Click-Food/
├── app/
│   ├── models/          # Modelos do banco de dados
│   ├── routes/          # Rotas da aplicação
│   ├── templates/       # Templates HTML
│   ├── static/          # Arquivos estáticos (CSS, JS, imagens)
│   └── __init__.py      # Configuração da aplicação
├── scripts/
│   ├── install.sh       # Script de instalação
│   └── run.sh          # Script de execução
├── instance/
│   └── database.db     # Banco de dados SQLite
├── requirements.txt    # Dependências Python
├── run.py             # Arquivo principal
└── README.md          # Este arquivo
```

## 🔧 Desenvolvimento

### Adicionar nova dependência
```bash
source .venv/bin/activate
pip install nome-do-pacote
pip freeze > requirements.txt
```

### Verificar status do banco
```bash
source .venv/bin/activate
python -c "from app import create_app, db; app = create_app(); app.app_context().push(); print('Banco conectado!')"
```

## 📖 Documentação Completa
Veja o arquivo `comandos.md` para comandos detalhados e troubleshooting.

## 🐛 Problemas Comuns

### Erro de permissão nos scripts
```bash
chmod +x scripts/*.sh
```

### Ambiente virtual não encontrado
O script `install.sh` criará automaticamente o ambiente virtual.

### Porta 5000 em uso
Altere a porta no arquivo `run.py` ou pare outros serviços usando a porta 5000. 
