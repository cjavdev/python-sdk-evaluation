# Samsara Python SDK Evaluation

To streamline and improve the developer experience when integrating the Samsara API, we will publish first party API client libraries (SDKs) starting with Python and C#.

This repository is a collection of three different Python SDKs from different vendors. The purpose of this repository is to evaluate the pros and cons of each option and to provide a reference for the Fern SDK that we will build.

## The SDKs

- [Fern](./fern_samsara)
- [Stainless](./stainless_samsara)
- [Speakeasy](./speakeasy_samsara)

## Before you begin

Make a new `.env` file in the root of the project and add your Samsara API key.

```bash
mv .env.example .env
```

Set your Samsara API key in the `.env` file.

```yaml
SAMSARA_API_KEY=your_api_key
```

## Getting started

From the root of the project, setup a python environment. Python 3.11 is preferred (when using 3.13 you may need to set some environment variables to enable the GIL).

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running the examples

```bash
python stainless_example.py
python speakeasy_example.py
python fern_example.py
```

## Run the server

```bash
python server.py
```
