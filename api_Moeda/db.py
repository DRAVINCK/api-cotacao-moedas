import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error

# Carrega as variáveis do .env
load_dotenv()

def get_currency_from_db(nome: str):
    try:
        conn = mysql.connector.connect(
            host= "localhost",
            user="root",
            password="root",
            database="cotacaoes"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT valor FROM moedas WHERE nome = %s", (nome,))
        result = cursor.fetchone()
        return result[0] if result else None
    except Error as e:
        print(f"Erro ao acessar o banco de dados: {e}")
        return None
    finally:
        if conn:
            cursor.close()
            conn.close()
