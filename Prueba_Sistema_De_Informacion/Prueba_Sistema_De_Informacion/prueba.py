import pandas as pd
paises = pd.read_csv("./Archivos/DiccionarioPaises.csv", encoding = "UTF-8", delimiter = ";")
alfabeto = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 
            'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 
            'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
def inicia_con(df):
    dic={}
    for letra in alfabeto:
        paises_por=lambda df: df[df["País en inglés"].str[0]==letra]
        dic.update({letra:len(paises_por(df))})
    return dic
print(inicia_con(paises))    