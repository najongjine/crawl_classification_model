import os
from Craw_image_naver import get_naver
from Craw_image_google import get_google
keywords=None
searchKeywords=None
cnt_count=None
search_datas=None
save_directory=""
while True:
   keywords = None
   searchKeywords = None
   cnt_count = None
   search_datas=None
   save_directory = input("검색후 저장할 디렉터리 이름을 드라이브명과 함께 적어주세요\n"
                          "ex) D:\\svimg\n")
   save_directory = r"{}".format(save_directory)
   searchKeyword_input = input("구글 및 네이버에서 이미지 검색할 한글 단어를 입력하세요(여러입력시 콤마로 구분)\n")
   keyword_input = input("정답으로 사용할 영문 이름(검색단어와 동일 형태로 콤마로 구분)\n")
   cnt_count = int(input("다운로드 받을 대략적인 수량을 입력하세요\n"))
   searchKeywords = searchKeyword_input.split(",")
   keywords = keyword_input.split(",")
   cnt_count=int(cnt_count*1.8)
   if not save_directory:
      print("저장할 디렉터리 이름을 반드시 적어주세요")
      continue
   try:
      if not os.path.exists(save_directory):
         os.mkdir(save_directory)
   except:
      print("디렉터리명이 잘못되었습니다. 다시 한번 작성해주세요")
   if len(searchKeywords)!=len(keywords):
       print("정답파일과 검색단어 수량이 일치하지 않습니다. 다시 입력해주세요")
   else : break
search_datas=zip(searchKeywords,keywords)
get_google(search_datas,save_directory,cnt_count)
search_datas=zip(searchKeywords,keywords)
get_naver(search_datas,save_directory,cnt_count)