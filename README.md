# DWG to PNG Converter

这是一个用 Python 编写的小工具，用于将 DWG 文件转换成 PNG 文件。

## 简介

DWG to PNG Converter 是一个简单易用的工具，可以将 DWG 文件批量转换为 PNG 格式。它使用 Python 编写，依赖 Open Design Alliance 的文件转换工具。

## 安装

请按照以下步骤安装和配置环境：

1. 克隆本项目：

    ```bash
    git clone https://github.com/Sherlock-Holmos/dwg_to_png.git
    cd dwg_to_png
    ```

2. 建立 Python 环境（推荐使用 Anaconda）：

    ```bash
    conda create --name dwg_to_png python=3.x
    conda activate dwg_to_png
    ```

3. 安装所需的 Python 库：

    ```bash
    pip install -r requirements.txt
    ```

4. 前往 [Open Design Alliance](https://www.opendesign.com/guestfiles/oda_file_converter) 网站下载 ODA 文件转换工具，并将工具的安装地址添加到系统环境变量中。

5. 在项目目录下新建两个文件夹 `input` 和 `output`。

## 使用方法

1. 将需要转换的 DWG 文件放入 `input` 文件夹中。

2. 运行 Python 脚本：

    ```bash
    python convert.py
    ```

3. 转换后的 PNG 文件将生成在 `output` 文件夹中。

## 功能

- 批量转换 DWG 文件为 PNG 格式
