"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""

from selene import browser, have


def test_github_desktop(browser_desktop_size):
    browser.open('https://github.com/')
    browser.element('.HeaderMenu-link--sign-in').press_enter()
    browser.element('#login').should(have.text('Sign in to GitHub'))


def test_github_mobile(browser_mobile_size):
    browser.open('https://github.com/')
    browser.element('.Button-label.Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').press_enter()
    browser.element('#login').should(have.text('Sign in to GitHub'))
