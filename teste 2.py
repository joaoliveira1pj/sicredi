from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import openpyxl

navegador = webdriver.Chrome()

url_challenge = "https://rpachallenge.com/"
navegador.get(url_challenge)

bt_start = navegador.find_element(By.XPATH, "//button[contains(text(),'Start')]")
bt_start.click()

bt_download = navegador.find_element(By.XPATH, "//a[contains(text(),'Download')]")
bt_download.click()

time.sleep(15)

caminho_arquivo_excel = os.path.join(os.path.expanduser("~"), "Downloads", "challenge.xlsx")
workbook = openpyxl.load_workbook(caminho_arquivo_excel)
planilha_atual = workbook.active

for linha in planilha_atual.iter_rows(min_row=2, values_only=True):
    if linha[0] is None:
        break
    else:
        campos = ["labelAddress", "labelFirstName", "labelLastName", "labelEmail", "labelRole", "labelPhone", "labelCompanyName"]
        for campo, valor in zip(campos, linha):
            input_campo = WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.XPATH, f"//input[@ng-reflect-name='{campo}']")))
            input_campo.send_keys(str(valor))
        bt_submit = navegador.find_element(By.XPATH, "//input[@value='Submit']")
        bt_submit.click()
        time.sleep(2)

navegador.quit()
workbook.close()
