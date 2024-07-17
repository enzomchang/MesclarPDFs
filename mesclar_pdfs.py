""" AUTOMAÇÃO PARA MESCLAR PDF'S """

# OBS: (É POSSÍVEL MESCLAR MÚLTIPLOS PDF'S - 2, 3, 4...)

##############################
### Bibliotecas Essenciais ###
##############################

import PyPDF2   # Manipular Pdf's
import tkinter as tk    # Criar a interface gráfica e permitir que o usuário selecione arquivos.
from tkinter.filedialog import askopenfilenames # Permite selecionar múltiplos arquivos

###############################
### Instalações Necessárias ###
###############################

#pip install PyPDF2

##############################
###### Funções Projeto #######
##############################

def selecionar_arquivos():
    """Função para abrir um diálogo para o usuário selecionar arquivos PDF"""
    root = tk.Tk()
    root.withdraw()  # Ocultar a janela principal
    arquivos = askopenfilenames(title="Selecione os arquivos PDF", filetypes=[("PDF Files", "*.pdf")])
    return arquivos

def mesclar_pdfs(lista_arquivos, output_path="PDF_Merged_Final.PDF"):
    """Função para mesclar arquivos PDF"""
    merger = PyPDF2.PdfMerger()
    
    for arquivo in lista_arquivos:
        merger.append(arquivo)
    
    merger.write(output_path)
    merger.close()

def main():
    # Selecionar arquivos PDF
    arquivos_selecionados = selecionar_arquivos()
    
    # Verificar se algum arquivo foi selecionado
    if not arquivos_selecionados:
        print("Nenhum arquivo selecionado.")
        return
    
    # Mesclar arquivos PDF
    mesclar_pdfs(arquivos_selecionados)
    print(f"PDFs mesclados e salvos como 'PDF_Merged_Final.PDF'.")

if __name__ == "__main__":
    main()
