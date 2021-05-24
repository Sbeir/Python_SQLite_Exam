# -*- coding: utf-8 -*-
"""
Created on Mon May  3 13:26:32 2021

@author: RobertoFormenti
"""

import sqlite3


#query per prendere in prestito un libro
def add_prestito(isbn, idp, tessera, data_iniz, data_fine, copie, nprest, stato, data_consegna):
    conn = sqlite3.Connection('file:biblio.sqlite?mode=rwc', uri=True)
    c = conn.cursor()
    sql_add = """INSERT or replace INTO prestito (isbn,id,tessera, data_iniz, data_fine, stato, data_consegna) VALUES (?,?,?,?,?,?,?)"""
    data_tuple = (isbn, idp, tessera, data_iniz, data_fine, stato, data_consegna)
    c.execute(sql_add, data_tuple)
    sql_up = """UPDATE libro SET copie = ? WHERE isbn = ?"""
    data = (copie, isbn)
    c.execute(sql_up, data)
    sql_up_user = """UPDATE utente SET nprest = ? WHERE tessera = ?"""
    data1 = (nprest, tessera)
    c.execute(sql_up_user, data1)    
    conn.commit()
    c.close()
    conn.close()
    return

#query ritorno del prestito
def return_prestito(idp, copie, nprest, stato, tessera, isbn, data_consegna):
    conn = sqlite3.Connection('file:biblio.sqlite?mode=rwc', uri=True)
    c = conn.cursor()
    sql_upd = """UPDATE prestito SET stato = ? WHERE id = ?"""
    data_tuple = (stato, idp)
    c.execute(sql_upd, data_tuple)
    sql_up = """UPDATE libro SET copie = ? WHERE isbn = ?"""
    data = (copie, isbn)
    c.execute(sql_up, data)
    sql_up_user = """UPDATE utente SET nprest = ? WHERE tessera = ?"""
    c.execute(sql_up_user, (nprest, tessera))    
    conn.commit()
    sql_up_stato = """UPDATE prestito SET stato = ? WHERE tessera = ?"""
    c.execute(sql_up_stato, (stato, tessera))
    sql_up_data = """UPDATE prestito SET data_consegna = ? WHERE tessera = ?"""
    c.execute(sql_up_data, (data_consegna, tessera))      
    conn.commit()
    c.close()
    conn.close()
    return

def del_prestiti(tessera):
    conn = sqlite3.Connection('file:biblio.sqlite?mode=rwc', uri=True)
    c = conn.cursor()
    sql_del = """DELETE FROM prestito WHERE tessera = ?"""
    c.execute(sql_del, (tessera, ))    
    conn.commit()
    c.close()
    conn.close()
    return 
    