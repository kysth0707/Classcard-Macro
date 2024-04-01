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


jsScript = """
var output = "";
$('#tab_set_section .flip-card-front .btn-favor i.cc2.star').closest('.flip-card').each(function() {
    var item = $(this).clone();
    var txt = item[0]["outerText"].replaceAll(' ','').replaceAll('\n','');
    txt = txt.substr(0,txt.length/2);

    
    output = output + txt;
});
"""



# 시작
driver = webdriver.Chrome('chromedriver.exe')

driver.implicitly_wait(10)
# driver.maximize_window()
driver.get("https://www.classcard.net/ClassMain/956015")
wait(100)


# 로그인
pasteString(ID)
tab()
pasteString(PW)
tab()
tab()
enter()

wait(1)



# 크롤링 ㄱㄱ
driver.get('https://www.classcard.net/set/4520841/1257210')
wait(0.2)

result = driver.execute_script(jsScript)
print(result)


driver.quit()

