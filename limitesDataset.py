import pandas as pd

def main():
	CAMINHO_DATASET = "hepatitis.data"
	NAMES = ['CLASS','AGE','SEX','STEROID','ANTIVIRALS','FATIGUE','MALAISE','ANOREXIA',
		      'LIVER BIG','LIVER FIRM','SPLEEN PALPABLE','SPIDERS','ASCITES','VARICES','BILIRUBIN',
		      'ALK PHOSPHATE','SGOT','ALBUMIN','PROTIME','HISTOLOGY'] 
	FEATURES = ['AGE','SEX','STEROID','ANTIVIRALS','FATIGUE','MALAISE','ANOREXIA',
		      'LIVER BIG','LIVER FIRM','SPLEEN PALPABLE','SPIDERS','ASCITES','VARICES','BILIRUBIN',
		      'ALK PHOSPHATE','SGOT','ALBUMIN','PROTIME','HISTOLOGY']


	df = pd.read_csv(
		  CAMINHO_DATASET,      # Nome do arquivo com dados
		  names=NAMES,          # Nome das colunas
		  usecols=FEATURES,     # Define as colunas que serão  utilizadas
		  na_values="?",        # Define que ? será considerado valores ausentes

	)                        

	def tableValues():
		  print(
		      "--------------------------------------------------------------------"
		      + "----------------------------------"
		  )
		  print("Limites dos atributos do dataset\n")

		  print(
		      "{:<15} {:<8} {:<8} {:<8} {:<15} {:<12} {:<15}".format(
		          "ATRIBUT",
		          "MIN VALUES |",
		          "MAX VALUES |",
		          "MEAN VALUES |",
		          "MEDIAN VALUES |",
		          "MODE VALUES |",
		          "MISSING VALUES |",
		      )
		  )
		  print(
		      "--------------------------------------------------------------------"
		      + "----------------------------------"
		  )
		  for c in FEATURES:
		      name = c

		      print(
		          "{:<20} {:<12} {:<10} {:<14.2f} {:<14.2f} {:<16.2f} {:<12}".format(
		              name,
		              df[name].min(),
		              df[name].max(),
		              df[name].mean(),
		              df[name].median(),
		              df[name].mode()[0],
		              df[name].isnull().sum(),
		          )
		      )


	tableValues()

if __name__ == "__main__":
  main()

