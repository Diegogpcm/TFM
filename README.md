# TFM
Repositorio para reproducir los resultados de mi Trabajo de Fin de Máster, "Perfeccionamiento de grandes modelos lingüísticos para resumir conversaciones escritas"

## Pasos a seguir

1. Descargar el repositorio llama.cpp y sustituirlo por la carpera vacía. Si se desea reproducir el LoRA, hacer lo mismo con text-generation-webui.

2. Descargar los modelos LLaMa-7b, LLaMa-13, Vicuna-7b y Vicuna-13b, y ponerlos en carpetas con su mismo nombre en llama.cpp/models

3. Desde una terminal, convertir los modelos a float16 con el comando 'python3 convert.py models/modelo/'

4. Desde la misma terminal, "cuantizarlo" al formato deseado con el comando './quantize ./models/7B/ggml-model-f16.bin ./models/7B/ggml-model-q4_0.bin q4_0' para 4-bit

