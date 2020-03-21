<div align="center">

[![Catalyst logo](https://raw.githubusercontent.com/catalyst-team/catalyst-pics/master/pics/catalyst_logo.png)](https://github.com/catalyst-team/catalyst)

**Accelerated RL**

[![Build Status](http://66.248.205.49:8111/app/rest/builds/buildType:id:Catalyst_Deploy/statusIcon.svg)](http://66.248.205.49:8111/project.html?projectId=Catalyst&tab=projectOverview&guest=1)
[![CodeFactor](https://www.codefactor.io/repository/github/catalyst-team/catalyst/badge)](https://www.codefactor.io/repository/github/catalyst-team/catalyst)
[![Pipi version](https://img.shields.io/pypi/v/catalyst.svg)](https://pypi.org/project/catalyst/)
[![Docs](https://img.shields.io/badge/dynamic/json.svg?label=docs&url=https%3A%2F%2Fpypi.org%2Fpypi%2Fcatalyst%2Fjson&query=%24.info.version&colorB=brightgreen&prefix=v)](https://catalyst-team.github.io/catalyst/index.html)
[![PyPI Status](https://pepy.tech/badge/catalyst)](https://pepy.tech/project/catalyst)

[![Twitter](https://img.shields.io/badge/news-on%20twitter-499feb)](https://twitter.com/catalyst_core)
[![Telegram](https://img.shields.io/badge/channel-on%20telegram-blue)](https://t.me/catalyst_team)
[![Slack](https://img.shields.io/badge/ODS-slack-red)](https://opendatascience.slack.com/messages/CGK4KQBHD)
[![Github contributors](https://img.shields.io/github/contributors/catalyst-team/catalyst.svg?logo=github&logoColor=white)](https://github.com/catalyst-team/catalyst/graphs/contributors)

</div>

PyTorch framework for RL research.
It was developed with a focus on reproducibility,
fast experimentation and code/ideas reusing.
Being able to research/develop something new,
rather than write another regular train loop. <br/>
Break the cycle - use the Catalyst!

Part of [PyTorch Ecosystem](https://pytorch.org/ecosystem/). Part of [Catalyst Ecosystem](https://docs.google.com/presentation/d/1D-yhVOg6OXzjo9K_-IS5vSHLPIUxp1PEkFGnpRcNCNU/edit?usp=sharing). Project [manifest](https://github.com/catalyst-team/catalyst/blob/master/MANIFEST.md).

---

## Installation

Common installation:
```bash
pip install -U catalyst-rl
```

Catalyst.RL is compatible with: Python 3.6+. PyTorch 1.0.0+.


## Getting started

For Catalyst.RL introduction, please follow [OpenAI Gym example](https://github.com/catalyst-team/catalyst-rl/tree/master/examples/rl_gym).


#### Docs and examples
- [Demo with minimal examples](https://github.com/catalyst-team/catalyst/tree/master/examples/notebooks/demo.ipynb) for CV, NLP, RecSys and GANs [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/catalyst-team/catalyst/blob/master/examples/notebooks/demo.ipynb)
- Detailed [classification tutorial](https://github.com/catalyst-team/catalyst/tree/master/examples/notebooks/classification-tutorial.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/catalyst-team/catalyst/blob/master/examples/notebooks/classification-tutorial.ipynb)
- Advanced [segmentation tutorial](https://github.com/catalyst-team/catalyst/tree/master/examples/notebooks/segmentation-tutorial.ipynb) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/catalyst-team/catalyst/blob/master/examples/notebooks/segmentation-tutorial.ipynb)
- Comprehensive [classification pipeline](https://github.com/catalyst-team/classification)
- Binary and semantic [segmentation pipeline](https://github.com/catalyst-team/segmentation)

API documentation and an overview of the library can be found here
[![Docs](https://img.shields.io/badge/dynamic/json.svg?label=docs&url=https%3A%2F%2Fpypi.org%2Fpypi%2Fcatalyst%2Fjson&query=%24.info.version&colorB=brightgreen&prefix=v)](https://catalyst-team.github.io/catalyst/index.html). <br/>
In the **[examples folder](examples)**
of the repository, you can find advanced tutorials and Catalyst best practices.

##### Infos
To learn more about Catalyst internals and to be aware of the most important features, you can read **[Catalyst-info](https://github.com/catalyst-team/catalyst-info)** – our blog where we regularly write facts about the framework.

We also supervise **[Awesome Catalyst list](https://github.com/catalyst-team/awesome-catalyst-list)** – Catalyst-powered projects, tutorials and talks. <br/>
Feel free to make a PR with your project to the list. And don't forget to check out current list, there are many interesting projects.

##### Releases
We deploy a major release once a month with a name like `YY.MM`. <br/>
And micro-releases with framework improvements during a month in the format `YY.MM.#`.

You can view the changelog on the **[GitHub Releases](https://github.com/catalyst-team/catalyst/releases)** page. <br/>
Current version: [![Pipi version](https://img.shields.io/pypi/v/catalyst.svg)](https://pypi.org/project/catalyst/)


## Overview

Catalyst.RL helps you write compact
but full-featured RL pipelines in a few lines of code.
You get a training loop with metrics, early-stopping, model checkpointing
and other features without the boilerplate.

#### Features

- Universal train/inference loop.
- Configuration files for model/data hyperparameters.
- Reproducibility – all source code and environment variables will be saved.
- Callbacks – reusable train/inference pipeline parts.
- Training stages support.
- Easy customization.
- PyTorch best practices (SWA, AdamW, Ranger optimizer, OneCycle, FP16 and more).

#### Structure

- **RL** – scalable Reinforcement Learning,
   all popular model-free algorithms implementations and their improvements
   with distributed training support.
- **contrib** - additional modules contributed by Catalyst users.
- **utils** - different useful utils for Deep Learning research.

## Contribution guide

We appreciate all contributions.
If you are planning to contribute back bug-fixes,
please do so without any further discussion.
If you plan to contribute new features, utility functions or extensions,
please first open an issue and discuss the feature with us.

- Please see the [contribution guide](CONTRIBUTING.md) for more information.
- By participating in this project, you agree to abide by its [Code of Conduct](CODE_OF_CONDUCT.md).

## License

This project is licensed under the Apache License, Version 2.0 see the [LICENSE](LICENSE) file for details
[![License](https://img.shields.io/github/license/catalyst-team/catalyst.svg)](LICENSE)

## Citation

Please use this bibtex if you want to cite this repository in your publications:

    @misc{catalyst,
        author = {Kolesnikov, Sergey},
        title = {Accelerated RL.},
        year = {2018},
        publisher = {GitHub},
        journal = {GitHub repository},
        howpublished = {\url{https://github.com/catalyst-team/catalyst-rl}},
    }
