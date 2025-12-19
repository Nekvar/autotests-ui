from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.create_course_title = page.get_by_test_id('create-course-form-title-input').locator('input')
        self.estimated_time = (
            page.get_by_test_id('create-course-form-estimated-time-input').locator('input')
        )
        self.description_textarea = (
            # При поиске поля описания будет найдено два тега textarea, берем первый из них
            page.get_by_test_id('create-course-form-description-input').locator('textarea').first
        )
        self.max_score_form = page.get_by_test_id('create-course-form-max-score-input').locator('input')
        self.min_score_form = page.get_by_test_id('create-course-form-min-score-input').locator('input')

    def fill_form(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str
    ):

        self.create_course_title.fill(title)
        expect(self.create_course_title).to_have_value(title)

        self.estimated_time.fill(estimated_time)
        expect(self.estimated_time).to_have_value(estimated_time)

        self.description_textarea.fill(description)
        expect(self.description_textarea).to_have_text(description)

        self.max_score_form.fill(max_score)
        expect(self.max_score_form).to_have_value(max_score)

        self.min_score_form.fill(min_score)
        expect(self.min_score_form).to_have_value(min_score)

    def check_visible(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str,
            is_text_fill: bool = False
    ):
        expect(self.create_course_title).to_be_visible()
        expect(self.estimated_time).to_be_visible()
        expect(self.description_textarea).to_be_visible()
        expect(self.max_score_form).to_be_visible()
        expect(self.min_score_form).to_be_visible()

        if is_text_fill:
            expect(self.create_course_title).to_have_value(title)
            expect(self.estimated_time).to_have_value(estimated_time)
            expect(self.description_textarea).to_have_text(description)
            expect(self.max_score_form).to_have_value(max_score)
            expect(self.min_score_form).to_have_value(min_score)

        if not is_text_fill:
            expect(self.create_course_title).to_have_value('')
            expect(self.estimated_time).to_have_value('')
            expect(self.description_textarea).to_have_text('')
            expect(self.max_score_form).to_have_value('0')
            expect(self.min_score_form).to_have_value('0')
