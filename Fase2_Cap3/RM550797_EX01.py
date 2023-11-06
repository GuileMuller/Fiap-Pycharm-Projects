ass_cliente = int(input("Qual será a sua assinatura?\n 1-Basic\n 2-Silver\n 3-Gold\n 4-Platinum\n Escolha um número: "))
faturamento = float(input("Qual foi o seu faturamento no último ano? "))
total = 0
if ass_cliente == 1:
    total = faturamento * 0.3
    ass_cliente = "Basic"
elif ass_cliente == 2:
    total = faturamento * 0.2
    ass_cliente = "Silver"
elif ass_cliente == 3:
    total = faturamento * 0.1
    ass_cliente = "Gold"
elif ass_cliente == 4:
    total = faturamento * 0.05
    ass_cliente = "Platinum"

print(str("O plano que foi escolhido foi o {} e voce tem de bônus o valor de {}" .format(ass_cliente, total)))