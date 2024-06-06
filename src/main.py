import argparse
from config import load_config
from generator import ImageBatchGenerator


def main():
    parser = argparse.ArgumentParser(description='批量生成带有文字的图片')
    parser.add_argument('--config', type=str, default='config.json', help='配置文件路径')
    parser.add_argument('--excel', type=str, default='data/data.xlsx', help='Excel文件路径')
    parser.add_argument('--template_dir', type=str, default='templates', help='模板目录路径')
    parser.add_argument('--output_dir', type=str, default='images/output', help='输出目录路径')
    parser.add_argument('--font', type=str, default='font/江西拙楷2.0.ttf', help='字体文件路径')

    args = parser.parse_args()

    config = load_config(args.config)
    generator = ImageBatchGenerator(config, args.font)
    generator.generate_images(args.excel, args.template_dir, args.output_dir)


if __name__ == "__main__":
    main()
