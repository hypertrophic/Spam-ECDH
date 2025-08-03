#!/bin/bash

set -e

if ! command -v python3 &> /dev/null; then
    echo "python3 is not installed. Please install python3."
    exit 1
fi

if ! python3 -m venv --help &> /dev/null; then
    echo "Python venv module is not available. Please install python3-venv."
    exit 1
fi

if [ ! -d "venv" ]; then
    python3 -m venv venv
    echo "Virtual environment created."
fi

source venv/bin/activate

pip install --upgrade pip
pip install "instagrapi==2.0.0"

echo "Running insta.py..."
python3 insta.py