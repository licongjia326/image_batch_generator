from llama import Llama

model_path = "../model_file/ggml-model-Q5_1.gguf"
llama_model = Llama(model_path=model_path)

def generate_text(prompt):
    output = llama_model(prompt=prompt, max_tokens=128, temperature=0.7, top_p=0.9)
    return output['choices'][0]['text'].strip()

print(generate_text("你好，LLaMA 模型！"))
