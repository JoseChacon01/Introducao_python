
print("HELLO WORLD")

numero = 10
print (numero)
print (type (numero)) # type -> informa p tipo de dado que esta na variavel.
print ("valor armazenado", numero) # para contatenas utiliza 

# OPERADORES:
print (numero / 3)
print (numero // 3)
print (numero ** 2)

#Atividade 1
numeror = 4.2
print ("O numero armazenado é", numeror)

#Atividade 2
ndobro = 30
print (ndobro * 2)

#Leitura de dados
nome = input ("Digite seu nome:")
print (nome)

#Formas de conversão
idade = int(input("Digite sua idade:"))  #inteiro
print (idade)

valor = float (input("Digite o valor de um produto:")) #real
print (valor)

#Operadores condicionais
print (10>5)
print (10==5)

#Operadores logicos: E (and)/ OU (or)/ Negação (not)!

#Condições (IF e ELSE)

#Atividade da media
notaa = int (input("Digite a primeira nota:")) #real
print (notaa)

notab = int (input("Digite a segunda nota:")) #real
print (notab)

geral = notaa + notab

media = geral / 2

if media > 7:
 print ("APROVADO")