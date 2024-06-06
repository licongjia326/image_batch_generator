import pandas as pd


def read_excel_file(file_path):
    """
    读取Excel文件，并返回处理后的数据。

    :param file_path: Excel文件路径
    :return: 结构化的数据列表
    """
    df = pd.read_excel(file_path)

    # 数据验证与清洗
    df = df.dropna(subset=['序列号', '标题'])  # 删除序列号和标题为空的行
    df = df.reset_index(drop=True)  # 重置索引

    # 数据结构化
    structured_data = []
    for index, row in df.iterrows():
        entry = {
            '序列号': row['序列号'],
            '标题': row['标题'],
            '内容': [row[f'内容{i}'] for i in range(1, 7) if pd.notna(row[f'内容{i}'])]  # 获取非空内容
        }
        structured_data.append(entry)

    return structured_data


if __name__ == "__main__":
    file_path = "path/to/your/excel/file.xlsx"  # 替换为你的Excel文件路径
    data = read_excel_file(file_path)
    for entry in data:
        print(entry)
