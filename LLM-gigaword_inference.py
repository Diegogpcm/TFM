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

#     CONTEXT = """A chat between a curious human ("[[USER_NAME]]") and an artificial intelligence assistant ("[[AI_NAME]]"). The assistant gives helpful, detailed, and polite answers to the human's questions.
    
#     [[USER_NAME]]: Hello, [[AI_NAME]].
#     [[AI_NAME]]: Hello. How may I help you today?
#     [[USER_NAME]]: Please tell me the largest city in Europe.
#     [[AI_NAME]]: Sure. The largest city in Europe is Moscow, the capital of Russia.
#     [[USER_NAME]]: Summarize in 10 words: __DOC__ \n[[AI_NAME]]:"""

df = pd.read_csv("gigaword_test.csv")
df = df[(df['document'].apply(len) > 50) & df['summary'].apply(lambda x: 'UNK' not in x)].reset_index(drop=True)
k = 200
    
CONTEXT = """A chat between a curious human and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the human's questions.
USER: Summarize in 5 words: __DOC__ 
ASSISTANT:"""


for MODEL, QUANTIZATION in ALL_MODELS:
    
    llm = Llama(model_path=f"./llama.cpp/models/{MODEL}/ggml-model-{QUANTIZATION}.bin")
    
    summs = []
    for i in list(df['document'][:k]):
        query = re.sub('__DOC__', i, CONTEXT)
        output = llm(query, max_tokens=64, echo=True) #stop=["[[USER_NAME]]:"],
        print(output)
        summs.append(output['choices'][0]['text'][len(query):])
    
    out = pd.DataFrame(np.array([list(df['document'][:k]),
                        list(df['summary'][:k]),
                        summs]).T, 
                       columns=['Document', 'Summary', 'Model output'])
    
    out.to_csv(f'output_{MODEL}_{QUANTIZATION}.csv', index=False)