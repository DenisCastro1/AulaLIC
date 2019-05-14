def receber_lista_nomes_e_pedidos():
    lista_nomes=[]
    lista_pedidos=[]
    i=1

    while i<=7:
        nome=str(input("Digite seu nome:"))
        lista_nomes.append(nome)
        pedido=str(input("Digite o pedido:"))
        lista_pedidos.append(pedido)
        i=i+1
    return lista_nomes,lista_pedidos



    
