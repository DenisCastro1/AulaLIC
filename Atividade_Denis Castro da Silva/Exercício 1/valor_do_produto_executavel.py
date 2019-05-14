import valorfuncoes as f

pedido=str(input("Digite o seu pedido:"))

preco=f.valor_do_produto(pedido)

print("Pedido:{} ; Preço:{}".format(pedido,preco))
