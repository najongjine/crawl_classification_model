from Preprocessing.util import getTrainData
from construct_Model import train_fit_run
label_list=x_train=x_test=y_train=y_test=None
userSel = input("디렉터리에서 훈련파일을 생성하여 가져오시겠습니까? 종료시 0 키를 입력\n"
                "ex) d:\\imgs 형태로 디렉터리 명을 입력하세요 아래는 디렉터리 구조를 표현합니다.\n"
                "d:\\imgs\\tiger\\mytigimg.jpg\n"
                "d:\\imgs\\bear\\mybear.jpg\n"
                "d:\\imgs\\frog\\myfrog01.jpg\n"
                "tiger,bear,frog 등은 정답파일의 이름 리스트 입니다.\n")
if userSel!="0":
    data_sets = getTrainData(r"{}".format(userSel))
    label_list = data_sets["label_list"]
    x_train,y_train = data_sets["train"]
    x_test, y_test = data_sets["test"]
    print("x_train(",len(x_train),") y_train(",len(y_train),")")
    print("x_test(", len(x_test), ") y_test(", len(y_test), ")")
userSel=input("순차모델을 구성합니다. 훈련회수를 입력하면 \n"
      "최적의 검증데이터 정확도에 맞춰 조기종료됩니다. 취소는 0 키 입력\n"
              "classification_image.history 파일로 훈련과정이 저장되며\n"
              "classification_image.keras 파일로 훈련 모델이 저장됩니다.\n"
              "훈련 횟수를 숫자로 입력하세요\n")
if userSel!="0" and len(x_train)>0 and len(y_train)>0 and len(x_test)>0 and len(y_test)>0:
    input("엔터키를 누르면 10개의 이미지를 확인합니다. 정답과 일치 하는지 확인하세요\n"
          "확인후 창을 닫으면 훈련이 시작됩니다.")
    train_fit_run(int(userSel), label_list, x_train, y_train, x_test, y_test)




