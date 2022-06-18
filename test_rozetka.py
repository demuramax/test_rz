from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class shopping_cart():

    def test_valid_add_to_cart(self):
        baseURL = "https://rozetka.com.ua/"
        driver = webdriver.Chrome(executable_path="/Users/maxmercury/Documents/SeleniumWebdriver/drivers/chromedriver")
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)

        search_field = driver.find_element_by_xpath('//input[@search-input]')
        search_field.send_keys("MD506Z/A")
        print('input text inserted')

        search_button = driver.find_element_by_xpath("//button[contains(@class, 'search-form__submit')]")
        search_button.click()
        time.sleep(2)
        print('search clicked')

        buy_button = driver.find_element_by_xpath("//button[contains(@class, 'buy-button button button--with-icon button--green button--medium ng-star-inserted')]")
        buy_button.click()
        print('buy button clicked')
        time.sleep(2)

        close_popup_btn = driver.find_element_by_xpath("//button[contains(@class, 'modal__close')]")
        close_popup_btn.click
        print('pop-up closed')
        time.sleep(2)

        logo_icon = driver.find_element_by_xpath('//*[@alt="Rozetka Logo"]')
        logo_icon.click()
        print('logo clicked')
        time.sleep(2)

        shopping_cart_btn = driver.find_element_by_xpath("//button[contains(@class, 'header__button--active')]")
        shopping_cart_btn.click()
        print('shopping cart clicked')
        time.sleep(3)
        cart_product = driver.find_element_by_class_name('cart-product ng-star-inserted')
        if cart_product.is_displayed():
            print('The product is added')
        else:
            print('The product is not added')


run_test = shopping_cart()
run_test.test_valid_add_to_cart()






