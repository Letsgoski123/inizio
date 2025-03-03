import mysql.connector

conn = mysql.connector.connect(
    host="192.168.3.92", #sostituisci l'indirizzo IP del server con il DB dentro
    user="UtenteDBSviluppoWeb2025",
    password="UtenteDBSviluppoWeb2025",
    database="UtenteDBSviluppoWeb2025",
    port=3306, #porta default di mySQL
    )

# a tutti passerei un dizionario così che dentro abbia le informazioni per presonalizzare le query 
def db_get(diz):
    cur = conn.cursor()

    # si chiama una funzione di libreria passando i parametri di ricerca dell'utente. esempio controlla_caratteri(nome)
    query = "SELECT * FROM User"
    cur.execute(query)
    dati = cur.fetchall()
    print(dati)
    return dati

def db_set(diz): 
    # query di insert
    pass

def db_update(diz):
    # query update
    pass

def db_delete(diz):
    # query delete
    pass


if __name__ == '__main_v4__':
    db_get()