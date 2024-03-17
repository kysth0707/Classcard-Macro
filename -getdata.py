import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import pyperclip

with open('data.txt', encoding='utf8') as f:
	ID, PW = f.readline().rstrip().split()

# 유용한 함수
def clickByCss(cssText):
	driver.find_element(By.CSS_SELECTOR, cssText).click()
	wait(0.1)

def textByCss(cssText):
	return driver.find_element(By.CSS_SELECTOR, cssText).text

def pasteString(string : str):
	pyperclip.copy(string)
	pyautogui.hotkey('ctrl', 'v')

def wait(t):
	time.sleep(t)

def tab():
	pyautogui.press('tab')

def enter():
	pyautogui.press('enter')


# 시작
driver = webdriver.Chrome('chromedriver.exe')

driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.classcard.net/ClassMain/956015")

# 로그인
pasteString(ID)
tab()
pasteString(PW)
tab()
tab()
enter()

wait(1)

# 데이터 추출
driver.get('https://www.classcard.net/set/12718409/956015')
wait(3)

# 화면 펼치기
clickByCss("#tab_set_section > div.set-main.panel.hpanel.panel-default.panel-collapse > div.panel-heading > div > div.text-right > a.showhide_battle.font-24.pull-right.m-l-md.m-r-sm > i")

japanData = []
koreaData = [ ]
for i in range(10):
	css = f"#tab_set_section > div:nth-child(1) > div.panel-body > div > div:nth-child({i+1}) > div.flip-card-inner > div.flip-card-front > div.card-content > div > div"
	japanData.append(textByCss(css))

	
	css = f"#tab_set_section > div:nth-child(1) > div.panel-body > div > div:nth-child({i+1}) > div.flip-card-inner > div.flip-card-back.bg-white.text-dark > div.card-content > div > div"
	koreaData.append(textByCss(css))

for i in range(4):
	css = f"#tab_set_section > div:nth-child(2) > div.panel-body > div > div:nth-child({i+1}) > div.flip-card-inner > div.flip-card-front > div.card-content > div > div"
	japanData.append(textByCss(css))

	css = f"#tab_set_section > div:nth-child(2) > div.panel-body > div > div:nth-child({i+1}) > div.flip-card-inner > div.flip-card-back.bg-white.text-dark > div.card-content > div > div"
	koreaData.append(textByCss(css))

print(japanData, koreaData)