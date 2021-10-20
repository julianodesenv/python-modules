import pymysql.cursors
from contextlib import contextmanager


# CRUD - CREATE, READ, UPDATE, DELETE


@contextmanager
def connect():
    connection = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='secret',
        db='db_python',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        yield connection
    finally:
        connection.close()


# INSERE UM REGISTRO NA BASE DE DADOS
#with connect() as connection:
#    with connection.cursor() as cursor:
#        sql = 'INSERT INTO clients (name, last_name, age, weight) VALUES ' \
#              '(%s, %s, %s, %s)'
#        cursor.execute(sql, ('Jack', 'Monroe', 112, 220))
#        connection.commit()

# INSERE VÁRIOS REGISTROS NA BASE DE DADOS
# with connect() as connection:
#     with connection.cursor() as cursor:
#         sql = 'INSERT INTO clients (name, last_name, age, weight) VALUES ' \
#               '(%s, %s, %s, %s)'
#
#         dados = [
#             ('MURIEL', 'FIGUEIREDO', 19, 55),
#             ('ROSE', 'FIGUEIREDO', 19, 55),
#             ('JOSE', 'FIGUEIREDO', 19, 55),
#         ]
#
#         cursor.executemany(sql, dados)
#         connection.commit()

# DELETA UM REGISTRO DA BASE DE DADOS
# with connect() as connection:
#     with connection.cursor() as cursor:
#         sql = 'DELETE FROM clients WHERE id = %s'
#         cursor.execute(sql, (6,))
#         connection.commit()

# DELETA QUANTage DETERMINADA DE REGISTROS
# with connect() as connection:
#     with connection.cursor() as cursor:
#         sql = 'DELETE FROM clients WHERE id IN (%s, %s, %s)'
#         cursor.execute(sql, (7, 8, 9))
#         connection.commit()

# DELETA REGISTRA ENTRE UM RANGE
# with connect() as connection:
#     with connection.cursor() as cursor:
#         sql = 'DELETE FROM clients WHERE id BETWEEN %s AND %s'
#         cursor.execute(sql, (10, 12))
#         connection.commit()

# ATUALIZA UM REGISTRO NA BASE DE DADOS
# with connect() as connection:
#     with connection.cursor() as cursor:
#         sql = 'UPDATE clients SET name=%s WHERE id=%s'
#         cursor.execute(sql, ('JOANA', 5))
#         connection.commit()


# ESTE SELECIONA OS DADOS DA BASE DE DADOS
with connect() as connection:
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM clients ORDER BY id ASC LIMIT 100')
        results = cursor.fetchall()

        for line in results:
            print(line)
