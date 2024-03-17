japanWords = ['あ', 'い', 'う', 'え', 'お', 'か', 'き', 'く', 'け', 'こ', 'さ', 'し', 'す', 'せ', 'そ']
koreaWords = ['아', '이', '으(우)', '에', '오', '카', '키', '크(쿠)', '케', '코', '사', '시', '스(수)', '세', '소']

for jap, kor in zip(japanWords, koreaWords):
	print(f"{jap} : {kor}")