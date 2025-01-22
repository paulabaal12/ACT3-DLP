# Código base para iniciar
def cargar_buffer(entrada, inicio, tamano_buffer):
  buffer = entrada[inicio:inicio + tamano_buffer]
  if len(buffer) < tamano_buffer:
    buffer.append("eof")
  return buffer

def procesar_buffer(buffer):
  # Procesar y extraer lexemas del buffer
   buffer = cargar_buffer(entrada, inicio, tamano_buffer)

   
entrada = list("Esto es un ejemplo eof")
inicio = 0
tamano_buffer = 10
buffer = cargar_buffer(entrada, inicio, tamano_buffer)
procesar_buffer(buffer)


def extraer_lexema(buffer):
    lexema = []
    while buffer:
        char = buffer.pop(0)
        if char == " " or char == "eof":
            break
        lexema.append(char)
    return ''.join(lexema)

while True:
    lexema = extraer_lexema(buffer)
    if lexema:
        print(f"Lexema: {lexema}")
    if "eof" in buffer:
        break
    inicio += len(lexema) + 1
    buffer = cargar_buffer(entrada, inicio, tamano_buffer)

