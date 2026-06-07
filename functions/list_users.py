import json
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "data" / "db.json"

def list_users(event: dict, context: dict) -> dict:
    users = json.loads(DB_PATH.read_text())
    return {"status_code": 200, "body": users}