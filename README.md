# TFM
Repositorio para reproducir los resultados de mi Trabajo de Fin de Máster, "Perfeccionamiento de grandes modelos lingüísticos para resumir conversaciones escritas"

## Pasos a seguir

1. Descargar el repositorio llama.cpp y sustituirlo por la carpera vacía. Si se desea reproducir el LoRA, hacer lo mismo con text-generation-webui.

2. Descargar los modelos LLaMa-7b, LLaMa-13, Vicuna-7b y Vicuna-13b, y ponerlos en carpetas con su mismo nombre en llama.cpp/models

3. Desde una terminal, navegar hasta la carpeta llama.cpp y convertir los modelos a float16 con el comando 'python3 convert.py models/modelo/'

4. Desde la misma terminal, "cuantizarlo" al formato deseado con el comando './quantize ./models/modelo/ggml-model-f16.bin ./models/modelo/ggml-model-q4_0.bin q4_0' para 4-bit y './quantize ./models/modelo/ggml-model-f16.bin ./models/modelo/ggml-model-q8_0.bin q8_0' para 8-bit.

5. Ejecutar el notebook 'download_gigaword.ipynb'. Este notebook descarga gigaword y genera dos archivos .csv, uno con el train y uno con el test.

6. Si se desea repetir la inferencia con los LLMs, ejecutar los scripts 'LLM-gigaword_inference.py' y 'LLM-messages_inference.py'. Se recomienda hacerlo desde la terminal, navegando hasta el directorio y usando el comando 'python3'. En los scripts están incluidos parámetros como el prompt o la cantidad de mensajes a resumir, por si se desean modificar. El output de estos scripts está incluido en el repositorio; se trata de todos los archivos .csv que comienzan con 'output'.

7. Para analizar los modelos, ejecutar los notebooks 'DistilBART_analysis.ipynb' y 'LLM_analysis.ipynb'. El primero realiza la inferencia a la vez que el análisis, mientras que el segundo carga los 'output-*.csv'. Ambos calculan las métricas BLEU y ROUGE.

8. Para realizar el LoRA, es necesario copiar el modelo que se desea fine-tunear en text-generation-webui/models. Después, se ejecuta el notebook 'generate_train_dataset.csv' y el archivo de salida, 'gigaword_vicuna.json', se copia en text-generation-webui/training/datasets. También es necesario que esté en text-generation-webui/training/formats el archivo que se incluye en este repositorio, que se ha desarrollado en el TFM especificamente para realizar el LoRA.

9. 

