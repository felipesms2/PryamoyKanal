from playwright.sync_api import sync_playwright
import json

url = "https://www.tiktok.com/@metropolesoficial/video/7551992484558097720"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # melhor deixar False para debug
    page = browser.new_page()
    page.goto(url, wait_until="networkidle")  # espera a página ficar "quieta"

    # Espera explicitamente pelo SIGI_STATE
    page.wait_for_selector("script#SIGI_STATE")

    raw_state = page.locator("script#SIGI_STATE").inner_text()
    data = json.loads(raw_state)

    # Salva o JSON
    filename = url.split("/")[-1] + ".json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"Arquivo salvo: {filename}")
    browser.close()
