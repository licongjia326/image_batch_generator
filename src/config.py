import json

def load_config(config_path):
    """
    加载配置文件

    :param config_path: 配置文件路径
    :return: 配置数据（字典形式）
    """
    with open(config_path, 'r') as f:
        config = json.load(f)
    return config
