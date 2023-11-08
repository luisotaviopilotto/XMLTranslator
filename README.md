## Obs.
`É possível utilzar apenas um arquivo, sem a necessidade da criação do ambiente virtual.`
`Basta usar o arquivo XMLTranslator.py após seguir os procedimentos de instalação 1, 2 e 3.`

# XML Translator
O XML Translator é um programa Python que permite traduzir o conteúdo de arquivos XML usando o serviço Deep Translator da Google. O programa suporta a tradução de arquivos XML a partir de uma URL ou de um arquivo local, fornecendo o idioma de origem e o idioma de destino para a tradução.

## Pré-requisitos
- Python 3.x
- Bibliotecas Python: `deep_translator`, `xml.etree.ElementTree`, `re`, `tqdm`, `xml.dom.minidom`, `requests`, `argparse`, `tabulate`

# Instalação
## Clone este repositório em seu ambiente local
```
git clone https://github.com/luisotaviopilotto/XMLTranslator.git
```

## Navegue até o diretório do projeto:
```
cd XMLTranslator
```

## Crie um ambiente virtual:
```
python -m venv .venv
```
## Ative o ambiente:
### Windows
```
.venv\Scripts\activate
```
### Linux/MacOS
```
 source .venv/bin/activate
```

Isso criará um ambiente virtual na pasta .venv e ativará-o.

## Atualize o pip para a versão mais recente:

```
python -m pip install --upgrade pip
```

## Instale as dependências usando o gerenciador de pacotes `pip`:
```
pip install -r requirements.txt
```

## Lista de Idiomas Suportados
Para verificar a lista de idiomas suportados pelo serviço Deep Translator da Google, execute o seguinte comando:
```
python main.py -a
```
| Idioma                | Código   | Idioma                | Código   | Idioma                | Código   |
|-----------------------|----------|-----------------------|----------|-----------------------|----------|
| afrikaans             | af       | albanian              | sq       | amharic               | am       |
| arabic                | ar       | armenian              | hy       | assamese              | as       |
| aymara                | ay       | azerbaijani           | az       | bambara               | bm       |
| basque                | eu       | belarusian            | be       | bengali               | bn       |
| bhojpuri              | bho      | bosnian               | bs       | bulgarian             | bg       |
| catalan               | ca       | cebuano               | ceb      | chichewa              | ny       |
| chinese (simplified)  | zh-CN    | chinese (traditional) | zh-TW    | corsican              | co       |
| croatian              | hr       | czech                 | cs       | danish                | da       |
| dhivehi               | dv       | dogri                 | doi      | dutch                 | nl       |
| english               | en       | esperanto             | eo       | estonian              | et       |
| ewe                   | ee       | filipino              | tl       | finnish               | fi       |
| french                | fr       | frisian               | fy       | galician              | gl       |
| georgian              | ka       | german                | de       | greek                 | el       |
| guarani               | gn       | gujarati              | gu       | haitian creole        | ht       |
| hausa                 | ha       | hawaiian              | haw      | hebrew                | iw       |
| hindi                 | hi       | hmong                 | hmn      | hungarian             | hu       |
| icelandic             | is       | igbo                  | ig       | ilocano               | ilo      |
| indonesian            | id       | irish                 | ga       | italian               | it       |
| japanese              | ja       | javanese              | jw       | kannada               | kn       |
| kazakh                | kk       | khmer                 | km       | kinyarwanda           | rw       |
| konkani               | gom      | korean                | ko       | krio                  | kri      |
| kurdish (kurmanji)    | ku       | kurdish (sorani)      | ckb      | kyrgyz                | ky       |
| lao                   | lo       | latin                 | la       | latvian               | lv       |
| lingala               | ln       | lithuanian            | lt       | luganda               | lg       |
| luxembourgish         | lb       | macedonian            | mk       | maithili              | mai      |
| malagasy              | mg       | malay                 | ms       | malayalam             | ml       |
| maltese               | mt       | manipuri              | mni      | maori                 | mi       |
| marathi               | mr       | mongolian             | mn       | nepali                | ne       |
| norwegian             | no       | occitan               | oc       | oriya                 | or       |
| pashto                | ps       | persian               | fa       | polish                | pl       |
| portuguese            | pt       | punjabi               | pa       | quechua               | qu       |
| romanian              | ro       | russian               | ru       | samoan                | sm       |
| sanskrit              | sa       | scots gaelic          | gd       | serbian               | sr       |
| sesotho               | st       | shona                 | sn       | sindhi                | sd       |
| sinhala               | si       | slovak                | sk       | slovenian             | sl       |
| somali                | so       | spanish               | es       | sundanese             | su       |
| swahili               | sw       | swedish               | sv       | tajik                 | tg       |
| tamil                 | ta       | telugu                | te       | thai                  | th       |
| tigrinya              | ti       | tongan                | to       | turkish               | tr       |
| turkmen               | tk       | ukrainian             | uk       | urdu                  | ur       |
| uzbek                 | uz       | vietnamese            | vi       | welsh                 | cy       |
| xhosa                 | xh       | yiddish               | yi       | yoruba                | yo       |
| zulu                  | zu       |


## Uso
```
python main.py -u <url> -l <idioma_destino> -o <idioma_origem>
```
```
python main.py -f <arquivo> -l <idioma_destino> -o <idioma_origem>
```

Opções:
- `-u, --url`: Especifica a URL do arquivo XML de entrada
- `-f, --arquivo`: Especifica o caminho para o arquivo XML de entrada
- `-l, --idioma`: Especifica o idioma de destino para a tradução
- `-o, --idioma_origem`: Especifica o idioma de origem do arquivo XML
- `-a, --ajuda`: Exibe informações de ajuda e lista de idiomas suportados

## Exemplos
Traduzir um arquivo XML a partir de uma URL:
```
python main.py -u https://exemplo.com/arquivo.xml -l pt -o en
```

Traduzir um arquivo XML a partir de um arquivo local:
```
python main.py -f caminho/do/arquivo.xml -l pt -o en
```

## Contribuição
Contribuições são bem-vindas! Se você encontrar algum problema, tiver alguma sugestão ou quiser adicionar um novo recurso, fique à vontade para abrir uma issue ou enviar um pull request.

## Licença
Este projeto é licenciado sob a [MIT License](LICENSE).
