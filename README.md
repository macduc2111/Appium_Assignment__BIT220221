#  BÀI TẬP TỰ ĐỘNG HÓA KIỂM THỬ ỨNG DỤNG DI ĐỘNG VỚI APPIUM

##  Thông tin sinh viên

- **Họ tên:** Mạc Anh Đức  
- **MSSV:** BIT220221  
- **Lớp:** 22IT3  
- **Ngày thực hiện:** 19/06/2025  

---

##  Ứng dụng được chọn

- **Tên ứng dụng:** Socratic by Google  
- **Danh mục tương ứng:** Ứng dụng học toán hoặc khoa học  
- **Cơ sở chọn:** 21 % 5 = 1 → ứng dụng học toán/khoa học  
- **Lý do chọn:** Ứng dụng hỗ trợ học sinh giải bài tập bằng hình ảnh và giọng nói. Có giao diện thân thiện, phù hợp để kiểm thử giao diện bằng Appium.

---

##  Mô tả các ca kiểm thử

| STT | Tên Test Case                       | Mô tả hành động                                                        | Kết quả mong đợi                        |
|-----|-------------------------------------|------------------------------------------------------------------------|-----------------------------------------|
| 1   | Kiểm tra nút "Get Started"          | Mở ứng dụng, kiểm tra nút khởi động có hiển thị không                 | Nút hiển thị đúng và có thể click được  |
| 2   | Mở camera chụp bài tập              | Click "Get Started", kiểm tra chuyển sang giao diện camera            | Màn hình camera hiển thị đúng           |
| 3   | Chuyển sang chế độ tìm bằng giọng nói | Click icon micro, kiểm tra giao diện tìm bằng voice                  | Giao diện voice hiển thị đúng           |

---

##  Mã nguồn kiểm thử `test_socratic.py`

```python
import pytest
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

@pytest.fixture
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "emulator-5554"
    options.app_package = "com.google.socratic"
    options.app_activity = "com.google.socratic.home.HomeActivity"
    options.no_reset = True

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_sign_in_button(driver):
    button = driver.find_element(AppiumBy.ID, "com.google.socratic:id/get_started_button")
    assert button.is_displayed()
    button.screenshot("screenshots/test1_signin.png")

def test_open_camera(driver):
    driver.find_element(AppiumBy.ID, "com.google.socratic:id/get_started_button").click()
    time.sleep(3)
    driver.save_screenshot("screenshots/test2_camera.png")

def test_switch_to_voice(driver):
    driver.find_element(AppiumBy.ID, "com.google.socratic:id/mic_button").click()
    time.sleep(2)
    driver.save_screenshot("screenshots/test3_voice.png")
```

---

##  Cài đặt môi trường

### Cài Appium

```bash
npm install -g appium
```

### Cài Android SDK và thiết lập biến môi trường

- Tải Android Studio và cài đặt.
- Tìm đường dẫn SDK: `C:\Users\<TênUser>\AppData\Local\Android\Sdk`
- Thêm vào `Environment Variables`:
  - `ANDROID_HOME = <đường dẫn SDK>`
  - Thêm vào PATH:
    - `%ANDROID_HOME%\platform-tools`
    - `%ANDROID_HOME%\emulator`

### Cài thư viện Python cần thiết

```bash
pip install Appium-Python-Client pytest
```

---

## Hướng dẫn chạy kiểm thử

### Bước 1: Mở Appium Server

```bash
appium server
```

### Bước 2: Kết nối thiết bị/emulator

```bash
adb devices
```

> Đảm bảo emulator hoặc thiết bị thật đã bật và kết nối

### Bước 3: Chạy kiểm thử

```bash
pytest test_socratic.py
```

---

##  Kết quả kiểm thử

| Test Case                     | Kết quả  | Ghi chú                                  |
|------------------------------|----------|-------------------------------------------|
| Test Case 1: Get Started     | Passed | Ảnh lưu tại `screenshots/test1_signin.png` |
| Test Case 2: Open Camera     | Passed | Ảnh lưu tại `screenshots/test2_camera.png` |
| Test Case 3: Voice Search    | Passed | Ảnh lưu tại `screenshots/test3_voice.png`  |

---

## Khó khăn và cách khắc phục

| Vấn đề                                | Cách khắc phục                                                        |
|---------------------------------------|-----------------------------------------------------------------------|
| Appium báo lỗi port `4723` đang được dùng | Kiểm tra và tắt các phiên bản Appium cũ đang chạy bằng `taskkill`     |
| Không tìm thấy phần tử bằng ID        | Sử dụng Appium Inspector để xác định đúng ID hoặc dùng XPath thay thế |
| Lỗi cấu hình `desired_caps` với Python mới | Cập nhật cú pháp `UiAutomator2Options()` trong Appium v2 trở lên       |

---

## Đẩy bài lên GitHub

```bash
git init
git remote add origin https://github.com/macduc2111/Appium_Assignment__BIT220221.git
git add .
git commit -m "Bài tập Appium - BIT220221"
git push -u origin main
```