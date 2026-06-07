import json
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "data" / "db.json"

def get_user(event: dict, context: dict) -> dict:
    user_id = event.get("params", {}).get("id", "")

    users = json.loads(DB_PATH.read_text())
    user  = next((u for u in users if u["id"] == user_id), None)

    if not user:
        return {"status_code": 404, "body": {"error": "Usuário não encontrado"}}

    return {"status_code": 200, "body": user}