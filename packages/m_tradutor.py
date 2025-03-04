import fitz  
from deep_translator import GoogleTranslator
from reportlab.pdfgen import canvas
from rich.progress import Progress
import os
import time

class TradutorPDF:
    def __init__(self, nome_arquivo, novo_nome_arquivo, primeira_idioma, segunda_idioma):
        self.nome_arquivo = nome_arquivo
        self.novo_nome_arquivo = novo_nome_arquivo
        self.tradutor = GoogleTranslator(source=primeira_idioma, target=segunda_idioma)

    def traduzir_pdf(self):   
        documento = fitz.open(self.nome_arquivo)
        documento_traduzido = ""

        with Progress() as progress:
            task = progress.add_task("[cyan]Traduzindo...", total=len(documento))
            
            #TRADUZINDO
            for pagina in documento:
                documento_extraido = pagina.get_text()
                texto_traduzido = self.tradutor.translate(documento_extraido)
                documento_traduzido += texto_traduzido + "\n\n"
                progress.update(task, advance=1)  
        
        self.salvar_pdf_traduzido(documento_traduzido)

    def salvar_pdf_traduzido(self, documento_traduzido):
        #MARGEM DA PAGINA TRADUZIDA
        c = canvas.Canvas(self.novo_nome_arquivo)   
        y = 780  
        linha_altura = 20 
        pagina_limite = 38
        contador_linhas = 0
        
        for linha in documento_traduzido.split("\n"):
            if contador_linhas >= pagina_limite:  
                c.showPage()  
                y = 780
                contador_linhas = 0

            c.drawString(50, y, linha) 
            y -= linha_altura 
            contador_linhas += 1

        c.save()


def escolher_idiomas():
    
    idiomas = ['pt', 'es', 'en', 'fr']
    print("Em qual idioma está seu arquivo? \n1. Português \n2. Espanhol \n3. Inglês \n4. Francês")
    #ESCOLHENDO O 1 IDIOMA
    try:
        primeiro_idioma = int(input("Resposta: "))
    except ValueError:
        os.system('cls')
        print('Opção indisponível, somente de 1 a 4. Tente novamente.')
        return escolher_idiomas()
    #IMPEDINDO OS ERROS
    if primeiro_idioma < 1 or primeiro_idioma > 4:
        os.system('cls')
        print("Opção indisponível, somente de 1 a 4. Tente novamente.")
        return escolher_idiomas() 

    try:
        os.system('cls')
        print("Para qual idioma deseja traduzir? \n1. Português \n2. Espanhol \n3. Inglês \n4. Francês")
        segundo_idioma = int(input("Resposta: "))
        
        #ESCOLHENDO O 2 IDIOMA
        if segundo_idioma < 1 or segundo_idioma > 4:
            os.system('cls')
            print("Opção indisponível, somente de 1 a 4. Tente novamente.")
            return escolher_idiomas()  
        
        #ESCOLHA DOS IDIOMAS
        segunda_idioma = idiomas[segundo_idioma - 1]
        primeira_idioma = idiomas[primeiro_idioma - 1]  
        
        #IMPEDINDO OS ERROS
        if primeira_idioma == segunda_idioma:
            os.system('cls')
            print("O idioma de origem e destino são iguais. Nada para traduzir.")
            return escolher_idiomas()  
    except ValueError:
        os.system('cls')
        print('Opção indisponível, somente de 1 a 4. Tente novamente.')


    return primeira_idioma, segunda_idioma


def Entrada_do_usuario():
    while True:
        try:
            nome_arquivo = input('Digite o nome do arquivo (ex: documento.pdf): ').strip()
            
            #IMPEDINDO OS ERROS
            if not nome_arquivo.endswith('.pdf'):
                raise ValueError("Erro: O arquivo precisa estar no formato PDF.")
            
            #IMPEDINDO OS ERROS
            if not os.path.exists(nome_arquivo):
                raise FileNotFoundError("Erro: Arquivo não encontrado.")

            primeira_idioma, segunda_idioma = escolher_idiomas()

            os.system('cls')
            novo_nome_arquivo = input('Digite o nome do novo arquivo (ex: traduzido.pdf): ').strip()
            
            #IMPEDINDO OS ERROS
            if not novo_nome_arquivo.endswith('.pdf'):
                raise ValueError("Erro: O novo arquivo precisa estar no formato PDF.")
            
            #IMPEDINDO OS ERROS
            if nome_arquivo == novo_nome_arquivo:
                raise ValueError("Erro: O nome do novo arquivo não pode ser o mesmo do original.")

            tradutor = TradutorPDF(nome_arquivo, novo_nome_arquivo, primeira_idioma, segunda_idioma)
            tradutor.traduzir_pdf()
            
            time.sleep(2)
            os.system('cls')
            pergunta = input("Digite qualquer tecla para voltar ao menu:")
            
            break

        except ValueError as erro:
            os.system('cls')
            print(erro)
            continue
        except FileNotFoundError as erro:
            os.system('cls')
            print(erro)
            continue
        except Exception as erro:
            os.system('cls')
            print(f"Ocorreu um erro inesperado: {erro}")
            continue
