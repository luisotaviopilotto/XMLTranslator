import os
import xml.etree.ElementTree as ET
from deep_translator import GoogleTranslator
import re
from tqdm import tqdm
import xml.dom.minidom
import requests
import datetime
import argparse
from tabulate import tabulate


def dividir_em_frases(texto):
    texto = re.sub(r'\s+', ' ', texto).strip()
    frases = re.split(r'(?<=[.!?])\s+', texto)
    return frases


def contem_texto(frase):
    return bool(re.search(r'[a-zA-Z]', frase))


def traduzir_frases(frases, idioma_origem, idioma_destino):
    tradutor = GoogleTranslator(source=idioma_origem, target=idioma_destino)
    traducoes = []
    for frase in frases:
        if contem_texto(frase):
            try:
                traducao = tradutor.translate(frase)
            except Exception as e:
                print(f"Erro ao traduzir a frase: {frase}")
                print(f"Mensagem de erro: {str(e)}")
                traducao = frase
        else:
            traducao = frase
        traducoes.append(traducao)
    texto_traduzido = ' '.join(traducoes)
    return texto_traduzido


def extrair_conteudo_e_traduzir_arquivo_xml(nome_arquivo, idioma_origem, idioma_destino):
    if nome_arquivo.startswith("http://") or nome_arquivo.startswith("https://"):
        response = requests.get(nome_arquivo)
        content = response.text
    else:
        with open(nome_arquivo, 'r', encoding='utf-8') as file:
            content = file.read()

    tree = ET.ElementTree(ET.fromstring(content))
    root = tree.getroot()

    total_segmentos = len(list(root.iter()))
    total_frases = sum(1 for elem in root.iter() if elem.text)

    with tqdm(total=total_frases, desc="Traduzindo", unit="frases") as pbar:
        for elem in root.iter():
            if elem.text:
                frases = dividir_em_frases(elem.text)
                texto_traduzido = traduzir_frases(frases, idioma_origem, idioma_destino)
                elem.text = texto_traduzido
                pbar.update(len(frases))

    pasta_saida = "XMLTranslator"
    os.makedirs(pasta_saida, exist_ok=True)

    idioma_anterior = idioma_origem.upper()
    idioma_atual = idioma_destino.upper()
    data_hora = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
    nome_arquivo_traduzido = f"{pasta_saida}/{idioma_anterior}_{idioma_atual}_{data_hora}.XML"
    tree.write(nome_arquivo_traduzido, encoding='utf-8')

    # Carrega o novo arquivo XML e formata com a mesma indentação do original, removendo linhas em branco
    doc = xml.dom.minidom.parse(nome_arquivo_traduzido)
    with open(nome_arquivo_traduzido, "w", encoding="utf-8") as file:
        file.write('\n'.join(line for line in doc.toprettyxml(indent="\t").split('\n') if line.strip()))

    return nome_arquivo_traduzido


def obter_ajuda():
    print("Uso:")
    print("python tradutor.py -u <url> -l <idioma_destino> -o <idioma_origem>")
    print("python tradutor.py -f <arquivo> -l <idioma_destino> -o <idioma_origem>")
    print("")
    print("Opções:")
    print("-u, --url               Especifica a URL do arquivo XML de entrada")
    print("-f, --arquivo           Especifica o caminho para o arquivo XML de entrada")
    print("-l, --idioma            Especifica o idioma de destino para a tradução")
    print("-o, --idioma_origem     Especifica o idioma de origem do arquivo XML")
    print("-a, --ajuda             Exibe informações de ajuda e lista de idiomas suportados")
    print("")

    idiomas_suportados = GoogleTranslator().get_supported_languages(as_dict=True)
    headers = ["Idioma", "Código"]
    table = [[idioma, descricao] for idioma, descricao in idiomas_suportados.items()]
    print(tabulate(table, headers, tablefmt="grid"))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", help="URL do arquivo XML de entrada")
    parser.add_argument("-f", "--arquivo", help="Caminho para o arquivo XML de entrada")
    parser.add_argument("-l", "--idioma", help="Idioma de destino para a tradução")
    parser.add_argument("-o", "--idioma_origem", help="Idioma de origem do arquivo XML")
    parser.add_argument("-a", "--ajuda", action="store_true", help="Exibe informações de ajuda")
    args = parser.parse_args()

    if args.ajuda:
        obter_ajuda()
        return

    if args.url and args.arquivo:
        print("Erro: Especifique apenas uma opção entre -u/--url e -f/--arquivo.")
        return
    if not args.url and not args.arquivo:
        print("Erro: É necessário especificar a opção -u/--url ou -f/--arquivo.")
        return
    if not args.idioma:
        print("Erro: É necessário especificar a opção -l/--idioma.")
        return
    if not args.idioma_origem:
        print("Erro: É necessário especificar a opção -o/--idioma_origem.")
        return

    idioma_origem = args.idioma_origem.lower()
    idioma_destino = args.idioma.lower()

    if args.url:
        conteudo_traduzido = extrair_conteudo_e_traduzir_arquivo_xml(args.url, idioma_origem, idioma_destino)
    else:
        conteudo_traduzido = extrair_conteudo_e_traduzir_arquivo_xml(args.arquivo, idioma_origem, idioma_destino)

    print(f"O arquivo traduzido foi salvo como {conteudo_traduzido}")


if __name__ == '__main__':
    main()
