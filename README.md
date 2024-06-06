# Image Batch Generator

## 简介

该项目是一个批量在图片上添加文字的工具，通过读取Excel文件中的数据，将标题和内容分别添加到图片模板中，并生成一系列带有文字的图片。

## 项目结构


```image_batch_generator/
├── .gitignore
├── config.json
├── data/
│   └── data.xlsx
├── font/
│   └── 江西拙楷2.0.ttf
├── images/
│   ├── template.png
│   └── output/
├── src/
│   ├── data_processing.py
│   ├── image_processing.py
│   └── main.py
├── templates/
│   └── template.png
├── .venv/
```

## 功能
从Excel文件中读取数据
将标题和内容分别添加到图片模板中
生成带有文字的图片
可配置字体大小和文本位置

## 依赖安装
请确保已安装Python，并按以下步骤安装所需依赖：
pip install -r requirements.txt


## 配置文件
项目使用 config.json 配置文件来调整字体大小和文本位置。

config.json 示例
json

{
    "title_font_size": 40,
    "content_font_size": 20,
    "title_position": {
        "x_percent": 50,
        "y_percent": 10
    },
    "content_position": {
        "x_percent": 50,
        "y_percent": 50
    }
}
title_font_size：标题文本的字体大小。
content_font_size：内容文本的字体大小。
title_position：标题文本在图片中的位置，使用百分比表示。
x_percent：水平位置百分比。
y_percent：垂直位置百分比。
content_position：内容文本在图片中的位置，使用百分比表示。
x_percent：水平位置百分比。
y_percent：垂直位置百分比。


## 使用方法
准备数据文件 data/data.xlsx，其中包含需要添加到图片中的内容。
配置模板图片 templates/template.png 和字体文件 font/江西拙楷2.0.ttf。
运行批量生成脚本：

python src/main.py
生成的图片将保存在 images/output 目录中。
## 项目逻辑
读取配置文件：加载 config.json 以获取字体大小和文本位置。
读取Excel数据：使用 data_processing.py 中的函数读取 data/data.xlsx 文件中的数据。
加载图片模板：从 templates 目录加载背景图片模板。
处理每条数据：
生成带有标题的图片：根据配置文件中的字体大小和位置，将标题添加到背景图片中。
生成带有内容的图片：根据配置文件中的字体大小和位置，将内容添加到背景图片中。
保存图片：将生成的图片保存到 images/output 目录中。
贡献
欢迎提交问题和功能请求，或通过提交PR来贡献代码。

## 许可证
本项目使用 MIT License。

