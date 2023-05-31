# XML Translator

O XML Translator é uma ferramenta simples e prática para tradução de parâmetros em arquivos XML. Com este projeto, você pode facilmente traduzir o conteúdo de um arquivo XML para diferentes idiomas, utilizando a API do Google Translate.

## Recursos

- Tradução automática de parâmetros em arquivos XML para o idioma desejado.
- Suporte a uma ampla variedade de idiomas disponíveis no Google Translate.
- Divisão automática de textos longos para contornar limitações de tamanho de tradução.
- Exibição de tabela com os idiomas suportados.
- Criação de arquivos de tradução em formato XML, mantendo a estrutura original do arquivo.
- Organização dos arquivos de tradução em uma pasta dedicada.

## Como usar

1. Clone este repositório para o seu ambiente local.
2. Certifique-se de ter o Python instalado em sua máquina.
3. Instale as dependências necessárias executando o comando `pip install -r requirements.txt`.
4. Execute o script `xml_translate.py` e forneça os argumentos necessários:
   - `-f` ou `--arquivo`: Caminho e nome do arquivo XML de entrada.
   - `-l` ou `--idioma`: Idioma para tradução.
   - `-t` ou `--tabela`: Exibir tabela de idiomas suportados.
5. O arquivo traduzido será salvo na pasta `Translate`, com o nome do idioma em formato de código.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas (issues) e enviar pull requests para aprimorar este projeto. Se você encontrar algum problema ou tiver alguma sugestão, não hesite em compartilhá-los.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
