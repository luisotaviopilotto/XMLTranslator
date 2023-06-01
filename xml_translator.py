import os
import xml.etree.ElementTree as ET
from deep_translator import GoogleTranslator
import re
from tqdm import tqdm
import xml.dom.minidom
import requests
import datetime

from helpers import dividir_em_frases, traduzir_frases


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
