# -*- coding: utf-8 -*-
"""iris.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1g-n7ce9zGUvbb4UdRzq8RLKVE-6Hx06h
"""

# Commented out IPython magic to ensure Python compatibility.
#Импортируем нужные библиотеки:

import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn import linear_model
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn import metrics
from pandas import DataFrame
# %pylab inline

# Загружаем набор данных Ирисы:
iris = datasets.load_iris()

iris_frame = DataFrame(iris.data)
# Делаем имена колонок такие же, как имена переменных:
iris_frame.columns = iris.feature_names
# Добавляем столбец с целевой переменной:
iris_frame['target'] = iris.target
# Для наглядности добавляем столбец с сортами:
iris_frame['name'] = iris_frame.target.apply(lambda x : iris.target_names[x])
#iris_frame.target.value_counts()

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import os.path
train_X, test_X_0, train_Y, test_Y_0 = train_test_split(iris_frame[['sepal length (cm)','sepal width (cm)','petal length (cm)','petal width (cm)']], iris_frame['target'], test_size = 0.1, random_state = 0)
clf = LogisticRegression(random_state=0).fit(train_X, train_Y)
if os.path.exists("test_X.csv") != True :
  print(clf.predict(test_X_0))
else :
  print(clf.predict(pd.read_csv("test_X.csv", sep=';')))

