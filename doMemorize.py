from favorDatas import datas

def isEn(txt : str) -> str:
	return True if txt in list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") else False

with open('output.txt', encoding='utf8', mode='w') as f:
	spaceLen = 18
	num = 0
	for line in datas.split('\n'):
		if len(line) == 0:
			num += 1
			f.write(f"========== [ {num} ] ==========\n")
			continue

		i = 0
		for x in line:
			if not isEn(x):
				break
			i += 1
		en, kr = line[:i], line[i:]
		f.write(f"{en}{' ' * (spaceLen - len(en))}: {kr}\n")
