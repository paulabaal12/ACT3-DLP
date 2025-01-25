
def cargar_buffer(entrada, inicio, tamano_buffer):
    #Carga un fragmento de la entrada dentro del buffer
    buffer = entrada[inicio:inicio + tamano_buffer]
    if len(buffer) < tamano_buffer:
        buffer.extend(["eof"] * (tamano_buffer - len(buffer)))
    return buffer

def procesar_buffer(buffer, lexema_incompleto):
    #Se procesan y extraen los lexemas del buffer
    lexemas = []
    lexema_actual = lexema_incompleto
    for caracter in buffer:
        if caracter.isspace() or caracter == "eof":
            if lexema_actual:
                lexemas.append(lexema_actual)
                lexema_actual = ""
            if caracter == "eof":
                break
        else:
            lexema_actual += caracter
    return lexemas, lexema_actual

def procesar_entrada(entrada, tamano_buffer):
    #Procesa la entrada completa utilizando el manejo de fragmentos mediante el buffer
    inicio = 0
    lexema_incompleto = ""

    while inicio < len(entrada):
        buffer = cargar_buffer(entrada, inicio, tamano_buffer)

        lexemas, lexema_incompleto = procesar_buffer(buffer, lexema_incompleto)

        for lexema in lexemas:
            print(f"Lexema procesado: {lexema}")

        # Actualizar el puntero para cargar el siguiente fragmento
        inicio += tamano_buffer

    # Imprimir cualquier lexema incompleto que quede al final
    if lexema_incompleto:
        print(f"Lexema procesado: {lexema_incompleto}")

# Entrada de prueba
entrada = list("Esto es un ejemplo de entrada con eof")
tamano_buffer = 10

procesar_entrada(entrada, tamano_buffer)