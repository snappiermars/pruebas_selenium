import time
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome() 
print('Iniciando pruebas . . .')

#Entra a la pagina a testear
driver.get('https://www.demoblaze.com/')
time.sleep(5)

#Verificar que la lista de temporada no este vacia
categorias = driver.find_elements(By.ID, 'itemc')
for categoria in categorias:
    print(categoria.text)

#Verificar que las categorias no esten vacias
assert len(categorias) > 0, 'La lista de categorias no puede estar vacia'
print('Prueba de categorias realizada')

#Click en la categoria de laptops
categorias[1].click()
time.sleep(5)

#Verificamos que contenga elementos la pagina
contenedor_laptops = driver.find_element(By.ID, 'tbodyid')
laptops = contenedor_laptops.find_elements(By.CLASS_NAME, 'card-title')
for laptop in laptops:
    print(laptop.text)
assert len(laptops) > 0, 'La lista de laptos no puede estar vacia'
print('Prueba de contenido realizada')

#Verificamos el link del segundo elemento de laptop
laptops[1].click()
current_url = str(driver.current_url)
print(current_url)
assert 'idp_=9' in current_url, 'No se cargo la pagina correcta'
print('Prueba de producto realiza')
time.sleep(5)

#Regresamos a la pagina anterior
driver.back()
time.sleep(5)

#Navegamos a la siguiente pestaña
next_btn = driver.find_element(By.ID, 'next2')
next_btn.click()
time.sleep(5)

#Cierra el navegador
driver.quit()

print('Pruebas completadas')