# 📋 Comandos do Projeto Click-Food

## 🚀 Configuração Inicial

### 1. Criar ambiente virtual
```bash
python3 -m venv .venv
```

### 2. Ativar ambiente virtual
```bash
source .venv/bin/activate
```

### 3. Instalar dependências
```bash
pip install -r requirements.txt
```

## 🏃‍♂️ Executar o Projeto

### Usando scripts automatizados (Recomendado)
```bash
# Instalar dependências
./scripts/install.sh

# Executar servidor
./scripts/run.sh
```

### Iniciar o servidor Flask manualmente
```bash
source .venv/bin/activate && python run.py
```

### Ou em duas etapas:
```bash
# 1. Ativar ambiente virtual
source .venv/bin/activate

# 2. Executar servidor
python run.py
```

## 🌐 Acessar a Aplicação
- **URL Local:** http://localhost:5000
- **URL Externa:** http://0.0.0.0:5000

## 🛑 Parar o Servidor
- Pressione `Ctrl + C` no terminal onde o servidor está rodando

## 📦 Gerenciar Dependências

### Instalar nova dependência
```bash
source .venv/bin/activate && pip install nome-do-pacote
```

### Atualizar requirements.txt
```bash
source .venv/bin/activate && pip freeze > requirements.txt
```

### Desativar ambiente virtual
```bash
deactivate
```

## 🔧 Comandos Úteis

### Verificar se o ambiente virtual está ativo
```bash
which python
# Deve mostrar: /root/Click-Food/.venv/bin/python
```

### Verificar dependências instaladas
```bash
source .venv/bin/activate && pip list
```

### Verificar status do banco de dados
```bash
source .venv/bin/activate && python -c "from app import create_app, db; app = create_app(); app.app_context().push(); print('Banco conectado!')"
```

## 📁 Estrutura de Scripts
```
Click-Food/
├── scripts/
│   ├── install.sh  # Instalar dependências
│   └── run.sh      # Executar servidor
├── app/            # Código da aplicação
├── requirements.txt
└── run.py
``` 