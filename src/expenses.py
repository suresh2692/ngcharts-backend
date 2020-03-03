# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 14:56:30 2019

@author: suresh
"""

import pandas as pd


df = pd.read_hdf(r'dataset/expenses.h5')


def total_expenses():
    return df.groupby(['Cr'])['amount'].sum().to_dict()

def top_expenses(n=5):
    cr = df[df['Cr'] == 'credit'].groupby(
                        ['Particulars'])['amount'].sum().nlargest(n).to_dict()
    dr = df[df['Cr'] == 'debit'].groupby(
                        ['Particulars'])['amount'].sum().nlargest(n).to_dict()    
    return {'credit':cr, 'debit':dr }

def daywise_transaction():
    day_trans = df.groupby(['dayname'])['amount'].sum().to_dict()
    return day_trans


def datewise_transaction():
    cr = df[df['Cr'] == 'credit'].groupby(
                        ['day'])['amount'].sum().to_dict()
    dr = df[df['Cr'] == 'debit'].groupby(
                        ['day'])['amount'].sum().to_dict()    
    return {'credit':cr, 'debit':dr }
    
    
