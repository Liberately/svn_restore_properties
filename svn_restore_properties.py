import os
import subprocess


def transfer_svn_properties(source_file, target_file):
    """
    传输源文件的 SVN 属性到目标文件。

    :param source_file: 源文件路径
    :param target_file: 目标文件路径
    """
    # 定义需要传输的 SVN 属性列表
    svn_properties = [
        "svn:executable",
        "svn:mime-type",
        "svn:ignore",
        "svn:keywords",
        "svn:eol-style",
        "svn:externals",
        "svn:special",
        "svn:needs-lock"
    ]

    # 逐个属性传输
    for prop in svn_properties:
        transfer_property(prop, source_file, target_file)


def transfer_property(prop, source_file, target_file):
    """
    从源文件传输单个 SVN 属性到目标文件。

    :param prop: 属性名称
    :param source_file: 源文件路径
    :param target_file: 目标文件路径
    """
    try:
        # 尝试删除目标文件中的已有属性
        subprocess.run(["svn", "propdel", prop, target_file], check=True)
    except subprocess.CalledProcessError as e:
        pass

    try:
        # 获取源文件中的属性值
        result = subprocess.run(["svn", "propget", prop, source_file], capture_output=True, text=True, check=True)
        output = result.stdout
        if output:
            # 如果属性值存在，则将其设置到目标文件中
            subprocess.run(["svn", "propset", prop, output, target_file], check=True)
    except subprocess.CalledProcessError as e:
        print(f"设置属性 '{prop}' 到目标文件 {target_file} 时出错: {e}")
        pass


def read_paths_from_file(file_path):
    """
    从指定的文件中读取每行的文件路径。

    :param file_path: 包含文件路径的文件
    :return: 文件路径列表
    """
    try:
        # 尝试打开文件并读取每一行，去除空行
        with open(file_path, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except IOError as e:
        # 处理读取文件时的错误
        print(f"读取文件 {file_path} 时出错: {e}")
        return []


if __name__ == "__main__":

    # 定义源文件和目标文件的基目录
    diff_file = "/home/ubuntu/diff.txt"
    base_source_dir = "/home/ubuntu/source"
    base_target_dir = "/home/ubuntu/target"

    # 从文件中读取所有路径
    paths = read_paths_from_file(diff_file)

    # 遍历每个路径，将 SVN 属性从源文件传输到目标文件
    for path in paths:
        source_file = os.path.join(base_source_dir, path)
        target_file = os.path.join(base_target_dir, path)
        transfer_svn_properties(source_file, target_file)
