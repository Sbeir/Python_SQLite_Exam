global db_autor, db_user, db_prest, db_libro, db_categoria


#funzioni per creare i vari dizionari
def autor():
     db_autor = {
    "nome": [],
    "cognome": [],
    "anno": [],
    "note": [],
    "id": []
    }
     return db_autor
def user():
    db_user = {
    "nome": [],
    "cognome": [],
    "anno_reg": [],
    "telefono": [],
    "tessera": [],
    "nprest": []
    }
    return db_user
def libro():
    db_libro = {
    "isbn": [],
    "titolo": [],
    "lingua": [],
    "anno": [],
    "editore": [],
    "pagine": [],
    "categoria": [],
    "copie": [],
    "autore": []
    }
    return db_libro
def categoria():
    db_categoria = {
    "id": [],
    "nome": []
    }
    return db_categoria

def prest():
    db_prest = {
    "isbn": [],
    "id": [],
    "tessera": [],
    "data_inizio": [],
    "data_fine": [],
    "stato": [],
    "data_consegna": []
    }
    return db_prest



#if __name__ == '__main__':
