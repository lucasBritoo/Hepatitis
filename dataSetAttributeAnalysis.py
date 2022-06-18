import pandas as pd
import matplotlib.pyplot as plt

def main():
  CAMINHO_DATASET = 'hepatitis.data'
  NAMES = ['CLASS','AGE','SEX','STEROID','ANTIVIRALS','FATIGUE','MALAISE','ANOREXIA',
          'LIVER BIG','LIVER FIRM','SPLEEN PALPABLE','SPIDERS','ASCITES','VARICES','BILIRUBIN',
          'ALK PHOSPHATE','SGOT','ALBUMIN','PROTIME','HISTOLOGY'] 
          
  FEATURES = ['AGE','SEX','STEROID','ANTIVIRALS','FATIGUE','MALAISE','ANOREXIA',
          'LIVER BIG','LIVER FIRM','SPLEEN PALPABLE','SPIDERS','ASCITES','VARICES','BILIRUBIN',
          'ALK PHOSPHATE','SGOT','ALBUMIN','PROTIME','HISTOLOGY']

  df = pd.read_csv(CAMINHO_DATASET,   # Nome do arquivo com dados
                  names = NAMES,      # Nome das colunas 
                  usecols = FEATURES, # Define as colunas que serão  utilizadas
                  na_values='?')      # Define que ? será considerado valores ausentes

def bilirubinAnalysis():
  bilirubin_y = [0, 0, 0,0 ,0 ]
  bilirubin_x = ['0.3 - 1.84', '1.85 - 3.38', '3.39 - 4.92', '4.93 - 6.46', '6.46 - 8.0']


  for c in df['BILIRUBIN']:

    if c > 0.3 and c <= 1.84:
      bilirubin_y[0] = bilirubin_y[0] + 1

    if c > 1.84 and c <= 3.38:
      bilirubin_y[1] = bilirubin_y[1] + 1

    elif c > 3.38 and c <= 4.92:
      bilirubin_y[2] = bilirubin_y[2] + 1

    elif c > 4.92 and c <= 6.64:
      bilirubin_y[3] = bilirubin_y[3] + 1

    elif c > 6.64 and c <= 8:
      bilirubin_y[4] = bilirubin_y[4] + 1
  plt.figure(figsize=(8,5))

  plt.xlabel('BILIRUBIN')
  plt.ylabel('Quantidade de amostras')


  plt.bar(bilirubin_x, bilirubin_y)
  plt.show()

def alkPhosphateAnalysis():

  alk_y = [0, 0, 0,0 ,0 ]
  alk_x = ['26 - 106.2', '106.3 - 153.4', '153.5 - 200.6', '200.7 - 247.8', '247.8 - 295']


  for c in df['ALK PHOSPHATE']:

    if c > 26 and c <= 106.2:
      alk_y[0] = alk_y[0] + 1

    if c > 106.2 and c <= 153.4:
      alk_y[1] = alk_y[1] + 1

    elif c > 153.4 and c <= 200.6:
      alk_y[2] = alk_y[2] + 1

    elif c > 200.6 and c <= 247.8:
      alk_y[3] = alk_y[3] + 1

    elif c > 247.8 and c <= 295:
      alk_y[4] = alk_y[4] + 1

  plt.figure(figsize=(8,5))

  plt.xlabel('ALK PHOSPHATE')
  plt.ylabel('Quantidade de amostras')

  plt.bar(alk_x, alk_y)
  plt.show() 

def sgotAnalysis():
  sgot_y = [0, 0, 0,0 ,0 ]
  sgot_x = ['14 - 140.8', '140.9 - 267.6', '267.7 - 394.4', '394.5 - 521.2', '521.3 - 648']


  for c in df['SGOT']:

    if c > 14 and c <= 140.8:
      sgot_y[0] = sgot_y[0] + 1

    if c > 140.8 and c <= 267.6:
      sgot_y[1] = sgot_y[1] + 1

    elif c > 267.6 and c <= 394.4:
      sgot_y[2] = sgot_y[2] + 1

    elif c > 394.4 and c <= 521.2:
      sgot_y[3] = sgot_y[3] + 1

    elif c > 521.2 and c <= 648:
      sgot_y[4] = sgot_y[4] + 1

  plt.figure(figsize=(8,5))

  plt.xlabel('SGOT')
  plt.ylabel('Quantidade de amostras')


  plt.bar(sgot_x, sgot_y)
  plt.show()

def albominAnalysis():
  albomin_y = [0, 0, 0,0 ,0 ]
  albomin_x = ['2.1 - 2.96', '2.97 - 3.82', '3.83 - 4.68', '4.69 - 5.54', '5.55 - 6.4']


  for c in df['ALBUMIN']:

    if c > 2.1 and c <= 2.96:
      albomin_y[0] = albomin_y[0] + 1

    if c > 2.96 and c <= 3.82:
      albomin_y[1] = albomin_y[1] + 1

    elif c > 3.82 and c <= 4.68:
      albomin_y[2] = albomin_y[2] + 1

    elif c > 4.68 and c <= 5.54:
      albomin_y[3] = albomin_y[3] + 1

    elif c > 5.54 and c <= 6.4:
      albomin_y[4] = albomin_y[4] + 1

  plt.figure(figsize=(8,5))

  plt.xlabel('ALBUMIN')
  plt.ylabel('Quantidade de amostras')


  plt.bar(albomin_x, albomin_y)
  plt.show()

def protimeAnalysis():
  protime_y = [0, 0, 0,0 ,0 ]
  protime_x = ['0 - 20', '20 - 40', '40 - 60', '60 - 80', '80 - 100']


  for c in df['PROTIME']:

    if c > 0 and c <= 20:
      protime_y[0] = protime_y[0] + 1

    if c > 20 and c <= 40:
      protime_y[1] = protime_y[1] + 1

    elif c > 40 and c <= 60:
      protime_y[2] = protime_y[2] + 1

    elif c > 60 and c <= 80:
      protime_y[3] = protime_y[3] + 1

    elif c > 80 and c <= 100:
      protime_y[4] = protime_y[4] + 1

  plt.figure(figsize=(8,5))

  plt.xlabel('PROTIME')
  plt.ylabel('Quantidade de amostras')


  plt.bar(protime_x, protime_y)
  plt.show()

bilirubinAnalysis()
alkPhosphateAnalysis()
sgotAnalysis()
albominAnalysis()
protimeAnalysis()

if __name__ == "__main__":
  main()
