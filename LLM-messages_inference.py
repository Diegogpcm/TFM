import pandas as pd
import numpy as np
import re
from llama_cpp import Llama


MODEL = 'vicuna-13b-v1.3'
QUANTIZATION = 'q4_0'

ALL_MODELS = [ 
    ('llama-7b','q4_0'),
    ('llama-7b','q8_0'),
    ('llama-13b','q4_0'),
    ('vicuna-7b-v1.3','q4_0'),
    ('vicuna-7b-v1.3','q8_0'),
    ('vicuna-13b-v1.3','q4_0'),
    ]


df = pd.read_csv("messages.csv")
    
CONTEXT = """A chat between a curious human and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the human's questions.
USER: Summarize in 5 words: __DOC__ 
ASSISTANT:"""


for MODEL, QUANTIZATION in ALL_MODELS:
    
    llm = Llama(model_path=f"./llama.cpp/models/{MODEL}/ggml-model-{QUANTIZATION}.bin")
    
    summs = []
    for i in list(df['Message']):
        query = re.sub('__DOC__', i, CONTEXT)
        output = llm(query, max_tokens=64, echo=True) #stop=["[[USER_NAME]]:"],
        print(output)
        summs.append(output['choices'][0]['text'][len(query):])
    
    out = pd.DataFrame(np.array([list(df['Message']),
                        list(df['Summary']),
                        summs]).T, 
                       columns=['Document', 'Summary', 'Model output'])
    
    out.to_csv(f'output_{MODEL}_{QUANTIZATION}_messages.csv', index=False)