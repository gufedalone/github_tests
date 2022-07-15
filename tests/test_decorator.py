import allure
from allure_commons.types import Severity
from selene import by, be
from selene.support.shared import browser


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "gufedalone")
@allure.feature("Issues tab")
@allure.story("Check that Issue with specific number is visible on the page")
@allure.link("https://github.com/eroshenkoam/allure-example/issues", name="TestingDecorator")
def test_decorator_steps():
    open_home_page()
    set_window_size()
    search_repository()
    go_to_repository()
    open_issues_tab()
    issue_76_is_visible()


@allure.step('Open homepage')
def open_home_page():
    browser.open('https://github.com')


@allure.step('Set browser window size')
def set_window_size():
    browser.config.driver.set_window_size(width=1920, height=1080)


@allure.step('Search for repository')
def search_repository():
    browser.element('.header-search-input').click()
    browser.element('.header-search-input').send_keys('eroshenkoam/allure-example')
    browser.element('.header-search-input').submit()


@allure.step('Follow repository link')
def go_to_repository():
    browser.element(by.link_text('eroshenkoam/allure-example')).click()


@allure.step('Open Issue tab')
def open_issues_tab():
    browser.element('#issues-tab').click()


@allure.step('Issue #76 is visible on page')
def issue_76_is_visible():
    browser.element(by.partial_text('#76')).should(be.visible)
