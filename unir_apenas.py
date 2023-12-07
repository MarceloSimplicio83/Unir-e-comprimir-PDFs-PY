import os
from PyPDF2 import PdfMerger

def unir_pdfs(caminho_saida, *caminhos_entrada):
    pdf_merger = PdfMerger()

    for caminho_entrada in caminhos_entrada:
        pdf_merger.append(caminho_entrada)

    with open(caminho_saida, 'wb') as pdf_output:
        pdf_merger.write(pdf_output)

if __name__ == "__main__":
    # Substitua os nomes dos arquivos de entrada e o nome do arquivo de saída conforme necessário
    pasta_entrada = 'C:\\Users\\maarc\\Downloads\\EntradaNotasAvulsas'    # Caminho pasta dos arquivos
    pasta_saida = 'C:\\Users\\maarc\\Downloads\\SaidaNotas'    # Caminho Pasta onde o arquivo será descarregado
    
    # Certifique-se de que a pasta de saída exista
    os.makedirs(pasta_saida, exist_ok=True)

    # Lista todos os arquivos na pasta de entrada
    arquivos_entrada = [os.path.join(pasta_entrada, arquivo) for arquivo in os.listdir(pasta_entrada) if arquivo.endswith('.pdf')]

    # Nome do arquivo de saída
    caminho_arquivo_saida = os.path.join(pasta_saida, 'ArquivoUnido.pdf')

    # Chamando a função para unir os arquivos sem comprimir
    unir_pdfs(caminho_arquivo_saida, *arquivos_entrada)

    print(f'Arquivos unidos com sucesso em {caminho_arquivo_saida}')
