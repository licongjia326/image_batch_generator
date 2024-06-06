import torch
from llama_cpp import Llama


class LlamaModel:
    """
    LLaMA 模型类，用于加载本地的 GGUF 格式的 LLaMA 模型并生成文本。
    """

    def __init__(self, model_file):
        """
        初始化 LLaMA 模型。

        参数:
        model_file (str): 存储预训练模型文件的本地路径。
        """
        self.model = Llama(model_path=model_file, n_ctx=2048, n_batch=126)
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        if self.device == "cuda":
            self.model.to(self.device)

    def generate_text(self, input_text, max_tokens=128, temperature=0.7, top_p=0.9, stop=None):
        """
        根据输入文本生成新文本。

        参数:
        input_text (str): 输入的文本。
        max_tokens (int): 生成的最大 token 数量。
        temperature (float): 采样温度。
        top_p (float): nucleus 采样参数。
        stop (list of str): 停止生成的标志符列表。

        返回:
        str: 生成的文本。
        """
        output = self.model(
            prompt=input_text,
            max_tokens=max_tokens,
            temperature=temperature,
            top_p=top_p,
            stop=stop
        )
        return output['choices'][0]['text'].strip()
