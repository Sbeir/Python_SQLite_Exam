# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 16:45:19 2021

@author: RobertoFormenti
"""

import sqlite3
from sqlite3 import Error

#connette al file biblio.sqlite se esiste se no lo crea
conn = sqlite3.Connection('file:biblio.sqlite?mode=rwc', uri=True)


def create_table(conn, create_table_sql): #funzione che crea le tabelle
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def table(): #struttura database sql e poi avvia funzione create_table
    sql_create_autore_table = """CREATE TABLE IF NOT EXISTS autore (
                                    nome varchar(255) NOT NULL,
                                    cognome varchar(255) NOT NULL,
                                    anno integer NOT NULL,
                                    note text,
                                    id integer PRIMARY KEY
                                );"""    


    sql_create_libro_table = """ CREATE TABLE IF NOT EXISTS libro (
                                        isbn integer PRIMARY KEY,
                                        titolo varchar(255) NOT NULL,
                                        lingua varchar(255) NOT NULL,
                                        anno integer NOT NULL,
                                        editore varchar(255) NOT NULL,
                                        pagine integer NOT NULL,
                                        categoria int NOT NULL,
                                        copie integer NOT NULL,
                                        autore integer NOT NULL,
                                        FOREIGN KEY (autore) REFERENCES autore (id),
                                        FOREIGN KEY (categoria) REFERENCES categoria (id)
                                    ); """

    sql_create_utente_table = """CREATE TABLE IF NOT EXISTS utente (
                                    nome varchar(255) NOT NULL,
                                    cognome varchar(255) NOT NULL,
                                    anno_reg date NOT NULL,
                                    telefono integer NOT NULL,
                                    tessera integer PRIMARY KEY,
                                    nprest integer NOT NULL
                                );"""
    
    
    sql_create_prestito_table = """CREATE TABLE IF NOT EXISTS prestito (
                                    isbn integer,
                                    id integer PRIMARY KEY,
                                    tessera integer NOT NULL,
                                    data_iniz date NOT NULL,
                                    data_fine date NOT NULL,
                                    stato integer NOT NULL,
                                    data_consegna date,
                                    FOREIGN KEY (tessera) REFERENCES utente (tessera),
                                    FOREIGN KEY (isbn) REFERENCES libro (isbn)
                                );"""
    
    
    sql_create_categoria_table = """CREATE TABLE IF NOT EXISTS categoria (
                                    id integr PRIMARY KEY,
                                    nome varchar(255) not null
                                );"""
       

    # create a database connection
    conn = sqlite3.Connection('file:biblio.sqlite?mode=rwc', uri=True)

    # create tables
    if conn is not None:
        create_table(conn, sql_create_autore_table)
        
        create_table(conn, sql_create_libro_table)

        create_table(conn, sql_create_utente_table)
        
        create_table(conn, sql_create_prestito_table)
        
        create_table(conn, sql_create_categoria_table)
        
    else:
        print("Error! cannot create the database connection.")
    
    conn.close()



if __name__ == '__main__':
    table()