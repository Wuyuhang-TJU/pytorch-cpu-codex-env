# PyTorch CPU development

This repository is for CPU-only development and small training experiments.

- Run `bash scripts/setup.sh` to create the virtual environment and verify it.
- Use `.venv/bin/python` and `.venv/bin/python -m pip` for commands on Linux.
- Check the environment with `.venv/bin/python scripts/check_environment.py`.
- Check training with `.venv/bin/python examples/train_cpu.py`.
- Keep PyTorch and torchvision versions compatible. Keep the CPU wheel index.
- Do not assume CUDA or a GPU is available.
- Use `MPLBACKEND=Agg` for figures in cloud tasks.
- Keep datasets, checkpoints, credentials, and experiment outputs out of Git.
- Do not start Jupyter unless the task requires it. If needed, bind it to
  `127.0.0.1`, retain its default authentication, and use the cloud platform's
  supported preview mechanism.
