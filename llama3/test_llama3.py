from time import sleep

from llama_cpp import Llama

# 指定模型文件路径
model_path = "../model_file/Meta-Llama-3-8B.Q2_K.gguf"

# 加载模型
llm = Llama(model_path=model_path)

# 与模型进行对话
while True:
    sleep(2)
    user_input = input("User: ")
    if user_input.lower() == "quit":
        break

    # 生成模型响应
    output = llm(user_input, max_tokens=100, stop=["User:", "\n"], echo=True)

    # 提取生成的文本
    generated_text = output["choices"][0]["text"]

    # 打印生成的文本
    print(generated_text.strip())