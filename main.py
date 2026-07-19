from selenium import webdriver
import data
import helpers
from pages import UrbanRoutesPage

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        URL = data.URBAN_ROUTES_URL
        if helpers.is_url_reachable(URL):
            print('Connected to the Urban Routes server')
        else:
            print('Cannot connect to Urban Routes. Check the server is on and still running')

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_routes(data.ADDRESS_FROM, data.ADDRESS_TO)
        actual_from_value = routes_page.get_from()
        expected_from_value = data.ADDRESS_FROM
        assert expected_from_value == actual_from_value

        actual_to_value = routes_page.get_to()
        expected_to_value = data.ADDRESS_TO
        assert expected_to_value == actual_to_value

    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.select_plan(data.ADDRESS_FROM, data.ADDRESS_TO)
        actual_active_selection_value = routes_page.get_supportive_plan()
        expected_active_selection_value = "active"
        assert expected_active_selection_value in actual_active_selection_value, f"Expected '{expected_active_selection_value}', but got '{actual_active_selection_value}'"

    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.fill_phone_number(data.ADDRESS_FROM, data.ADDRESS_TO, data.PHONE_NUMBER)
        actual_phone_number = routes_page.phone_number_check()
        expected_phone_number = data.PHONE_NUMBER
        assert expected_phone_number == actual_phone_number

    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.fill_card(data.ADDRESS_FROM, data.ADDRESS_TO, data.CARD_NUMBER, data.CARD_CODE)
        actual_payment = routes_page.payment_method_card_text()
        expected_payment = "Card"
        assert expected_payment == actual_payment, f"Expected '{expected_payment}', but got '{actual_payment}'"

    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.comment_for_driver(data.ADDRESS_FROM, data.ADDRESS_TO, data.MESSAGE_FOR_DRIVER)
        actual_message = routes_page.get_message_to_driver()
        expected_message = data.MESSAGE_FOR_DRIVER
        assert expected_message == actual_message, f"Expected '{expected_message}', but got '{actual_message}'"
    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.order_blanket_and_handkerchiefs(data.ADDRESS_FROM, data.ADDRESS_TO)
        actual_status = routes_page.get_blanket_status()
        expected_status = True
        assert expected_status == actual_status, f"Expected '{expected_status}', but got '{actual_status}'"
    def test_order_2_ice_creams(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.order_2_ice_creams(data.ADDRESS_FROM, data.ADDRESS_TO)
        actual_ice_cream_count = routes_page.ice_cream_count()
        expected_ice_cream_count = 2
        assert expected_ice_cream_count == actual_ice_cream_count, f"Expected '{expected_ice_cream_count}', but got '{actual_ice_cream_count}'"

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.car_search_model_appears(data.ADDRESS_FROM, data.ADDRESS_TO, data.PHONE_NUMBER, data.MESSAGE_FOR_DRIVER)
        actual_car_search_status = routes_page.car_search_modal()
        expected_car_search_status = True
        assert expected_car_search_status == actual_car_search_status, f"Expected '{expected_car_search_status}', but got '{actual_car_search_status}'"

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()