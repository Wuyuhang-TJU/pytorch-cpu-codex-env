# PyTorch CPU 环境 · Codex Cloud

**一句话：这是 Codex Cloud 云端环境 `pytorch-cpu` 的配置仓库——一键装好固定版本的 PyTorch（仅 CPU）和常用科学计算库，并自动验证环境可用，用于在云端写代码、做张量计算和小规模模型训练。**

本仓库不放项目代码，只放搭建这个环境所需的依赖清单、安装脚本和验证示例；云端环境本身在 Codex 中配置并发布。

## 仓库内容

| 文件 | 作用 |
|---|---|
| `requirements-torch-cpu.txt` | PyTorch 2.7.0、torchvision 0.22.0（官方 CPU wheel 源） |
| `requirements.txt` | numpy、pandas、scipy、matplotlib、scikit-learn、JupyterLab、tqdm、pytest（固定版本） |
| `scripts/setup.sh` | 创建 `.venv`、安装依赖并运行两项验证（Codex 的安装脚本） |
| `scripts/check_environment.py` | 检查是 CPU 版 PyTorch、各库能导入、自动求导正常 |
| `examples/train_cpu.py` | 用合成数据训练 `y = 3x + 2`，检查训练能收敛 |
| `AGENTS.md` | 给 Codex 的使用约定（用 `.venv/bin/python`、不假设有 GPU 等） |
| `CODEX_ENVIRONMENT_SETUP.txt` | 在 Codex 中创建该环境时可直接粘贴的配置说明 |

## 依赖

推荐 Python 3.12；安装脚本支持 Python 3.10–3.13。
使用兼容的固定版本 PyTorch 2.7.0、torchvision 0.22.0 和官方 CPU wheel 源。
科学计算依赖、JupyterLab、tqdm 和 pytest 在 requirements.txt 中固定版本。

版本选择用于保持这套初始配置兼容和可复现，不代表最新版本。

## 在 Codex Cloud 配置

1. 在 Codex 的 `设置 → Codex Cloud → Environments → Create environment`
   中选择 `Wuyuhang-TJU/pytorch-lab`。也可以从新任务的
   `Work in → Cloud → Select environment` 进入创建环境。
2. 环境名称使用 `pytorch-cpu`，仅限本人使用。
3. 在环境配置对话中要求使用 Python 3.12，执行 `bash scripts/setup.sh`。
   若页面有 Install script（安装脚本）字段，填入相同命令。
4. 安装依赖需要访问官方软件包源。使用 Package managers 网络预设，并按实际
   安装报错补充 `pypi.org`、`files.pythonhosted.org`、`download.pytorch.org`、
   `download-r2.pytorch.org`
   以及下载时明确报告的官方 CDN 域名。
5. 确认环境检查和训练示例通过，保存配置并 Publish。
   等待显示 Environment published 后，再从该环境开始新任务。

Codex Cloud 的设置位于 Codex 中。GitHub 仓库用于存放代码和依赖文件；
GitHub 仓库 Settings 中的 Environments 不是这里的计算环境。

## 使用

在仓库根目录运行：

```bash
bash scripts/setup.sh
.venv/bin/python scripts/check_environment.py
.venv/bin/python examples/train_cpu.py
```

验证不下载数据集。训练示例使用合成数据拟合 `y = 3x + 2`，检查梯度更新、
损失收敛和参数数值是否符合预期。

云端任务中使用 `.venv/bin/python`，无需依赖终端激活状态。

## 官方资料

- [Codex Cloud 环境](https://learn.chatgpt.com/docs/environments/cloud-environments)
- [PyTorch 安装说明](https://pytorch.org/get-started/locally/)
- [PyTorch 固定版本安装与 CPU wheel 命令](https://pytorch.org/get-started/previous-versions/)
