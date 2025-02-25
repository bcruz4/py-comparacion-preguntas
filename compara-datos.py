import pandas as pd

# Cargar los archivos Excel (.xlsx)
preguntas_gral = pd.read_excel('preguntas_gral.xlsx')
preguntas_1 = pd.read_excel('preguntas_1.xlsx')

# Crear una lista para almacenar los resultados
resultados = []

# Verificar las preguntas y respuestas
for index, row in preguntas_1.iterrows():
    pregunta = row['Pregunta']
    respuesta_1 = {row['a'], row['b'], row['c'], row['d'], row['e']}  # Opciones de respuesta de preguntas_1
    
    # Buscar la pregunta en preguntas_gral
    pregunta_gral = preguntas_gral[preguntas_gral['Pregunta'] == pregunta]
    
    if not pregunta_gral.empty:
        # Opciones de respuesta de preguntas_gral
        respuesta_gral = {pregunta_gral['a'].values[0], pregunta_gral['b'].values[0], 
                          pregunta_gral['c'].values[0], pregunta_gral['d'].values[0], 
                          pregunta_gral['e'].values[0]}
        
        # Comparar las respuestas (sin importar el orden)
        if respuesta_1 == respuesta_gral:
            resultados.append([pregunta, "Correcto"])
        else:
            resultados.append([pregunta, "Incorrecto"])
    else:
        resultados.append([pregunta, "Pregunta no encontrada"])

# Convertir los resultados en un DataFrame
resultados_df = pd.DataFrame(resultados, columns=['Pregunta', 'Estado'])

# Guardar el DataFrame en un nuevo archivo Excel
resultados_df.to_excel('comparacion_resultados.xlsx', index=False)

print("El archivo comparacion_resultados.xlsx se ha generado con éxito.")
