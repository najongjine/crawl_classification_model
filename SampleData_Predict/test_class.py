import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from Preprocessing.remove_background import singleRemoveBackground
from Preprocessing.util import getPred_Preprocess
from Preprocessing.util import saveConfig
import pickle
import os
import cv2 as cv
curpath = os.path.dirname(os.path.abspath(__file__))  # 프로젝트 루트 경로 페치
path_list = curpath.split("\\")[:-1]
rootpath = "\\".join(path_list)
with open(f"{rootpath}\\config","rb") as fp:
    label_list  = pickle.load(fp)
print("라벨리스트확인:",label_list)
sample_data = input("라벨리스트가 불러와 졌는지 확인후 \n"
                    "샘플데이터의 파일 경로와 파일명을 지정해주세요\n")
origin_img = cv.imread(sample_data,cv.COLOR_BGR2RGB)
origin_img = cv.resize(origin_img,(128,128))
rembg_img = singleRemoveBackground(r"{}".format(sample_data))
rembg_img = getPred_Preprocess(rembg_img)
rembg_img = np.array([rembg_img])
#D:\frog-7605433_1280.webp
#모델 로딩
model = load_model(f"{rootpath}\\Trainning\\classification_image.keras")
y_pred = model.predict(rembg_img)
plt.imshow(origin_img)
plt.xlabel("pred:"+label_list[np.argmax(y_pred)])
plt.xticks([]);plt.yticks([])
plt.show()







