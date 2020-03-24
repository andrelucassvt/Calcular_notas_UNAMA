import sys
##Notas UNAMA
nota1 = float(input("Digite sua nota da 1º avaliação: \n"))
notaProvaColegiada = float(input("Digite sua nota da prova colegiada: \n"))

##Calculos da unama
CalcDasNotas = (nota1 + notaProvaColegiada)/2
CalcProvaFinal = (10 - CalcDasNotas)


if (nota1 <0) or (nota1 >10):
    print("Nota invalida")
    sys.exit(0)

elif (notaProvaColegiada < 0) or (notaProvaColegiada >10):
    print("Nota inválida")
    sys.exit(0)
else:
    ##Condições
    if CalcDasNotas >= 7:
        print("Você passou")
        sys.exit(0)
    elif (CalcDasNotas < 7) and (CalcDasNotas >= 4):
        print("Você está na prova final")
        print("Precisa tirar {} para passar".format(CalcProvaFinal))
        sys.exit
    elif CalcDasNotas < 4:
        print("Você reprovou")
        sys.exit
