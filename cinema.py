mapaAssento = [  {"cadeira": "A1", "status": "Livre"},
    {"cadeira": "A2", "status": "Livre"},
    {"cadeira": "A3", "status": "Livre"},
    {"cadeira": "B1", "status": "Livre"},
    {"cadeira": "B2", "status": "Livre"},
    {"cadeira": "B3", "status": "Livre"}]

while True:
    menu = [
        "assentos",
        "reservar assento",
        "cancelar reserva",
        "validar se o assento existe",
        "validar se esta reservado",
        "Encerrar sistema"
    ]

    cont = 1
    for i in menu:
        print(f"{cont} - {i}")
        cont += 1

    escolha = int(input("Digite o numero desejado: "))

    if escolha == 1:
        cont = 1
        for lugar in mapaAssento:
            print(f"{cont} - ´{lugar['cadeira']} | {lugar['status']} ")
            cont += 1

        voltar = int(input("Aperte 0 para voltar ao menu principal: "))

    elif escolha == 2:
        cont = 1
        for lugar in mapaAssento:
            print(f"{cont} - {lugar['cadeira']} | {lugar['status']}")
            cont += 1

        queroEsse = int(input("Digite o numero do assento desejado "))

        if queroEsse == 0:
            break

        if 1 <= queroEsse <= len(mapaAssento):
            meuAssento = mapaAssento [queroEsse - 1]

            