# Código base para iniciar
def cargar_buffer(entrada, inicio, tamano_buffer):
  buffer = entrada[inicio:inicio + tamano_buffer]
  if len(buffer) < tamano_buffer:
    buffer.append("eof")
  return buffer

def procesar_buffer(entrada, buffer):
  # Procesar y extraer lexemas del buffer
  inicio = 0
  avance = 0
  buffer = cargar_buffer(entrada, inicio, tamano_buffer)
  lexema = ""

  while True:
    if avance >= len(buffer):
      inicio += tamano_buffer
      buffer = cargar_buffer(entrada, inicio, tamano_buffer)
      avance = 0

    if buffer[avance] == "eof":
      if lexema:
        print(f"Lexema procesado: {lexema}")
      print("Fin de la entrada")
      break

    char = buffer[avance]

     # Si encontramos un espacio o el final, imprimir el lexema acumulado
    if char == " ":
        if lexema:
            print(f"Lexema procesado: {lexema}")
            lexema = ""  # Reiniciar el lexema
    else:
        lexema += char  # Acumular el carácter en el lexema

    # Mover el puntero avance
    avance += 1


# Entrada de prueba
entrada = list("Esto es un ejemplo de entrada con eof")
tamano_buffer = 10

# Procesar la entrada
procesar_buffer(entrada, tamano_buffer)


