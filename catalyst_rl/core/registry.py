from catalyst_rl.contrib.registry import (
    Criterion, CRITERIONS, GRAD_CLIPPERS, Model, MODELS, Module, MODULES,
    Optimizer, OPTIMIZERS, Sampler, SAMPLERS, Scheduler, SCHEDULERS, Transform,
    TRANSFORMS
)
from catalyst_rl.utils.tools.registry import Registry


def _callbacks_loader(r: Registry):
    from catalyst_rl.core import callbacks as m
    r.add_from_module(m)


CALLBACKS = Registry("callback")
CALLBACKS.late_add(_callbacks_loader)
Callback = CALLBACKS.add

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
