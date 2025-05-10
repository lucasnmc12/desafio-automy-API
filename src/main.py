from auth import obter_token
from query import buscar_baterias
from mensagens import gerar_mensagem



if __name__ == "__main__":
    email_cliente = input ("Digite o e-mail do cliente: ").strip()


print("Autenticando...")
token = obter_token()

if token:
    print("Token obtido")

    dados = buscar_baterias(token, email_cliente)

    print(f"Registros encontrados: {len(dados)}\n")
    for i, item in enumerate(dados, 1):
        print(f"Registro {i}: ")
        for chave, valor in item.items():
            print(f"{chave}: {valor}")

    mensagem = gerar_mensagem(dados)

    print(mensagem)

else:
    print("Nao foi possivel autenticar")
