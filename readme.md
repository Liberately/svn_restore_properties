# SVN 属性恢复脚本

## 介绍

`svn_restore_properties.py` 是一个用于恢复大量文件 SVN 属性的 Python 脚本。在文件目录结构保持一致的情况下，该脚本可以从备份目录中还原文件的 SVN 属性到目标目录，以修复意外更改的 SVN 属性。

## 功能

- **恢复 SVN 属性**: 从源目录的备份文件中读取 SVN 属性，并将这些属性设置到目标目录中的对应文件上。
- **支持属性列表**: 恢复以下 SVN 属性：
    - `svn:executable`
    - `svn:mime-type`
    - `svn:ignore`
    - `svn:keywords`
    - `svn:eol-style`
    - `svn:externals`
    - `svn:special`
    - `svn:needs-lock`

## 目录结构

假设源目录和目标目录结构相同，以下是目录结构示例：

```
source_dir/
├── path/
│   ├── file1.txt
│   ├── file2.sh
│   └── subdir/
│       └── file3.c
```

```
target_dir/
├── path/
│   ├── file1.txt
│   ├── file2.sh
│   └── subdir/
│       └── file3.c
```

## 依赖

- Python 3.6+
- SVN 客户端

## 安装

1. **安装 Python**: 确保系统安装了 Python 3.6 及以上版本。
2. **安装 SVN 客户端**: 确保系统安装了 SVN 客户端并且命令行中可以访问 `svn`。

## 使用

1. **准备路径文件**: 创建一个文件（例如 `diff.txt`），该文件列出需要恢复 SVN 属性的相对路径，每行一个路径。例如：
    ```
    path/file1.txt
    path/file2.sh
    path/subdir/file3.c
    ```

2. **运行脚本**: 在命令行中运行脚本，传输 SVN 属性：
    ```bash
    python svn_restore_properties.py
    ```

   在运行脚本之前，确保修改脚本中的 `base_source_dir` 和 `base_target_dir` 为实际的源目录和目标目录路径。

3. **脚本输出**: 脚本会输出每个文件的 SVN 属性传输结果，包括成功的操作和任何错误。

## 脚本参数

`svn_restore_properties.py` 的默认设置读取 `diff.txt` 文件中的路径，并从源目录传输 SVN 属性到目标目录。您可以通过修改脚本中的以下变量来调整脚本：

- `base_source_dir`：源目录路径，包含备份的文件。
- `base_target_dir`：目标目录路径，需要恢复 SVN 属性的文件所在目录。

## 示例

假设 `diff.txt` 文件内容如下：
```
path/file1.txt
path/file2.sh
path/subdir/file3.c
```

并且您的源目录为 `/home/user/source_backup`，目标目录为 `/home/user/target_files`，请更新脚本中的 `base_source_dir` 和 `base_target_dir`：

```python
base_source_dir = "/home/user/source_backup"
base_target_dir = "/home/user/target_files"
```

运行脚本后，`file1.txt`、`file2.sh`、`file3.c` 的 SVN 属性将从源目录恢复到目标目录。

## 故障排除

- **未找到 SVN 命令**: 确保 SVN 已正确安装，并且在系统的 PATH 环境变量中。
- **路径错误**: 确保 `diff.txt` 文件中的路径相对于 `base_source_dir` 和 `base_target_dir` 是正确的。
- **权限问题**: 如果遇到权限问题，确保脚本对源文件和目标文件具有足够的读写权限。

## 贡献

欢迎对该项目进行贡献。如果您有改进建议或发现了问题，请创建 Issue 或提交 Pull Request。

## 许可证

本项目使用 [MIT 许可证](LICENSE) 开源。

