import pytest

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(courses_list_page: CoursesListPage):
    courses_list_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")
    courses_list_page.sidebar.check_visible()
    courses_list_page.navbar.check_visible('username')
    courses_list_page.toolbar_view.check_visible()
    courses_list_page.check_visible_empty_view()


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
    # Проверки на странице Create Course
    create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
    create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
    create_course_page.create_course.check_visible(
        title="",
        estimated_time="",
        description="",
        max_score="0",
        min_score="0",
        is_text_fill=False
    )
    create_course_page.check_visible_exercises_empty_view()
    # Действия по созданию курса
    create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
    create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
    create_course_page.create_course.fill_form(
        title="Playwright",
        estimated_time="2 weeks",
        description="Playwright",
        max_score="100",
        min_score="10"
    )
    create_course_page.create_course.check_visible(
        title="Playwright",
        estimated_time="2 weeks",
        description="Playwright",
        max_score="100",
        min_score="10",
        is_text_fill=True
    )
    # Проверка корректности отображения панели управления и нажатие на кнопку создания задания
    create_course_page.create_course_toolbar_view.check_visible()
    create_course_page.create_course_toolbar_view.click_create_exercise_button()
    # Проверка корректности отображения панели управления и нажатие на кнопку создания курса
    create_course_page.create_course_toolbar.check_visible()
    create_course_page.create_course_toolbar.click_create_course_button()
    # Проверки после редиректа на Courses
    courses_list_page.toolbar_view.check_visible()
    courses_list_page.course_view.check_visible(
        index=0,
        title="Playwright",
        max_score="100",
        min_score="10",
        estimated_time="2 weeks"
    )
