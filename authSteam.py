from time import sleep
from selenium.webdriver.common.by import By

def authSteam(driver, login, password):
    #acessa steam para efetuar a autenticação
    driver.get('https://steamcommunity.com/login/')                     #site login steam
    driver.find_element(By.ID, 'input_username').send_keys(login)       #inserir username steam
    driver.find_element(By.ID, 'input_password').send_keys(password)    #inserir password steam
    driver.find_element(By.CLASS_NAME, 'btn_blue_steamui').click()      #clicar no botão login
    input('o steam guard já foi inserido?')
    sleep(1)