"""Check CPU-only PyTorch, scientific packages, and autograd without downloads."""

import json
import platform

import matplotlib
import numpy as np
import pandas as pd
import scipy
import sklearn
import torch
import torchvision


def main():
    assert torch.version.cuda is None, "Expected a CPU-only PyTorch build."
    assert torch.version.hip is None, "Expected a CPU-only PyTorch build."
    assert not torch.cuda.is_available(), "This environment is configured for CPU."

    x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
    (x.square().sum()).backward()
    torch.testing.assert_close(x.grad, torch.tensor([2.0, 4.0, 6.0]))
    np.testing.assert_allclose(np.array([1.0, 2.0]) * 2, [2.0, 4.0])
    assert pd.DataFrame({"value": [1, 2]}).value.sum() == 3

    report = {
        "python": platform.python_version(),
        "platform": platform.platform(),
        "device": "cpu",
        "torch": torch.__version__,
        "torchvision": torchvision.__version__,
        "numpy": np.__version__,
        "pandas": pd.__version__,
        "scipy": scipy.__version__,
        "matplotlib": matplotlib.__version__,
        "scikit_learn": sklearn.__version__,
        "autograd": "passed",
    }
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
