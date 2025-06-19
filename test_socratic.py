import pytest
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

# Khởi tạo driver Appium
@pytest.fixture
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "emulator-5554"  # thay bằng device thật nếu dùng điện thoại
    options.app_package = "com.google.socratic"
    options.app_activity = "com.google.socratic.home.HomeActivity"
    options.no_reset = True

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# Test Case 1: Kiểm tra nút "Get Started"
def test_sign_in_button(driver):
    button = driver.find_element(AppiumBy.ID, "com.google.socratic:id/get_started_button")
    assert button.is_displayed()
    button.screenshot("screenshots/test1_signin.png")

# Test Case 2: Mở camera sau khi bấm nút
def test_open_camera(driver):
    driver.find_element(AppiumBy.ID, "com.google.socratic:id/get_started_button").click()
    time.sleep(3)
    driver.save_screenshot("screenshots/test2_camera.png")

# Test Case 3: Bấm nút chuyển qua tìm bằng giọng nói
def test_switch_to_voice(driver):
    driver.find_element(AppiumBy.ID, "com.google.socratic:id/mic_button").click()
    time.sleep(2)
    driver.save_screenshot("screenshots/test3_voice.png")
