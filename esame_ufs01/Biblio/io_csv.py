# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 15:50:55 2021

@author: RobertoFormenti
"""

import pandas as pd
import csv
import sqlite3



class categoria:
    #funzione che legge csv e inserisce i dati in sqlite
    def csv_categoria():
        conn = sqlite3.Connection('file:biblio.sqlite?mode=rwc', uri=True)
        c = conn.cursor()
            
        with open('categoria.csv', 'r') as csv_categoria:
            reader = csv.reader(csv_categoria)
            next(reader, None)
            c.executemany("INSERT or replace INTO categoria VALUES (?, ?)", reader)
            c.execute("SELECT * FROM categoria")
            conn.commit()
            c.close()
            conn.close()
        return
    
    #popolamento dizionario
    def dict_categoria(db_categoria):
        csv_categoria = open(r'categoria.csv')
        dict_reader = csv.DictReader(csv_categoria)
        for row in dict_reader:
            id_categoria = row['id']
            nome_categoria = row['nome']
            db_categoria['id'].append(id_categoria)
            db_categoria['nome'].append(nome_categoria)
        return db_categoria
    


class autore:
    #funzione che legge csv e inserisce i dati in sqlite
    def csv_autore():
        conn = sqlite3.Connection('file:biblio.sqlite?mode=rwc', uri=True)
        c = conn.cursor()
            
        csv_autor = open(r'autore.csv')
        reader = csv.reader(csv_autor)
        next(reader, None)
        c.executemany("INSERT or replace INTO autore VALUES (?,?,?,?,?)", reader)
        c.execute("SELECT * FROM autore")
        conn.commit()
        c.close()
        conn.close()
        return
    
    #popolamento dizionario
    def dict_autore(db_autor):
        dict_autore = open(r'autore.csv')
        dict_reader = csv.DictReader(dict_autore)
        for row in dict_reader:
            nome = row['nome']
            cognome = row['cognome']
            anno = row['anno']
            note = str(row['note'])
            id_autore = row['id']
            db_autor["nome"].append(nome)
            db_autor["cognome"].append(cognome)
            db_autor["anno"].append(anno)
            db_autor["note"].append(note)
            db_autor["id"].append(id_autore)
        return db_autor



class libro:
    #funzione che legge csv e inserisce i dati in sqlite
    def csv_libro():
        conn = sqlite3.Connection('file:biblio.sqlite?mode=rwc', uri=True)
        c = conn.cursor()
            
        with open('libro.csv', 'r') as csv_libro:
            reader = csv.reader(csv_libro)
            next(reader, None)
            c.executemany("INSERT or replace INTO libro VALUES (?,?,?,?,?,?,?,?,?)", reader)
            c.execute("SELECT * FROM libro")
            conn.commit()
            c.close()
            conn.close()
        return
    
    #popolamento dizionario
    def dict_libro(db_libro):
        dict_libro = open(r'libro.csv')
        dict_reader = csv.DictReader(dict_libro)
        for row in dict_reader:
            isbn = row['isbn']
            anno = row['anno']
            lingua = row['lingua']
            titolo = row['titolo']
            editore = row['editore']
            pagine = row['pagine']
            categoria = row['categoria']
            copie = row['copie']
            autore = row['autore']
            db_libro["isbn"].append(isbn)
            db_libro["anno"].append(anno)
            db_libro["lingua"].append(lingua)
            db_libro["titolo"].append(titolo)
            db_libro["editore"].append(editore)
            db_libro["pagine"].append(pagine)
            db_libro["categoria"].append(categoria)
            db_libro["copie"].append(copie)
            db_libro["autore"].append(autore)
        return db_libro
    

class utente:
    #funzione che legge csv e inserisce i dati in sqlite
    def csv_utente():
        conn = sqlite3.Connection('file:biblio.sqlite?mode=rwc', uri=True)
        c = conn.cursor()
            
        csv_user = open(r'user.csv')
        reader = csv.reader(csv_user)
        next(reader, None)
        c.executemany("INSERT or replace INTO utente VALUES (?,?,?,?,?,?)", reader)
        c.execute("SELECT * FROM utente")
        conn.commit()
        c.close()
        conn.close()
        return
    
    #popolamento dizionario
    def dict_utente(db_user):
        dict_utente = open(r'user.csv')
        dict_reader = csv.DictReader(dict_utente)
        for row in dict_reader:
            nome = row['nome']
            cognome = row['cognome']
            anno_reg = row['anno_reg']
            telefono = row['telefono']
            tessera = row['tessera']
            nprest = row['nprest']
            db_user["nome"].append(nome)
            db_user["cognome"].append(cognome)
            db_user["anno_reg"].append(anno_reg)
            db_user["telefono"].append(telefono)
            db_user["tessera"].append(tessera)
            db_user["nprest"].append(nprest)
        return db_user
    
class prestito:
    #funzione che legge csv e inserisce i dati in sqlite
    def csv_prestito():
        conn = sqlite3.Connection('file:biblio.sqlite?mode=rwc', uri=True)
        c = conn.cursor()
            
        csv_prest = open(r'prest.csv')
        reader = csv.reader(csv_prest)
        next(reader, None)
        c.executemany("INSERT or replace INTO prestito VALUES (?,?,?,?,?,?,?)", reader)
        c.execute("SELECT * FROM prestito")
        conn.commit()
        c.close()
        conn.close()
        return
    
    #popolamento dizionario
    def dict_prestito(db_prest):
        dict_prest = open(r'prest.csv')
        dict_reader = csv.DictReader(dict_prest)
        for row in dict_reader:
            isbn = row['isbn']
            idp = row['id']
            tessera = row['tessera']
            data_inizio = row['data_inizio']
            data_fine = row['data_fine']
            stato = row["stato"]
            data_consegna = row["data_consegna"]
            db_prest["isbn"].append(isbn)
            db_prest["id"].append(idp)
            db_prest["tessera"].append(tessera)
            db_prest["data_inizio"].append(data_inizio)
            db_prest["data_fine"].append(data_fine)
            db_prest["stato"].append(stato)
            db_prest["data_consegna"].append(data_consegna)
        return db_prest
        

#with open('Biblio\categoria.csv', 'r') as csv_categoria:
    #x = pd.read_csv(csv_categoria, header=None, index_col=False, squeeze=True).to_dict()
        












