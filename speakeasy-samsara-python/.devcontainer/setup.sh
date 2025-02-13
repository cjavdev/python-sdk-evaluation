#!/bin/bash

# Install the speakeasy CLI
curl -fsSL https://raw.githubusercontent.com/speakeasy-api/speakeasy/main/install.sh | sh

# Setup samples directory
rmdir samples || true
mkdir samples

python -m pip install --upgrade pip
pip install -e .

# Generate starter usage sample with speakeasy
speakeasy generate usage -s https://developers.samsara.com/openapi/5f4d3be3f2168e0024cb1741 -l python -o samples/root.py