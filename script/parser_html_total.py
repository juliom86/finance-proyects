from bs4 import BeautifulSoup
import pandas as pd

with open ('income.txt') as file:
    html = file.read()
# Parsear HTML

soup = BeautifulSoup(html, 'html.parser')

# Encontrar filas

rows = soup.find_all('tr')

# Extraer periodos y revenues

periods = [x.find('div').text for x in rows[0].find_all('th')[1:]]


# Convertit a un csv

data = []

for row in rows[1:]:
    td = row.find_all('td')
    if len(td) == 5: #excluye las subtablas
        values = [x.text for x in td[1:]]
        data.append([td[0].text.strip()]+values)

#Creamos un DataFrame

df=pd.DataFrame(data).set_index(0).transpose()
df.columns.name = None
df.insert(0, 'Perios', periods)

#guardamos el CSV
df.to_csv('income_output.csv', index = False)
