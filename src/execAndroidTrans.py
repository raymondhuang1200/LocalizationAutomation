import stringsFormat

languageDic = stringsFormat.supportedLanguagesDisplay()

def execAndroid():
	for lang in languageDic:
		stringsFormat.start("-csvtoxml", languageDic[lang])