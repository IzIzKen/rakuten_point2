from selenium import webdriver
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests


def line_send_message(message):
    line_token = '0ixwVQ5yAmnNu7a5wNK73QKyOOiurdmYs9Dg3zpwSHv'

    headers = {
        'Authorization': f'Bearer {line_token}',
    }
    data = {
        'message': f'message: {message}',
    }
    requests.post('https://notify-api.line.me/api/notify', headers=headers, data=data)


# chromeDriverの設定
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('--window-size=1280,1080')
chromeOptions.add_argument('--headless')
chromeDriver = "/app/.chromedriver/bin/chromedriver"
chrome_service = fs.Service(executable_path=chromeDriver)
driver = webdriver.Chrome(service=chrome_service, options=chromeOptions)
wait = WebDriverWait(driver=driver, timeout=60)
# ユーザー情報の設定
USERID = '111420knt@gmail.com'
PASSWORD = '111420knt'

driver.get('https://rakucoin.appspot.com/rakuten/kuji/')
wait.until(EC.presence_of_element_located)
time.sleep(1)

lotteries = driver.find_elements(By.TAG_NAME, 'a')
login_flag = True
outputs = []

urls = []
for lottery in lotteries:
    urls.append(lottery.get_attribute("href"))

line_send_message('楽天くじを開始します')
for url in urls:
    driver.get(url)
    current_url = driver.current_url
    wait.until(EC.presence_of_element_located)
    time.sleep(3)

    if login_flag:
        driver.find_element(By.ID, 'loginInner_u').send_keys(USERID)
        driver.find_element(By.ID, 'loginInner_p').send_keys(PASSWORD)
        driver.find_element(By.CLASS_NAME, 'loginButton').click()
        wait.until(EC.presence_of_element_located)
        time.sleep(3)
        login_flag = False

    try:
        if len(driver.find_elements(By.ID, 'entry')) > 0:
            driver.find_element(By.ID, 'entry').click()
            wait.until(EC.url_changes(current_url))

    except:
        # import traceback
        #
        # traceback.print_exc()
        print(f'error:{url}')
        pass

driver.close()
driver.quit()

line_send_message('楽天くじを終了します')
