# ACT3-DLP
## Actividad Práctica: Implementación de un Búfer de Entrada

Este programa implementa un sistema para procesar cadenas de entrada por partes, utilizando buffers de tamaño fijo. Permite manejar lexemas (palabras o tokens) incluso si están divididos entre buffers, asegurando que ninguna parte de la entrada se pierda en el proceso.

## Funciones Principales

### `cargar_buffer(entrada, inicio, tamano_buffer)`
Carga un fragmento de la entrada en el buffer.
- **Parámetros:**
  - `entrada` (lista): Lista de caracteres a procesar.
  - `inicio` (int): Índice inicial para cargar el buffer.
  - `tamano_buffer` (int): Tamaño máximo del buffer.
- **Retorno:**
  - `buffer` (lista): Fragmento de la entrada, rellenado con "eof" si el tamaño es menor al requerido.

### `procesar_buffer(buffer, lexema_incompleto)`
Procesa el buffer y extrae lexemas, considerando un lexema incompleto previo.
- **Parámetros:**
  - `buffer` (lista): Fragmento de entrada cargado.
  - `lexema_incompleto` (string): Parte de un lexema que quedó incompleto en el buffer anterior.
- **Retorno:**
  - `lexemas` (lista): Lista de lexemas extraídos del buffer.
  - `lexema_incompleto` (string): Cualquier lexema incompleto que no se terminó de formar.

### `procesar_entrada(entrada, tamano_buffer)`
Coordina el procesamiento de la entrada completa dividiéndola en buffers y extrayendo los lexemas.
- **Parámetros:**
  - `entrada` (lista): Lista de caracteres a procesar.
  - `tamano_buffer` (int): Tamaño máximo de cada buffer.

## Ejemplo de Uso
### Entrada
Cadena de entrada:
```
"Esto es un ejemplo de entrada con eof"
```
Tamaño del buffer:
```
10
```

### Salida
El programa procesará la entrada y mostrará:
```
Lexema procesado: Esto
Lexema procesado: es
Lexema procesado: un
Lexema procesado: ejemplo
Lexema procesado: de
Lexema procesado: entrada
Lexema procesado: con
Lexema procesado: eof
```

## Instalación
1. Asegúrate de tener [Python](https://www.python.org/downloads/) instalado en tu sistema.
2. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/paulabaal12/ACT3-DLP.git
   ```

## Como Ejecutar
2. Ejecuta el archivo `main.py` para iniciar el procesamiento:
   ```bash
   python main.py
   ```

## Detalles Técnicos
- **Manejo de Lexemas Incompletos:** Si un lexema está dividido entre dos buffers, el programa conserva la parte incompleta y la completa al procesar el siguiente buffer.
- **"eof":** Se utiliza como marcador para indicar el final de la entrada.

## Video de Ejecución
A continuación se muestra el enlace al video del funcionamiento y ejecución del programa:
[Enlace a video](https://youtu.be/CImyw4KiR64).

## Desarrollado por:
- **[Mónica Salvatierra - 22249](https://github.com/alee2602)**
- **[Paula Barillas - 22764](https://github.com/paulabaal12)**
- **[Derek Arreaga - 22537](https://github.com/FabianKel)**
- **[Andrés Kou - 22305](https://github.com/EdwinOrtegaK)**
- **[Esteban Zambrano - 22119](https://github.com/EstebanZG999)**
