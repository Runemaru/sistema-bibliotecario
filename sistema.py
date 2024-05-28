from datetime import datetime, timedelta
import biblioteca

usuarios = []
livro = biblioteca.livros()
livros_em_posse = 0
contador_cadastro = 1
contador_sistema = 1

while contador_cadastro == 1:
    inicio_cadastro = int(input(f'''
{75 * '-'}
Selecione uma opção:

[1] - Cadastrar Usuário
[2] - Realizar Login
[3] - Encerrar Sistema
[4] - Relatório
Digite a opção:'''))
    
    if inicio_cadastro == 1:
        print(75 * '-')
        nome = input('Digite o seu nome:')
        ID = int(input('Digite o seu número de identificação:'))
        telefone = (input('Digite o número do seu celular com DDD:'))
        
        print(75 * '-')
        
        usuarios.append({'Nome' : nome, 'ID' : ID, 'Telefone' : telefone, 'Livros_em_posse:' : livros_em_posse})
        print(f'Foi cadastro um novo usuário com as seguintes credenciais: \nNome: {nome} \nID: {ID} \nTelefone: {telefone} \nLivros em posse: {livros_em_posse}')
            
    elif inicio_cadastro == 2:
        verificar_login = int(input('Digite o seu ID:'))
        for usuario in usuarios:
            if usuario['ID'] == verificar_login:
                print(f'Bem-vindo {usuario['Nome']}!')
                while contador_sistema == 1:
                    inicio_sistema = int(input(f'''
{75 * '-'}                                     
Para acessar os nossos sistemas basta digitar conforme a opção:
[1] - Cadastrar de livro                                           
[2] - Emprestimo de livro
[3] - Devolução de livro
[4] - Consulta de livro
[5] - Relatórios
[0] - Sair
Digite a opção:'''))
                
                    if inicio_sistema == 1:
                        print(75 * '-')
                        cadastrar_livro = livro.cadastrar_livro()
                        print(cadastrar_livro)
                        
                    elif inicio_sistema == 2:
                        print(75 * '-')
                        emprestimo_livro = livro.emprestimo_livro()
                        print(emprestimo_livro)
                        usuario['Livros_em_posse:'] += 1

                    elif inicio_sistema == 3:
                        devolucao_livro = livro.devolver_livro()
                        print(devolucao_livro)
                        usuario['Livros_em_posse:'] -=1

                    elif inicio_sistema == 4:
                        consultar_livro = livro.consultar_livro()
                        print(consultar_livro)

                    elif inicio_sistema == 5:
                        tipos_relatorios = int(input('''
[1] - Relatório de empréstimos
[2] - Relatório de livros disponíveis                                            
Digite sua opção:'''))
                        if tipos_relatorios == 1:
                            print(livro.emprestados)
                        elif tipos_relatorios == 2:
                            print(livro.livros)
                        else:
                            'Saindo da sessão de relatórios.'
                    elif inicio_sistema == 6:
                        print('Realizando logout do seu ID em sistema...')

                    else:
                        inicio_sistema not in [1, 2, 3, 4, 5, 6]
                        print('Digite uma das opções desejadas')
                        break
                    
                else:
                    print('Usuário não encontrado.')
                

    elif inicio_cadastro == 3:
        print('Encerrando nossos sistemas... \nFoi um prazer lhe atender!')
        break

    elif inicio_cadastro == 4:
        print('Os seguintes usuários foram cadastrados')
        for usuario in usuarios:
            print(usuario)

    elif inicio_cadastro not in [1, 2, 3]:
            print('Por favor, digite uma das opções')