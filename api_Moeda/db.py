
import mysql.connector
from mysql.connector import Error
from senhas import PASSWORD_DB, USER_DB

def get_currency_from_db(nome: str):
    try:
        conn = mysql.connector.connect(
            host="mysql",
            user=USER_DB,
            password=PASSWORD_DB,
            database="cotacoes"
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
