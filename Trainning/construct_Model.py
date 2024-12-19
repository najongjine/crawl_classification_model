import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import random
import os
from tensorflow.keras import Sequential,Input
from tensorflow.keras.layers import Dense,Conv2D,Dropout,MaxPool2D,Flatten
from seaborn import heatmap
from sklearn.metrics import confusion_matrix,classification_report
from Preprocessing.util import saveConfig
# image confirm
def train_fit_run(train_count,label_list,x_train,y_train,x_test,y_test):
    rlist = [ random.randint(0,len(x_train)) for i in range(10)]
    print(rlist)
    curpath = os.path.dirname(os.path.abspath(__file__))  # 프로젝트 루트 경로 페치
    path_list = curpath.split("\\")[:-1]
    rootpath = "\\".join(path_list)
    saveConfig(label_list,rootpath)
    for ix,xnum in enumerate(rlist):
        plt.subplot(2,5,ix+1)
        plt.imshow(x_train[ix])
        plt.title(label_list[np.argmax(y_train[ix])])
        plt.xticks([]);plt.yticks([])
    plt.show()

    model = Sequential()
    model.add(Input(shape=(64,64,3)))
    model.add(Conv2D(
        filters=64,kernel_size=5,strides=2,padding="same",activation="relu"))
    model.add(MaxPool2D(3,2))
    model.add(Dropout(0.2))
    model.add(Conv2D(
        filters=128,kernel_size=5,strides=1,padding="same",activation="relu"))
    model.add(MaxPool2D(3,2))
    model.add(Dropout(0.2))
    model.add(Conv2D(
        filters=256,kernel_size=5,strides=1,padding="same",activation="relu"))
    model.add(MaxPool2D(3,2))
    model.add(Dropout(0.2))
    model.add(Flatten())
    model.add(Dropout(0.3))
    model.add(Dense(256,activation="relu"))
    model.add(Dropout(0.3))
    model.add(Dense(128,activation="relu"))
    model.add(Dropout(0.3))
    model.add(Dense(32,activation="relu"))
    model.add(Dropout(0.3))
    model.add(Dense(10,activation="softmax"))
    model.summary()
    model.compile(loss="categorical_crossentropy",optimizer="adam",
                  metrics=["acc"])
    cb = tf.keras.callbacks.EarlyStopping(
        monitor='val_acc',
        patience=30,
        verbose=1,
        mode='auto',
        restore_best_weights=True,
    )
    fit_his = model.fit(x_train,y_train,epochs=train_count,validation_data=(x_test,y_test),
                        callbacks=[cb],batch_size=100)
    import pickle
    with open("../classification_image.history", "wb") as fp:
        pickle.dump(fit_his,fp)
    model.save("classification_image.keras")
    input("훈련이 종료되었습니다. 모델과 결과를 저장하였으며,\n"
          "엔터키를 누르면 손실도와 정확률을 평가합니다.")
    losses, acces = model.evaluate(x_test, y_test)
    print("손실도:", losses, " 정확률:", "{:.2f}".format(acces * 100), "%")
    input("엔터키를 누르면 훈련 결과 손실도와 정확도 그래프를 시각화 합니다.")
    plt.subplot(1, 2, 1)
    plt.plot(fit_his.history["acc"], label="Train Acc")
    plt.plot(fit_his.history["val_acc"], label="Valid Acc")
    plt.legend()
    plt.title("ACCURACY")
    plt.subplot(1, 2, 2)
    plt.plot(fit_his.history["loss"], label="Train Loss")
    plt.plot(fit_his.history["val_loss"], label="Valid Loss")
    plt.legend()
    plt.title("LOSSES")
    plt.show()
    input("시각화 창을 닫고 엔터키를 누르면 테스트 파일 예측을 시각화 합니다.")
    y_pred = model.predict(x_test)
    rindex = [random.randint(0, len(x_test)) for ix in range(10)]
    for i in range(len(rindex)):
        plt.subplot(2, 5, i + 1)
        plt.imshow(x_test[rindex[i]])
        plt.title(f"true:{label_list[np.argmax(y_test[rindex[i]])]}")
        plt.xlabel(f"predict : {label_list[np.argmax(y_pred[rindex[i]])]}")
        plt.xticks([]);
        plt.yticks([])
    plt.show()
    input("엔터키를 누르면 혼동행렬을 작성하여 시각화 합니다.")
    # 혼동행렬
    y_conv_true = np.array([label_list[np.argmax(ll)] for ll in y_test])
    y_conv_pred = np.array([label_list[np.argmax(ll)] for ll in y_pred])
    # confusion_matrix()
    print(len(label_list))
    print(label_list)
    cm = confusion_matrix(y_conv_true, y_conv_pred)
    print(cm)
    heatmap(cm, cmap="Blues", annot=True, fmt=".1f", xticklabels=label_list, yticklabels=label_list)
    plt.show()
    input("창을 닫고 엔터를 입력하시면 최종 훈련결과 리포트를 출력합니다.")
    print(classification_report(y_conv_true,y_conv_pred))

#







