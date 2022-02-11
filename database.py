import sqlite3 as sql

def crearFila(nombre1,nombre2,puntos1,puntos2):
    conn = sql.connect('historial.db')
    cursor = conn.cursor()
    idFila = generarID() 
    escritura = f"INSERT INTO historiaNombres (ID,Jugador1,Jugador2,Puntos1,Puntos2) VALUES ({idFila},'{nombre1}','{nombre2}',{puntos1},{puntos2})"
    cursor.execute(escritura)
    conn.commit()
    conn.close()

def vaciarTabla():
    conn = sql.connect('historial.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM historiaNombres')
    conn.commit()
    conn.close()

def generarID():
    conn = sql.connect('historial.db')
    cursor = conn.cursor()
    filas = cursor.execute('SELECT * FROM historiaNombres').fetchall()
    conn.commit()
    conn.close()
    print(filas)
    if len(filas) == 0:
        return 1
    else:
        return 0
    

def get(elemento):
    pass

