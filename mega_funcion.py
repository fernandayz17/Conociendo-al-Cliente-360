def  imputar(df, objetivo, operacion, filtro1, filtro2, tc):
    
    import pandas as pd
    import numpy as np
    
    print('Antes')
    
    frecuencia_tabla = df[objetivo].value_counts().sort_index()
    print(f"Tabla de frecuencia de {objetivo}:")
    print(frecuencia_tabla)
    
    if tc == 'media': 
    
        if operacion == 'nulo':
            df["media_segmentada"] = (
                df.groupby([filtro1, filtro2])[objetivo]
                .transform(lambda x: x[~x.isnull()].mean())
            )
            df.loc[df[objetivo].isnull(), objetivo] = df.loc[df[objetivo].isnull(), "media_segmentada"]
            df.drop(columns="media_segmentada", inplace=True)
            
        elif operacion == 'negativo':
            df["media_segmentada"] = (
                df.groupby([filtro1, filtro2])[objetivo]
                .transform(lambda x: x[x >= 0].mean())
            )
            df.loc[df[objetivo] < 0, objetivo] = df.loc[df[objetivo] < 0, "media_segmentada"]
            df.drop(columns="media_segmentada", inplace=True)
            
        elif operacion == 'cero':
            df["media_segmentada"] = (
                df.groupby([filtro1, filtro2])[objetivo]
                .transform(lambda x: x[x != 0].mean())
            )
            df.loc[df[objetivo] == 0, objetivo] = df.loc[df[objetivo] == 0, "media_segmentada"]
            df.drop(columns="media_segmentada", inplace=True)
            
            
    elif tc == 'mediana':
    
        if operacion == 'nulo':
            df["mediana_segmentada"] = (
                df.groupby([filtro1, filtro2])[objetivo]
                .transform(lambda x: x[~x.isnull()].median())
            )
            df.loc[df[objetivo].isnull(), objetivo] = df.loc[df[objetivo].isnull(), "mediana_segmentada"]
            df.drop(columns="mediana_segmentada", inplace=True)
            
        elif operacion == 'negativo':
            df["mediana_segmentada"] = (
                df.groupby([filtro1, filtro2])[objetivo]
                .transform(lambda x: x[x >= 0].median())
            )
            df.loc[df[objetivo] < 0, objetivo] = df.loc[df[objetivo] < 0, "mediana_segmentada"]
            df.drop(columns="mediana_segmentada", inplace=True)
            
        elif operacion == 'cero':
            df["mediana_segmentada"] = (
                df.groupby([filtro1, filtro2])[objetivo]
                .transform(lambda x: x[x != 0].median())
            )
            df.loc[df[objetivo] == 0, objetivo] = df.loc[df[objetivo] == 0, "mediana_segmentada"]
            df.drop(columns="mediana_segmentada", inplace=True)
            
            
    elif tc == 'moda':
    
        if operacion == 'nulo':
            df["moda_segmentada"] = (
                df.groupby([filtro1, filtro2])[objetivo]
                .transform(lambda x: x[~x.isnull()].mode()[0] if not x[~x.isnull()].mode().empty else np.nan)
            )
            df.loc[df[objetivo].isnull(), objetivo] = df.loc[df[objetivo].isnull(), "moda_segmentada"]
            df.drop(columns="moda_segmentada", inplace=True)
            
        elif operacion == 'negativo':
            df["moda_segmentada"] = (
                df.groupby([filtro1, filtro2])[objetivo]
                .transform(lambda x: x[x >= 0].mode()[0] if not x[x >= 0].mode().empty else np.nan)
            )
            df.loc[df[objetivo] < 0, objetivo] = df.loc[df[objetivo] < 0, "moda_segmentada"]
            df.drop(columns="moda_segmentada", inplace=True)
            
            
        elif operacion == 'cero':
            df["moda_segmentada"] = (
                df.groupby([filtro1, filtro2])[objetivo]
                .transform(lambda x: x[x != 0].mode()[0] if not x[x != 0].mode().empty else np.nan)
            )
            df.loc[df[objetivo] == 0, objetivo] = df.loc[df[objetivo] == 0, "moda_segmentada"]
            df.drop(columns="moda_segmentada", inplace=True)
              
            
            
    print(f"Imputación de {objetivo} con {operacion} por {filtro1} y {filtro2} usando {tc} completada.")
    
    print('----'*5)
    print('Después')
    frecuencia_tabla = df[objetivo].value_counts().sort_index()
    
    print(f"Tabla de frecuencia de {objetivo}:")
    
    print(frecuencia_tabla)
    return df

