# pyauto selenium

## ๐ selenium ๋ผ์ด๋ธ๋ฌ๋ฆฌ
์๋ ๋์์ driver ๋ฑ์ ์ด์ฉํ์ฌ ๋์ ์ผ๋ก ์น์ ์ปจํธ๋กค ํ ์ ์๊ฒ ๋ง๋ค์ด์ฃผ๋ ๋ผ์ด๋ธ๋ฌ๋ฆฌ๋ค.
์ค๋น ๋ด์ฉ์ ๋ค์๊ณผ ๊ฐ๋ค.

```
from selenium import webdriver # ์๋ ๋์์ด ๊น๋ ค์์ด์ผํจ.

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome() # ๊ฐ ํฌ๋กฌ์ ๋ง๋ ๋๋ผ์ด๋ฒ๊ฐ ๊น๋ ค์์ด์ผํจ

driver.get("http://www.google.com") # ์ด๊ณ  ์ถ์ ์ฌ์ดํธ
```

<br>

## โ๏ธ ์๋ ๋์ ํ์ด์ง ์ด๊ณ  ์์์ ์ฐพ์๊ฐ์ ๊ฐ ๋ฃ๊ธฐ
```
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("http://www.google.com")

elem = driver.find_element_by_name("") # name ์์๊ฐ q์ธ ๊ฒ์ ์ฐพ๊ธฐ(๊ตฌ๊ธ ๊ฒ์์ฐฝ)


elem.send_keys("์์ด์ ") # elem ๊ฐ์ "์์ด์ "๋ผ๋ ๊ฐ์ ๋ณด๋ด๊ธฐ
elem.send_keys(Keys.RETURN) # ์ํฐ ์๋ ฅ

```

## โ๏ธ ์ด๋ฏธ์ง ์ ์ฅํ๊ธฐ 

```
import urllib.request

driver.find_element_by_css_selector("").click() # css๊ฐ "" ์ธ๊ฒ์ ์ฐพ๊ณ  ๊ทธ๊ฒ์ ํด๋ฆญ ํ๊ธฐ

driver.find_element_by_css_selector("").send_keys("") # css๊ฐ "" ์ธ๊ฒ์ ์ฐพ๊ณ  ๊ฑฐ๊ธฐ์ ""๊ฐ์ ๋ฃ๊ธฐ

imgUrl = driver.find_element_by_css_selector("").get_attribute("src") # css๊ฐ "" ์ธ๊ฒ์์ ์์ฑ src ๊ฐ์ ๋ฐํํ๊ธฐ

urllib.request.urlretrieve(imgUrl, "test.jpg") # ํด๋น ์ด๋ฏธ์ง ์ฃผ์๋ฅผ test.jpg ํ์ผ๋ก ๋ณํ
```

๋ง์ฝ ์ฌ๋ฌ ์ด๋ฏธ์ง๊ฐ ์๋ค๋ฉด elements๋ก ๋ฐ๊ฟ์ ๋ฆฌ์คํธ์ ๋ด๊ณ  for ๋ฌธ์ ๋๋ ค๊ฐ๋ฉด์ ํ๋์ฉ ์ ์ฅํ๋ ๊ฒ์ ํ๋ฉด ๋๋ค. 