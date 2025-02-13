# Samsara Python SDK Evaluation

To streamline and improve the developer experience when integrating the Samsara API, we will publish first party API client libraries (SDKs) starting with Python and C#.

This repository is a collection of three different Python SDKs from different vendors. The purpose of this repository is to evaluate the pros and cons of each option and to provide a reference for the Fern SDK that we will build.

## The SDKs

- [fern_samsara](./fern_samsara)
- [samsara-python](./samsara-python)
- [samsara-python-sdk](./samsara-python-sdk)

## Getting started

From the root of the project, setup a python environment. Python 3.11 is preferred (when using 3.13 you may need to set some environment variables to enable the GIL).

```bash
python -m venv venv
source venv/bin/activate
```