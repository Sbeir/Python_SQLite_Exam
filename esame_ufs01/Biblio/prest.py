import datetime as d
import query_prestito as qp
from dateutil.relativedelta import relativedelta


def add_prestito(db_libro, db_prest, db_user): #funzio pre prendere in prestito un libro
    while True:
        try:
            tessera = int(input("inserisci id della tessera "))
            break
        except ValueError:
            print("Oops!  tessera non valida, riprova ")    
    oggi = d.datetime.now()
    oggi = oggi.strftime("%x")
    data_consegna = "00/00/00"
    go = False
    for b in range(len(db_user["tessera"])):
        if int(db_user["tessera"][b]) == tessera:
            go = True
    if go == False:
        print('la tessera non esiste')
    if go == True:
        for a in range(len(db_user["tessera"])):
            if (int(db_user["tessera"][a]) == tessera):
                if (int(db_user["nprest"][a]) >= 5):
                    print('hai raggiunto il limite di prestiti disponibili!')
                    go = None
    if go == True:
        for x in range(len(db_prest["tessera"])):
            if (int(db_prest["tessera"][x]) == tessera):
                if (db_prest["data_fine"][x] <= oggi):
                    print('Non puoi prendere in prestito un libro se devi restituirne uno!')
                    go = None
    if go == True:
        while True:
            try:
                isbn = int(input("inserisci l'isbn del libro che vuoi prendere in prestito "))
                break
            except ValueError:
                print("Oops!  isbn non valido, riprova ")        
        for x in range(len(db_prest["isbn"])):
            if (int(db_prest["tessera"][x]) == tessera) and (int(db_prest["stato"][x]) == 1):
                if (int(db_prest["isbn"][x]) == isbn):
                    print('Non puoi prendere in prestito un libro che hai già preso in prestito! ')
                    go = None
    if go == True:
        for x in range(len(db_libro["isbn"])):
            if (int(db_libro["isbn"][x]) == isbn):
                go = True  
                break
            else: go = False
    if go == False:
        print('il libro non esiste')              
    nprest = 0
    if go == True:
        for a in range(len(db_user["tessera"])):
            if (int(db_user["tessera"][a]) == tessera):
                    nprest = int(db_user["nprest"][a])+1
                    db_user["nprest"][x] = nprest
    if go == True:
        data_iniz = d.datetime.now()
        data_iniz = data_iniz.strftime("%x")
        data_fine = d.datetime.now() + relativedelta(months=+1)
        data_fine = data_fine.strftime("%x")
        idp, copie, stato = 0,0,1
        for x in range(len(db_libro["isbn"])):
            if (int(db_libro["isbn"][x]) == isbn) and (int(db_libro["copie"][x]) > 0):
                db_prest["data_inizio"].append(data_iniz)
                db_prest["data_fine"].append(data_fine)                
                db_prest["isbn"].append(isbn)
                db_prest["tessera"].append(tessera)
                db_prest["stato"].append(stato)
                db_prest["data_consegna"].append(data_consegna)
                idp = len(db_prest["id"]) + 1
                db_prest["id"].append(idp)
                copie = int(db_libro["copie"][x]) - 1
                db_libro["copie"][x] = copie
            elif ((db_libro["isbn"][x] == isbn) and (db_libro["copie"][x] <= 0)):
                print("libro attualmente non disponibile ")
                go = False 
    if go == True:
        qp.add_prestito(isbn, idp, tessera, data_iniz, data_fine, copie, nprest, stato, data_consegna)
        go = None
    return db_prest, db_libro, db_user

def restituisci_prestito(db_libro, db_prest, db_user):#funzione per restituire il prestito
        while True:
            try:
                idp = int(input("inserisci id del prestito"))
                break
            except ValueError:
                print("Oops!  id non valido, riprova ")
        check = False
        isbn, copie, tessera, stato= 0,0,0,0
        for x in range(len(db_prest["id"])):
            if int(db_prest["id"][x]) == idp:
                isbn = db_prest["isbn"][x]
                db_prest["stato"][x] = 0  
                tessera = int(db_prest["tessera"][x])
                check = True
        if check == True:
                for x in range(len(db_libro["isbn"])):
                    if int(db_libro["isbn"][x]) == isbn:
                        copie = int(db_libro["copie"][x]) + 1
                        db_libro["copie"][x] = copie
                        check = True    
        if check == True:
                for x in range(len(db_user["nprest"])):
                    if int(db_user["tessera"][x]) == tessera:
                        nprest = int(db_user["nprest"][x]) - 1
                        db_user["nprest"][x] = nprest
                        check = True  
        if check == True:
            data_consegna = d.datetime.now()
            data_consegna = data_consegna.strftime("%x")            
        if check == True:
            qp.return_prestito(idp, copie, nprest, stato, tessera, isbn, data_consegna)
        return db_libro, db_prest, db_user
    
 



#if __name__ == '__main__':
 #   add_prestito(db_libro, db_prest, db_user)