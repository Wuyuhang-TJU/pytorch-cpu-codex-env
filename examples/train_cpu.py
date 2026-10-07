"""Fit y = 3x + 2 with CPU PyTorch; fail if training does not converge."""

import json

import torch


def main():
    torch.manual_seed(42)
    torch.set_num_threads(2)
    x = torch.linspace(-1, 1, 128, device="cpu").reshape(-1, 1)
    y = 3 * x + 2
    model = torch.nn.Linear(1, 1).to("cpu")
    optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
    loss_fn = torch.nn.MSELoss()

    with torch.no_grad():
        initial_loss = loss_fn(model(x), y).item()
    for _ in range(200):
        optimizer.zero_grad()
        loss = loss_fn(model(x), y)
        loss.backward()
        optimizer.step()
    with torch.no_grad():
        final_loss = loss_fn(model(x), y).item()
        assert final_loss < 1e-6, f"Training failed to converge: {final_loss}"
        assert final_loss < initial_loss
        assert abs(model.weight.item() - 3.0) < 0.01
        assert abs(model.bias.item() - 2.0) < 0.01

    print(json.dumps({
        "device": "cpu",
        "initial_loss": initial_loss,
        "final_loss": final_loss,
        "weight": model.weight.item(),
        "bias": model.bias.item(),
        "training": "passed",
    }, indent=2))


if __name__ == "__main__":
    main()
