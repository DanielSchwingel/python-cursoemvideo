#Calculando descontos
preco = float(input('Digite o preço do produto: R$'))
desconto = preco * 5 / 100
print('O novo preço considerando o desconto é de R${:.2f}'.format((preco - desconto)))