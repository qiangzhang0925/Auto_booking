from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import ddddocr
import time

def Login(username, password):
    chrome_options = webdriver.ChromeOptions()
    service = Service(executable_path=r"C:/Users/qiangzhang/Desktop/chromedriver.exe")
    # 使用headless无界面浏览器模式
    # chrome_options.add_argument('--headless')  # 增加无界面选项
    chrome_options.add_argument('--disable-gpu')  # 如果不加这个选项，有时定位会出现问题

    # 启动浏览器，获取网页源代码
    browser = webdriver.Chrome(service=service,options=chrome_options)
    browser.implicitly_wait(30)

    try:
        mainUrl = "https://newids.seu.edu.cn/authserver/login"
        browser.get(mainUrl)

        # 登陆
        username_input = browser.find_element(by=By.ID, value="username")
        password_input = browser.find_element(by=By.ID,value="password")
        submit_button = browser.find_element(by=By.XPATH,value="//*[@id=\"casLoginForm\"]/p[5]/button")

        username_input.send_keys(username)
        password_input.send_keys(password)

        submit_button.click()
        # 截图
        browser.get_screenshot_as_file("login.png")

        ## 预约
        browser.get("http://yuyue.seu.edu.cn/eduplus/order/initOrderIndex.do?sclId=1")
        WebDriverWait(browser, 1).until(EC.visibility_of_element_located((By.CLASS_NAME, 'time-line-wrap')))

        # 找到第三天
        browser.find_element(by=By.XPATH,value="//*[@id=\"container\"]/div/div/table/tbody/tr/td[1]/ul/li[3]/a").click()
        # li[1]是乒乓球，li[4]是羽毛球
        browser.find_element(by=By.XPATH,value="//*[@id=\"container\"]/div/div/table/tbody/tr/td[2]/div[1]/ul/li[1]/input").click()
        time.sleep(0.5)
        browser.find_element(by=By.XPATH,value="//*[@id=\"orderInfo\"]/div[1]/div[1]/div[4]/a").click()
        frame = browser.find_element(by=By.TAG_NAME,value="iframe")
        browser.switch_to.frame(frame)

        # 截图
        browser.get_screenshot_as_file("booking_iframe.png")

        # 手机号码
        browser.find_element(by=By.XPATH,value="//*[@id=\"phone\"]").send_keys("")
        # 验证码
        validateimg = browser.find_element(by=By.XPATH,value="//*[@id=\"fm\"]/table/tbody/tr[6]/td[2]/img")
        
        # ocr
        ocr = ddddocr.DdddOcr()
        # screenshot_as_png属性可直接进行OCR识别
        validcode = ocr.classification(validateimg.screenshot_as_png)
        print(validcode)
        browser.find_element(by=By.XPATH,value="//*[@id=\"validateCode\"]").send_keys(validcode)
        browser.find_element(by=By.ID,value="do-submit").click()
    except:
        print("booking failed")
    finally:
        time.sleep(5)
        browser.quit()


if __name__ == "__main__":
    Login("","")