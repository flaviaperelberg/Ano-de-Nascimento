# Implemente um programa capaz de solicitar para o usuário o seu nome e a sua idade. Após isso, deve imprimir na tela o nome do usuário e o ano do seu nascimento. 

nome = input('Digite seu nome: \n ')
idade = input('Qual é a sua idade: \n ')
ano = input('Em que ano você está: \n ')
print ('Você nasceu no ano de: \n')
print( int(ano) - int(idade) )