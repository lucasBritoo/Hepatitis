import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def main():
  # CAMINHO_DATASET_CLEAR = 'hepatitisClear.data'
  CAMINHO_DATASET_NORMAL= 'hepatitisNormal.data'
  NAMES = ['CLASS','AGE','SEX','STEROID','ANTIVIRALS','FATIGUE','MALAISE','ANOREXIA',
          'LIVER BIG','LIVER FIRM','SPLEEN PALPABLE','SPIDERS','ASCITES','VARICES','BILIRUBIN',
          'ALK PHOSPHATE','SGOT','ALBUMIN','PROTIME','HISTOLOGY'] 
  # FEATURES = ['AGE','SEX','STEROID','ANTIVIRALS','FATIGUE','MALAISE','ANOREXIA',
  #         'LIVER BIG','LIVER FIRM','SPLEEN PALPABLE','SPIDERS','ASCITES','VARICES','BILIRUBIN',
  #         'ALK PHOSPHATE','SGOT','ALBUMIN','PROTIME','HISTOLOGY']
  TARGET = 'CLASS'  

  # Faz a leitura do arquivo
  df = pd.read_csv(CAMINHO_DATASET_NORMAL, # Nome do arquivo com dados
                      names = NAMES)  # Nome das colunas

            
  def VisualizePcaProjection(finalDf, targetColumn):
      fig = plt.figure(figsize = (8,8))
      ax = fig.add_subplot(1,1,1) 
      ax.set_xlabel('Principal Component 1', fontsize = 15)
      ax.set_ylabel('Principal Component 2', fontsize = 15)
      ax.set_title('PCA Hepatits Dataset', fontsize = 20)
      targets = [0, 1, ]
      colors = ['r', 'g']
      for target, color in zip(targets,colors):
          indicesToKeep = finalDf[targetColumn] == target
          ax.scatter(finalDf.loc[indicesToKeep, 'principal component 1'],
                    finalDf.loc[indicesToKeep, 'principal component 2'],
                    c = color, s = 50)
      ax.legend(targets)
      ax.grid()
      plt.show()
                
  # Separating out the features
  x = df.loc[:, FEATURES].values

  # Separating out the target
  y = df.loc[:,[TARGET]].values

  # Standardizing the features
  x = StandardScaler().fit_transform(x)
  normalizedDf = pd.DataFrame(data = x, columns = FEATURES)
  normalizedDf = pd.concat([normalizedDf, df[[TARGET]]], axis = 1)


  # PCA projection
  pca = PCA()    
  principalComponents = pca.fit_transform(x)
  #print("Explained variance per component:")
  #print(pca.explained_variance_ratio_.tolist())
  #print("\n\n")

  principalDf = pd.DataFrame(data = principalComponents[:,0:2], 
                                columns = ['principal component 1', 
                                            'principal component 2'])
  finalDf = pd.concat([principalDf, df[[TARGET]]], axis = 1)

  VisualizePcaProjection(finalDf, TARGET)

if __name__ == "__main__":
    main()
