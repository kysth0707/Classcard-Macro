# 거의 개당 0.85초에 가능하니까
# 이상적으로 3분에 211 문제 가능
# 따라서 개당 200점 하면 최소 4만점 가능?

# CURL TO BASH
# python

import random
import requests
import time


TID = '24134f486376a10a24600dee60b3c2d494428afe98c2d0628b859e58db43c704'
# console에 tid 입력

# ggk['a']() 치셈 (arr_key 임)
ARR_KEY = ['k', 'l', 'z', 'q', 'n', 'm', 'u', 'h', 'b', 'a', 'y', 'g', 's', 'i', 'p', 'j', 'o', 'w', 'f', 'r', 'x', 't', 'c', 'd', 'e', 'v']

ARR_KEY = "".join(ARR_KEY)

QUESTION_COUNT = 30
QUESTION_SCORE = 100
TIME_PER_QUESTION = 3 * 60 / QUESTION_COUNT

startTime = time.time() - 3 * 60

URL = [
"https://www.classcard.net/Match/save?",
"set_idx=12718409",
]



# 암호화
# alphabets = list("abcdefghijklmnopqrstuvwxyz")
# random.shuffle(alphabets)
# keyData = "".join(alphabets)
keyData = ARR_KEY

valueData = "0123456789abcdefghijklmnopqrstuvwxyz"[:len(keyData)]
encodeDict = {}

print(keyData)

for key, value in zip(keyData, valueData):
	encodeDict[value] = key
	print(value, ':', key)
	URL.append(
		f"&arr_key[]={key}"
	)

def encodeIt(text):
	output = []
	for txt in text:
		d = encodeDict.get(txt)
		output.append(d if d != None else txt)

	return "".join(output)


# 점수 추가

for i in range(QUESTION_COUNT):
	URL.append(f"&arr_score[{i}][t]={encodeIt(str(round(time.time() + i * TIME_PER_QUESTION + random.random() / 5,3)))}")
	URL.append(f"&arr_score[{i}][s]={encodeIt(str(QUESTION_SCORE))}")
	URL.append(f"&arr_score[{i}][m]={encodeIt('1')}")


# Need to add
# &arr_score[0][t]=ixiedidoeh.ses <= str(round(time.time(),3))
# &arr_score[0][s]=e
# &arr_score[0][m]=i
# &arr_score[1][t]=ixiedidoii.ods
# &arr_score[1][s]=de
# &arr_score[1][m]=e

URL.append("&activity=4")
URL.append(f"&tid={TID}")
URL.append("&class_idx=956015")

URL = "".join(URL).replace(' ','').replace('\n','')
print(URL)


# cookies = {
#     'a': '1',
#     's': '1',
#     'u': '1',
#     'u_idx': '1358810',
#     'login_user_type': '2',
#     'login_school_type': '-1',
#     'u_type': '2',
#     'ci_session': '4ee0584e59965ed9fce3cee4fb88162bba3592ad',
# }

# headers = {
#     'Accept': 'application/json, text/javascript, */*; q=0.01',
#     'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
#     'Connection': 'keep-alive',
#     'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
#     # 'Cookie': 'a=1; s=1; u=1; u_idx=1358810; login_user_type=2; login_school_type=-1; u_type=2; ci_session=4ee0584e59965ed9fce3cee4fb88162bba3592ad',
#     'Origin': 'https://www.classcard.net',
#     'Referer': 'https://www.classcard.net/Match/12718409?c=956015&s=1',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'same-origin',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
#     'X-Requested-With': 'XMLHttpRequest',
#     'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
#     'sec-ch-ua-arch': '"x86"',
#     'sec-ch-ua-bitness': '"64"',
#     'sec-ch-ua-full-version': '"122.0.6261.129"',
#     'sec-ch-ua-full-version-list': '"Chromium";v="122.0.6261.129", "Not(A:Brand";v="24.0.0.0", "Google Chrome";v="122.0.6261.129"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-model': '""',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-ch-ua-platform-version': '"10.0.0"',
#     'sec-ch-ua-wow64': '?0',
# }

# response = requests.post(URL)#, cookies=cookies, headers=headers)
# print(response.text)