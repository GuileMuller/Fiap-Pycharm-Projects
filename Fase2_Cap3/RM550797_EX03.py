# soma_nota_impar = 0
# for alunos_imp in range(1,50,2) :
#     print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS IMPARES")
#     nota_impares = float(input(str("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: " .format(alunos_imp))))
#     soma_nota_impar = nota_impares + soma_nota_impar
#
# media_impar = soma_nota_impar / 25

soma_nota_par = 0
for alunos_par in range(2,51,2) :
    print("VOCÊ ESTÁ DIGITANDO AS NOTAS DOS ALUNOS PARES")
    nota_par = float(input(str("POR FAVOR, INSIRA A NOTA DO ALUNO DE NÚMERO {}: " .format(alunos_par))))
    soma_nota_par = nota_par + soma_nota_par

media_par = soma_nota_par / 25
print("A média dos alunos PARES é {} " .format(media_par))
print("A média dos alunos IMPARES é {} " .format(media_impar))

if media_par > media_impar:
    print("A média dos alunos de número par é maior que a dos alunos impares")
else:
    print("A média dos alunos de número impar é maior que a dos alunos pares")