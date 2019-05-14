def receber_pedido():
    lista_nomes=[]
    lista_pedidos=[]
    lista_preços=[]
    
    i=1
    while i<=7:
        nome=str(input("Digite seu nome:"))
        lista_nomes.append(nome)
        pedido=str(input("Digite seu pedido:"))
        
        if pedido=="Salgado" or pedido=="salgado":
            preço1=4.0
            lista_preços.append(preço1)
        
        elif pedido=="Refrigerante" or pedido=="refrigerante":
            preço2=4.5
            lista_preços.append(preço2)
        
        elif pedido=="Suco" or pedido=="suco":
            preço3=5.0
            lista_preços.append(preço3)
        elif pedido=="Sorvete" or pedido=="sorvete":
            preço4=6.0
            lista_preços.append(preço4)
        elif pedido=="café" or pedido=="Café" or pedido=="cafe" or pedido=="Cafe":
            preço5=4.0
            lista_preços.append(preço5)
       
        elif pedido=="Capuccino" or pedido=="capuccino":
            preço6=6.0
            lista_preços.append(preço6)
     
        elif pedido=="Bolo" or pedido=="bolo":
            preço7=4.5
            lista_preços.append(preço7)
        
        elif pedido=="Dadinho" or pedido=="dadinho":
            preço8=0.5
            lista_preços.append(preço8)
            
        lista_pedidos.append(pedido)
        
        i=i+1

    print("Os nomes são:{},os respectivos pedidos são:{}, e os respectivos preços são:{}".format(lista_nomes,lista_pedidos,lista_preços))
    caixa=sum(lista_preços)
    print("O valor final do caixa é {}".format(caixa))
    

receber_pedido()


    
        
        
        
