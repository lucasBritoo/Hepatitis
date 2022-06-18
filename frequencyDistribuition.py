import pandas as pd

def main():
  CAMINHO_DATASET_CLEAR = 'hepatitisClear.data'
  NAMES = ['CLASS','AGE','SEX','STEROID','ANTIVIRALS','FATIGUE','MALAISE','ANOREXIA',
          'LIVER BIG','LIVER FIRM','SPLEEN PALPABLE','SPIDERS','ASCITES','VARICES','BILIRUBIN',
          'ALK PHOSPHATE','SGOT','ALBUMIN','PROTIME','HISTOLOGY'] 
  
  ################### IDADE #####################
  def age():
    df = pd.read_csv(CAMINHO_DATASET_CLEAR, names = NAMES)
    # df = df.apply(lambda x: pd.factorize(x, sort=True)[0])
    age_y = [0, 0, 0, 0, 0]
    age_x = ['7 - 14', '15 - 30', '31 - 45', '46 - 60', '61 - 78']
    for c in df['AGE']:

      if c > 7 and c <= 14:
        age_y[0] = age_y[0] + 1

      if c > 14 and c <= 30:
        age_y[1] = age_y[1] + 1

      elif c > 30 and c <= 45:
        age_y[2] = age_y[2] + 1

      elif c > 45 and c <= 60:
        age_y[3] = age_y[3] + 1

      elif c > 60 and c <= 78:
        age_y[4] = age_y[4] + 1
    plt.subplots(figsize=(9, 9))
    plt.pie(age_y,labels=age_x)
    plt.xlabel('IDADE')
    plt.show()

  ################### IDADE X CLASSE #####################
  def ageXclass():
    df=pd.read_csv(CAMINHO_DATASET_CLEAR,names=NAMES)
    plt.subplots(figsize=(10, 5))
    plt.scatter(df['CLASS'],df['AGE'])
    plt.xlabel('CLASS')
    plt.ylabel('AGE')

  ################### ALBUMINA X CLASSE #####################
  def albuminXclass():
    df=pd.read_csv(CAMINHO_DATASET_CLEAR,names=NAMES)
    plt.subplots(figsize=(10, 5))
    plt.scatter(df['CLASS'],df['ALBUMIN'])
    plt.xlabel('CLASS')
    plt.ylabel('ALBUMIN')

  age()
  ageXclass()
  albuminXclass()

if __name__ == "__main__":
    main()
