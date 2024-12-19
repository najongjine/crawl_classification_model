import pickle

import tensorflow as tf
import numpy as np
import cv2 as cv
import os

def getTrainData(dpath):
    label_list, y_data, x_data = load_directory_sub(dpath)
    # suffle
    from sklearn.model_selection import train_test_split  # pycharm version 3.11
    x_train, x_test, y_train, y_test = train_test_split(
        x_data, y_data, test_size=0.2, random_state=10, stratify=y_data)
    x_train = x_train/255.;x_test = x_test/255.
    y_train = tf.one_hot(y_train,10)
    y_test = tf.one_hot(y_test, 10)
    print("훈련파일:",x_train.shape)
    print("테스트파일:",x_test.shape)
    print("훈련정답:",y_train.shape)
    print("테스트정답:",y_test.shape)
    print("훈련파일 80% 테스트 파일 20% 를 suffle 후 분할이 완료 되었습니다.")
    return {"label_list":label_list,"train":(x_train,y_train),
            "test":(x_test,y_test)}

def getPred_Preprocess(target_img):#샘플데이터 전처리
    target_img = cv.cvtColor(target_img, cv.COLOR_BGR2RGB)
    target_img = cv.resize(target_img, (64, 64))
    target_img = target_img/255.
    return target_img

def imageAugment_sub(orimg): #이미지 증강
    rn = np.random.randint(2,6)
    rn = round(rn/10,1)
    testimge1 = tf.image.random_brightness(orimg, rn)
    # testimge1=tf.image.random_crop(testimge1, size=(150,150,3))
    # testimge1 = tf.image.resize(
    #     testimge1,size=(256,256),method="nearest",preserve_aspect_ratio=True)

    # testimge1=tf.image.random_flip_left_right(testimge1)
    # testimge1=tf.image.random_flip_up_down(testimge1)
    pre_model=tf.keras.layers.RandomRotation((-0.2,0.3))#레이어 출력을 다시 정수로 변환
    testimge1 = pre_model(testimge1)
    pre_model=tf.keras.layers.RandomFlip(mode="HORIZONTAL_AND_VERTICAL")
    testimge1 = pre_model(testimge1)
    pre_model=tf.keras.layers.RandomZoom((-0.15,0.15),(-0.15,0.15))
    testimge1 = pre_model(testimge1)
    return np.array(testimge1).astype(np.uint8)

def readImageDirect(rpath,get_count):
    cnt = 0
    f_lists = os.listdir(rpath)
    for folder in f_lists:
        f_names = os.listdir(rpath + "\\" + folder)
        print(folder, ":", end="")
        for f_name in f_names:
            ori_img = cv.imread(rpath + "\\" + folder + "\\" + f_name)
            ori_img = cv.resize(ori_img, (256, 256))
            for ix in range(get_count):
                arg_img = imageAugment_sub(ori_img)
                cv.imwrite(rpath + "\\" + folder + "\\" + str(cnt)+f_name, arg_img)
                cnt+=1
            print(".", end="")
        print()

def load_directory_sub(rootpath):#{label:[이미지 리스트]}
    f_lists = os.listdir(rootpath)
    print(f_lists)
    y_labels = []
    x_files = []
    for label,fpath in enumerate(f_lists):
        print(".", end="")
        f_name = r"{}\{}".format(rootpath,fpath)
        f_names = os.listdir(f_name)
        #print(f_names)
        for p in f_names:
            y_labels.append(label)
            fimg = cv.imread(r"{}\{}".format(f_name, p))
            fimg = cv.cvtColor(fimg,cv.COLOR_BGR2RGB)
            fimg = cv.resize(fimg,(64,64))
            x_files.append(fimg)
    return f_lists,np.array(y_labels),np.array(x_files)
def saveConfig(label_list,rootpath):#레이블 리스트 저장
    with open(f"{rootpath}\\config","wb") as fp:
        pickle.dump(label_list,fp)

if __name__=="__main__":
    print("preprocessing_running 파일을 실행하세요")