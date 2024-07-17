import subprocess
import os
import ezdxf
import matplotlib.pyplot as plt

# 参数:
# 输入文件夹
# 输出文件夹
# 输出版本: ACAD9, ACAD10, ACAD12, ACAD14, ACAD2000, ACAD2004, ACAD2007, ACAD20010, ACAD2013, ACAD2018
# 输出文件类型: DWG, DXF, DXB
# 递归输入文件夹: 0, 1
# 审核每个文件: 0, 1
# (可选) 输入文件过滤器: *.DWG, *.DXF

TEIGHA_PATH = "ODAFileConverter"
INPUT_FOLDER = r"input"
OUTPUT_FOLDER = r"input"
OUTVER = "ACAD2018"
OUTFORMAT = "DXF"
RECURSIVE = "0"
AUDIT = "1"
INPUTFILTER = "*.DWG"


def dxf_to_png(dxf_path, png_path, dpi=600):
    # 读取 DXF 文件
    doc = ezdxf.readfile(dxf_path)
    msp = doc.modelspace()

    # 创建 matplotlib 图形
    fig, ax = plt.subplots(figsize=(20, 20))  # 设置图形大小，单位为英寸

    # 绘制 DXF 数据
    for entity in msp:
        if entity.dxftype() == 'LINE':
            start = entity.dxf.start
            end = entity.dxf.end
            ax.plot([start[0], end[0]], [start[1], end[1]], color='black')

    # 设置图形参数
    ax.set_aspect('equal', 'box')
    ax.axis('off')

    # 保存为 PNG 图像，设置 dpi 参数
    plt.savefig(png_path, dpi=dpi, bbox_inches='tight', pad_inches=0)
    plt.close(fig)

def convert_folder(input_folder, output_folder, dpi=600):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 遍历输入文件夹中的所有 DXF 文件
    for filename in os.listdir(input_folder):
        if filename.endswith(".dxf"):
            dxf_path = os.path.join(input_folder, filename)
            png_path = os.path.join(output_folder, filename.replace(".dxf", ".png"))
            # 转换 DXF 到 PNG
            dxf_to_png(dxf_path, png_path, dpi=dpi)
            # 删除输入文件夹中的 DXF 文件
            os.remove(dxf_path)

if __name__ == "__main__":
    input_folder = "input"
    output_folder = "output"
    dpi = 600
    # 执行命令
    cmd = [TEIGHA_PATH, INPUT_FOLDER, OUTPUT_FOLDER, OUTVER, OUTFORMAT, RECURSIVE, AUDIT, INPUTFILTER]
    subprocess.run(cmd, shell=True)
    # 转换
    convert_folder(input_folder, output_folder, dpi=dpi)