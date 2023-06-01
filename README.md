# XML Translator
O XML Translator é um programa Python que permite traduzir o conteúdo de arquivos XML usando o serviço Deep Translator da Google. O programa suporta a tradução de arquivos XML a partir de uma URL ou de um arquivo local, fornecendo o idioma de origem e o idioma de destino para a tradução.

## Pré-requisitos
- Python 3.x
- Bibliotecas Python: `deep_translator`, `xml.etree.ElementTree`, `re`, `tqdm`, `xml.dom.minidom`, `requests`, `argparse`, `tabulate`

## Instalação
1. Clone este repositório em seu ambiente local:
git clone https://github.com/seu-usuario/xml-translator.git

2. Navegue até o diretório do projeto:
cd xml-translator

3. Instale as dependências usando o gerenciador de pacotes `pip`:
pip install -r requirements.txt

4. Crie um ambiente virtual Linux/Mac
pip -m venv .
source bin/active

## Uso
python XMLTranslator.py -u <url> -l <idioma_destino> -o <idioma_origem>
python XMLTranslator.py -f <arquivo> -l <idioma_destino> -o <idioma_origem>

Opções:
- `-u, --url`: Especifica a URL do arquivo XML de entrada
- `-f, --arquivo`: Especifica o caminho para o arquivo XML de entrada
- `-l, --idioma`: Especifica o idioma de destino para a tradução
- `-o, --idioma_origem`: Especifica o idioma de origem do arquivo XML
- `-a, --ajuda`: Exibe informações de ajuda e lista de idiomas suportados

## Exemplos
Traduzir um arquivo XML a partir de uma URL:
python XMLTranslator.py -u https://exemplo.com/arquivo.xml -l fr -o en

Traduzir um arquivo XML a partir de um arquivo local:
python XMLTranslator.py -f caminho/do/arquivo.xml -l es -o pt

## Lista de Idiomas Suportados
Para verificar a lista de idiomas suportados pelo serviço Deep Translator da Google, execute o seguinte comando:
python XMLTranslator.py -a

## Contribuição
Contribuições são bem-vindas! Se você encontrar algum problema, tiver alguma sugestão ou quiser adicionar um novo recurso, fique à vontade para abrir uma issue ou enviar um pull request.

## Licença
Este projeto é licenciado sob a [MIT License](LICENSE).
