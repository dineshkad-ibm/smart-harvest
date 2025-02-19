# Fruit Ripeness Classification and Harvest Alert System

This AI-powered system classifies fruit from images, determines its ripeness, and alerts farmers when the fruit is ready for harvest.

## Features

- Classifies fruit and provides ripeness information.
- Analyzes ripeness based on classification results.
- Alerts farmers when fruit is ready for harvest.

## Requirements

- Python 3.9+
- PyTorch
- Hugging Face Transformers
- PIL
- Pydantic

## Installation

1. Clone the repository:
   git clone https://github.com/dineshkad-ibm/smart-harvest.git
   cd smart-harvest

2.Set up a virtual environment:

python3 -m venv myenv
source myenv/bin/activate

3.Install dependencies:

pip install -r requirements.txt

Add an image (e.g., fruit.jpg) of the fruit to classify.
Run the script:
python src/main.py