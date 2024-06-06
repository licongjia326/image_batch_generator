from PIL import Image, ImageFont
from image_processing import calculate_text_position, add_text_to_image, save_image
import os
from data_processing import read_excel_file

class ImageBatchGenerator:
    def __init__(self, config, font_path=None):
        self.config = config
        self.font_path = font_path
        self.title_font = self.load_font(config['title_font_size'])
        self.content_font = self.load_font(config['content_font_size'])

    def load_font(self, font_size):
        """
        加载字体文件

        :param font_size: 字体大小
        :return: 字体对象
        """
        try:
            return ImageFont.truetype(self.font_path, font_size) if self.font_path else ImageFont.load_default()
        except OSError:
            print(f"Cannot open font resource: {self.font_path}. Using default font.")
            return ImageFont.load_default()

    def load_templates(self, template_dir):
        """
        从指定目录加载所有图片模板

        :param template_dir: 模板目录路径
        :return: 模板图片列表
        """
        templates = []
        for filename in os.listdir(template_dir):
            if filename.endswith(('.png', '.jpg', '.jpeg')):
                templates.append(Image.open(os.path.join(template_dir, filename)))
        return templates

    def generate_images(self, excel_file_path, template_dir, output_directory):
        """
        批量生成图片，分别添加标题和内容

        :param excel_file_path: Excel文件路径
        :param template_dir: 模板目录路径
        :param output_directory: 输出目录路径
        """
        data = read_excel_file(excel_file_path)
        templates = self.load_templates(template_dir)

        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        for index, entry in enumerate(data):
            sequence_number = entry['序列号']
            title = entry['标题']
            contents = entry['内容']

            for template_index, template in enumerate(templates):
                self.generate_image_with_text(template, title, sequence_number, template_index, output_directory, 'title')
                for i, content in enumerate(contents):
                    self.generate_image_with_text(template, content, sequence_number, template_index, output_directory, 'content', i)

    def generate_image_with_text(self, template, text, sequence_number, template_index, output_directory, text_type, content_index=0):
        """
        在图片上添加文字，并保存生成的图片

        :param template: 背景图片模板
        :param text: 要添加的文字
        :param sequence_number: 序列号
        :param template_index: 模板索引
        :param output_directory: 输出目录路径
        :param text_type: 文字类型（'title' 或 'content'）
        :param content_index: 内容索引
        """
        image = template.copy()
        image_size = image.size

        if text_type == 'title':
            position = (
                int(image_size[0] * (self.config['title_position']['x_percent'] / 100)),
                int(image_size[1] * (self.config['title_position']['y_percent'] / 100))
            )
            font = self.title_font
            output_filename = f"{sequence_number}_{text[:10]}.png"
        else:
            position = (
                int(image_size[0] * (self.config['content_position']['x_percent'] / 100)),
                int(image_size[1] * (self.config['content_position']['y_percent'] / 100))
            )
            font = self.content_font
            output_filename = f"{sequence_number}_内容{content_index+1}.png"

        image = add_text_to_image(image, text, position, font, "black")
        output_path = os.path.join(output_directory, output_filename)
        save_image(image, output_path)
        print(f"Generated {text_type} image: {output_path}")
