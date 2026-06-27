import psycopg2


def get_connection():

    return psycopg2.connect(
        host="localhost",
        database="ai_os",
        user="postgres",
        password="postgres"
    )