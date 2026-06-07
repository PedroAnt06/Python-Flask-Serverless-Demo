# 🧪 Serverless Demo — Simulação Didática

> **⚠️ Este projeto é uma demonstração acadêmica.**
> Ele simula localmente os componentes do padrão arquitetural Serverless para fins didáticos.
> Não é uma aplicação de produção e não está conectado a nenhum serviço de nuvem real.

---

## 📌 Sobre o Projeto

Este projeto foi desenvolvido como parte do **Seminário de Padrões Arquiteturais** da disciplina de Arquitetura de Software.

O objetivo é demonstrar, de forma prática e executável, os principais componentes do padrão **Serverless (FaaS — Functions as a Service)**, simulando localmente o comportamento que serviços como o **AWS Lambda** oferecem em produção.

---

## 🏗️ Componentes Arquiteturais Simulados

| Componente Real (AWS) | Simulação neste projeto | Arquivo |
|---|---|---|
| **API Gateway** | Servidor Flask com rotas HTTP | `app.py` |
| **Lambda Runtime** | Invocador que cria contexto isolado | `runtime/invoker.py` |
| **Lambda Function** | Funções independentes e stateless | `functions/*.py` |
| **BaaS / DynamoDB** | Arquivo JSON simples | `data/db.json` |

---

## 📁 Estrutura de Pastas

```
serverless-demo/
├── app.py                  # API Gateway simulado (Flask)
├── runtime/
│   └── invoker.py          # Runtime serverless simulado
├── functions/
│   ├── create_user.py      # Function: criar usuário
│   ├── get_user.py         # Function: buscar usuário por ID
│   └── list_users.py       # Function: listar todos os usuários
├── data/
│   └── db.json             # Persistência externa simulada (BaaS)
└── requirements.txt
```

---

## ⚙️ Como Executar

### Pré-requisitos
- Python 3.10+
- pip

### Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/serverless-demo.git
cd serverless-demo

# Instale as dependências
pip install -r requirements.txt

# Certifique-se que o db.json está vazio
echo [] > data/db.json

# Rode o servidor
python app.py
```

O servidor sobe em `http://localhost:5000`.

---

## 🔁 Fluxo de uma Requisição

```
Cliente (Postman)
      ↓  HTTP POST /users
app.py  →  monta o "event"
      ↓
invoker.py  →  cria o "context" isolado  →  invoca a função
      ↓
functions/create_user.py  →  valida, lê db.json, salva, retorna
      ↓
app.py  →  devolve resposta HTTP ao cliente
```

Cada função **não conhece as outras** — o invoker é quem faz a ponte, assim como o AWS Lambda Runtime faz em produção.

---

## 📬 Endpoints Disponíveis

### `POST /users` — Criar usuário
```bash
curl -X POST http://localhost:5000/users \
  -H "Content-Type: application/json" \
  -d '{"name": "Pedro", "email": "pedro@email.com"}'
```

**Resposta `201`:**
```json
{
  "id": "4d45991c-...",
  "name": "Pedro",
  "email": "pedro@email.com",
  "created_at": "2026-06-07T..."
}
```

---

### `GET /users` — Listar todos
```bash
curl http://localhost:5000/users
```

---

### `GET /users/:id` — Buscar por ID
```bash
curl http://localhost:5000/users/4d45991c-...
```

---

## ❌ O que este projeto NÃO é

- Não é uma aplicação serverless real
- Não está hospedado em nenhum provedor de nuvem
- Não usa AWS Lambda, Google Cloud Functions ou Azure Functions
- O `db.json` substitui um banco de dados real (ex: DynamoDB) apenas para fins didáticos
- O Flask substitui o API Gateway da AWS apenas para fins didáticos

---

## ✅ O que este projeto demonstra

- Isolamento entre funções (cada `.py` em `functions/` é independente)
- Stateless por design (nenhuma função guarda estado entre execuções)
- Separação clara de responsabilidades (gateway → runtime → function → baas)
- Event-driven (funções só executam quando invocadas)

---

## 🚀 Como seria em produção real

Em um ambiente real na AWS, cada função em `functions/` seria deployada como uma **Lambda Function** separada, o `app.py` seria substituído pelo **API Gateway da AWS**, e o `db.json` seria substituído pelo **DynamoDB**.

```bash
# Exemplo de deploy real com AWS CLI
aws lambda create-function \
  --function-name create_user \
  --runtime python3.12 \
  --handler create_user.create_user \
  --zip-file fileb://create_user.zip \
  --role arn:aws:iam::SEU_ID::role/lambda-role
```
