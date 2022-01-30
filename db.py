import sqlite3
import datetime

def writeDB(name,price):
    dataRegistro = datetime.datetime.now()


    conn = sqlite3.connect('ludo2.db')

    cursor = conn.cursor()

    try:
        cursor.execute(""" CREATE TABLE bg
                    (    id      INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                    bgname  STRING  NOT NULL,
                    ranking INT
                    """)
        print("Criando Tabela!")
    except:
        print("Tabela ja existe!")

    # Example
    #reg  = ['Azul', '33,50', dataRegistro]
    #conn.execute("INSERT INTO ludo (name,price,date) VALUES (?,?,?)",  (reg[0],reg[1],reg[2])
    
    reg  = [name, price, dataRegistro]
    conn.execute("INSERT INTO bg (bgname,ranking) VALUES (?,?)",  (reg[0],"ND"))
    conn.commit()


def writeDBprice(price,bgid):
    dataRegistro = datetime.datetime.now()


    conn = sqlite3.connect('ludo2.db')

    cursor = conn.cursor()

    try:
        cursor.execute(""" CREATE TABLE bg
                    (    id      INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                    bgname  STRING  NOT NULL,
                    ranking INT
                    """)
        print("Criando Tabela!")
    except:
        print("Tabela ja existe!")

    # Example
    #reg  = ['Azul', '33,50', dataRegistro]
    #conn.execute("INSERT INTO ludo (name,price,date) VALUES (?,?,?)",  (reg[0],reg[1],reg[2])
    
    reg  = [price, dataRegistro, bgid]
    conn.execute("INSERT INTO historic (price,date,id_bg) VALUES (?,?,?)",  (reg[0],reg[1],reg[2]))
    conn.commit()

"""
INSERT INTO historic (
                         id,
                         price,
                         date,
                         id_bg
                     )
                     VALUES (
                         'id',
                         'price',
                         'date',
                         'id_bg'
                     );

"""

def queryDB(name,price):

    conn = sqlite3.connect('ludo2.db')

    cursor = conn.cursor()


    sql = """
            SELECT * FROM bg
            WHERE bgname LIKE 'Zombicide: Friends and Foes' """

    cursor.execute(sql)
    print(cursor.fetchall())

def queryDBall():

    conn = sqlite3.connect('ludo2.db')

    cursor = conn.cursor()


    sql = """
            SELECT bg.bgname, historic.price,historic.date
            FROM bg
            INNER JOIN historic ON bg.id=historic.id_bg;
            
            """

    cursor.execute(sql)
    result = cursor.fetchall()
    return result

def queryDBid(name):

    conn = sqlite3.connect('ludo2.db')

    cursor = conn.cursor()


    sql = '''
            SELECT * FROM bg
            WHERE bgname LIKE "{}" '''.format(name)

    cursor.execute(sql)
    id = cursor.fetchall()
    return id


"""
SELECT id
  FROM bg
  WHERE bgname = "New York 1901";

"""