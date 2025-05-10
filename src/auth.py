import requests

LOGIN_URL = "https://appsaccess.automy.com.br/login"

USERNAME = "fldoaogopdege"
SENHA = "ygalepsm"

def obter_token():
    payload = {
        "username": USERNAME,
        "password": SENHA
    }
    
    headers = {
         "Content-Type": "application/json"
    }

    try:
        response = requests.post(LOGIN_URL, json=payload, headers=headers)
        response.raise_for_status()
        token = response.json().get("token")


        if not token:
            raise ValueError("Token nao encontrado")
        
        return token
    
    except requests.RequestException as e:
        print(f"Erro na requisição: {e}")
    except ValueError as ve:
        print(f"Erro ao obter token: {ve}")
    return None
