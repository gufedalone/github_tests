import allure
from allure_commons.types import Severity
from selene import by, be
from selene.support.shared import browser


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "gufedalone")
@allure.feature("Issues tab")
@allure.story("Check that Issue with specific number is visible on the page")
@allure.link("https://github.com/eroshenkoam/allure-example/issues", name="TestingLambda")
def test_dynamic_steps():
    with allure.step('Open homepage'):
        browser.open('https://github.com')

    with allure.step('Set browser window size'):
        browser.config.driver.set_window_size(width=1920, height=1080)

    with allure.step('Search for repository'):
        browser.element('.header-search-input').click()
        browser.element('.header-search-input').send_keys('eroshenkoam/allure-example')
        browser.element('.header-search-input').submit()

    with allure.step('Follow repository link'):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Open Issue tab'):
        browser.element('#issues-tab').click()

    with allure.step('Issue #76 is visible on page'):
        browser.element(by.partial_text('#76')).should(be.visible)
