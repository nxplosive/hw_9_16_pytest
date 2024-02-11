import pytest

from selene import browser


@pytest.fixture(params=["1920*1080", "1600*900"])
def browser_desktop_size(request):
    [width, height] = request.param.split("*")
    browser.config.window_width = width
    browser.config.window_height = height
    yield browser
    browser.quit()


@pytest.fixture(scope='function', params=["480*853", "414*896"])
def browser_mobile_size(request):
    [width, height] = request.param.split("*")
    browser.config.window_width = width
    browser.config.window_height = height
    yield browser
    browser.quit()


@pytest.fixture(params=["1920*1080", "1600*900", "480*853", "414*896"])
def browser_desktop_mobile(request):
    [width, height] = request.param.split("*")
    browser.config.window_width = width
    browser.config.window_height = height
    yield browser
    browser.quit()