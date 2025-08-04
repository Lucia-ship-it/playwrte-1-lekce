from playwright.sync_api import Page

#pytest test_projekt.py

def test_title_lekarna(page: Page):
    page.goto("https://www.lekarnalemon.cz/?utm_source=google&utm_medium=cpc&utm_campaign=COG%20%7C%20CZ%2BCS%20%7C%20SEA%20%7C%20EXT%20%7C%20Brand%20%7C%20Lemon%20%7C%20tROAS&utm_id=15439773109&gad_source=1&gad_campaignid=15439773109&gbraid=0AAAAABR9GfMaH0ZxkUnat-zS4u1z8gvhE&gclid=Cj0KCQjwtMHEBhC-ARIsABua5iRlU_QPg3ABICo7dl4zomFpMHlPFZqmjkpWoUIoGhJp_92YsbDUicsaAlrAEALw_wcB")
    title = page.title()

    assert title == "Profesionální péče o Vaše zdraví a krásu"