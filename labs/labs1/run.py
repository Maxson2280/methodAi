from labs.labs1 import svm
from scipy.io import loadmat
from svm import *
import numpy as np

#task 1
data = loadmat('dataset1.mat')

y = data['y'].astype(np.float64)
X = data['X']

title = 'Исходные данные'
visualize_boundary_linear(X, y, None, title)

# task 2
C = 1
model = svm.svm_train(X, y, C, svm.linear_kernel, 0.001, 20)
svm.visualize_boundary_linear(X, y, model, title='Визуализация гиперплоскости')

#task 3
C = 100

model = svm.svm_train(X, y, C, svm.linear_kernel, 0.001, 20)

svm.visualize_boundary_linear(X, y, model, 'Разделяюшая граница при С = 100')
# task 4

def gaussian_kernel(x1, x2, sigma=1.0):
    return np.exp(-np.sum(np.power(x1 - x2, 2)) / (2 * sigma**2))

svm.contour(1)
svm.contour(3)

#task 5

data = loadmat('dataset2.mat')

y = data['y'].astype(np.float64)
X = data['X']

title = ' Данные из файла dataset2.mat'
visualize_boundary_linear(X, y, None, title)

#task 6
title = 'Результирующая граница на основе гауссова ядра'
C =1.0
sigma =0.1
gaussian = svm.partial(svm.gaussian_kernel, sigma=sigma)
gaussian.__name__ = svm.gaussian_kernel.__name__
model = svm.svm_train(X, y, C, gaussian)
svm.visualize_boundary(X, y, model, title)

#task 7

data = loadmat('dataset3.mat')
X = data['X']
y = data['y'].astype(np.float64)

Xval = data['Xval']
yval = data['yval'].astype(np.float64)

title = 'Обучающая выборка'
visualize_boundary_linear(X, y, None, title)

title = ' Тестовая выборка'
visualize_boundary_linear(Xval, yval, None, title)

# task 8
C =1.0
sigma =0.5
gaussian = svm.partial(svm.gaussian_kernel, sigma=sigma)
gaussian.__name__ = svm.gaussian_kernel.__name__
model = svm.svm_train(X, y, C, gaussian)
svm.visualize_boundary(X, y, model,'Модель при неоптимальных параметрах')

# task 9
best_model = None
best_C = None
best_sigma = None
best_error = float('inf')

for C in [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30]:
    for sigma in [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30]:
        gaussian = svm.partial(svm.gaussian_kernel, sigma=sigma)
        gaussian.__name__ = svm.gaussian_kernel.__name__
        model = svm.svm_train(X, y, C, gaussian)
        ypred = svm.svm_predict(model, Xval)

        error = np.mean(ypred != yval.ravel())

        if error < best_error:
            best_error = error
            best_model = model
            best_C = C
            best_sigma = sigma

print("Наилучшие параметры:")
print(f"C = {best_C}")
print(f"sigma = {best_sigma}")
print(f"Ошибка = {best_error}")


svm.visualize_boundary(X, y, best_model, title='Наилучшая модель (обучающая выборка)')
svm.visualize_boundary(Xval, yval, best_model, title='Наилучшая модель (тестовая выборка)')

