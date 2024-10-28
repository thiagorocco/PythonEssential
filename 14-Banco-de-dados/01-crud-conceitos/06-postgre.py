import psycopg2

# Configurações de conexão
host = "localhost"
database = "banco_novo"
user = "postgres"
password = "tr*890711"

# Conecta ao banco de dados
try:
    connection = psycopg2.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )

    # Cria um cursor
    cursor = connection.cursor()

    # Exemplo de consulta SELECT
    cursor.execute("SELECT * FROM usuarios")
    rows = cursor.fetchall()

    # Exibindo resultados
    for row in rows:
        print(row)

except (Exception, psycopg2.Error) as error:
    print("Erro ao se conectar ao PostgreSQL:", error)

finally:
    # Fecha a conexão
    if connection:
        cursor.close()
        connection.close()
        print("Conexão encerrada.")
