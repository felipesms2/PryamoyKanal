from playwright.sync_api import sync_playwright
import json

url = "https://www.tiktok.com/@metropolesoficial/video/7551992484558097720"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(url)

    raw_state = page.locator("script#SIGI_STATE").inner_text()
    data = json.loads(raw_state)

    print(json.dumps(data, indent=2))
    browser.close()
from playwright.sync_api import sync_playwright
import json

url = "https://www.tiktok.com/@metropolesoficial/video/7551992484558097720"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto(url)

    raw_state = page.locator("script#SIGI_STATE").inner_text()
    data = json.loads(raw_state)

    print(json.dumps(data, indent=2))
    browser.close()
