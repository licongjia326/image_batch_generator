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

def batch_generate_images(excel_file_path, template_dir, output_directory, font_path=None, title_font_size=40, content_font_size=20):
    """
    批量生成图片，分别添加标题和内容。

    :param excel_file_path: Excel文件路径
    :param template_dir: 模板目录路径
    :param output_directory: 输出目录路径
    :param font_path: 字体文件路径
    :param title_font_size: 标题字体大小
    :param content_font_size: 内容字体大小
    """
    data = read_excel_file(excel_file_path)
    templates = load_templates(template_dir)

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # 加载字体
    try:
        title_font = ImageFont.truetype(font_path, title_font_size) if font_path else ImageFont.load_default()
        content_font = ImageFont.truetype(font_path, content_font_size) if font_path else ImageFont.load_default()
    except OSError:
        print(f"Cannot open font resource: {font_path}. Using default font.")
        title_font = ImageFont.load_default()
        content_font = ImageFont.load_default()

    for index, entry in enumerate(data):
        sequence_number = entry['序列号']
        title = entry['标题']
        contents = entry['内容']

        # 每条内容使用不同的背景图片模板
        for template_index, template in enumerate(templates):
            # 生成标题图片
            image = template.copy()
            image_size = image.size

            # 计算并添加标题
            title_position, adjusted_title_font = calculate_text_position(image_size, title, title_font, position_type="center")
            image = add_text_to_image(image, title, title_position, adjusted_title_font, "black")

            # 保存标题图片
            title_output_path = os.path.join(output_directory, f"title_{sequence_number}_{template_index}.png")
            save_image(image, title_output_path)
            print(f"Generated title image: {title_output_path}")

            # 生成内容图片
            image = template.copy()
            for i, content in enumerate(contents):
                content_position, adjusted_content_font = calculate_text_position(image_size, content, content_font, position_type="center")
                image = add_text_to_image(image, content, content_position, adjusted_content_font, "black")

            # 保存内容图片
            content_output_path = os.path.join(output_directory, f"content_{sequence_number}_{template_index}.png")
            save_image(image, content_output_path)
            print(f"Generated content image: {content_output_path}")

if __name__ == "__main__":
    excel_file_path = "data/data.xlsx"  # 确保路径正确
    template_dir = "templates"  # 确保路径正确
    output_directory = "images/output"  # 确保路径正确
    font_path = "font/江西拙楷2.0.ttf"  # 确保路径正确

    # 调用函数时可以手动设置标题和内容的字体大小
    batch_generate_images(excel_file_path, template_dir, output_directory, font_path, title_font_size=100, content_font_size=80)
