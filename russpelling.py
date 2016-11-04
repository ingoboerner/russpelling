import re

def replace_letters(inputtext):
    # Replace Іі Ѣѣ Ѳѳ Ѵѵ
    oldstring = "ІіѢѣѲѳѴѵ"
    newstring = "ИиЕеФфИи"
    translationtable = str.maketrans(oldstring, newstring)
    return inputtext.translate(translationtable)

    
def eja(inputtext):    
    # jeja|ея|ЕЯ
    eja = re.sub(r'\bЕЯ\b', 'ЕЕ', re.sub(r'\bея\b', 'ее', re.sub(r'\bЕя\b', 'Ее' ,inputtext)))
    return eja
    
    
def tverdyj(inputtext):
    # Final tverdyj znak
    tverdyj = re.sub(r'\B[ъЪ]\b', '', inputtext)
    return tverdyj
    

def prefixZ(inputtext):
    # prefixes before z
    prefixZ = re.sub(r'\b(БЕ|В|ВО|И|НИ|РА|РО|ЧЕРЕ|ЧРЕ)З([ПФТСКЦШЩЧ])', r'\1с\2', \
                            re.sub(r'\b(Бе|В|Во|И|Ни|Ра|Ро|Чере|Чре)з([пфтскцшщч])', r'\1с\2' ,\
                            re.sub(r'\b(бе|в|во|и|ни|ра|ро|чере|чре)з([пфтскцшщч])', r'\1с\2', inputtext)))
    return prefixZ
    
def ago(inputtext):
    exceptions = ('благо', 'всеблаго', 'наго', 'полунаго', 'преблаго')
    if re.search(r'[яа]го\b', inputtext, re.IGNORECASE) and inputtext not in exceptions:
        if re.search(r'аго\b', inputtext):
            return re.sub(r'аго\b', 'ого', inputtext)
        elif re.search(r'яго\b', inputtext):
            return re.sub(r'яго\b', 'его', inputtext)
        elif re.search(r'АГО\b', inputtext):
            return re.sub(r'АГО\b', 'ОГО', inputtext)
        else: 
            return re.sub(r'ЯГО\b', 'ЕГО', inputtext)
    else:
        return inputtext
        
def ei(inputtext):
    if re.search('іэ', inputtext, re.IGNORECASE):
        if re.search('іэ', inputtext):
            return re.sub('іэ', 'ие', inputtext)
        else:
            return re.sub('ІЭ', 'ИЕ', inputtext) 
    else:
        return inputtext    
        

def normalize(inputtext):
    return ago(prefixZ(tverdyj(eja(replace_letters(re.sub("\s+$","", ei(inputtext)))))))
    
    
def create_token(inputtext):
    return {'t':inputtext, 'n':normalize(inputtext)}

