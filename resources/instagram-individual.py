# instagram-individual.py
# pip install -U selenium

import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.instagram.com/p/B0wQkAcCae1/"

# Configurações do navegador
options = Options()
options.add_argument("--headless=new")  # roda sem abrir janela
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument(
    "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/140.0 Safari/537.36"
)

# Usa o chromedriver já instalado no PATH (nenhum webdriver-manager aqui)
driver = webdriver.Chrome(options=options)
driver.set_window_size(1200, 1600)

try:
    driver.get(URL)
    wait = WebDriverWait(driver, 15)

    # Espera o post carregar (tag <article>)
    post = wait.until(EC.presence_of_element_located((By.TAG_NAME, "article")))

    time.sleep(2)  # tempo extra p/ imagens renderizarem

    # Salvar screenshot do post
    output_dir = "screenshots"
    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, "insta_post_B0wQkAcCae1.png")
    post.screenshot(out_path)

    print("✅ Screenshot salva em:", out_path)

except Exception as e:
    print("⚠️ Erro:", e)
    fallback = "screenshots/fullpage_B0wQkAcCae1.png"
    driver.save_screenshot(fallback)
    print("📸 Fallback salvo em:", fallback)

finally:
    driver.quit()
# instagram-individual.py
# pip install -U selenium

import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.instagram.com/p/B0wQkAcCae1/"

# Configurações do navegador
options = Options()
options.add_argument("--headless=new")  # roda sem abrir janela
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument(
    "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/140.0 Safari/537.36"
)

# Usa o chromedriver já instalado no PATH (nenhum webdriver-manager aqui)
driver = webdriver.Chrome(options=options)
driver.set_window_size(1200, 1600)

try:
    driver.get(URL)
    wait = WebDriverWait(driver, 15)

    # Espera o post carregar (tag <article>)
    post = wait.until(EC.presence_of_element_located((By.TAG_NAME, "article")))

    time.sleep(2)  # tempo extra p/ imagens renderizarem

    # Salvar screenshot do post
    output_dir = "screenshots"
    os.makedirs(output_dir, exist_ok=True)
    out_path = os.path.join(output_dir, "insta_post_B0wQkAcCae1.png")
    post.screenshot(out_path)

    print("✅ Screenshot salva em:", out_path)

except Exception as e:
    print("⚠️ Erro:", e)
    fallback = "screenshots/fullpage_B0wQkAcCae1.png"
    driver.save_screenshot(fallback)
    print("📸 Fallback salvo em:", fallback)

finally:
    driver.quit()
