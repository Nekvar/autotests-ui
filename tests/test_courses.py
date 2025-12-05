import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list():
    with sync_playwright() as playwright:
        # Открываем браузер и создаем контекст
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        # Создание страницы
        page = context.new_page()

        # Переходим на страницу входа
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

        # Заполняем поле Email
        email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        email_input.fill("user.name@gmail.com")

        # Заполняем поле Username
        username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        username_input.fill("username")

        # Заполняем поле Password
        password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        password_input.fill("password")

        # Нажимаем на кнопку Registration
        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        # Сохранение состояния браузера
        context.storage_state(path='browser_courses-state.json')

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        # Указываем файл с сохраненным состоянием
        context = browser.new_context(storage_state='browser_courses-state.json')
        page = context.new_page()

        # Переходим на страницу "Courses"
        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        # Проверяем наличие и текст заголовка "Courses"
        courses_title = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_title).to_have_text('Courses')

        # Проверяем наличие и текст блока "There is no results"
        resultsText = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(resultsText).to_have_text('There is no results')

        # Проверяем наличие и видимость иконки пустого блока
        icon_view = page.get_by_test_id('courses-list-empty-view-icon')
        expect(icon_view).to_be_visible()

        # Проверяем наличие и текст описания блока: "Results from the load test pipeline will be displayed here"
        block_description_text = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(block_description_text).to_have_text('Results from the load test pipeline will be displayed here')
