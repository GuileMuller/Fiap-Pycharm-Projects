minuto_atual = int(input("Qual o minuto atual: "))
fatorial = 1

for i in range(1, minuto_atual+1):
    fatorial *= i

print("LIBERDADE" + str(fatorial))