import time
import hashlib
from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import pyperclip


# 아이디 비밀번호 가져옴
with open('data.txt', encoding='utf8') as f:
	ID, PW = f.readline().rstrip().split()


# 일본어 한국어 가져옴
japanWords = ['あ', 'い', 'う',     'え', 'お', 'か', 'き', 'く',     'け', 'こ', 'さ', 'し', 'す',     'せ', 'そ']
koreaWords = ['아', '이', '으(우)', '에', '오', '카', '키', '크(쿠)', '케', '코', '사', '시', '스(수)', '세', '소']

hashedData = {
	hashlib.md5(word.encode('utf8')).hexdigest()
	: word
	for word in japanWords
}

answerDict = {
	jap : kor
	for jap, kor in zip(japanWords, koreaWords)
}



# 유용한 함수
def clickByCss(cssText):
	driver.find_element(By.CSS_SELECTOR, cssText).click()

def textByCss(cssText):
	return driver.find_element(By.CSS_SELECTOR, cssText).text

def textByAudioCss(cssText):
	txt = driver.find_element(By.CSS_SELECTOR, cssText).get_attribute('data-src')
	try:
		txt = txt.split('/')[-1][:-4]

		if hashedData.get(txt) != None:
			return hashedData.get(txt)
		else:
			return '??'
	except Exception as e:
		print("asdfasdf", e)
		return '??'



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
# driver.maximize_window()
driver.get("https://www.classcard.net/ClassMain/956015")



# 로그인
pasteString(ID)
tab()
pasteString(PW)
tab()
tab()
enter()

wait(1)



# 매칭 게임
driver.get('https://www.classcard.net/Match/12718409?c=956015&s=1')

# 시작 클릭
clickByCss("#wrapper-learn > div.vertical-mid.center.fill-parent > div.start-opt-body > div > div > div.start-opt-box > div:nth-child(4) > a")

cssJapan = [
	f"#left_card_{i} > div > div.flip-card-front > div > div"
	for i in range(4)
]

cssAudioJapan = [
	f"#left_card_{i} > div > div.flip-card-front > div > a > i"
	for i in range(4)
]

cssKorea = [
	f"#right_card_{i} > div > div > div > div"
	for i in range(4)
]

wait(2.5)

{'あ': '아', 'い': '이', 'う': '으(우)', 'え': '에', 'お': '오', 'か': '카', 'き': '키', 'く': '크(쿠)', 'け': '케', 'こ': '코', 'さ': 
'사', 'し': '시', 'す': '스(수)', 'せ': '세', 'そ': '소'}

while True:
	try:
		askJapanWords = [textByAudioCss(css) for css in cssAudioJapan]
		# for textCss, audioCss in zip(cssJapan, cssAudioJapan):
		# 	d = textByCss(textCss)
		# 	if len(d) == 0:
		# 	askJapanWords.append(textByAudioCss(audioCss))
		# 	else:
		# 		askJapanWords.append(d)

		askKoreaWords = [textByCss(css) for css in cssKorea]

		print(askJapanWords, askKoreaWords)
		exitIt = False
		for i, askJap in enumerate(askJapanWords):
			answer = answerDict.get(askJap)
			if answer != None:
				for j, askKor in enumerate(askKoreaWords):
					if answer == askKor:
						clickByCss(f"#left_card_{i} > div > div.flip-card-front > div > div")
						clickByCss(f"#right_card_{j} > div > div > div > div")

						print(i, j)
						
						exitIt = True
						break
			
			if exitIt:
				break
		print("Passed.")
		wait(0.01)
	except Exception as e:
		print(e)
		wait(0.01)


# while True:
# 	wait(1)