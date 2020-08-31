# 모델 학습 과정 표시하기

#
# filename : check_overfitting_graph.py
# history
# =============================
# 20200823 v.1.0 초안 작성 (안지민)
# =============================
# Ver 1.0

import matplotlib.pyplot as plt

fig, loss_ax = plt.subplots()

acc_ax = loss_ax.twinx()

print(hist.history) #버전마다 hist에 저장되어 있는 acc/ accuracy 이름이 다를 수 있으므로 체크 후 그래프 그리기

loss_ax.plot(hist.history['loss'], 'y', label='train loss')
loss_ax.plot(hist.history['val_loss'], 'r', label='val loss')

acc_ax.plot(hist.history['accuracy'], 'b', label='train acc')
acc_ax.plot(hist.history['val_accuracy'], 'g', label='val acc')

loss_ax.set_xlabel('epoch')
loss_ax.set_ylabel('loss')
acc_ax.set_ylabel('accuray')

loss_ax.legend(loc='upper left')
acc_ax.legend(loc='lower left')

plt.show() 
