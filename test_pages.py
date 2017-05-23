"""
End to end test for page's visit.
"""
from bok_choy.web_app_test import WebAppTest

from regression.pages.lms.course_page_lms import CourseInfoPageExtended
from regression.tests.helpers.api_clients import LmsLoginApi
from regression.pages.lms.dashboard_lms import DashboardPageExtended
from regression.pages.lms.lms_courseware import CoursewarePageExtended
from regression.pages.lms.instructor_dashboard import InstructorDashboardPageExtended
from regression.pages.lms.course_drupal_page import DemoCourseSelectionPage
from regression.tests.helpers.utils import visit_all


class PagesTest(WebAppTest):
    """
    E2E test that we can visit pages in the Selected Course.
    """

    def setUp(self):

        super(PagesTest, self).setUp()

        # Log in as a student
        login_api = LmsLoginApi()
        login_api.authenticate(self.browser)
        dashboard_page = DashboardPageExtended(self.browser)
        dashboard_page.visit()

    def test_course_pages(self):
        """
        Verifies that user can navigate to LMS Pages
        """

        visit_all([
            clz(self.browser, 'course-v1:ArbiRaees+AR-1000+fall') for clz in
            [CourseInfoPageExtended]
        ])

    def test_lms_courseware(self):
        """
        Verifies the LMS Courseware Page
        """

        visit_all([
            clz(self.browser, 'course-v1:ArbiRaees+AR-1000+fall') for clz in
            [CoursewarePageExtended]
        ])

    def test_instructor_dashboard(self):
        """
        Verifies the LMS Instructor Dashboard Page
        """

        visit_all([
            clz(self.browser, 'course-v1:ArbiRaees+AR-1000+fall') for clz in
            [InstructorDashboardPageExtended]
        ])

    def test_course_selection_page(self):
        """
        Verifies the Demo Course Selection Page
        """

        visit_all([
            clz(self.browser, 'course-v1:ArbiRaees+AR-1000+fall') for clz in
            [CoursewarePageExtended]
        ])
