import pandas as pd
from bs4 import BeautifulSoup as BS
from urllib import request

url = 'https://en.wikipedia.org/wiki/List_of_largest_cities'
html = request.urlopen(url)
bs = BS(html.read(), 'html.parser')

# table = bs.find('table', class_= 'wikitable sortable')
table = bs.find('table',{'class':"wikitable"})
# print(table)
df = pd.read_html(str(table))
df = pd.concat(df)
print(df)
first_column = df.iloc[1:, 0]
print(first_column)
first_column.to_csv('cities.csv', header=False, index=False) 