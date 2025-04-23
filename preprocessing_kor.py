import re
import pandas as pd
from konlpy.tag import Okt

def clear_special_characters(text):
  ''' 특수문자 제거 '''
  text = re.sub(r'[^ㄱ-ㅎ가-힣\s]', '', text)
  text = re.sub(r'\n|\r\n', '', text)
  return text

def clear_stopwords(text):
  # 형태소 구분
  okt = Okt()
  okt_tokens = okt.nouns(text)
  
  # 불용어 제거
  url = "https://gist.githubusercontent.com/spikeekips/40eea22ef4a89f629abd87eed535ac6a/raw/4f7a635040442a995568270ac8156448f2d1f0cb/stopwords-ko.txt"
  ko_stopwords = pd.read_csv(url, header=None).values.tolist()
  ko_stopwords = [w for word in ko_stopwords for w in word]

  filtered_tokens = [w for w in okt_tokens if w not in ko_stopwords and len(w) >= 2]
  return " ".join(filtered_tokens)

  
