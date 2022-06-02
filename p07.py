# p07.py
# Nome do programador: Henrique Abeldt Nepomoceno
# Matrícula: 106296
# Data: 10/02/2022
# Faz um relatório dos salários brutos auferidos pelos funcionários de
# uma empresa. Os registros dos funcionários são lidos do arquivo
# 'funcionarios.csv' e as horas trabalhadas, do arquivo 'horas_trab.dat'.

#OBS: no meu os nomes das pessoas estao saindo bugados, mas espero que seja o computador


import os
import csv

def main():
    # cwd = os.getcwd()
    # arq1 = "funcionarios.csv"
    # arq2 = "horas_trab.dat"
    dadosFuncionarios = lerFuncionarios("C:\Users\danie\Documents\VSCODE\PROJETOS\HENRIQUE\horas_trab.dat")
    dadosHorasTrab = lerHorasTrab("C:\Users\danie\Documents\VSCODE\PROJETOS\HENRIQUE\funcionarios.csv")
    salariosBrutos = calcSalBruto(dadosFuncionarios, dadosHorasTrab)

    # Imprime relatório dos salários brutos de todos os funcionários.
    print("\n-------   Relatório dos Salários Brutos   -------"
          "\nMatrícula         Nome          Salário Bruto")
    for i in range(len(dadosFuncionarios)):
        print("{:7d}    {:20s}    {:8.2f}".format(dadosFuncionarios[i][0],
                                             dadosFuncionarios[i][1],
                                             salariosBrutos[i]))


                                          
def lerFuncionarios(nomeArq):
    infos = []
    with open (nomeArq, 'r') as arqFuncionarios:
        reader = csv.reader(arqFuncionarios)  
        for row in reader:
            matricula = row[0]
            nome = row[1]
            cargo = row[2]
            salHr =   row[3]
            infos.append((matricula, nome, cargo, salHr))
    arqFuncionarios.close()
    print(infos)
    return infos

def lerHorasTrab(nomeArq):
    infos = []
    with open (nomeArq, 'r') as arqHorasTrab:
        reader = csv.reader(arqHorasTrab)   
        for row in reader:
            horasTrab = row[0]
            horaExt = row[1]
            infos.append((horasTrab, horaExt)) 
            print(row)
    arqHorasTrab.close()
    print(infos)
    return infos

 
def calcSalBruto(reader, reader2):
    salarios = []
    multiplicador = 1.5
    for linha in reader:
         salario = (reader2[linha][0] * reader[linha][3]) + (reader2[linha][1] * multiplicador * reader[linha][3])
         salarios.append(salario)
    return salarios

if __name__ == "__main__":
    main()
