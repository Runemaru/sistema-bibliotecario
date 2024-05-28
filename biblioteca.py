from datetime import datetime as dt, timedelta as td
livros_devolvidos = True
class livros:
    '''
    A classe Livro contêm as seguintes funções, focando nas seguintes resoluções:

    cadastrar_livro : Permite o cadastro de livros em sistema incluindo informações como título, autor, ano de publicação e cópias disponíveis.
    emprestimo_de_livro : Permite que o usuário solicite o empréstimo de livro por determinado período. Utiliza elementos da biblioteca datetime.
    devoluçao_de_livro : Trás a possibilidade de devolução de um livro que foi emprestado. Utiliza elementos da biblioteca datetime.
    consultar_livro : Trás a possibilidade de consultar livros por nome de autor, ano de publicação ou título.
    '''

    def __init__(self):
        self.livros = []
        self.emprestados = []


    def cadastrar_livro(self): #Esta classe trás algumas informações referentes aos dados do livro que será cadastrado em sistema, onde o usuário do sistema trará o título, autor, ano de publicação e número de cópias disponíveis do livro em questão. Após isto, o mesmo é colocado na lista vazia que foi criada na classe Livro em seu construtor. Fazendo com que a lista receba o valor em um dado do tipo dicionário, para que assim tenhamos maior facilidade para acessar e organizar os valores.
        titulo = input('Qual o titulo do livro:')
        autor = input('Nome do autor:')
        ano_publicacao = int(input('Qual o ano de lançamento:'))
        copias_disponiveis = int(input('Quantia de cópias disponiveis:'))
        self.livros.append({'Titulo' : titulo, 'Autor' : autor, 'Publicado' : ano_publicacao, 'Copias' : copias_disponiveis})
        return f'Livro cadastro em nosso sistema: \n Titulo: {titulo} \n Autor: {autor} \n Publicado: {ano_publicacao} \n Copias: {copias_disponiveis}'


    def emprestimo_livro(self):
        data_atual = dt.now()
        data_entrega = data_atual + td(days = 7)

        solicitar_emprestimo = input('Digite o título do livro que gostaria de solicitar empréstimo:')
        for livro in self.livros:
            print(75 * '-')
            if livro['Titulo'] == solicitar_emprestimo and livro['Copias'] >= 1:
                livro['Copias'] -= 1
                print(f'O livro {solicitar_emprestimo} foi emprestado com sucesso na data {data_atual}')
                print(f'E deve ser devolvido na data {data_entrega}')
                self.emprestados.append({'Titulo' : solicitar_emprestimo})
                return 'Empréstimo feito com sucesso.'

            elif livro['Copias'] == 0 and livro['Titulo'] == solicitar_emprestimo:
                print(75 * '-')
                print(f'O livro {solicitar_emprestimo} não possui mais cópias para empréstimo.')
                return 'Pedimos desculpas pelo inconveniente.'
        
        return f'Não possuímos o titulo buscado. Solicite o acréscimo em sistema.'


    def devolver_livro(self):
        livros_devolvidos
        devolucao = input('Digite o título do que livro que gostaria de devolver:')

        for livro in self.livros:
            if livro['Titulo'] == devolucao:
                livro['Copias'] +=1
                if livros_devolvidos:
                    for livros_emprestados in self.emprestados:
                        if livros_emprestados['Titulo'] == devolucao:
                             del livros_emprestados['Titulo']
                             return f'Livro {devolucao} devolvido com sucesso.'
            if not livros_devolvidos:
                return f'O livro de titulo {devolucao}, não foi encontrado, certifique-se de digitar exatamente igual ao título'


    
    def consultar_livro(self):

        tipo_de_consulta = int(input('''
Como gostaria de buscar por seus livros:
[1] Busca por títulos:
[2] Busca por autores:
[3] Busca por ano de publicação:
[0] Encerrar serviços de busca:
Digite de acordo com sua necessidade:'''))

        if tipo_de_consulta == 1:
            busca_titulos = input('Digite o titulo do livro:')
            livros_encontrados = False

            for livro in self.livros:
                if livro['Titulo'] == busca_titulos:
                    print(f'Livro: {busca_titulos}, existente em sistema, temos: {livro["Copias"]} em estoque!')
                    livros_encontrados = True
                    if livros_encontrados:
                        return f'Encerrando busca'
                if not livros_encontrados:
                     return f'Busca sem resultados.'
                    


        elif tipo_de_consulta == 2:
            busca_autores = input('Digite o nome do autor:')
            livros_encontrados = True

            for livro in self.livros:
                if livro['Autor'] == busca_autores:
                    print(f'Título encontrado: {livro['Titulo']}')
                    livros_encontrados = False
                    if livros_encontrados:
                        return f'Encerrando busca'
                if not livros_encontrados:
                     return f'Busca sem resultados.'

        elif tipo_de_consulta == 3:
            busca_ano = int(input('Digite o ano de publicação do livro:'))
            livros_encontrados = True

            for livro in self.livros:
                if livro['Publicado'] == busca_ano:
                    print(f'Titulo encontrado: {livro['Titulo']}')
                    livros_encontrados = False
                    if livros_encontrados:
                        return f'Encerrando busca'
                if not livros_encontrados:
                     return f'Busca sem resultados.'
        
        elif tipo_de_consulta not in [1, 2, 3, 0]:
            return 'Digite uma das opções presentes.'