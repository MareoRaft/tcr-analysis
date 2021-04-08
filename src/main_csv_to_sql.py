import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, Text, MetaData, Table
from sqlalchemy import select

def init_sql():
  # globals
  engine = create_engine('sqlite://')
  return engine

def main():
  # pandas read_csv
  df = pd.read_csv('data/csv/hs_a_53535_1k.csv',
    encoding='utf_8',
    delimiter=',',
    names=['ID','qual','label','mult','V','Vrange','v_len','J','Jrange','j_len','cdr3_ext','cdr3_len','aa','vframe','jframe','frag'],
    index_col='ID',
    nrows=3,
  )
  print(df)
  # pandas to sql using sqlalchemy
  engine = init_sql()
  df.to_sql('matttable', engine)
