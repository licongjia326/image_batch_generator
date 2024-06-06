class ConversationManager:
    """
    对话管理类，用于管理多轮对话的上下文。
    """

    def __init__(self, model):
        """
        初始化对话管理器。

        参数:
        model (LlamaModel): 已初始化的 LLaMA 模型实例。
        """
        self.model = model
        self.context = []

    def add_user_input(self, user_input):
        """
        添加用户输入到上下文中。

        参数:
        user_input (str): 用户的输入文本。
        """
        self.context.append(f"用户: {user_input}")

    def get_response(self, user_input):
        """
        获取模型的响应，并更新上下文。

        参数:
        user_input (str): 用户的输入文本。

        返回:
        str: 模型生成的响应。
        """
        self.add_user_input(user_input)
        context_text = "\n".join(self.context)
        response = self.model.generate_text(context_text)
        self.context.append(f"模型: {response}")
        return response

    def clear_context(self):
        """
        清除对话上下文。
        """
        self.context = []
