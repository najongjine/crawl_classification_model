from Craw_image_naver import get_naver

keywords=None
searchKeywords=None
cnt_count=None
search_datas=None
while True:
   keywords = None
   searchKeywords = None
   cnt_count = None
   search_datas=None
   searchKeyword_input = input("구글에서 이미지 검색할 단어를 입력하세요(여러입력시 콤마로 구분)\n")
   keyword_input = input("정답으로 사용할 영문 이름(검색단어와 동일 형태로 콤마로 구분)\n")
   cnt_count = int(input("다운로드 받을 수량을 입력하세요\n"))
   searchKeywords = searchKeyword_input.split(",")
   keywords = keyword_input.split(",")
   search_datas=zip(searchKeywords,keywords)
   cnt_count=int(cnt_count*1.8)
   if len(searchKeywords)!=len(keywords):
       print("정답파일과 검색단어 수량이 일치하지 않습니다. 다시 입력해주세요")
   else : break

search_datas=zip(searchKeywords,keywords)
get_naver(search_datas,cnt_count)