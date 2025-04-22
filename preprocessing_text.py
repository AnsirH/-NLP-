import re
def clean_special_characters(text):
  ''' 특수문자 제거 '''
  text = re.sub(r'[^ㄱ-ㅎ가-힣\s]', '', text)
  text = re.sub(r'\n|\r\n', '', text)
  return text
