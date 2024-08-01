from pytesseract import pytesseract
import re
import mysql.connector
from mysql.connector import Error

# Configuração do Tesseract
tesseract_path = r"/caminho/para/tesseract.exe"
pytesseract.tesseract_cmd = tesseract_path

try:
    # Conexão com o banco de dados
    con = mysql.connector.connect(
        host="seu_host",
        user="seu_usuario",
        password="sua_senha",
        database="nome_do_banco_de_dados"
    )
    if con.is_connected():
        print("Conexão com o banco de dados realizada com sucesso.")

    cursor = con.cursor()

    # Extração de dados da imagem
    dados = pytesseract.image_to_string("caminho/para/dados.png")

    # Regex para encontrar email
    match = re.findall(r'[\w\.-]+@[\w\.-]+', dados)
    email = str(match[0])

    # Regex para encontrar telefone
    padrao = r"\(\d+\)[ ]?\d+[-. ]?\d+"
    resultado = re.findall(padrao, dados)
    telefone = str(resultado[0])

    # Inserção dos dados no banco de dados
    cursor.execute(f"""INSERT INTO tbl_contatos (tbl_telefone, tbl_email) VALUES ('{telefone}','{email}')""")
    con.commit()
    print("Dados cadastrados com sucesso.")

except Error as e:
    print(f"Erro ao conectar ou inserir dados no banco de dados: {e}")

finally:
    if con.is_connected():
        cursor.close()
        con.close()
        print("Conexão com o banco de dados encerrada.")
