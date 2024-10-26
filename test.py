import requests


headers = {
    "Accept": "*/*",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
    "Connection": "keep-alive",
    "Content-Type": "application/json; charset=UTF-8",
    "Origin": "https://prob05.geekgame.pku.edu.cn",
    "Referer": "https://prob05.geekgame.pku.edu.cn/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "cross-site",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0",
    "^sec-ch-ua": "^\\^Microsoft",
    "sec-ch-ua-mobile": "?0",
    "^sec-ch-ua-platform": "^\\^Windows^^^"
}
url = "https://gator.volces.com/list"
data = '^^[^{^\\^events^^:^[^{^\\^event^^:^\\^predefine_pageview^^,^\\^params^^:^\\^^{^^^^title^\\^\\^\\^:^^^^^不^许^复^制^\\^\\^\\^,^^^^url^\\^\\^\\^:^^^^https://prob05.geekgame.pku.edu.cn/hacker^\\^\\^\\^,^^^^url_path^\\^\\^\\^:^^^^/hacker^\\^\\^\\^,^^^^time^\\^\\^\\^:1729334039351,^^^^referrer^\\^\\^\\^:^^^^https://prob05.geekgame.pku.edu.cn/page2^\\^\\^\\^,^^^^^$is_first_time^\\^\\^\\^:^^^^false^\\^\\^\\^,^^^^event_index^\\^\\^\\^:1729334847180^}^^,^\\^local_time_ms^^:1729334039351,^\\^is_bav^^:0,^\\^session_id^^:^\\^444bf6cc-c7a3-4cd2-bf02-e698f75f959d^^^}^],^\\^user^^:^{^\\^user_unique_id^^:^\\^cpj4t6m768j5a4g31690^^,^\\^web_id^^:^\\^7427429838534753035^^^},^\\^header^^:^{^\\^app_id^^:20001731,^\\^app_version^^:^\\^1.1.2^^,^\\^os_name^^:^\\^windows^^,^\\^os_version^^:^\\^10^^,^\\^device_model^^:^\\^Windows'.encode('unicode_escape')
response = requests.post(url, headers=headers, data=data)

print(response.text)
print(response)