"""
Tests for new users using Otto
"""
from unittest import skip
from regression.pages.whitelabel.const import (
    PASSWORD,
    PROF_COURSE_ID,
    PROF_COURSE_TITLE,
    PROF_COURSE_PRICE
)
from regression.pages.whitelabel.course_about_page import CourseAboutPage
from regression.pages.whitelabel.course_info_page import CourseInfoPage
from regression.pages.whitelabel.home_page import HomePage
from regression.pages.whitelabel.inactive_account import InactiveAccount
from regression.tests.whitelabel.course_enrollment_test import CourseEnrollmentTest


class TestNewUserOtto(CourseEnrollmentTest):
    """
    Tests for Otto Enrollment for New Users
    """

    def setUp(self):
        """
        Initialize all page objects
        """
        super(TestNewUserOtto, self).setUp()
        self.course_about = CourseAboutPage(self.browser, PROF_COURSE_ID)
        self.course_info = CourseInfoPage(self.browser, PROF_COURSE_ID)
        self.home = HomePage(self.browser)
        self.inactive_account = InactiveAccount(self.browser)
        # Initialize common objects
        self.course_id = PROF_COURSE_ID
        self.course_title = PROF_COURSE_TITLE
        self.course_price = PROF_COURSE_PRICE
        self.total_price = PROF_COURSE_PRICE

    #@skip('disabling temporarily due to an issue with chrome on jenkins')
    def test_01_select_course_and_register(self):
        """
        Scenario: Otto Flow - A new user is able to select a course, register
        and make payment for the course using the credit card
        """
        # Open the home page as a new unregistered used
        self.find_courses.visit()
        # click on the target course to go to it's about page
        self.find_courses.go_to_course_about_page(self.course_about)
        # Verify that course price is correct on course about page
        self.assertEqual(self.course_price, self.course_about.course_price)
        # register for course
        self.course_about.register_using_enrollment_button()
        self.register_user(self.inactive_account)
        # Application should take user to the page where activate account
        # message is displayed
        self.assertTrue(self.inactive_account.is_activation_message_present())
        self.account_activation()
        # Verify course name, course price and total price on basket page
        self.verify_course_name_on_basket()
        self.verify_price_on_basket()
        # Fill out all the billing and payment details and submit the form
        self.otto_payment_using_cyber_source()
        # Application should take user to the receipt page
        # Verify on receipt page that information like course title, course
        # price, total price order date and billing to is displayed correctly
        self.verify_receipt_info()
        self.receipt.go_to_dashboard()
        # Verify that course is added to user dashboard and user can access
        # the course
        self.assertTrue(self.is_course_added_to_dashboard())

    #@skip('disabling temporarily due to an issue with chrome on jenkins')
    def test_02_register_and_select_course(self):
        """
        Scenario: Otto flow - A new user is able to register, select a course
        and make payment for the course using the credit card
        """
        # Go to registration page and register for the course
        self.home.visit()
        self.home.go_to_registration_page()
        self.register_user(self.dashboard)
        # click on the target course to go to it's about page
        self.dashboard.go_to_find_courses_page()
        # find the target course and click on it to go to about page
        self.find_courses.go_to_course_about_page(self.course_about)
        # Verify that course price is correct on course about page
        self.assertEqual(self.course_price, self.course_about.course_price)
        # Verify that clicking on Enroll button takes inactive user to
        # activation page
        self.course_about.go_to_inactive_page()
        # activate the account which should lead user to basket page
        self.account_activation()
        # Verify course name, course price and total price on basket page
        self.verify_course_name_on_basket()
        self.verify_price_on_basket()
        # Fill out all the billing and payment details and submit the form
        self.otto_payment_using_cyber_source()
        # Application should take user to the receipt page
        # Verify on receipt page that information like course title,
        # course price, total price
        # order date and billing to is displayed correctly
        self.verify_receipt_info()
        self.receipt.go_to_dashboard()
        # Verify that course is added to user dashboard and user can access
        # the course
        self.assertTrue(self.is_course_added_to_dashboard())

