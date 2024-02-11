"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser, be
from selene import have


@pytest.mark.parametrize("browser_desktop_mobile", ["1920*1080", "1600*900"], indirect=True)
def test_github_desktop(browser_desktop_mobile):
    browser.open("https://github.com")
    browser.element('.HeaderMenu-link--sign-in').should(be.visible).press_enter()
    browser.element('#login').should(have.text('Sign in to GitHub'))


@pytest.mark.parametrize("browser_desktop_mobile", ["480*853", "414*896"], indirect=True)
def test_github_mobile(browser_desktop_mobile):
    browser.open("https://github.com")
    browser.element('.Button-label.Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').press_enter()
    browser.element('#login').should(have.text('Sign in to GitHub'))