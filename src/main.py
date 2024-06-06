from data_processing import read_excel_file
from image_processing import load_image, calculate_text_position, add_text_to_image, save_image
from PIL import ImageFont
import os

def batch_generate_images(excel_file_path, image_template_path, output_directory, font_path=None):
    data = read_excel_file(excel_file_path)

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # 加载字体
    try:
        title_font = ImageFont.truetype(font_path, 20) if font_path else ImageFont.load_default()
        content_font = ImageFont.truetype(font_path, 15) if font_path else ImageFont.load_default()
    except OSError:
        print(f"Cannot open font resource: {font_path}. Using default font.")
        title_font = ImageFont.load_default()
        content_font = ImageFont.load_default()

    for entry in data:
        sequence_number = entry['序列号']
        title = entry['标题']
        contents = entry['内容']

        image = load_image(image_template_path)
        image_size = image.size

        # 计算并添加标题
        title_position = calculate_text_position(image_size, title, title_font, position_type="center")
        image = add_text_to_image(image, title, title_position, title_font, "black")

        # 计算并添加内容
        for i, content in enumerate(contents):
            content_position = calculate_text_position(image_size, content, content_font, position_type="center")
            image = add_text_to_image(image, content, content_position, content_font, "black")

        output_path = os.path.join(output_directory, f"image_{sequence_number}.png")
        save_image(image, output_path)
        print(f"Generated image: {output_path}")

if __name__ == "__main__":
    # 使用绝对路径确保文件路径正确
    excel_file_path = "/Users/qiao/PycharmProjects/image_batch_generator/data/data.xlsx"
    image_template_path = "/Users/qiao/PycharmProjects/image_batch_generator/images/template.png"
    output_directory = "/Users/qiao/PycharmProjects/image_batch_generator/images/output"
    font_path = "/Users/qiao/PycharmProjects/image_batch_generator/font/江西拙楷2.0.ttf"  # 确认路径是否正确

    batch_generate_images(excel_file_path, image_template_path, output_directory, font_path)
