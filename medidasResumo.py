import pandas as pd

def main():
  CAMINHO_DATASET_CLEAR = 'hepatitisClear.data'
  NAMES = ['CLASS','AGE','SEX','STEROID','ANTIVIRALS','FATIGUE','MALAISE','ANOREXIA',
          'LIVER BIG','LIVER FIRM','SPLEEN PALPABLE','SPIDERS','ASCITES','VARICES','BILIRUBIN',
          'ALK PHOSPHATE','SGOT','ALBUMIN','PROTIME','HISTOLOGY'] 
  
  ################### IDADE #####################
  def medidasResumoIdade():
      # Faz a leitura do arquivo
    df = pd.read_csv(CAMINHO_DATASET_CLEAR, names = NAMES)

    def MedidasTendenciaCentral(df, column):

        # Calculo da  média
        mean = df[column].mean()

        # Calculo da mediana 
        median = df[column].median()
          
        # Calculo da moda
        mode = df[column].mode().mode()[0]

        # Calculo do ponto medio
        maior_valor = df[column].min()
        menor_valor = df[column].max()
        ponto_medio = (maior_valor + menor_valor)/2

        # Print dos valores
        # print('Coluna: ' , column)
        # print('Média: ', mean)
        # print('Mediana: ', median)
        # print('Moda: ', mode)
        # print('Ponto Médio: ', ponto_medio)
        # print('\n')

    def MedidasDispercao(df, column):

        # Calculo Amplitude
        maior_valor = df[column].max()
        menor_valor = df[column].min()
        amplitude = maior_valor - menor_valor
        
        # Calculo Desvio Padrao
        desvio_padrao = df[column].std()

        # Calculo Variancia
        variancia = df[column].var()

        # Calculo coeficiente de variacao
        media = df[column].mean()
        coeficiente_variacao = (media/desvio_padrao) * (100/100)

        # Print dos valores
        # print('Coluna: ' , column)
        # print('Amplitude: ', amplitude)
        # print('Desvio Padrao: ', desvio_padrao)
        # print('Varianica: ', variancia)
        # print('Coeficiente Variaacao: ', coeficiente_variacao, ' %')
        # print('\n')

    def MedidasPosicaoRelativa(df, column):
        
        # Calculo Z-Score
        media = df[column].mean()
        desvio_padrao = df[column].std()
        z = (df[column] - media)/ desvio_padrao

        # Calculo Quantis
        q1 = df[column].quantile(q=0.25)
        q2 = df[column].quantile(q=0.50)
        q3 = df[column].quantile(q=0.75)
        iqr = q3 - q1

        # Printa os valores
        print('ATRIBUTO: ', column)
        print('Z-score:', z)
        # print('Quantis: ')
        # print('   Q1 (25%): ', q1)
        # print('   Q2 (50%): ', q2)
        # print('   Q3 (75%): ', q3)
        # print('   IQR: ', iqr)
        # print('\n')

    def MedidasAssociacao(df):

        # Calculo Covariancia
        covariancia = df.cov()

        # Calculo Correlacao
        correlacao = df.corr()

        print('Covariancia: ')
        print(covariancia)
        print('\n')
        print('Correlacao: ')
        print(correlacao)

    MedidasTendenciaCentral(df, 'AGE')
    MedidasDispercao(df, 'AGE')
    MedidasPosicaoRelativa(df,'AGE')
    MedidasAssociacao(df)

  def medidasResumoAlkPhosphate():
        # Faz a leitura do arquivo
    df = pd.read_csv(CAMINHO_DATASET_CLEAR, names = NAMES)

    def MedidasTendenciaCentral(df, column):

        # Calculo da  média
        mean = df[column].mean()

        # Calculo da mediana 
        median = df[column].median()
          
        # Calculo da moda
        mode = df[column].mode().mode()[0]

        # Calculo do ponto medio
        maior_valor = df[column].min()
        menor_valor = df[column].max()
        ponto_medio = (maior_valor + menor_valor)/2

        # Print dos valores
        # print('Coluna: ' , column)
        # print('Média: ', mean)
        # print('Mediana: ', median)
        # print('Moda: ', mode)
        # print('Ponto Médio: ', ponto_medio)
        # print('\n')

    def MedidasDispercao(df, column):

        # Calculo Amplitude
        maior_valor = df[column].max()
        menor_valor = df[column].min()
        amplitude = maior_valor - menor_valor
        
        # Calculo Desvio Padrao
        desvio_padrao = df[column].std()

        # Calculo Variancia
        variancia = df[column].var()

        # Calculo coeficiente de variacao
        media = df[column].mean()
        coeficiente_variacao = (media/desvio_padrao) * (100/100)

        # Print dos valores
        # print('Coluna: ' , column)
        # print('Amplitude: ', amplitude)
        # print('Desvio Padrao: ', desvio_padrao)
        # print('Varianica: ', variancia)
        # print('Coeficiente Variaacao: ', coeficiente_variacao, ' %')
        # print('\n')

    def MedidasPosicaoRelativa(df, column):
        
        # Calculo Z-Score
        media = df[column].mean()
        desvio_padrao = df[column].std()
        z = (df[column] - media)/ desvio_padrao

        # Calculo Quantis
        q1 = df[column].quantile(q=0.25)
        q2 = df[column].quantile(q=0.50)
        q3 = df[column].quantile(q=0.75)
        iqr = q3 - q1

        # Printa os valores
        print('ATRIBUTO: ', column)
        print('Z-score:', z)
        # print('Quantis: ')
        # print('   Q1 (25%): ', q1)
        # print('   Q2 (50%): ', q2)
        # print('   Q3 (75%): ', q3)
        # print('   IQR: ', iqr)
        # print('\n')

    def MedidasAssociacao(df):

        # Calculo Covariancia
        covariancia = df.cov()

        # Calculo Correlacao
        correlacao = df.corr()

        print('Covariancia: ')
        print(covariancia)
        print('\n')
        print('Correlacao: ')
        print(correlacao)

    ## 
    MedidasTendenciaCentral(df, 'ALK PHOSPHATE')
    MedidasDispercao(df, 'ALK PHOSPHATE')
    MedidasPosicaoRelativa(df,'ALK PHOSPHATE')
    MedidasAssociacao(df)


  medidasResumoIdade()
  medidasResumoAlkPhosphate()


if __name__ == "__main__":
    main()
