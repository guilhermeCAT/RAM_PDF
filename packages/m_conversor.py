from pdf2docx import Converter
import os
import time

def conversor():
    while True:
        try:
            nome_arquivo = input('Digite o nome do arquivo (ex: documento.pdf): ')
            os.system('cls')

            #IMPEDINDO OS ERROS
            if not nome_arquivo.endswith('.pdf'):
                os.system('cls')
                raise ValueError("Erro: O arquivo precisa estar no formato PDF.")
            
            #IMPEDINDO OS ERROS
            if not os.path.exists(nome_arquivo):
                os.system('cls')
                raise FileNotFoundError("Erro: Arquivo não encontrado.")


        except ValueError as erro:
            print(erro)
            continue
        except FileNotFoundError as erro:
            print(erro)
            continue
        except Exception as erro:
            print(f"Ocorreu um erro inesperado: {erro}")
        break 

    formatos = ['docx', 'xlsx', 'pptx', 'txt']

    while True:
        print('Para qual formato você deseja converter?')
        print('1. Word (.docx) \n2. Excel (.xlsx) \n3. PowerPoint (.pptx) \n4. Texto (.txt)')


        formato_arquivo = int(input("Resposta: "))

        #IMPEDINDO OS ERROS
        if formato_arquivo < 1 or formato_arquivo > 4:
            os.system('cls')
            print('Opção indisponível, somente de 1 a 4. Tente novamente.')
            continue

        #ESCOLHENDO O FORMATO
        formato_arquivo = formatos[formato_arquivo - 1]
        break 


    novo_nome = nome_arquivo.replace('.pdf', f'.{formato_arquivo}')
    
    try:
        os.system('cls')
        cv = Converter(nome_arquivo)
        cv.convert(novo_nome)
        cv.close()
        print()
        time.sleep(2)
        os.system('cls')
        print(f"Arquivo convertido para {formato_arquivo} com sucesso!")
        pergunta = input("Digite qualquer tecla para voltar ao menu:")
        os.system('cls')
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado. Verifique o nome e tente novamente.")
    except Exception as erro:
        print(f"Erro inesperado: {erro}")





