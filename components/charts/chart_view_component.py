from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class ChartViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier: str, chart_type: str):
        super().__init__(page)

        self.title = page.get_by_test_id(f'{identifier}-widget-title-text')
        self.chart = page.get_by_test_id(f'{identifier}-{chart_type}-chart')

    def check_visible_students_chart(self):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text('Students')
        expect(self.chart).to_be_visible()

    def check_visible_courses_chart(self):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text('Courses')
        expect(self.chart).to_be_visible()

    def check_visible_activities_chart(self):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text('Activities')
        expect(self.chart).to_be_visible()

    def check_visible_scores_chart(self):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text('Scores')
        expect(self.chart).to_be_visible()


