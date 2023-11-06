print("VERIFICADOR DE FREQUÊNCIAS CARDÍACAS")
idade = int(input("Qual é a sua idade?: "))
bpm = int(input("Quanto batimentos por minuto você contou?: "))

if idade <= 2:
    if bpm >= 120:
        if bpm <= 140:
            print("Batimentos DENTRO dos indicados para a idade")
        else:
            print("Batimentos ACIMA dos indicados para a idade")
    else:
        print("Batimentos ABAIXO dos indicados para a idade")

if idade >= 8:
    if idade <= 17:
        if bpm >= 80:
            if bpm <= 100:
                print("Batimentos DENTRO dos indicados para a idade")
            else:
                print("Batimentos ACIMA dos indicados para a idade")
                print("Batimentos ideais para crianças entre 8 e 17 anos é 120BPM")
        else:
            print("Batimentos ABAIXO dos indicados para a idade")