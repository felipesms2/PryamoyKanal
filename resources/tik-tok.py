from playwright.sync_api import sync_playwright
import json

url = "https://www.tiktok.com/@metropolesoficial/video/7551992484558097720"

# Extrair o ID do vídeo da URL
video_id = url.split("/")[-1]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(url)

    raw_state = page.locator("script#SIGI_STATE").inner_text()
    data = json.loads(raw_state)

    # Salvar o JSON em arquivo
    filename = f"{video_id}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Arquivo salvo como {filename}")
    browser.close()
