import os
import sys
sys.stdout = open(os.devnull, 'w') # Suppress warnings and output

!python -m spacy download zh_core_web_sm
!pip install pinyin

import spacy
from spacy.lang.zh.examples import sentences
from spacy import displacy

!pip install -U deep_translator
from deep_translator import GoogleTranslator
import pinyin
import pandas as pd
from IPython.core.display import display, HTML

sys.stdout = sys.__stdout__  # Reset the stdout'

nlp = spacy.load("zh_core_web_sm")
doc = nlp("新京报讯（记者 张畅）11月29日，故宫发布消息称，为进一步贯彻落实《中华人民共和国未成年人保护法》，故宫博物院决定在原有6岁以下或身高1.2米以下儿童，以及每周二统一预约的中小学生免费的基础上，试行所有开放日对未成年人免费开放。")

print('Input text:')
print("\t"+doc.text+'\n')
print('Translation:')
translated = GoogleTranslator(source='auto', target='en').translate(doc.text)
print("\t"+translated+'\n')
print("Extracted entites:")
for ent in doc.ents:
    print("\t"+ent.text,  ent.label_, ent.start_char, ent.end_char,)
print("NER")
displacy.render(doc, style="ent", jupyter=True)