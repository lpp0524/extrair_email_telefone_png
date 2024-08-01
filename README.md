# Projeto de Extração e Armazenamento de Contatos

Este projeto utiliza a biblioteca `pytesseract` para extrair dados de uma imagem e armazena esses dados em um banco de dados MySQL. Especificamente, ele extrai emails e números de telefone de uma imagem e os insere em uma tabela do banco de dados.

## Requisitos

- Python 3.x
- Tesseract-OCR
- Bibliotecas Python:
  - pytesseract
  - mysql-connector-python

## Instalação

1. **Tesseract-OCR**: Instale o Tesseract-OCR no seu sistema e adicione o caminho do executável na variável `tesseract_path` no script Python.

   - [Instruções de instalação do Tesseract-OCR](https://github.com/tesseract-ocr/tesseract)

2. **Bibliotecas Python**: Instale as bibliotecas necessárias utilizando o pip.

   ```sh
   pip install pytesseract mysql-connector-python
