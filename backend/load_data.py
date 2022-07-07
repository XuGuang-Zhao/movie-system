import sqlite3, pandas
conn = sqlite3.connect('main/test.db')
user_ban = pandas.read_csv('user_ban.csv')
user_ban.to_sql('user_ban', conn)

user_movie = pandas.read_csv('user_movie.csv')
user_movie.to_sql('user_movie', conn)

conn.close()