import pytest
from pages.registration_page import RegistrationPage
from pages.dashboard_page import DashboardPage


@pytest.mark.regression
@pytest.mark.registration
def test_successful_registration(registration_page: RegistrationPage, dashboard_page: DashboardPage):
    # Переходим на страницу регистрации
    registration_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Заполняем форму регистрации
    registration_page.fill_registration_form(email='user.name@gmail.com', username='username', password='password')

    # Нажимаем кнопку "REGISTRATION"
    registration_page.click_registration_button()

    # Проверяем видимость и текст заголовка “Dashboard”
    dashboard_page.check_visible_dashboard_title_toolbar()
