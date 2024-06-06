from data_processing import read_excel_file
from image_processing import load_image, calculate_text_position, add_text_to_image, save_image
import os
from PIL import Image, ImageDraw, ImageFont

def batch_generate_images(excel_file_path, image_template_path, output_directory, font_path=None):
    data = read_excel_file(excel_file_path)

    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for entry in data:
        sequence_number = entry['序列号']
        title = entry['标题']
        contents = entry['内容']

        image = load_image(image_template_path)
        image_size = image.size

        # 计算并添加标题
        title_position = calculate_text_position(image_size, title, ImageFont.truetype(font_path,
                                                                                       20) if font_path else ImageFont.load_default(),
                                                 position_type="top")
        image = add_text_to_image(image, title, title_position, font_path, 20, "black")

        # 计算并添加内容
        for i, content in enumerate(contents):
            content_position = calculate_text_position(image_size, content, ImageFont.truetype(font_path,
                                                                                               15) if font_path else ImageFont.load_default(),
                                                       position_type=f"content_{i}")
            image = add_text_to_image(image, content, content_position, font_path, 15, "black")

        output_path = os.path.join(output_directory, f"image_{sequence_number}.png")
        save_image(image, output_path)
        print(f"Generated image: {output_path}")


if __name__ == "__main__":
    excel_file_path = "data/data.xlsx"
    image_template_path = "images/template.png"
    output_directory = "images/output"
    font_path = "path/to/font.ttf"

    batch_generate_images(excel_file_path, image_template_path, output_directory, font_path)
