# JSON Parser - Teses e Dissertações

Este repositório contém um script Python para parsear o conteúdo de arquivos não formatados de teses e dissertações, estruturando-os em um formato JSON legível e organizado. O script identifica padrões específicos no texto para extrair informações como área de interesse, autor, título, programa de pós-graduação, instituição de ensino superior (IES), orientador, coorientador e linha de pesquisa.

## Funcionalidades

- Leitura de arquivos não formatados (`.json`) contendo dados de teses e dissertações.
- Extração e estruturação de informações como área, autor, título, programa, IES, orientador, coorientador e pesquisa.
- Geração de um arquivo JSON unificado com todos os dados estruturados.

## Como Utilizar

1. Coloque seus arquivos não formatados na pasta `unformatted-files`.
2. Execute o script principal: `python3 main.py`
3. O resultado será gerado no arquivo `result.json` na raiz do projeto.

## Estrutura do Projeto

- `unformatted-files/`: Pasta para colocar os arquivos não formatados.
- `main.py`: Script Python principal.
- `result.json`: Arquivo de saída com os dados estruturados.

## Requisitos

- Python 3.x

## Exemplo de Uso

1. Adicione um arquivo `MH2021.json` na pasta `unformatted-files`.

**Obs.:** O conteúdo do arquivo deve estar neste padrão:

```
Área: lorem ipsum
Autor: lorem ipsum
Tese: lorem ipsum
Orientadora: lorem ipsum
Programa: lorem ipsum
Pesquisa: lorem ipsum

Área: lorem ipsum
Autor: lorem ipsum
Tese: lorem ipsum
Orientadora: lorem ipsum
Programa: lorem ipsum
Pesquisa: lorem ipsum
```

3. Execute o script.
4. Verifique o arquivo `result.json` para ver os dados estruturados.

## Licença

[MIT](https://choosealicense.com/licenses/mit/)
