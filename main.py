# Función para cargar un búfer desde la entrada
def cargar_buffer(entrada, inicio, tamano_buffer):
    buffer = entrada[inicio:inicio + tamano_buffer]
    if len(buffer) < tamano_buffer:
        buffer.extend(["eof"] * (tamano_buffer - len(buffer)))
    return buffer

# Función para procesar el contenido del búfer y extraer lexemas
def procesar_buffer(buffer, lexema_incompleto):
    lexemas = []
    lexema_actual = lexema_incompleto  # Iniciar con cualquier lexema incompleto previo

    for caracter in buffer:
        if caracter.isspace() or caracter == "eof":
            if lexema_actual:
                lexemas.append(lexema_actual)
                lexema_actual = ""
            if caracter == "eof":
                break
        else:
            lexema_actual += caracter

    return lexemas, lexema_actual  # Devolver los lexemas y cualquier lexema incompleto

# Entrada simulada como una lista de caracteres
entrada = list("Esto es un ejemplo de entrada con eof")
inicio = 0
tamano_buffer = 10
lexema_incompleto = ""

while inicio < len(entrada):
    buffer = cargar_buffer(entrada, inicio, tamano_buffer)
    lexemas, lexema_incompleto = procesar_buffer(buffer, lexema_incompleto)

    for lexema in lexemas:
        print(f"Lexema procesado: {lexema}")

    # Actualizamos el puntero inicio para cargar el siguiente fragmento
    inicio += tamano_buffer

# Si queda un lexema incompleto después de procesar todo, imprimirlo
if lexema_incompleto:
    print(f"Lexema procesado: {lexema_incompleto}")