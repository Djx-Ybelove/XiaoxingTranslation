import requests
import re
import json


class TranslateSprider:
    def __init__(self):
        self.url_home = "https://cn.bing.com/translator" # 必应翻译网页
        self.url_translate = "https://cn.bing.com/ttranslatev3"
        self.token = "" # 必应翻译token
        self.key = 0 # 必应翻译key
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
        }
        self.params = {
            "isVertical": "1",
            "IG": "E6A349F4A916479A91038EF537D8D78B",
            "IID": "translator.5025"
        }   # 设置必应翻译请求参数

    def get_Languages(self): # 获取语言列表
        response = requests.get(self.url_home, headers=self.headers)
        pattern = r'<option aria-label="(.*?)" value="(.*?)">' # 正则匹配语言列表
        languages = re.findall(pattern, response.text)
        languages_dict = {}
        for language in languages:
            languages_dict[language[0]] = language[1]
        with open("languages", 'w', encoding='utf-8') as file:
            json.dump(languages_dict, file, ensure_ascii=False, indent=4) # 保存语言列表为json文件

    def get_TokenKey(self): # 获取必应翻译token和key
        response = requests.get(self.url_home, headers=self.headers)
        index = response.text.find("var params_AbusePreventionHelper = ") + 35 # 进行查找匹配
        token_key = response.text[index: index + 58].lstrip("[").rstrip("]").split(",")
        self.token = token_key[1].split('"')[1] # 获取token
        self.key = token_key[0] # 获取key

    def get_Translate(self, text, fromLang, to): # 获取翻译结果
        data = {
            "fromLang": fromLang, # 翻译源语言
            "to": to, # 翻译目标语言
            "token": self.token,
            "key": f"{self.key}",
            "text": text,
            "tryFetchingGenderDebiasedTranslations": "true"
        }
        response = requests.post(self.url_translate, headers=self.headers, params=self.params, data=data)
        traslated_text = response.json()[0]["translations"][0]["text"]
        return traslated_text


sprider = TranslateSprider()
