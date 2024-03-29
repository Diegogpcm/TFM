# TFM
Repositorio para reproducir los resultados de mi Trabajo de Fin de Máster, "Perfeccionamiento de grandes modelos lingüísticos para resumir conversaciones escritas"

## Pasos a seguir

1. Descargar el repositorio llama.cpp y sustituirlo por la carpeta vacía. Si se desea reproducir el LoRA, hacer lo mismo con text-generation-webui.

2. Hacer la build de `llama.cpp`. Para ello, navegar desde la terminal a la carpeta `llama.cpp` y ejecutar el comando `make` (es necesario usar Linux o MacOS, en Windows se recomienda usar WSL).

3. Instalar PyTorch si no se tiene ya instalado. Instalar el resto de librerías desde la terminal con `pip install -r requirements.txt`.

4. Descargar los modelos [LLaMA-7b](huggingface.co/huggyllama/llama-7b), [LLaMa-13](huggingface.co/huggyllama/llama-13b), [Vicuna-7b](huggingface.co/lmsys/vicuna-7b-v1.3) y [Vicuna-13b](huggingface.co/lmsys/vicuna-13b-v1.3), y ponerlos en carpetas con su mismo nombre en llama.cpp/models

5. Desde una terminal, navegar hasta la carpeta llama.cpp y convertir los modelos a float16 con el comando `python3 convert.py models/modelo/`.

6. Desde la misma terminal, "cuantizarlo" al formato deseado con el comando adecuado. En el trabajo, los modelos 7b se han cuantizado en 4 y 8 bits y los modelos 13b en 4 bits.
   - Para 8 bits: `./quantize ./models/modelo/ggml-model-f16.bin ./models/modelo/ggml-model-q4_0.bin q4_0`
   - Para 4 bits: `./quantize ./models/modelo/ggml-model-f16.bin ./models/modelo/ggml-model-q8_0.bin q8_0`

7. Ejecutar el notebook `download_gigaword.ipynb`. Este notebook descarga gigaword y genera dos archivos .csv, uno con el train y uno con el test.

8. Si se desea repetir la inferencia con los LLMs, ejecutar los scripts 'LLM-gigaword_inference.py' y 'LLM-messages_inference.py'. Se recomienda hacerlo desde la terminal, navegando hasta el directorio y usando el comando 'python3'. En los scripts están incluidos parámetros como el prompt o la cantidad de mensajes a resumir, por si se desean modificar. El output de estos scripts está incluido en el repositorio; se trata de todos los archivos .csv que comienzan con 'output'.

9. Para analizar los modelos, ejecutar los notebooks `DistilBART_analysis.ipynb` y `LLM_analysis.ipynb`. El primero realiza la inferencia a la vez que el análisis, mientras que el segundo carga los `output-*.csv`. Ambos calculan las métricas BLEU y ROUGE.

10. Para realizar el LoRA, seguir los siguientes pasos:
      - Copiar el modelo que se desea fine-tunear en text-generation-webui/models.
      - Ejecutar el notebook `generate_train_dataset.csv`
      - Copiar el archivo de salida, `gigaword_vicuna.json`, en text-generation-webui/training/datasets.
      - Copiar en text-generation-webui/training/formats el archivo que se incluye en este repositorio en la carpeta placeholder text-generation-webui/training/formats, que se ha desarrollado en el TFM especificamente para realizar el LoRA.
      - Generar la interfaz de usuario de text-generation-webui accediendo a la carpeta con la terminal y ejecutando el comando `python3 server.py`.
      - Acceder a la interfaz pegando la dirección que aparezca en la terminal en un buscador.
      - Cargar el modelo que se desee desde la pestaña 'Model'.
      - Acceder a la pestaña de 'Training', donde si todo se ha realizado correctamente debería permitir seleccionar `gigaword_vicuna.json` como dataset y `custom-vicuna-format.json` como formato.
      - Darle al botón 'Start LoRA Training'.
   
      ![image](https://github.com/Diegogpcm/TFM/assets/95076543/a551aaae-f4ba-4897-ae25-5a2aaa24fa38)
      ![image](https://github.com/Diegogpcm/TFM/assets/95076543/29116589-035a-43a3-995b-2d8bb54af977)



  

