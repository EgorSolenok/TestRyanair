"""
This module contains step definitions for cars_search.feature.
It uses Selenium WebDriver for browser interactions
"""

from pytest_bdd import scenarios, given, when, then, parsers

from pages.user_main_page import UserMainPage
from utils.url_storage import PageUrl
from utils.page_builder import PageConstructor

scenarios('../features/cars_search.feature')


@when(parsers.cfparse('I choose "{cars}" tab on "{main}" page'))
def select_tab(browser, cars, main):
    user_main_page = PageConstructor.get_class(main)(browser, browser.current_url)
    user_main_page.go_to_tab(cars)


@when(parsers.cfparse('I input "{location}" on "{cars}" tab'))
def input_destination_location(browser, location, cars):
    cars_page = PageConstructor.get_class(cars)(browser, browser.current_url)
    cars_page.input_location(location)


@when(parsers.cfparse('I select "{pick_up_date}" on "{cars}" tab to pick'))
def input_pickup_date(browser, pick_up_date, cars):
    cars_page = PageConstructor.get_class(cars)(browser, browser.current_url)
    cars_page.select_pickup_date(pick_up_date)


@when(parsers.cfparse('I select "{drop_off_date}" on "{cars}" tab to drop'))
def input_dropoff_date(browser, drop_off_date, cars):
    cars_page = PageConstructor.get_class(cars)(browser, browser.current_url)
    cars_page.select_dropoff_date(drop_off_date)


@when(parsers.cfparse('I choose "{pick_up_time}" on "{cars}" tab to pick'))
def input_pickup_time(browser, pick_up_time, cars):
    cars_page = PageConstructor.get_class(cars)(browser, browser.current_url)
    cars_page.select_pickup_time(pick_up_time)


@when(parsers.cfparse('I choose "{drop_off_time}" on "{cars}" tab to drop'))
def input_dropoff_time(browser, drop_off_time, cars):
    cars_page = PageConstructor.get_class(cars)(browser, browser.current_url)
    cars_page.select_dropoff_time(drop_off_time)
    cars_page.go_search()


@then(parsers.cfparse('I should see car cards in "{location}" on "{search_cars}" page'))
def should_be_correct_location(browser, location, search_cars):
    searh_cars_page = PageConstructor.get_class(search_cars)(browser, browser.current_url)
    searh_cars_page.accept_cookies()
    searh_cars_page.should_be_car_card()
    searh_cars_page.should_be_correct_location(location)


@then(parsers.cfparse(
    'I should see "{pick_up_date}" to "{drop_off_date}" and "{pick_up_time}" to "{drop_off_time}" on "{search_cars}" '
    'page'))
def should_be_correct_values(browser, pick_up_date, drop_off_date, pick_up_time, drop_off_time, search_cars):
    searh_cars_page = PageConstructor.get_class(search_cars)(browser, browser.current_url)
    searh_cars_page.should_be_correct_pick_up_date(pick_up_date)
    searh_cars_page.should_be_correct_drop_off_date(drop_off_date)
    searh_cars_page.should_be_correct_pick_up_time(pick_up_time)
    searh_cars_page.should_be_correct_drop_off_time(drop_off_time)
    searh_cars_page.go_to_main_page()
    user_main_page = UserMainPage(browser, browser.current_url)
    user_main_page.log_out()