from datetime import datetime


# função utilizada apenas na interação pelo terminal

def gerar_mensagem(baterias: list[dict]) -> str:
    hoje = datetime.now().date()
    agendadas = []
    passadas =[]


    for bateria in baterias:
        data_str = bateria.get("data_agendamento")
        try:
            data = datetime.strptime(data_str, "%d/%m/%Y").date()
            if data >= hoje:
                agendadas.append(bateria)
            else:
                passadas.append(bateria)
        except ValueError:
            print(f"Data inválida:  {data_str}")

    mensagem = ("")


    deseja_proximas = input("Deseja visualizar suas próximas baterias?\n1 - Sim\n2 - Não\n>").strip()
    if not agendadas:
        print("Nenhuma amostra de próximas baterias")
    else:
        if deseja_proximas == "1":
            mensagem += "Proximas baterias agendadas:\n"
            for b in agendadas:
                mensagem += f"- {b['data_agendamento']} às {b['horario_agendamento']} - {b['qtde_pessoas']} pessoas\n"
            print(mensagem)
        else:
            print("Proximas baterias não exibidas")
        
        

    deseja_passadas = input("Deseja visualizar suas baterias passadas?\n1 - Sim\n2 - Não\n>").strip()
    if not passadas:
        print("Nenhuma amostra de baterias passadas")
    else:
        if passadas and isinstance(passadas[0], dict):
            if deseja_passadas == "1":
                mensagem += "\n Baterias passadas: \n"
                for b in passadas:
                    mensagem += f"- {b['data_agendamento']} às {b['horario_agendamento']} — {b['qtde_pessoas']} pessoas\n"
                print(mensagem)
            else:
                print("Baterias passadas não exibidas")
            

    return mensagem
            