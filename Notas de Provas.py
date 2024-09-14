#Notas das Provas
#Inserir as Notas
x = 0
while x ==0:
    prova_1 = float(input(' Prova 1: ', ))
    prova_2 = float(input(' Prova 2: ', ))
    prova_3 = float(input(' Prova 3: ', ))
    prova_4 = float(input(' Prova 4: ', ))
    prova_5 = float(input(' Prova 5: ', ))

#Lista dos Pontos das Provas

    lista = [prova_1, prova_2, prova_3, prova_4, prova_5]

#Criei Duas Funções

    def soma(prova_1, prova_2, prova_3, prova_4, prova_5,):
        resultado_soma = prova_1+ prova_2+ prova_3+ prova_4+ prova_5
        return resultado_soma
    total_soma = float(soma(prova_1, prova_2, prova_3, prova_4, prova_5,))

    def media(total_soma):
        resultado_media = total_soma / len(lista)
        return resultado_media
    total_media = float(media(total_soma))
    media_arredondada = int(total_media)

#Relatório

    escolha1 = str(input('Deseja Acessar o seu Relatório? ', ))
    if escolha1 == 'sim':
        print('Média das Provas: ',f'{media_arredondada} Pontos')
        print('Média Necessária de 7 Pontos')
        print('Total de Pontos: ', f'{total_soma} Pontos')
        print('Suas Notas Foram: ', lista)
        if media_arredondada >= 7:
            print('Situação:  Aprovado')
        else:
            print('Situação:  Reprovado')
    elif escolha1 == 'não':
        print('Ok, Muito Obrigado!!')
        break
    elif escolha1 != 'sim' and 'não':
        print('Responda com sim ou não')
        break

    escolha2 = str(input('Deseja Repetir o Código? ', ))
    if escolha2 == 'não':
        print('Ok, Muito Obrigado!!')
        break
    elif escolha2 == 'sim':
        print()
    elif escolha2 != 'sim' and 'não':
        print('Responda com sim ou não')
        break