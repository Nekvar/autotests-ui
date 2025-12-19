import pytest
from pages.login_page import LoginPage


@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize("email, password",
                         [("user.name@gmail.com", "password"), ("user.name@gmail.com", "  "), ("  ", "password")])
# Использование фикстуры 'chromium_page', которая автоматически предоставляет готовую страницу
def test_wrong_email_or_password_authorization(login_page: LoginPage, email: str, password: str):
    login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")
    # Заполняем форму авторизации
    login_page.login_form.check_visible(email='', password='', is_text_fill=False)
    login_page.login_form.fill_login(email=email, password=password)
    login_page.login_form.check_visible(email=email, password=password, is_text_fill=True)
    # Нажимаем кнопку "Login"
    login_page.click_login_button()
    # Проверяем наличие сообщения об ошибке
    login_page.check_visible_wrong_email_or_password_alert()
