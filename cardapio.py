cardapio = [
    {"nome": "X-Burger", "preco": 25.00},
    {"nome": "X-Frango", "preco": 23.00},
    {"nome": "Batata frita", "preco": 12.00},
    {"nome": "suco", "preco": 10.00},
    {"nome": "Refri", "preco": 8.00},
]
pedido = []

while True:
    menu = [
        "Cardapio",
        "Mostrar pedido",
        "Remover do pedido",
        "Valor total",
        "Finalizar",
    ]

    cont = 1
    for i in menu:
        print(f"{cont} - {i}")

        cont += 1

    escolha = int(input("Digite o que deseja: "))

    if escolha == 1:
    # mostrar cardapio e adc pedido
        while True:
            cont = 1
            for comida in cardapio:
                print(f"{cont} - {comida['nome']}      Preço: {comida['preco']}")
                cont += 1

            desejo = int(input("Digite o numero do que deseja pedir (ou 0 para voltar ao menu principal): "))

            if 1 <= desejo <= len(cardapio):
                itemPedido = cardapio[desejo - 1]
                pedido.append(itemPedido)
                print(f"{itemPedido['nome']}")

            elif desejo == 0:
                print("Voltando ao menu...")
                break

            else:
                print("Invalido")

    elif escolha == 2:  # mostrar pedido

        if len(pedido) == 0:
            print("Nada adicionado ao pedido")

        else:
            for comida in pedido:
                print(f"- {comida['nome']} | Preço: {comida['preco']}")

            voltar = int(input("aperte 0 para voltar: "))

    elif escolha == 3:  # remover pedido

        if len(pedido) == 0:
            print("Seu pedido esta vazio")                                                                                                   
        else:

            cont = 1
            for comida in pedido:
                print(f"{cont} - {comida['nome']}")
                cont += 1

            remover = int(input("Qual numero deseja apagar: "))


            if 1 <= remover <= len(pedido):
                deletar = pedido.pop(remover - 1)
                print(f"Removido - {deletar['nome']}")

            else:
                print("Esse numero ta invalido ")

        voltar = int(input("aperte 0 para voltar: "))

        if voltar != 0:
            print("Aperte 0 para voltar ao menu principal")

    elif escolha == 4:
        # total da compra
        calculo = 0

        for comida in pedido:
            calculo += comida["preco"]

        print(f"O total da compra é {calculo} :")

        voltar = int(input("aperte 0 para voltar ao menu: "))

        if voltar != 0:
            print("Aperte 0 para voltar ao menu principal")

    elif escolha == 5:
        break