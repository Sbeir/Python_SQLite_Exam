# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 12:44:29 2021

@author: RobertoFormenti
"""

import datetime as d
import Biblio.my_query as mq
import query_prestito as qp


def add_utente(db_user):#funzione aggiunta utente
    while True:
        try:
            nome = str(input("inserisci: nome "))
            nome = nome.lower()
            break
        except ValueError:
            print("Oops!  nome non valido, riprova ")
    while True:
        try:
            cognome = str(input("cognome "))
            cognome = cognome.lower()
            break
        except ValueError:
            print("Oops! cognome non valido, riprova ")            
    anno_reg = d.datetime.now()
    anno_reg = anno_reg.strftime("%x")
    while True:
        try:
            telefono = int(input("telefono "))
            break
        except ValueError:
            print("Oops! numero non valido, riprova ") 
    nprest = int(0)
    tf = False
    for x in range(len(db_user["nome"])):
        if db_user["telefono"][x] == telefono:
            print(" hai già inserito questo utente")
            tf = True
            break
    if tf == False:
        idl = db_user['tessera']
        idl = [int(i) for i in idl]
        tessera = max(idl)+1
        db_user["nome"].append(nome)
        db_user["cognome"].append(cognome)
        db_user["anno_reg"].append(anno_reg)
        db_user["telefono"].append(telefono)
        db_user["tessera"].append(tessera)
        db_user["nprest"].append(nprest)
        mq.query_add_utente(nome, cognome, anno_reg, telefono, tessera, nprest)
    return db_user




def add_autore(db_autor):#funzione aggiunta autore
    while True:
        try:
            nome = str(input("inserisci: nome "))
            nome = nome.lower()
            break
        except ValueError:
            print("Oops!  nome non valido, riprova ")
    while True:
        try:
            cognome = str(input("cognome "))
            cognome = cognome.lower()
            break
        except ValueError:
            print("Oops! cognome non valido, riprova ")
    while True:
        try:
            anno = int(input("anno di nascita "))
            break
        except ValueError:
            print("Oops! anno non valido, riprova ")
    while True:
        try:
            note = str(input("inserisci una nota "))
            note = note.lower()
            break
        except ValueError:
            print("Oops! testo non valido, riprova ")
    tf = False
    for x in range(len(db_autor["nome"])):
        if (db_autor["nome"][x] == nome) and (db_autor["cognome"][x] == cognome) and (db_autor["anno"][x] == anno):
            print(" hai già inserito questo autore")
            tf = True
            break
    if tf == False:
        ida = db_autor['id']
        ida = [int(i) for i in ida]
        id_autore = max(ida)+1
        db_autor["nome"].append(nome)
        db_autor["cognome"].append(cognome)
        db_autor["anno"].append(anno)
        db_autor["id"].append(id_autore)
        db_autor["note"].append(note)
        mq.query_add_autore(nome, cognome, anno, note, id_autore)      
    return db_autor

#funzione aggiunta libro
def add_libro(db_categoria, db_libro, db_autor):
    while True:
        try:
            isbn = int(input("inserisci: isbn "))
            break
        except ValueError:
            print("Oops!  isbn non valido, riprova ")
    while True:
        try:
            anno = int(input("anno "))
            break
        except ValueError:
            print("Oops! anno non valido, riprova ")
    while True:
        try:
            lingua = str(input("lingua "))
            lingua = lingua.lower()
            break
        except ValueError:
            print("Oops! lingua non valida, riprova ")
    while True:
        try:
            titolo = str(input("titolo "))
            titolo = titolo.lower()
            break
        except ValueError:
            print("Oops! titolo non valido, riprova ")
    while True:
        try:
            editore = str(input("editore "))
            editore = editore.lower()
            break
        except ValueError:
            print("Oops! editore non valido, riprova ")
    while True:
        try:
            pagine = int(input("pagine "))
            break
        except ValueError:
            print("Oops! pagine non valide, riprova ")    
    categoria = str(input("categoria "))
    categoria = categoria.lower()
    autore = 0
    for x in range(len(db_categoria["nome"])):
        if categoria == db_categoria["nome"][x]:
            categoria = db_categoria["id"][x]
    te = 0
    while te <= 0:
        copie = int(input("copie "))
        te = copie
        if copie <= 0:
            print('non puoi inserire meno di una copia')
    nautore = str(input("nome autore "))
    cautore = str(input("cognome autore "))
    check = True
    for isbn1 in range(len(db_libro["isbn"])):
        if db_libro["isbn"][isbn1] == isbn:
            print('hai già inserito il libro')
            check = False
    if check == True:
        db_libro["isbn"].append(isbn)
        db_libro["anno"].append(anno)
        db_libro["lingua"].append(lingua)
        db_libro["titolo"].append(titolo)
        db_libro["editore"].append(editore)
        db_libro["pagine"].append(pagine)
        db_libro["categoria"].append(categoria)
        db_libro["copie"].append(copie)
        tf = False
        for x in range(len(db_autor["nome"])):
            if (db_autor["nome"][x] == nautore) and (db_autor["cognome"][x] == cautore):
                tf = True
                autore = db_autor["id"][x]
                db_libro["autore"].append(autore)
        if tf == False:
            print("non hai ancora inserito questo autore, inseriscilo")
            autore = len(db_autor["id"])+1
            add_autore(db_autor)
        if check == True:
            mq.query_add_libro(isbn, titolo, lingua, anno, editore, pagine, categoria, copie, autore)
    return db_categoria, db_libro, db_autor

#funzione eliminazione libro
def del_libro(db_libro):
    while True:
        try:
            isbn = int(input("inserisci l'isbn del libro che vuoi eliminare "))
            break
        except ValueError:
            print("Oops!  isbn non valido, riprova ")
    tf = False
    for x in range(len(db_libro["isbn"])):
        print(db_libro["isbn"][x])
        if int(db_libro["isbn"][x]) == isbn:
            tf = True
    if tf == True:
        del db_libro["isbn"][x]
        del db_libro["autore"][x]
        del db_libro["anno"][x]
        del db_libro["categoria"][x]
        del db_libro["titolo"][x]
        del db_libro["editore"][x]
        del db_libro["lingua"][x]
        del db_libro["pagine"][x] 
        del db_libro["copie"][x]
    if tf == True:
        mq.query_del_libro(isbn)
    if tf == False:
        print("non esiste nessun libro con questo isbn ")
    return db_libro
    
def modifica_libro(db_libro):
    while True:
        try:
            isbn = input("inserisci l'isbn del libro dove vuoi modificare le copie disponibili ")
            break
        except ValueError:
            print("Oops!  isbn non valido, riprova ")
    check = False
    for isbn1 in range(len(db_libro["isbn"])):
        if db_libro["isbn"][isbn1] == isbn:
            check = True
            te = 0
            while te <= 0:
                copie = int(input("inserisci il nuovo numero di copie disponibili "))
                te = copie
                if copie <= 0:
                    print('non puoi inserire meno di una copia')
            db_libro["copie"][isbn1] = copie
            mq.query_modifica_libro(copie, isbn)
    if check == False:
        print("non esiste nessun libro con questo isbn")
    return db_libro

#funzione eliminazione utente
def del_utente(db_user, db_prest):
    while True:
        try:
            tessera = int(input("inserisci id della tessera "))
            break
        except ValueError:
            print("Oops!  tessera non valida, riprova ")  
    check = True
    for x in range(len(db_user["nome"])):
        if int(db_user["tessera"][x]) == tessera:
            if int(db_user["nprest"][x]) > 1:
                check = False
    if check == True:
        qp.del_prestiti(tessera)
        mq.query_del_utente(tessera)
    if check == True: 
        for a in range(len(db_user["nome"])):
            if int(db_user["tessera"][a]) == tessera:
                del db_user["nome"][a]
                del db_user["cognome"][a]
                del db_user["anno_reg"][a]
                del db_user["telefono"][a]
                del db_user["tessera"][a]
                del db_user["nprest"][a]
                break
    if check == True:
        for b in range(len(db_prest["tessera"])):
            if int(db_prest["tessera"][b]) == tessera:
                del db_prest["tessera"][b]
                del db_prest["stato"][b]
                del db_prest["isbn"][b]
                del db_prest["id"][b]
                del db_prest["data_inizio"][b]
                del db_prest["data_fine"][b]
                del db_prest["data_consegna"][b] 
                break
    return db_user, db_prest

if __name__ == '__main__': 
    del_utente(db_user, db_prest)
    #add_libro(db_categoria, db_libro, db_autor)


    
