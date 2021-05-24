# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 16:04:24 2021

@author: RobertoFormenti
"""

#import csv
import pandas as pd

#ripopolamenti csv
def writer(db_autor, db_categoria, db_libro, db_user, db_prest):
    (pd.DataFrame.from_dict(data=db_autor).to_csv('autore.csv', header=True, index=None))
    (pd.DataFrame.from_dict(data=db_categoria).to_csv('categoria.csv', header=True, index=None))
    (pd.DataFrame.from_dict(data=db_libro).to_csv('libro.csv', header=True, index=None))
    (pd.DataFrame.from_dict(data=db_user).to_csv('user.csv', header=True, index=None))
    (pd.DataFrame.from_dict(data=db_prest).to_csv('prest.csv', header=True, index=None))
    return db_autor, db_categoria, db_libro, db_user, db_prest

if __name__ == '__main__': 
    writer(db_autor, db_categoria, db_libro, db_user, db_prest)
