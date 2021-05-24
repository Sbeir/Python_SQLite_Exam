# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 11:12:50 2021

@author: RobertoFormenti
"""
import sqlite3
import datetime as d

conn = sqlite3.Connection('file:biblio.sqlite?mode=rwc', uri=True)
c = conn.cursor()

#c.execute("SELECT isbn FROM libro where titolo = 1984")
#x = c.fetchall()
#a = x[0][0]

#query mostra catalogo
def catalogo():
    """
    query che mostra tutto il catalogo dei libri 
    presenti nel db.
    """
    conn = sqlite3.Connection('file:biblio.sqlite?mode=rwc', uri=True)
    c = conn.cursor()
    c.execute("SELECT * FROM libro")

    rows = c.fetchall()

    c.close()
    conn.close() 
    for isbn,titolo,lingua,anno,editore,pagine,categoria,copie,autore in rows:
        print('isbn: ',isbn)
        print('titolo: ',titolo)
        print('lingua: ',lingua)
        print('anno: ',anno)
        print('editore: ',editore)
        print('pagine: ',pagine)
        print('categoria: ',categoria)
        print('copie: ',copie)
        print('autore: ',autore)

#query per ricerca tramite isbn
def select_isbn(isbn):
    """
    query che tramite l'input dell'utente
    cerca il libro con lo stesso parametro
    e lo stampa a schermo
    """
    conn = sqlite3.Connection('file:biblio.sqlite?mode=rwc', uri=True)
    c = conn.cursor()
    sql = """SELECT * FROM libro WHERE isbn = ?"""
    c.execute(sql, (isbn, ))
    rows = c.fetchall()
    
    c.close()
    conn.close() 

    for isbn,titolo,lingua,anno,editore,pagine,categoria,copie,autore in rows:
        print('isbn: ',isbn)
        print('titolo: ',titolo)
        print('lingua: ',lingua)
        print('anno: ',anno)
        print('editore: ',editore)
        print('pagine: ',pagine)
        print('categoria: ',categoria)
        print('copie: ',copie)    
        print('autore: ',autore)
        

#query ricerca tramite titolo
def select_titolo(titolo):
    conn = sqlite3.Connection('file:biblio.sqlite?mode=rwc', uri=True)
    c = conn.cursor()
    sql_del = """SELECT * FROM libro WHERE titolo = ?"""
    c.execute(sql_del, (titolo, ))
    rows = c.fetchall()
    
    c.close()
    conn.close() 

    for isbn,titolo,lingua,anno,editore,pagine,categoria,copie,autore in rows:
        print('isbn: ',isbn)
        print('titolo: ',titolo)
        print('lingua: ',lingua)
        print('anno: ',anno)
        print('editore: ',editore)
        print('pagine: ',pagine)
        print('categoria: ',categoria)
        print('copie: ',copie)
        print('autore: ',autore)

#catalogo dei libri con stato attivo tramite tessera        
def select_prestito(tessera):
    conn = sqlite3.Connection('file:biblio.sqlite?mode=rwc', uri=True)
    c = conn.cursor()
    sql_del = """SELECT * FROM prestito WHERE tessera = ? AND stato = 1"""
    c.execute(sql_del, (tessera,))
    rows = c.fetchall()
    
    c.close()
    conn.close() 

    for isbn,idp,tessera,datainizio,datafine,stato,dataconsegna in rows:
        print('isbn: ',isbn)
        print('id: ',idp)
        print('tessera: ',tessera)
        print('data inizio prestito: ',datainizio)
        print('data scadenza prestito: ',datafine)
        
if __name__ == '__main__':
    select_prestito(1)