import stringsFormat

languageDic = stringsFormat.supportedLanguagesDisplay()

def execAndroid():
	for lang in languageDic:
		# print (lang, languageDic[lang])
		if languageDic[lang] != '':
			stringsFormat.start("-csvtoxml", languageDic[lang])