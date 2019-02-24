# huelights

![python](https://img.shields.io/pypi/pyversions/huelights.svg)
[![pypi](https://img.shields.io/pypi/v/huelights.svg?color=blue)](https://pypi.org/project/huelights/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

A Python wrapper to interact with Philips Hue smart lights

## Installation

Install from PyPI:

`pip install huelights`

## Example

A small example for interacting with your Philips Bridge to manipulate Philips Hue smart lights:

```python
from huelights.bridge import Bridge

bridge = Bridge('username')

lights = bridge.get_lights()

for light in lights:
    light.effect = 'colorloop'
```
