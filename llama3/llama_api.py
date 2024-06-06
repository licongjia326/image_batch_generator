from llama_model import LlamaModel
from conversation_manager import ConversationManager


class LlamaAPI:
    """
    LLaMA API 类，提供对外的 API 接口。
    """

    def __init__(self, model_file):
        """
        初始化 LLaMA API。

        参数:
        model_file (str): 存储预训练模型文件的本地路径。
        """
        self.llama_model = LlamaModel(model_file)
        self.conversation_manager = ConversationManager(self.llama_model)

    def generate_response(self, user_input):
        """
        生成对用户输入的响应。

        参数:
        user_input (str): 用户的输入文本。

        返回:
        str: 模型生成的响应。
        """
        return self.conversation_manager.get_response(user_input)

    def clear_conversation(self):
        """
        清除对话上下文。
        """
        self.conversation_manager.clear_context()
