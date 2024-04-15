# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 11:08:44 2024

@author: ml_mauroadrianmodica
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


ticker = "GGAL"
ticker = "PAMP"

url = "https://www.investing.com/search/?q=" + ticker

navegador = webdriver.Chrome()
navegador.get(url)
tick = navegador.find_element(By.XPATH , "/html/body/div[6]/section/div/div[2]/div[2]/div[1]/a[1]/span[2]")
ActionChains(navegador).move_to_element(tick).click(tick).perform()
financials = navegador.find_element(By.XPATH , "/html/body/div[1]/div[2]/div[2]/div[2]/div[1]/nav/div[1]/ul/li[4]")
try:
    ActionChains(navegador).move_to_element(financials).click(financials).perform()
except:
    popup = navegador.find_element(By.XPATH , "/html/body/div[8]/div[2]/i")                      
    ActionChains(navegador).move_to_element(popup).click(popup).perform()


#Baja el resumen

ratio = navegador.find_element(By.XPATH , "/html/body/div[6]/section/div[12]")
ratios = ratio.get_attribute('innerHTML')

#print(ratios)
f = open("resumen.txt", "a")
f.write(ratios)
f.close()


"""
"""
#Baja el income statement completo
"""
inc = navegador.find_element(By.XPATH , "/html/body/div[6]/section/ul[2]/li[2]")
ActionChains(navegador).move_to_element(inc).click(inc).perform()
    
datas = navegador.find_element(By.XPATH , "/html/body/div[6]/section/div[9]/table")
data = datas.get_attribute('innerHTML')

print(data)
"""

#Baja el balance completo
"""
balanc = navegador.find_element(By.XPATH , "/html/body/div[6]/section/ul[2]/li[3]")
ActionChains(navegador).move_to_element(balanc).click(balanc).perform()
    
datas = navegador.find_element(By.XPATH , "/html/body/div[6]/section/div[9]/table")
data = datas.get_attribute('innerHTML')

print(data)

"""
#Baja el cash flow completo

"""

cash = navegador.find_element(By.XPATH , "/html/body/div[6]/section/ul[2]/li[4]")
ActionChains(navegador).move_to_element(cash).click(cash).perform()
    
datas = navegador.find_element(By.XPATH , "/html/body/div[6]/section/div[9]/table")
data = datas.get_attribute('innerHTML')

print(data)
"""

#Baja los ratios
"""
rat = navegador.find_element(By.XPATH , "/html/body/div[6]/section/ul[2]/li[5]")
ActionChains(navegador).move_to_element(rat).click(rat).perform()
    
datas = navegador.find_element(By.XPATH , "/html/body/div[6]/section/table/tbody")
data = datas.get_attribute('innerHTML')

print(data)

"""
#Baja los dividendos
"""
div = navegador.find_element(By.XPATH , "/html/body/div[6]/section/ul[2]/li[6]")
ActionChains(navegador).move_to_element(div).click(div).perform()
    
datas = navegador.find_element(By.XPATH , "/html/body/div[6]/section/table")
data = datas.get_attribute('innerHTML')

print(data)
"""

#Baja las ganancias
"""
earn = navegador.find_element(By.XPATH , "/html/body/div[6]/section/ul[2]/li[7]")
ActionChains(navegador).move_to_element(earn).click(earn).perform()
    
datas = navegador.find_element(By.XPATH , "/html/body/div[6]/section/table")
data = datas.get_attribute('innerHTML')

print(data)
"""
