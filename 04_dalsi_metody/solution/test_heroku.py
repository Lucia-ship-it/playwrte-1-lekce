def test_login(page):
    page.goto("https://the-internet.herokuapp.com/login")
    username = "tomsmith"
    passwd = "SuperSecretPassword"

    username_input = page.locator("#username")
    password_input = page.locator("#password")

    username_input.fill(username)
    password_input.fill(passwd)

    password_input.press("Enter")

    # check url
    assert page.url == "https://the-internet.herokuapp.com/login"

    # check error mesage
    error_msg = page.locator("div.flash.error")
    assert error_msg.is_visible()


def test_hover(page):
    page.goto("https://the-internet.herokuapp.com/hovers")

    user = page.locator(".figure").nth(0)

    user.hover()

    link = user.locator("a")

    link.click()
