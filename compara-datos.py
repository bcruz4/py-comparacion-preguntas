import pandas as pd

# Cargar los archivos Excel (.xlsx)
preguntas_gral = pd.read_excel('preguntas_gral.xlsx')
preguntas_1 = pd.read_excel('preguntas_1.xlsx')

# Crear una lista para almacenar los resultados
resultados = []

# Verificar las preguntas y respuestas
for index, row in preguntas_1.iterrows():
    pregunta = row['Pregunta']
    respuesta_1 = row['Respuesta']
    
    # Buscar la pregunta en preguntas_gral
    pregunta_gral = preguntas_gral[preguntas_gral['Pregunta'] == pregunta]
    
    if not pregunta_gral.empty:
        respuesta_gral = pregunta_gral['Respuesta'].values[0]
        
        # Comparar las respuestas
        if respuesta_1 == respuesta_gral:
            resultados.append([pregunta, respuesta_1, "Correcto"])
        else:
            resultados.append([pregunta, respuesta_1, "Incorrecto"])
    else:
        resultados.append([pregunta, respuesta_1, "Pregunta no encontrada"])

# Convertir los resultados en un DataFrame
resultados_df = pd.DataFrame(resultados, columns=['Pregunta', 'Respuesta', 'Estado'])

# Guardar el DataFrame en un nuevo archivo Excel
resultados_df.to_excel('comparacion_resultados.xlsx', index=False)

print("El archivo comparacion_resultados.xlsx se ha generado con éxito.")
