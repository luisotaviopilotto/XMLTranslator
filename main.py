# -*- coding: utf-8 -*-
import argparse
from xml_translator import extrair_conteudo_e_traduzir_arquivo_xml
from helpers import obter_ajuda

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
