import pandas as pd
import matplotlib.pyplot as plt

def main():
  CAMINHO_DATASET = 'hepatitis.data'
  CAMINHO_DATASET_CLEAR = 'hepatitisClear.data'
  NAMES = ['CLASS','AGE','SEX','STEROID','ANTIVIRALS','FATIGUE','MALAISE','ANOREXIA',
          'LIVER BIG','LIVER FIRM','SPLEEN PALPABLE','SPIDERS','ASCITES','VARICES','BILIRUBIN',
          'ALK PHOSPHATE','SGOT','ALBUMIN','PROTIME','HISTOLOGY'] 
  FEATURES = ['AGE','SEX','STEROID','ANTIVIRALS','FATIGUE','MALAISE','ANOREXIA',
          'LIVER BIG','LIVER FIRM','SPLEEN PALPABLE','SPIDERS','ASCITES','VARICES','BILIRUBIN',
          'ALK PHOSPHATE','SGOT','ALBUMIN','PROTIME','HISTOLOGY']
  TARGET = 'CLASS'  

                            # Faz a leitura do arquivo
  df = pd.read_csv(
        CAMINHO_DATASET,    # Nome do arquivo com dados
        names=NAMES,        # Nome das colunas
        usecols=FEATURES,   # Define as colunas que serão  utilizadas
        na_values="?")      # Define que ? será considerado valores ausentes

  df_class = pd.read_csv(CAMINHO_DATASET, # Nome do arquivo com dados
                          names=NAMES)      # Nome das colunas

  def UpdateMissingValues(df, column, method="mode", number=0):

      # Substituindo valores ausentes por um número
      if method == "number":
          df[column].fillna(number, inplace=True)

      # Substituindo valores ausentes pela mediana
      elif method == "median":
          median = df[column].median()
          df[column].fillna(median, inplace=True)

      # Substituindo valores ausentes pela média
      elif method == "mean":
          mean = df[column].mean()
          df[column].fillna(mean, inplace=True)

      # Substituindo valores ausentes pela moda
      elif method == "mode":
          mode = df[column].mode()[0]
          df[column].fillna(mode, inplace=True)

  columns_missing_value = df.columns[df.isnull().any()]

  for c in columns_missing_value:

      if c == "BILIRUBIN" or c == "SGOT" or c == "ALBUMIN" or c == "ALK PHOSPHATE":
          UpdateMissingValues(df, c, "mean")

      elif c == "PROTIME":
          UpdateMissingValues(df, c, "mean")

      else:
          UpdateMissingValues(df, c, "mode")


  # Concatena o resultado CLASS no dataset já limpo de valores ausentes
  df = pd.concat([df_class[[TARGET]], df], axis=1)

  # Salva arquivo com o tratamento para dados faltantes
  df.to_csv(CAMINHO_DATASET_CLEAR, header=False, index=False)

if __name__ == "__main__":
    main()
