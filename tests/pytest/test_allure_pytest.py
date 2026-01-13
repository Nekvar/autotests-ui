import allure


def test_something():
    with allure.step("Opening browser"):
        ...

    with allure.step("Creating course"):
        ...

    with allure.step("Closing browser"):
        ...


@allure.step("Open browser with title '{title}'")
def create_course(title: str):
    ...


@allure.step("Opening browser")
def open_browser():
    with allure.step("Get browser"):
        with allure.step("Something else"):
            ...

    with allure.step("Start browser"):
        pass


def test_feature():
    test_something()
    create_course(title='Pytest')
    open_browser()