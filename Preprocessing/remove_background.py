import cv2 as cv
import numpy as np
from rembg import remove # numpy v2.0.2  require module (onnxruntime)
import os
#rpath=r"D:\imgs"
def removeBackgroundFolder(rpath):
    f_lists = os.listdir(rpath)
    #https://github.com/xuebinqin/U-2-Net
    #https://github.com/xuebinqin/DIS
    for folder in f_lists:
        f_names = os.listdir(rpath+"\\"+folder)
        print(folder,":",end="")
        for f_name in f_names:
            ori_img = cv.imread(rpath+"\\"+folder+"\\"+f_name)
            ori_img = cv.resize(ori_img,(256,256))
            #cv.imshow("ori "+f_name,ori_img)
            rmbg_img = remove(ori_img)
            cv.imwrite(rpath+"\\"+folder+"\\"+f_name,rmbg_img)
            # cv.imshow(f_name,rmbg_img)
            # cv.waitKey(0)
            # cv.destroyAllWindows()
            print(".",end="")
        print()
    print("모든 파일의 변경이 완료 되었습니다.")
def singleRemoveBackground(imagePathName):
    ori_img = cv.imread(imagePathName)
    ori_img = cv.resize(ori_img, (256, 256))
    # cv.imshow("ori "+f_name,ori_img)
    rmbg_img = remove(ori_img)
    cv.imwrite(imagePathName,rmbg_img)
    print("배경이미지 제거가 완료 되었습니다.")
if __name__=="__main__":
    print("preprocessing_running 파일을 실행하세요")
else:
    pass # 다른 파일에서 import 시 작동되는 코드
#grabCut

