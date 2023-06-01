import re
from deep_translator import GoogleTranslator
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


def obter_ajuda():
    print("Uso:")
    print("python main.py -u <url> -l <idioma_destino> -o <idioma_origem>")
    print("python main.py -f <arquivo> -l <idioma_destino> -o <idioma_origem>")
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
