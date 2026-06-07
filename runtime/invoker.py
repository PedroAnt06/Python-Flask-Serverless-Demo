from datetime import datetime, timezone

def invoke(fn, event: dict) -> dict:
    # Simula o AWS Lambda criando um contexto isolado
    # Na AWS real, isso acontece dentro de um container efêmero
    context = {
        "invoked_at": datetime.now(timezone.utc).isoformat(),
        "function_name": fn.__name__,
    }

    print(f"[Runtime] Invocando função: {fn.__name__}")

    # Entrega o evento e o contexto pra função — ela não sabe mais nada
    return fn(event, context)