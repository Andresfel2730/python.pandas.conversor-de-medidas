import pandas as pd

def cm_a_pulgadas(cm):
    return cm / 2.54

#leer el archivo excel:

df = pd.read_excel("muebles_medidas.xlsx")

# añadir una columna al Dataframe que sea de pulgadas y se rellene con el calculo de cm / 2.54

df["Pulgadas"] = df["Centimetros"].apply(cm_a_pulgadas)
df.to_excel("mueble_medida_convertidas.xlsx", index=False)
print("conversion completada y guardada en un nuevo archivo llamado 'mueble_medida_convertidas.xlsx'")
