"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest

from selene import have
from selene import browser


@pytest.fixture(params=["1920*1080", "1600*900", "480*853", "414*896"])
def second_browser(request):
    [width, height] = request.param.split("*")
    browser.config.window_width = width
    browser.config.window_height = height
    if (width, height) in [("480", "853"), ("414", "896")]:
        return 'mobile'
    if (width, height) in [("1920", "1080"), ("1600", "900")]:
        return 'desktop'


def test_github_desktop(second_browser):
    if second_browser == "mobile":
        pytest.skip("размер не подходит для desktop версии")
    browser.open("https://github.com")
    browser.element('.HeaderMenu-link--sign-in').press_enter()
    browser.element('#login').should(have.text('Sign in to GitHub'))


def test_github_mobile(second_browser):
    if second_browser == "desktop":
        pytest.skip("размер не подходит для mobile версии")
    browser.open("https://github.com")
    browser.element('.Button-label.Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').press_enter()
    browser.element('#login').should(have.text('Sign in to GitHub'))
