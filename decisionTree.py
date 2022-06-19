from matplotlib import pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.decomposition import PCA
import pandas as pd


def main():
  CAMINHO_DATASET = 'hepatitis.data'
  CAMINHO_DATASET_CLEAR = 'hepatitisClear.data'
  CAMINHO_DATASET_NORMAL= 'hepatitisNormal.data'
  NAMES = ['CLASS','AGE','SEX','STEROID','ANTIVIRALS','FATIGUE','MALAISE','ANOREXIA',
          'LIVER BIG','LIVER FIRM','SPLEEN PALPABLE','SPIDERS','ASCITES','VARICES','BILIRUBIN',
          'ALK PHOSPHATE','SGOT','ALBUMIN','PROTIME','HISTOLOGY'] 

  FEATURES = ['AGE','SEX','STEROID','ANTIVIRALS','FATIGUE','MALAISE','ANOREXIA',
          'LIVER BIG','LIVER FIRM','SPLEEN PALPABLE','SPIDERS','ASCITES','VARICES','BILIRUBIN',
          'ALK PHOSPHATE','SGOT','ALBUMIN','PROTIME','HISTOLOGY']

  TARGET = 'CLASS'

  df = pd.read_csv(CAMINHO_DATASET_CLEAR,   # Nome do arquivo com dados
                names = NAMES)
  iris = df
  # Separating out the features
  X = df.loc[:, FEATURES].values
  print(X.shape)

  # Separating out the target
  y = df.loc[:,[TARGET]].values

  # Standardizing the features
  X = StandardScaler().fit_transform(X)
  normalizedDf = pd.DataFrame(data = X, columns = FEATURES)
  normalizedDf = pd.concat([normalizedDf, df[[TARGET]]], axis = 1)

  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
  print(X_train.shape)
  print(X_test.shape)

  clf = DecisionTreeClassifier(max_leaf_nodes=3)
  clf.fit(X_train, y_train)
  tree.plot_tree(clf)
  plt.show()

  predictions = clf.predict(X_test)
  print(predictions)

  result = clf.score(X_test, y_test)
  print('Acuraccy:')
  print(result)

if name == "main":
  main()
