from bs4 import BeautifulSoup
import csv

html = '''
<tbody><tr class="alignBottom" id="header_row">
<th><span class="lightgrayFont arial_11 noBold">Period Ending:</span></th>
<th><span class="bold">2023</span><div class="noBold arial_11">31/12</div></th>
<th><span class="bold">2023</span><div class="noBold arial_11">30/09</div></th>
<th><span class="bold">2023</span><div class="noBold arial_11">30/06</div></th>
<th><span class="bold">2023</span><div class="noBold arial_11">31/03</div></th>
</tr>

</tbody><tbody>
<tr class="openTr pointer" id="parentTr">
<td><span class=" bold">Total Revenue<span class="dropDownArrowLightGray"></span></span></td>
<td>166770</td>
<td>152701</td>
<td>110341</td>
<td>83915</td>
'''

# Parsear HTML

soup = BeautifulSoup(html, 'html.parser')

# Encontrar filas

rows = soup.find_all('tr')

# Extraer periodos y revenues

periods = [x.find('div').text for x in rows[0].find_all('th')[1:]]
revenues = [x.text for x in rows[1].find_all('td')[1:]]


# Convertit a un csv

with open('revenues.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Period', 'Total Revenue'])
    for period, revenue in zip(periods, revenues):
        writer.writerow([period+'/2023',revenue])
