#구글 모듈
import os.path
#사자,호랑이,곰,앵무새,개구리,표범,독수리,코끼리,타조,말
#lion,tiger,bear,parrot,frog,leopard,eagle,elephant,ostrich,horse
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import  ActionChains
import time
from urllib import request,parse
import uuid

def get_google(search_datas,save_directory,cnt_count):
    for searchKeyword,keyword in search_datas:
       searchKeyword =searchKeyword .strip()
       keyword = keyword.strip()
       time.sleep(5)
       """구글 이미지 검색창 열기"""
       driver = webdriver.Chrome()
       driver.get("https://images.google.com/?hl=ko")
       """
| 항목                  | 설명                                                         |
| ------------------- | ---------------------------------------------------------- |
| `driver`            | 크롬 브라우저를 자동으로 조작하는 객체예요 (Selenium이 만든 브라우저)                |
| `find_element(...)` | 웹페이지에서 원하는 요소 하나를 찾는 함수                                    |
| `By.CSS_SELECTOR`   | CSS 선택자를 기준으로 요소를 찾겠다                                      |
| `"[title=검색]"`      | `title="검색"`이라는 속성을 가진 HTML 요소를 찾는다<br>즉, **검색 입력창**을 의미해요 |
| `f_ele`             | 찾은 검색창(input)을 저장하는 변수 (나중에 여기에 키보드 입력을 넣을 수 있음)           |
<input type="text" title="검색" ... />
       """
       f_ele = driver.find_element(By.CSS_SELECTOR,"[title=검색]")
       #print(f_ele.tag_name)
       f_ele.send_keys(searchKeyword)
       f_ele.send_keys(Keys.ENTER)
       """구글 이미지 검색창 열기 END"""
       driver.implicitly_wait(1)
       #구글 이미지는 마우스 오버링 후에 주소가 생성된다.
       # 전체 페이지 로딩
       time.sleep(2)
       driver.fullscreen_window()
       """
| 항목                  | 설명                                                               |
| ------------------- | ---------------------------------------------------------------- |
| `find_element(...)` | 웹페이지에서 특정 요소(HTML 태그)를 하나 찾는 함수                                  |
| `By.CSS_SELECTOR`   | CSS 선택자를 이용해 찾는다                                                 |
| `"#sfooter"`        | `id="sfooter"`인 HTML 요소를 찾겠다는 의미<br>즉, 페이지의 **하단 푸터** 박스를 찾는 거예요 |
| `sfooter`           | 찾은 푸터 요소를 저장하는 변수. 이후에 "끝까지 로딩됐는지" 확인용으로 사용돼요                    |
🤖 이 코드가 왜 필요해?
구글 이미지 검색은 스크롤을 내리면 더 많은 이미지가 계속 로딩돼요 (무한 스크롤).

그런데 끝까지 내리면 더 이상 안 나올 때가 있죠.

이때 푸터 영역이 나타나면, "이제 진짜 끝까지 내려왔다"고 판단할 수 있어요.

그래서 아래 코드에서 이런 조건이 있어요:

if not "none" in sfooter.get_attribute("style"):
    break
→ 이건 푸터가 보이면 스크롤 그만 내리겠다는 뜻이에요.
       """
       sfooter = driver.find_element(By.CSS_SELECTOR,"#sfooter");
       cnt=0

       """이미지 많이 불러오기 (스크롤 내리기)"""
       for i in range(100):
           cnt += 50
           if cnt >= cnt_count:
               break
           ActionChains(driver).send_keys(Keys.END).perform()
           time.sleep(2)
           if not "none" in sfooter.get_attribute("style"):
               break
           """이미지 많이 불러오기 (스크롤 내리기) END"""

       """
구글 이미지 검색 결과에서 **이미지 태그(g-img)**들을 여러 개 찾아서
over_tar라는 리스트에 저장하는 거예요.
| 코드                                  | 설명                                              |
| ----------------------------------- | ----------------------------------------------- |
| `driver.find_elements`              | 웹페이지에서 **여러 개의 요소들**을 한꺼번에 찾는 함수                |
| `By.CSS_SELECTOR`                   | CSS 선택자로 요소를 찾겠다는 의미                            |
| `f"[data-q={searchKeyword}] g-img"` | `data-q="검색어"`를 가진 요소 아래에 있는 `g-img` 태그를 찾는다는 뜻 |
| `over_tar`                          | 이미지 DOM 요소들을 담는 리스트. 마우스를 올릴 때 사용할 대상들          |
<div data-q="lion">
  <div>
    <g-img>
      <img src="..." />
    </g-img>
  </div>
</div>
data-q="lion" → 현재 검색한 단어

그 안에 <g-img> 태그가 들어있어요.

즉, 구글이 검색어에 따라 DOM 구조를 구분지어 놨기 때문에,
그 안에 있는 이미지(g-img)만 정확히 잡으려고 이 조건을 넣은 거예요.
       """
       over_tar = driver.find_elements(By.CSS_SELECTOR,f"[data-q={searchKeyword}] g-img")
       print(f"## over: {over_tar}")
       cnt=0

       """마우스 오버해서 이미지 주소 생성 유도"""
       for target in over_tar:
           if int(cnt*0.5) > cnt_count:
               break
           cnt+=1
           """
마우스를 target 요소 위로 자동으로 올리는 동작을 실행합니다.
즉, 마우스를 해당 이미지 위에 올려주는 행동이에요!
| 코드                         | 설명                                        |
| -------------------------- | ----------------------------------------- |
| `ActionChains(driver)`     | 마우스, 키보드 조작 등 복잡한 동작을 할 수 있는 **액션 체인 도구** |
| `.move_to_element(target)` | `target`이라는 요소(예: 이미지) 위로 마우스를 **이동시킴**   |
| `.perform()`               | 준비한 액션을 **실제로 실행**                        |
이미지들이 처음엔 저화질 썸네일만 보임.
마우스를 올려야만 진짜 원본 이미지 주소가 생성됨.
           """
           ActionChains(driver).move_to_element(target).perform()
           print(".",end="")
           time.sleep(0.3)
           """마우스 오버해서 이미지 주소 생성 유도 END"""
       #a href="/imgres?q=
       print()

       """이미지 주소 수집"""
       """
<div data-q="lion">
  ...
  <a href="/imgres?imgurl=https://example.com/lion.jpg&imgrefurl=...">...</a>
  ...
</div>
data-q="lion" 같은 블록 안에서

<a> 태그인데

href 속성에 imgres라는 글자가 포함된 것 |
       """
       result_url = (
           driver.find_elements(By.CSS_SELECTOR,\
                                f"[data-q={searchKeyword}] a[href*=imgres]"))
       """이미지 주소 수집 END"""
       import re

       """주소에서 진짜 이미지 링크 추출"""
       """ 정규식
       https://www.google.com/imgres?imgurl=https%3A%2F%2Fexample.com%2Flion.jpg&imgrefurl=...
        여기서 우리가 필요한 건 이 부분이죠:
        imgurl=https%3A%2F%2Fexample.com%2Flion.jpg
       """
       pattern = r".*imgurl=(.*)&imgrefurl.*"
       iurls=[]
       """주소에서 진짜 이미지 링크 추출 END"""

       for iurl in result_url:
           """
           https://www.google.com/imgres?imgurl=https%3A%2F%2Fexample.com%2Flion.jpg&imgrefurl=...
            여기서 필요한 부분만 뽑으면:
            https%3A%2F%2Fexample.com%2Flion.jpg
           """
           iurls.append(re.sub(pattern, r"\1", iurl.get_attribute("href")))
       #print(parse.unquote(iurls[0]))  %XX => url 문자를 일반 전환
       save_path = f"{save_directory}/{keyword}"
       if not os.path.exists(save_path):
           os.makedirs(save_path, exist_ok=True)
       icount=0
       for iurl in iurls:
           try:
               # 구글에서 추출한 URL 중에서 이미지 파일만 골라내기     re.findall(...)  →  ['https://example.com/lion.jpg']    [0]을 써서 리스트에서 첫 번째(진짜 주소)만 꺼내는 거예요.
               img_url = (
                   re.findall(r"(.*\.jpg|.*\.JPG|.*\.jpeg|.*\.JPEG|.*\.png|.*\.PNG|.*\.webp|.*\.WEBP)$",iurl))[0]
               img_url = parse.unquote(img_url)
               expandfile = img_url.split(".")[-1]
               ru = "g"+str(uuid.uuid4())
               file_path=ru+"."+expandfile
               """이미지 다운로드 및 저장"""
               datafile = requests.get(img_url)
               time.sleep(0.7)
               #print((datafile.headers["content-length"])) 파일 용량 byte
               if int(datafile.headers["content-length"])<5100:
                   continue
               #request.urlretrieve(img_url,save_path+file_path)
               with open(save_path+"/"+file_path,"wb") as fp:
                   fp.write(datafile.content)
                   icount+=1
                   """이미지 다운로드 및 저장 END"""
               if icount>=cnt_count:
                   break
           except:
               print("err")
       print("구글에서 ",icount," 개의 이미지 저장")
       driver.quit();

if __name__=="__main__":
    search_datas = [
        ("사자", "lion"),
    ]
    save_directory = "c:/myimages"
    cnt_count = 1

    get_google(search_datas=search_datas,save_directory=save_directory,cnt_count=cnt_count)
