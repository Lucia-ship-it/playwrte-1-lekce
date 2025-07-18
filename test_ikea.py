from playwright.sync_api import Page

# SPUSTENIE: pytest test_ikea.py

def test_title_ikea(page: Page):
    #prejit na stranku
    page.goto("https://www.ikea.com/cz/cs/")
    #zistit co je v title
    title = page.title()
    #zistit, ci title odpoveda : Nábytek se švédskou tradicí pro každou domácnost
    assert "Nábytek se švédskou tradicí pro každou domácnost" in title
    # pustit len ako subor 

def test_cookies_ikea(page: Page):
    # přejdeme na ikea.cz
    page.goto("https://www.ikea.com/cz/cs/")
    
    # klikneme na tlačítko "Přijmout vše"
    # 1. najdu tlačítko
    button = page.locator("#onetrust-accept-btn-handler")
    # 2. kliknu na tlačítko
    button.click()
    
    # Zkontrolujeme, že cookies čtverec není vidět
    # 1. najdu čtverec
    cookies_square = page.locator("#onetrust-banner-sdk")
    # 2. zkontroluju, že není vidět
    page.screenshot(path="sc.png")
    assert cookies_square.is_visible() == False

    #trosku pozastavime test na 2 skundu. cislo dole je v milisekundach
    #page.wait_for_timeout(2000)
    