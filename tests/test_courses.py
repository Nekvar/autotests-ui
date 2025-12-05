import pytest
from playwright.sync_api import Playwright, Page, expect


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state):
    # Переходим на страницу "Courses"
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверяем наличие и текст заголовка "Courses"
    courses_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_title).to_have_text('Courses')

    # Проверяем наличие и текст блока "There is no results"
    resultsText = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(resultsText).to_have_text('There is no results')

    # Проверяем наличие и видимость иконки пустого блока
    icon_view = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(icon_view).to_be_visible()

    # Проверяем наличие и текст описания блока: "Results from the load test pipeline will be displayed here"
    block_description_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(block_description_text).to_have_text('Results from the load test pipeline will be displayed here')
