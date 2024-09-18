import matplotlib.pyplot as plt

class Livro:
    def __init__(self, título, autor, gênero, quantidade):
        self.título = título
        self.autor = autor
        self.gênero = gênero
        self.quantidade = quantidade

    def __str__(self):
        return (f'\nO Livro {self.título} \nAutor: {self.autor} \nGênero: {self.gênero} \nQuantidade {self.quantidade} livros disponível')

Biblioteca = []

def adicionar_livro(título, autor, gênero, quantidade):
    for livro in Biblioteca:
        if livro.título.lower() == título.lower() and livro.autor.lower() == autor.lower()\
                and livro.gênero.lower() == gênero.lower():
            livro.quantidade += quantidade
            print(f'\nQuantidade do livro {título and autor} foi atualizada')
            print(f'\n{livro.quantidade} livros \nQuantidade Atualizada ')
            return

    novo_livro = Livro(título, autor, gênero, quantidade)
    Biblioteca.append(novo_livro)
    print('\nO Livro {} adicionado na Biblioteca'.format(título))


def listar_livro():
    if not Biblioteca:
        print('\nAinda não temos Livros na Biblioteca')
    else:
        print('Livros na Biblioteca')
        for livro in Biblioteca:
            print(livro)

def pesquisar_livro(título):
    resultados = [livro for livro in Biblioteca
                  if (título is None or livro.título.lower() == título.lower())]
    if not resultados:
        print('\nSua pesquisa sobre esse livro não existe em nossa Biblioteca')
    else:
        print('Resultados da pesquisa')
        for livro in resultados:
            print(livro)

def gráfico_quantidade_livros():
    gêneros_quantidade = {}
    for livro in Biblioteca:
        if livro.gênero in gêneros_quantidade:
            gêneros_quantidade[livro.gênero] += livro.quantidade
        else:
            gêneros_quantidade[livro.gênero] = livro.quantidade

    gêneros = list(gêneros_quantidade.keys())
    quantidades= list(gêneros_quantidade.values())

    plt.bar(gêneros, quantidades)
    plt.xlabel('Gênero')
    plt.ylabel('Quantidade')
    plt.title('Quantidade de Livros por Gênero')
    plt.show()

def menu():
    while True:
        print('\n"'+'"'*29)
        print('\n1. Cadastrar um novo Livro')
        print('\n2. Listar todos os Livros')
        print('\n3. Buscar um Livro')
        print('\n4. Gráfico de Quantidade de Livros')
        print('\n5. Sair')
        print('\n"'+'"'*29)

        escolha = input('Digite uma opção (1-5): ')
        if escolha == '1':
            print('\nVocê escolheu Cadastrar um novo Livro')
            título = input('\nDigite o título do Livro: ')
            autor = input('Digite o autor do Livro: ')
            gênero = input('Digite o gênero do Livro: ')
            quantidade = int(input('Digite a quantidade: '))
            adicionar_livro(título, autor, gênero, quantidade)

        elif escolha == '2':
            print('\nVocê escolheu listar todos os Livros')
            listar_livro()

        elif escolha == '3':
            print('\nVocê escolheu buscar um Livro')
            título = input('Título do Livro: ')
            pesquisar_livro(título)

        elif escolha == '4':
            gráfico_quantidade_livros()

        elif escolha == '5':
            print('\nVocê escolheu Sair')
            print('\nSaindo...')
            break

        else:
            print('Opção Inválida. Selecione entre 1 e 5.')
menu()