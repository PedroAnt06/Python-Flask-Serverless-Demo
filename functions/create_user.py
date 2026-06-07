import json, uuid
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "data" / "db.json"

def create_user(event: dict, context: dict) -> dict:
    # event.body = corpo da requisição HTTP (vem do API Gateway)
    body  = event.get("body", {})
    name  = body.get("name", "").strip()
    email = body.get("email", "").strip()

    # Validação — sem estado, sem depender de nada externo
    if not name or not email:
        return {"status_code": 400, "body": {"error": "Nome e email obrigatórios"}}

    # Lê o "banco" externo — stateless: lê do zero a cada execução
    users = json.loads(DB_PATH.read_text())

    if any(u["email"] == email for u in users):
        return {"status_code": 409, "body": {"error": "Email já cadastrado"}}

    new_user = {
        "id": str(uuid.uuid4()),
        "name": name,
        "email": email,
        "created_at": context["invoked_at"],  # usa o contexto do runtime
    }

    users.append(new_user)
    DB_PATH.write_text(json.dumps(users, indent=2))

    return {"status_code": 201, "body": new_user}