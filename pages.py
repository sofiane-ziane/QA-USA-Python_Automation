import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helpers import retrieve_phone_code

class UrbanRoutesPage:
    FROM_LOCATOR = (By.ID, 'from')
    TO_LOCATOR = (By.ID, 'to')
    CALL_TAXI_BUTTON = (By.XPATH, '//button[text()="Call a taxi"]')
    SUPPORTIVE_PLAN_SELECTION = (By.XPATH, '//div[text()="Supportive"]')
    SUPPORTIVE_PLAN_SELECTION_PARENT = (By.XPATH, '//div[text()="Supportive"]/..')
    PHONE_NUMBER_CLICK_LOCATOR =  (By.XPATH, '//div[text()="Phone number"]')
    PHONE_NUMBER_ENTER_LOCATOR = (By.NAME, "phone")
    NEXT_BUTTON_LOCATOR = (By.XPATH, '//button[text()="Next"]')
    CODE_FROM_SMS_LOCATOR = (By.XPATH, '//input[@placeholder="xxxx"]')
    CONFIRM_CODE_BUTTON = (By.XPATH, '//button[text()="Confirm"]')
    PHONE_CHECK_LOCATOR = (By.XPATH, '//div[@class="np-text"]')

    PAYMENT_METHOD_CLICK_LOCATOR = (By.XPATH, '//div[@class="pp-value-text"]')
    ADD_CARD_CLICK_LOCATOR = (By.XPATH, '//img[@class="pp-plus"]')
    ENTER_CARD_LOCATOR = (By.ID, 'number')
    ENTER_CARD_CODE_LOCATOR = (By.CSS_SELECTOR, '#code.card-input')
    ADD_CARD_TITLE_CLICK_LOCATOR = (By.XPATH, '//div[text()="Adding a card"]')
    LINK_BUTTON_CLICK_LOCATOR = (By.XPATH, '//button[text()="Link"]')
    CLOSE_BUTTON_LOCATOR = (By.XPATH, '(//button[@class="close-button section-close"])[3]')
    COMMENT_TO_DRIVER_LOCATOR = (By.ID, 'comment')
    ADD_BLANKET_LOCATOR = (By.XPATH, '(//div[@class="switch"])[1]')
    ADD_BLANKET_CHECK_LOCATOR = (By.XPATH, '(//input[@class="switch-input"])[1]')
    PLUS_BUTTON_CLICK_LOCATOR = (By.XPATH, '(//div[@class="counter-plus"])[1]')
    ICE_CREAM_COUNT_LOCATOR = (By.XPATH, '(//div[@class="counter-value"])[1]')
    ORDER_BUTTON_CLICK_LOCATOR = (By.XPATH, '//button[@class="smart-button"]')
    CAR_SEARCH_MODAL_LOCATOR = (By.XPATH, '//div[text()="Car search"]')

    def __init__(self, driver):
        self.driver = driver
    def enter_from_location(self, from_text):
        self.driver.find_element(*self.FROM_LOCATOR).send_keys(from_text)
    def enter_to_location(self, to_text):
        self.driver.find_element(*self.TO_LOCATOR).send_keys(to_text)

    def get_from(self):
        return  self.driver.find_element(*self.FROM_LOCATOR).get_property("value")
    def get_to(self):
        return self.driver.find_element(*self.TO_LOCATOR).get_property("value")
    def click_call_taxi_button(self):
        # self.driver.find_element(*self.CALL_TAXI_BUTTON).click()
        WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located(self.CALL_TAXI_BUTTON)).click()
    def click_supportive_plan(self):
        self.driver.find_element(*self.SUPPORTIVE_PLAN_SELECTION).click()
    def get_supportive_plan(self):
        return self.driver.find_element(*self.SUPPORTIVE_PLAN_SELECTION_PARENT).get_attribute("class")
    def phone_number_click(self):
        self.driver.find_element(*self.PHONE_NUMBER_CLICK_LOCATOR).click()
    def phone_number_enter(self, phone_number):
        self.driver.find_element(*self.PHONE_NUMBER_ENTER_LOCATOR).send_keys(phone_number)

    def next_click(self):
        self.driver.find_element(*self.NEXT_BUTTON_LOCATOR).click()
    def code_fill(self):
        code = retrieve_phone_code(self.driver)
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(self.CODE_FROM_SMS_LOCATOR)).send_keys(code)
    def confirm_click(self):
        self.driver.find_element(*self.CONFIRM_CODE_BUTTON).click()
    def phone_number_check(self):
        return self.driver.find_element(*self.PHONE_CHECK_LOCATOR).text

    def payment_method_click(self):
        self.driver.find_element(*self.PAYMENT_METHOD_CLICK_LOCATOR).click()
    def add_card_click(self):
        self.driver.find_element(*self.ADD_CARD_CLICK_LOCATOR).click()
    def enter_card_number(self, card_number):
        self.driver.find_element(*self.ENTER_CARD_LOCATOR).send_keys(card_number)
    def enter_card_code(self, card_code):
        self.driver.find_element(*self.ENTER_CARD_CODE_LOCATOR).send_keys(card_code)
    def add_card_title(self):
        self.driver.find_element(*self.ADD_CARD_TITLE_CLICK_LOCATOR).click()
    def link_button_click(self):
        self.driver.find_element(*self.LINK_BUTTON_CLICK_LOCATOR).click()
    def close_button_click(self):
        self.driver.find_element(*self.CLOSE_BUTTON_LOCATOR).click()
    def payment_method_card_text(self):
        return self.driver.find_element(*self.PAYMENT_METHOD_CLICK_LOCATOR).text
    def enter_message_to_driver(self, comment):
        self.driver.find_element(*self.COMMENT_TO_DRIVER_LOCATOR).send_keys(comment)
    def get_message_to_driver(self):
        return  self.driver.find_element(*self.COMMENT_TO_DRIVER_LOCATOR).get_property("value")
    def add_blanket_click(self):
        self.driver.find_element(*self.ADD_BLANKET_LOCATOR).click()
    def get_blanket_status(self):
        return self.driver.find_element(*self.ADD_BLANKET_CHECK_LOCATOR).get_property('checked')
    def plus_button_click(self, clicks = 2):
        for i in range (clicks):
            self.driver.find_element(*self.PLUS_BUTTON_CLICK_LOCATOR).click()
    def ice_cream_count(self):
        return int(self.driver.find_element(*self.ICE_CREAM_COUNT_LOCATOR).text)
    def order_button_click(self):
        self.driver.find_element(*self.ORDER_BUTTON_CLICK_LOCATOR).click()
    def car_search_modal(self):
        return self.driver.find_element(*self.CAR_SEARCH_MODAL_LOCATOR).is_displayed()
