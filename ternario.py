# Caso a idade seja maior ou igual a 18 anos, essa pessoa é maior de idade, caso contrario ela é menor de idade
# idade = 15
# if idade >= 18:
#     print('maior de idade')
# else:
#     print('menor de idade')

idade = 25
print('maior de idade') if idade >= 18 else print('Menor de idade')
#       expressão       if  condição    else       expressão  
possui_passaporte = False
print('favor embarcar')  if possui_passaporte else print('favor tirar passaporte')


#Desafio
##Use expressão condicional(operador ternario) para criar a seguinte condição
#  *se velocidade estiver acima de 100,  exibir : "Você foi multado". Caso contrario exiba siga em frente.

#*declare uma variavle com o valor de 80.

velocidade = 80
print('Você foi multado') if velocidade >= 100 else print('siga em frente')