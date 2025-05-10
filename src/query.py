import requests

QUERY_URL = "https://appsaccess.automy.com.br/api/api/desafio/custom/do/query"

def buscar_baterias(token: str, email: str) -> list[dict]:
    sql = (
        f"""SELECT * 
        FROM desafio.cadastro_baterias_desafio 
        WHERE email = '{email}'"""
    )

    body = {
        "query": sql,
        "db": "desafio"
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }

    try:
        response = requests.post(QUERY_URL, json=body, headers=headers)
        response.raise_for_status()
        return response.json()

    except requests.RequestException as e:
        print(f"❌ Erro ao consultar API: {e}")
        return []