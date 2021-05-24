# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 16:45:19 2021

@author: RobertoFormenti
"""
import create_table as ct
import deladd as da
import io_csv as io
import create_db as cd
import view as v
import write as w
import prest as p
import query_prestito as qp



ct.table()

#funzione per popolamenti
def start(): #avvio le funzioni del modulo io_csv
    io.utente.dict_utente(db_user)
    io.libro.dict_libro(db_libro)
    io.categoria.dict_categoria(db_categoria)
    io.autore.dict_autore(db_autor)
    io.prestito.dict_prestito(db_prest)
    
    io.utente.csv_utente()
    io.categoria.csv_categoria()
    io.autore.csv_autore()
    io.libro.csv_libro()
    io.prestito.csv_prestito()
    return

#riprendo le funzioni per la creazione dei dict
db_user = cd.user()
db_autor = cd.autor()
db_categoria = cd.categoria()
db_libro = cd.libro()
db_prest = cd.prest()

start()

#menu UI
ans=True
while ans:
    print("""
    1.Aggiungere/eliminare/modificare
    2.Prendi in prestito/Restituisci libro/ricerca prestito
    3.Cerca libro
    4.Exit/Quit
    """)
    ans= input("Cosa vuoi fare? ")
    if ans=="1":
        ans1=True
        while ans1:
            print("""
            1.Aggiungere libro
            2.aggiungere utente
            3.Aggiungere autore
            4.Modificare libro
            5.Eliminare libro
            6.Eliminare utente
            7.Torna al menu precedente
            """)
            ans1= input("Cosa vuoi fare? ")
            if ans1=="1":
                da.add_libro(db_categoria, db_libro, db_autor)
                print("\nCompletato")
            elif ans1=="2":
                da.add_utente(db_user)
                print("\n Completato")
            elif ans1=="3":
                da.add_autore(db_autor)
                print("\n Completato")
            elif ans1=="4":
                da.modifica_libro(db_libro)
                print("\n Completato")
            elif ans1=="5":
                da.del_libro(db_libro)
                print("\n Completato")
            elif ans1=="6":
                da.del_utente(db_user, db_prest)
                print("\n Completato")
            elif ans1=="7":
                print("\n")
                ans1 = None
            else:
                print("\n input non valido, riprova")
            print("\nCompletato")
    elif ans=="2":
        ans2=True
        while ans2:
            print("""
            1.Prendi in prestito un libro
            2.Ritorna un libro
            3.Torna al menu precedente
            """)
            ans2= input("Cosa vuoi fare? ")
            if ans2=="1":
                p.add_prestito(db_libro, db_prest, db_user)
            elif ans2=="2":
                p.restituisci_prestito(db_libro, db_prest, db_user)
                print("\n Completato")
            elif ans2=="3":
                while True:
                    try:
                        tesserap = int(input("inserisci tessere per vedere i prestiti "))
                        break
                    except ValueError:
                        print("Oops!  tessera non valida, riprova ")                 
                v.select_prestito(tesserap)
                print("\n Completato")
            elif ans2=="4":
                print("\n")
                ans2 = None
            else:
                print("\n input non valido, riprova")
        print("\n Completato")
    elif ans=="3":
        ans3=True
        while ans3:
            print("""
            1.Visualizza catalogo
            2.Cerca libro tramite isbn
            3.Cerca libro tramite titolo
            4.Torna al menu precedente
            """)
            ans3= input("Cosa vuoi fare? ")
            if ans3=="1":
                v.catalogo()
                print("\nCompletato")
            elif ans3=="2":
                while True:
                    try:
                        isbnv = int(input("inserisci isbn "))
                        break
                    except ValueError:
                        print("Oops!  isbn non valido, riprova ")                
                v.select_isbn(isbnv)
                print("\n Completato")
            elif ans3=="3":
                while True:
                    try:
                        titolov = str(input("inserisci titolo che vuoi cercare "))
                        titolov = titolov.lower()
                        break
                    except ValueError:
                        print("Oops!  titolo non valido")
                v.select_titolo(titolov)
                print("\n Completato")
            elif ans3=="4":
                print("\n")
                ans3 = None
            else:
                print("\n input non valido, riprova")
        print("\n Completato")
    elif ans=="4":
      print("\n Arrivederci")
      ans = None
    else:
       print("\n input non valido, riprova")


    
w.writer(db_autor, db_categoria, db_libro, db_user, db_prest)