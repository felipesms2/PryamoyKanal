from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Configura o Chrome headless
options = Options()
options.add_argument("--headless=new")  # rodar sem abrir janela
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

# Abre o perfil público
username = "adelle.fr"
driver.get(f"https://www.instagram.com/{username}/")

# espera carregar
time.sleep(5)

# Pega posts (miniaturas, legendas, links)
posts = driver.find_elements(By.CSS_SELECTOR, "article a")
for post in posts[:5]:  # só os 5 primeiros
    print(post.get_attribute("href"))

driver.quit()
