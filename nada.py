from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configura as opções do Chrome para usar o Opera
chrome_options = Options()
chrome_options.binary_location = "C:/Users/Gabriel/Documents/Python/chrome-win64/chrome-win64/chrome.exe"  # Caminho para o executável do Opera

# Configura o serviço do WebDriver
service = Service(executable_path="C:/Users/Gabriel/Documents/Python/chromedriver-win64/chromedriver-win64/chromedriver.exe")
#service = Service(ChromeDriverManager().install())

# Inicialize o WebDriver com as opções do Chrome e o caminho do OperaDriver
driver = webdriver.Chrome(service=service, options=chrome_options)
##driver = webdriver.Chrome(service="C:/Users/Gabriel/Documents/Python/operadriver.exe", options=chrome_options)

try:
    # Abra a página de login
    driver.get('http://localhost:8000/login')

    # Encontre o campo de email e preencha com o valor desejado
    email_field = driver.find_element(By.NAME, 'email')  # Substitua 'email' pelo nome correto do campo
    email_field.send_keys('12345678@gmail.com')

    # Encontre o campo de senha e preencha com o valor desejado
    password_field = driver.find_element(By.NAME, 'password')  # Substitua 'password' pelo nome correto do campo
    password_field.send_keys('12345678')

    # Encontre o botão de submit e clique nele
    submit_button = driver.find_element(By.XPATH, '//button[@type="submit"]')  # Ajuste o seletor conforme necessário
    submit_button.click()

    # Aguarde até que o texto esperado esteja presente na página
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, 'body'), "You're logged in!")
    )

    # Verifique se o texto está presente no corpo da página
    page_text = driver.find_element(By.TAG_NAME, 'body').text
    if "You're logged in!" in page_text:
        print("O texto 'You're logged in!' foi encontrado na página.")
        driver.get('http://localhost:8000/users')
    else:
        print("O texto 'You're logged in!' não foi encontrado na página.")

    time.sleep(5)
finally:
    # Feche o navegador
    driver.quit()
