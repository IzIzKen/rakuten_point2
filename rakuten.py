from selenium import webdriver
from selenium.webdriver.chrome import service as fs
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# chromeDriverの設定
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_argument('--window-size=1370,1000')
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

for url in urls:
    driver.get(url)
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
            time.sleep(20)

    except:
        import traceback

        traceback.print_exc()
        pass

driver.close()
driver.quit()
