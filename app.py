from flask import Flask, request, jsonify
from runtime.invoker import invoke
from functions.create_user import create_user
from functions.get_user    import get_user
from functions.list_users  import list_users

app = Flask(__name__)

# API Gateway: recebe HTTP → monta event → chama invoker → chama função
@app.post("/users")
def route_create_user():
    event = {"body": request.get_json(silent=True) or {}, "params": {}}
    result = invoke(create_user, event)
    return jsonify(result["body"]), result["status_code"]

@app.get("/users/<user_id>")
def route_get_user(user_id):
    event = {"body": {}, "params": {"id": user_id}}
    result = invoke(get_user, event)
    return jsonify(result["body"]), result["status_code"]

@app.get("/users")
def route_list_users():
    event = {"body": {}, "params": {}}
    result = invoke(list_users, event)
    return jsonify(result["body"]), result["status_code"]

if __name__ == "__main__":
    app.run(debug=True, port=5000)