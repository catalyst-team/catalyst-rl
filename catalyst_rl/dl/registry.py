from catalyst_rl.contrib.registry import (
    Criterion, CRITERIONS, GRAD_CLIPPERS, Model, MODELS, Module, MODULES,
    Optimizer, OPTIMIZERS, Sampler, SAMPLERS, Scheduler, SCHEDULERS, Transform,
    TRANSFORMS
)
from catalyst_rl.core.registry import Callback, CALLBACKS
from catalyst_rl.utils.tools.registry import Registry


def _callbacks_loader(r: Registry):
    from catalyst_rl.dl import callbacks as m
    r.add_from_module(m)


CALLBACKS.late_add(_callbacks_loader)

__all__ = [
    "Callback",
    "Criterion",
    "Optimizer",
    "Scheduler",
    "Module",
    "Model",
    "Sampler",
    "Transform",
    "CALLBACKS",
    "CRITERIONS",
    "GRAD_CLIPPERS",
    "MODELS",
    "MODULES",
    "OPTIMIZERS",
    "SAMPLERS",
    "SCHEDULERS",
    "TRANSFORMS",
]
