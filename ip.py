import requests
import re
 
html_text = requests.get("https://ip.cn/").text
#正则匹配
ip_text = re.search(u"<span>Your IP</span>: (.*?)</span>", html_text)
print (ip_text.group(1))
