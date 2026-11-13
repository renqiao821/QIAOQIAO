# QIAOQIAO

个人项目与实验代码的归档仓库。

## 说明

本仓库用于存放个人开发过程中的项目代码、脚本与实验记录，内容会随进度持续补充。

## 目录约定

| 目录 | 用途 |
| --- | --- |
| `docs/` | 设计说明与笔记 |
| `src/` | 主要代码 |
| `scripts/` | 辅助脚本与工具 |

项目采用 `src` 布局：

```
src/qiaoqiao/     包源码
tests/            单元测试
pyproject.toml    项目配置
```

## 使用方式

```bash
git clone git@github.com:renqiao821/QIAOQIAO.git
cd QIAOQIAO
python -m pip install -e .
qiaoqiao
```

不安装也可以直接运行：

```bash
python -m qiaoqiao        # 需先设置 PYTHONPATH=src
```

运行测试：

```bash
python -m unittest discover -s tests -v
```

## 许可

如无特别说明，仓库内代码仅用于个人学习与研究。