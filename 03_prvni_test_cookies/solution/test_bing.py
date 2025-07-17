import pytest


def test_title(page):
    page.goto("https://www.knihydobrovsky.cz/")
    title = page.title()
    assert title == "Knihy Dobrovský | Vaše (nejen) online knihkupectví s tradicí"


def test_cookies(page):
    page.goto("https://www.knihydobrovsky.cz/")
    button_allow_loc = "#ch2-dialog >> .ch2-allow-all-btn"
    cookies_bar_loc = "#ch2-dialog"

    button_allow = page.locator(button_allow_loc)
    button_allow.click()

    cookies_bar = page.locator(cookies_bar_loc)
    assert cookies_bar.is_visible() == False


@pytest.fixture()
def page_knihy(page):
    page.goto("https://www.knihydobrovsky.cz/")
    button_allow_loc = "#ch2-dialog >> .ch2-allow-all-btn"

    button_allow = page.locator(button_allow_loc)
    button_allow.click()
    yield page
