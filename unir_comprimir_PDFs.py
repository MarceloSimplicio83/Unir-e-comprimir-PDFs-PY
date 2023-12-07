# Top - funcionando e compactando, preservando as assinaturas -Show

import os
import subprocess
from PyPDF2 import PdfMerger

def unir_e_comprimir_pdfs(caminho_saida, *caminhos_entrada):
    pdf_merger = PdfMerger()

    for caminho_entrada in caminhos_entrada:
        pdf_merger.append(caminho_entrada)

    caminho_temporario = caminho_saida.replace('.pdf', '_temp.pdf')

    # Salva o documento temporário antes de comprimir
    with open(caminho_temporario, 'wb') as pdf_output:
        pdf_merger.write(pdf_output)

    # Use Ghostscript para realizar uma compressão extrema
    comando = [
        'gswin64c',  # ou 'gs' para sistemas diferentes
        '-sDEVICE=pdfwrite',
        '-dCompatibilityLevel=1.4',
        '-dNOPAUSE',
        '-dQUIET',
        '-dBATCH',
        '-dCompressPages=true',  # Ativa a compressão extrema
        '-dCompressFonts=true',  # Comprime as fontes
        f'-sOutputFile={caminho_saida}',
        caminho_temporario
    ]
    subprocess.run(comando)

    # Remove o arquivo temporário
    os.remove(caminho_temporario)

if __name__ == "__main__":
    # Substitua os nomes dos arquivos de entrada e o nome do arquivo de saída conforme necessário
    pasta_entrada = 'C:\\Users\\maarc\\Downloads\\EntradaNotasAvulsas'
    pasta_saida = 'C:\\Users\\maarc\\Downloads\\SaidaNotas'
    
    # Certifique-se de que a pasta de saída exista
    os.makedirs(pasta_saida, exist_ok=True)

    # Lista todos os arquivos na pasta de entrada
    arquivos_entrada = [os.path.join(pasta_entrada, arquivo) for arquivo in os.listdir(pasta_entrada) if arquivo.endswith('.pdf')]

    # Nome do arquivo de saída compactado
    caminho_arquivo_saida_compactado = os.path.join(pasta_saida, 'ArquivoUnido_Compactado.pdf')

    # Chamando a função para unir e comprimir os arquivos
    unir_e_comprimir_pdfs(caminho_arquivo_saida_compactado, *arquivos_entrada)

    print(f'Arquivos unidos e comprimidos com sucesso em {caminho_arquivo_saida_compactado}')
