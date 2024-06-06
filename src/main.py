import json
from data_processing import read_excel_file
from image_processing import load_image, calculate_text_position, add_text_to_image, save_image
from PIL import ImageFont,Image
import os

def load_templates(template_dir):
    """
    从指定目录加载所有图片模板。

    :param template_dir: 模板目录路径
    :return: 模板图片列表
    """
    templates = []
    for filename in os.listdir(template_dir):
        if filename.endswith(('.png', '.jpg', '.jpeg')):
            templates.append(Image.open(os.path.join(template_dir, filename)))
    return templates

def load_config(config_path):
    """
    加载配置文件

    :param config_path: 配置文件路径
    :return: 配置数据
    """
    with open(config_path, 'r') as f:
        config = json.load(f)
    return config

def batch_generate_images(excel_file_path, template_dir, output_directory, font_path=None, config_path='config.json'):
    """
    批量生成图片，分别添加标题和内容。

    :param excel_file_path: Excel文件路径
    :param template_dir: 模板目录路径
    :param output_directory: 输出目录路径
    :param font_path: 字体文件路径
    :param config_path: 配置文件路径
    """
    data = read_excel_file(excel_file_path)
    templates = load_templates(template_dir)
    config = load_config(config_path)

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # 加载字体
    try:
        title_font = ImageFont.truetype(font_path, config['title_font_size']) if font_path else ImageFont.load_default()
        content_font = ImageFont.truetype(font_path, config['content_font_size']) if font_path else ImageFont.load_default()
    except OSError:
        print(f"Cannot open font resource: {font_path}. Using default font.")
        title_font = ImageFont.load_default()
        content_font = ImageFont.load_default()

    for index, entry in enumerate(data):
        sequence_number = entry['序列号']
        title = entry['标题']
        contents = entry['内容']

        for template_index, template in enumerate(templates):
            image = template.copy()
            image_size = image.size

            title_position = (
                int(image_size[0] * (config['title_position']['x_percent'] / 100)),
                int(image_size[1] * (config['title_position']['y_percent'] / 100))
            )
            image = add_text_to_image(image, title, title_position, title_font, "black")

            title_output_path = os.path.join(output_directory, f"title_{sequence_number}_{template_index}.png")
            save_image(image, title_output_path)
            print(f"Generated title image: {title_output_path}")

            image = template.copy()
            content_position = (
                int(image_size[0] * (config['content_position']['x_percent'] / 100)),
                int(image_size[1] * (config['content_position']['y_percent'] / 100))
            )
            for i, content in enumerate(contents):
                image = add_text_to_image(image, content, content_position, content_font, "black")

            content_output_path = os.path.join(output_directory, f"content_{sequence_number}_{template_index}.png")
            save_image(image, content_output_path)
            print(f"Generated content image: {content_output_path}")


if __name__ == "__main__":
    excel_file_path = "data/data.xlsx"  # 确保路径正确
    template_dir = "templates"  # 确保路径正确
    output_directory = "images/output"  # 确保路径正确
    font_path = "font/江西拙楷2.0.ttf"  # 确保路径正确

    # 调用函数时传递配置文件路径
    batch_generate_images(excel_file_path, template_dir, output_directory, font_path, config_path='config.json')
