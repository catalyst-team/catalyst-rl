from torch import nn, optim

from catalyst_rl.contrib.nn import optimizers as module
from catalyst_rl.contrib.nn.optimizers import Lookahead


def test_criterion_init():
    model = nn.Linear(10, 10)
    for name, cls in module.__dict__.items():
        if isinstance(cls, type):
            if name == "Optimizer":
                continue
            elif cls == Lookahead:
                instance = optim.SGD(model.parameters(), lr=1e-3)
                instance = cls(instance)
            else:
                instance = cls(model.parameters(), lr=1e-3)
            assert instance is not None
