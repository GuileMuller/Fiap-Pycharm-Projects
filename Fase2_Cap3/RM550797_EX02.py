segunda = int(input("Quantos votos Segunda-Feira recebeu?: "))
terca = int(input("Quantos votos Terça-Feira recebeu?: "))
quarta = int(input("Quantos votos Quarta-Feira recebeu?: "))
quinta = int(input("Quantos votos Quinta-Feira recebeu?: "))
sexta = int(input("Quantos votos Sexta-Feira recebeu?: "))

print("Segunda-Feira recebeu {} votos\n Terça-Feira recebeu {} votos\n Quarta-Feira recebeu {} votos\n Quinta-Feira recebeu {} votos\n Sexta1-Feira recebeu {} votos\n" .format(segunda, terca, quarta, quinta, sexta))

if segunda > terca and segunda > quarta and segunda > quinta and segunda > sexta :
    print("Segunda-Feira foi o dia com mais votos!")
elif (terca > segunda) and (terca > quarta) and (terca > quinta) and (terca > sexta) :
    print("Terça-Feira foi o dia com mais votos!")
elif (quarta > segunda) and (quarta > terca) and (quarta > quinta) and (quarta > sexta) :
    print("Quarta-Feira foi o dia com mais votos!")
elif (quinta > segunda) and (quinta > terca) and (quinta > quarta) and (quinta > sexta) :
    print("Quinta-Feira foi o dia com mais votos!")
elif (sexta > segunda) and (sexta > terca) and (sexta > quarta) and (sexta > quinta) :
    print("Sexta-Feira foi o dia com mais votos!")