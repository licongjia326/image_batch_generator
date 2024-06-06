from PIL import Image, ImageDraw, ImageFont


def load_image(image_path):
    """
    加载图像模板。

    :param image_path: 图像模板路径
    :return: 图像对象
    """
    return Image.open(image_path)


def calculate_text_position(image_size, text, font, position_type="center"):
    """
    计算文字在图像上的位置。

    :param image_size: 图像尺寸（宽，高）
    :param text: 要添加的文字
    :param font: 字体对象
    :param position_type: 文字位置类型，默认居中
    :return: 计算后的文字位置（x, y）
    """
    draw = ImageDraw.Draw(Image.new("RGB", image_size))
    text_width, text_height = draw.textsize(text, font=font)

    if position_type == "center":
        position = ((image_size[0] - text_width) // 2, (image_size[1] - text_height) // 2)
    else:
        position = (10, 10)  # 默认左上角

    return position


def add_text_to_image(image, text, position, font_path=None, font_size=20, font_color="black"):
    """
    在图像上添加文字。

    :param image: 图像对象
    :param text: 要添加的文字
    :param position: 文字位置（x, y）
    :param font_path: 字体文件路径
    :param font_size: 字体大小
    :param font_color: 字体颜色
    :return: 添加文字后的图像对象
    """
    draw = ImageDraw.Draw(image)
    if font_path:
        font = ImageFont.truetype(font_path, font_size)
    else:
        font = ImageFont.load_default()

    draw.text(position, text, font=font, fill=font_color)
    return image


def save_image(image, output_path):
    """
    保存生成的图像。

    :param image: 图像对象
    :param output_path: 保存路径
    """
    image.save(output_path)


if __name__ == "__main__":
    image_path = "path/to/template.png"  # 替换为你的图像模板路径
    output_path = "path/to/output.png"  # 替换为保存图像的路径
    text = "Hello, World!"
    position = (50, 50)
    font_path = "path/to/font.ttf"  # 可选：替换为你的字体文件路径

    # 加载图像
    image = load_image(image_path)

    # 计算文字位置
    image_size = image.size
    calculated_position = calculate_text_position(image_size, text, ImageFont.truetype(font_path,
                                                                                       20) if font_path else ImageFont.load_default(),
                                                  position_type="center")

    # 添加文字
    image_with_text = add_text_to_image(image, text, calculated_position, font_path, 20, "black")

    # 保存图像
    save_image(image_with_text, output_path)
    print(f"Image saved at: {output_path}")
