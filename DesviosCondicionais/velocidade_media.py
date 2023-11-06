#Esse programa recebe a distância e o tempo e calcula a velocidade média
#Primeiro vamos pedir a distância e o tempo
print("Esser é o calculador de velocidade médio")
distancia = input("Digite a distância percorrida: ")
tempo = input("Digite o tempo percorrido: ")

#Realizando o calculo
velocidade_media = float(distancia) / float(tempo)

#Exibindo a mensagem
print("A velocidade média calculada foi de {:.2f} km/h" .format(velocidade_media))