nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade >= 18:
    #aluno maior
    print("Aluno maior de idade")
else:
    #aluno menor
    print("O aluno {} é menor de idade. Consultar os responsáveis" .format(nome))