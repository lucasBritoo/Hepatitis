import pandas as pd
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

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


# carrega os dados
def main():
  df = pd.read_csv(CAMINHO_DATASET_CLEAR,   # Nome do arquivo com dados
                names = NAMES)
  X = df
  y = df['CLASS']
  print(df.head())

  # separa em set de treino e teste
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

  regr = LinearRegression()
  regr.fit(X_train, y_train)

  r2_train = regr.score(X_train, y_train)
  r2_test = regr.score(X_test, y_test)
  print('R2 no set de treino: %.2f' % r2_train)
  print('R2 no set de teste: %.2f' % r2_test)

  y_pred = regr.predict(X_test)
  abs_error = mean_absolute_error(y_pred, y_test)
  print('Erro absoluto no set de treino: %.2f' % abs_error)

if __name__ == "__main__":
  main()
