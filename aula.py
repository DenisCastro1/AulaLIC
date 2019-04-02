valor=int(input("Digite o valor:"))
dia=0
x=1


while valor>0 :
    
    


    if valor%2!=0:
        
        valor=(valor*3+1)/2
        
        dia=dia+1
       
    
        
    
        
        
    if valor%2==0:
       
        valor=valor/2
        
        dia=dia+1

    if valor==1:
        print("Levam",dia,"dias para o preço chegar a 1 real")
        break
    
