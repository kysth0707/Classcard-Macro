# a = 'https://mobile3.classcard.net/uploads/audio/u/gg/ja/20180825/31e55ff7f86aaee740277059a9983d89.mp3'
# print(a.split('/')[-1][:-4])

japanWords = ['あ', 'い', 'う',     'え', 'お', 'か', 'き', 'く',     'け', 'こ', 'さ', 'し', 'す',     'せ', 'そ']
koreaWords = ['아', '이', '으(우)', '에', '오', '카', '키', '크(쿠)', '케', '코', '사', '시', '스(수)', '세', '소']


answerDict = {
	jap : kor
	for jap, kor in zip(japanWords, koreaWords)
}
print(answerDict)