# combined methods
    def set_routes(self, from_text, to_text):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)

    def select_plan(self, from_text, to_text):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)
        self.click_call_taxi_button()
        time.sleep(2)
        self.click_supportive_plan()

    def fill_phone_number(self, from_text, to_text,phone_number):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)
        self.click_call_taxi_button()
        self.phone_number_click()
        self.phone_number_enter(phone_number)
        self.next_click()
        time.sleep(2)
        self.code_fill()
        self.confirm_click()
        time.sleep(2)

    def fill_card(self, from_text, to_text, card_number, card_code):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)
        self.click_call_taxi_button()
        time.sleep(2)
        self.click_supportive_plan()
        self.payment_method_click()
        self.add_card_click()
        self.enter_card_number(card_number)
        self.enter_card_code(card_code)
        self.add_card_title()
        self.link_button_click()
        self.close_button_click()

    def comment_for_driver(self, from_text, to_text, comment_text ):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)
        self.click_call_taxi_button()
        time.sleep(2)
        self.click_supportive_plan()
        self.enter_message_to_driver(comment_text)

    def order_blanket_and_handkerchiefs(self, from_text, to_text):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)
        self.click_call_taxi_button()
        time.sleep(2)
        self.click_supportive_plan()
        self.add_blanket_click()

    def order_2_ice_creams(self, from_text, to_text):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)
        self.click_call_taxi_button()
        time.sleep(2)
        self.click_supportive_plan()
        self.plus_button_click()

    def car_search_model_appears(self, from_text, to_text, phone_number,comment_text):
        self.enter_from_location(from_text)
        self.enter_to_location(to_text)
        self.click_call_taxi_button()
        time.sleep(2)
        self.click_supportive_plan()
        self.phone_number_click()
        self.phone_number_enter(phone_number)
        self.next_click()
        time.sleep(2)
        self.code_fill()
        self.confirm_click()
        time.sleep(2)
        self.enter_message_to_driver(comment_text)
        self.order_button_click()
        time.sleep(5)