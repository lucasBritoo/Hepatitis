import pandas as pd
import numpy as np
from scipy.spatial.distance import cdist 
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.mixture import GaussianMixture
from sklearn.metrics import silhouette_score
from sklearn.metrics import silhouette_samples
import matplotlib.pyplot as plt
CAMINHO_DATASET_CLEAR = 'hepatitisClear.data'
NAMES = ['CLASS','AGE','SEX','STEROID','ANTIVIRALS','FATIGUE','MALAISE','ANOREXIA',
        'LIVER BIG','LIVER FIRM','SPLEEN PALPABLE','SPIDERS','ASCITES','VARICES','BILIRUBIN',
        'ALK PHOSPHATE','SGOT','ALBUMIN','PROTIME','HISTOLOGY'] 


def plot_samples(projected, labels, title):    
    fig = plt.figure()
    u_labels = np.unique(labels)
    for i in u_labels:
        plt.scatter(projected[labels == i , 0] , projected[labels == i , 1] , label = i,
                    edgecolor='none', alpha=0.5, cmap=plt.cm.get_cmap('tab10', 10))
    plt.xlabel('component 1')
    plt.ylabel('component 2')
    plt.legend()
    plt.title(title)

def main():
  #Load dataset Digits
  df = pd.read_csv(CAMINHO_DATASET_CLEAR,   # Nome do arquivo com dados
                  names = NAMES)
  digits = df

  #Transform the data using PCA
  pca = PCA(2)
  projected = pca.fit_transform(digits)
  print(pca.explained_variance_ratio_)
  print(digits.shape)
  print(projected.shape)    
  plot_samples(projected, digits["CLASS"], 'Original Labels') 

  #Applying sklearn GMM function
  gm  = GaussianMixture(n_components=2).fit(projected)
  print(gm.weights_)
  print(gm.means_)
  x = gm.predict(projected)

  #Visualize the results sklearn
  plot_samples(projected, x, 'Clusters Labels GMM')

  plt.show()


if __name__ == "__main__":
  main()
