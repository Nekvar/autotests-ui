from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.exercises_title = page.get_by_test_id('create-course-toolbar-title-text')
        self.create_course_button = page.get_by_test_id('create-course-toolbar-create-course-button')

    def check_visible(self, is_create_course_disabled: bool = True):
        expect(self.exercises_title).to_be_visible()
        expect(self.exercises_title).to_have_text('Create course')
        if is_create_course_disabled:
            expect(self.create_course_button).to_be_enabled()
        else:
            expect(self.create_course_button).to_be_disabled()

    def click_create_course_button(self):
        expect(self.create_course_button).to_be_visible()
        self.create_course_button.click()





