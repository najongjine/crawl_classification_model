
from remove_background import removeBackgroundFolder,singleRemoveBackground
from util import readImageDirect
userSel = input("배경을 제거할 대상을 선택하세요\n"
      "(단일 제거는 1, 여러파일 제거는 다른 키를 눌러주세요, \n"
                "수행하지 않을시 0 키를 입력\n")
if userSel!="0":
    if userSel=="1":# 단일제거
        print("::::::::::::::::::::::::::::")
        imagePathName=input("배경을 제거할 파일 경로와 파일명 확장명까지 입력해주세요\n"
              "ex) d:\\img\\myimg.jpg\n")
        singleRemoveBackground(r"{}".format(imagePathName))
    else :#여러개 제거
        print("::::::::::::::::::::::::::::")
        rpath = input("배경을 제거할 디렉토리 경로루트 경로를 입력해주세요\n"
                      "ex) d:\\imgs  < 해당경로에는 tiger\\mytigimg.jpg 형태로\n"
                      "하위 디렉토리 내에 파일이 존재해야 합니다.\n"
                      "d:\\imgs\\tiger\\mytigimg.jpg\n"
                      "d:\\imgs\\bear\\mybear.jpg\n"
                      "d:\\imgs\\frog\\myfrog01.jpg\n")
        removeBackgroundFolder(r"{}".format(rpath))
while(1):
    userSel = input("이미지 증강 전처리를 수행하나요? 수행하지 않는다면 0키를 눌러주세요\n"
                    "수행 실행시 이전처럼 디렉터리 경로와 증강수량을 콤마로 구분하여 넣어주세요\n")
    if userSel=="0":
        break
    prolist = userSel.split(",")
    if len(prolist)<2:
        print(" 경로와 수량을 콤마로 구분하여 정확히 입력해주세요 ")
        continue
    #해당 경로가 존재하는지, 수량이 숫자로 바뀌는지?
    readImageDirect(r"{}".format(prolist[0]),int(prolist[1]))

# readImageDirect 이미지 증강 호출
#