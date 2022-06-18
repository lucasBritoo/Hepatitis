import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def main():
  CAMINHO_DATASET_CLEAR = 'hepatitisClear.data'
  CAMINHO_DATASET_NORMAL= 'hepatitisNormal.data'
  NAMES = ['CLASS','AGE','SEX','STEROID','ANTIVIRALS','FATIGUE','MALAISE','ANOREXIA',
          'LIVER BIG','LIVER FIRM','SPLEEN PALPABLE','SPIDERS','ASCITES','VARICES','BILIRUBIN',
          'ALK PHOSPHATE','SGOT','ALBUMIN','PROTIME','HISTOLOGY'] 
  FEATURES = ['AGE','SEX','STEROID','ANTIVIRALS','FATIGUE','MALAISE','ANOREXIA',
          'LIVER BIG','LIVER FIRM','SPLEEN PALPABLE','SPIDERS','ASCITES','VARICES','BILIRUBIN',
          'ALK PHOSPHATE','SGOT','ALBUMIN','PROTIME','HISTOLOGY']
  TARGET = 'CLASS'  

  df = pd.read_csv(CAMINHO_DATASET_CLEAR, # Nome do arquivo com dados
                      names = NAMES)      # Nome das colunas


  # Separating out the features
  x = df.loc[:, FEATURES].values

  # Separating out the target
  y = df.loc[:,[TARGET]].values


  def ShowInformationDataFrame(df, message=""):
      print(message+"\n")
      print(df.info())
      print(df.describe())
      print(df.head(10))
      print("\n") 


  #   # Min-Max normalization
  x_minmax = MinMaxScaler().fit_transform(df)
  normalized2Df = pd.DataFrame(data = x_minmax, columns = NAMES)


  # Salva arquivo normalizado com a técnica Min-Max
  normalized2Df.to_csv(CAMINHO_DATASET_NORMAL, header=False, index=False)

  print(normalized2Df)

if __name__ == "__main__":
    main()
