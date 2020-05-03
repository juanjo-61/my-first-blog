import sqlite3



def consultar():
    db2 = sqlite3.connect("db.sqlite3")
    print("Estas en la función Consultar")
    db2.row_factory = sqlite3.Row
    consulta = db2.cursor()
    consulta.execute('select * from BASE_DIR')
    filas = consulta.fetchall()
    lista = []
    for fila in filas:
        s = {}
        s['author'] = fila['autor']
        s['title'] = fila['titulo']
        s['text'] = fila['text']
        lista.append(s)
    consulta.close()
    db2.close()
    return (lista)

consultar()
