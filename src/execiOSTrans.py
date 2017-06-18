import stringsFormat
#from unicodeCsv import UnicodeWriter, UnicodeReader

filePath = './out/infoPlist.strings'

keyIdx, langAry = stringsFormat.supportedLanguages()

def writeFile(desFile, lang, content, keyIdx):
    for row in content:        
        langIdx = langAry.index(lang)
        if row[keyIdx] != "":
            line = "\"%s\"=\"%s\";\n"%(row[keyIdx], row[langIdx])
        desFile.write(line.encode('utf8'))

def createLanguageFile(lang, content, keyIdx):
    langFilePath = '%s.%s' %(filePath, lang)
    langFile = open(langFilePath,'w+')
    writeFile(langFile, lang, content, keyIdx)

    if(langFile):
        langFile.close()

def execiOS():
    content = stringsFormat.readOriginalCsvData()
    for idx, lang in enumerate(langAry):
        if idx == keyIdx or langAry[idx] == '':
            continue
        createLanguageFile(lang, content, keyIdx)    

