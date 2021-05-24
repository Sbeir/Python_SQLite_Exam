# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 16:09:01 2021

@author: RobertoFormenti
"""
import sqlite3
import Biblio.io_csv as io

#query aggiunta utente
def query_add_utente(nome, cognome, anno_reg, telefono, tessera, nprest):
    conn = sqlite3.Connection('file:biblio.sqlite?mode=rwc', uri=True)
    c = conn.cursor()
    sql_insert = """INSERT or replace INTO utente (nome , cognome, anno_reg, telefono, tessera, nprest)
    VALUES(?,?,?,?,?,?);"""
    data_tuple = (nome, cognome, anno_reg, telefono, tessera, nprest)
    c.execute(sql_insert, data_tuple)
    conn.commit()
    conn.close()
    c.close()
    return

#query eliminazione utente    
def query_del_utente(tessera):
    conn = sqlite3.Connection('file:biblio.sqlite?mode=rwc', uri=True)
    c = conn.cursor()
    sql_del = """DELETE FROM utente WHERE tessera = ?"""
    c.execute(sql_del, (tessera, ))
    conn.commit()
    c.close()
    conn.close()
    return

#query aggiunta libro    
def query_add_libro(isbn,titolo,lingua,anno,editore,pagine,categoria,copie,autore):
    conn = sqlite3.Connection('file:biblio.sqlite?mode=rwc', uri=True)
    c = conn.cursor()
    sql_insert = """INSERT or replace INTO libro (isbn ,titolo , lingua, anno, editore, pagine, categoria, copie, autore)
    VALUES(?,?,?,?,?,?,?,?,?);"""
    data_tuple = (isbn, titolo, lingua, anno, editore, pagine, categoria, copie, autore)
    c.execute(sql_insert, data_tuple)
    conn.commit()
    c.close()
    conn.close()
    return

#quesry eliminazione libro
def query_del_libro(isbn):
    conn = sqlite3.Connection('file:biblio.sqlite?mode=rwc', uri=True)
    c = conn.cursor()
    sql_del = """DELETE FROM libro WHERE isbn = ?"""
    c.execute(sql_del, (isbn, ))
    conn.commit()
    c.close()
    conn.close()
    return
 
#query modifica libro   
def query_modifica_libro(copie, isbn):
    conn = sqlite3.Connection('file:biblio.sqlite?mode=rwc', uri=True)
    c = conn.cursor()
    sql_update = """UPDATE libro SET copie = ? WHERE isbn = ?"""
    data = (copie, isbn)
    c.execute(sql_update, data)
    conn.commit()
    c.close()
    conn.close()
    return

#query aggiunta autore    
def query_add_autore(nome , cognome, anno, note, id_autore):
    conn = sqlite3.Connection('file:biblio.sqlite?mode=rwc', uri=True)
    c = conn.cursor()
    sql_insert = """INSERT or replace INTO autore (nome , cognome, anno, note, id)
    VALUES(?,?,?,?,?);"""
    data_tuple = (nome, cognome, anno, note, id_autore)
    c.execute(sql_insert, data_tuple)
    conn.commit()
    c.close()
    conn.close() 
    return

#query eliminazione autore
def query_del_autore(nome, cognome, anno):
    conn = sqlite3.Connection('file:biblio.sqlite?mode=rwc', uri=True)
    c = conn.cursor()
    sql_del = """DELETE FROM autore WHERE nome = ? AND cognome = ? AND anno = ?"""
    c.execute(sql_del, (nome, cognome, anno ))
    conn.commit()
    c.close()
    conn.close()
    return

    
    