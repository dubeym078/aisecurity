# Sentiment Analysis Demo App

This is a simple sentiment analysis web application built using [Gradio](https://gradio.app/) and [Hugging Face Transformers](https://huggingface.co/docs/transformers/). The app uses a pre-trained sentiment analysis model to classify text input as positive, negative, or neutral.

## Features

- Accepts user input text and predicts its sentiment.
- Displays the sentiment label along with the confidence score.
- Easy-to-use web interface powered by Gradio.

## Requirements

The application requires the following Python libraries:
# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment (Mac/Linux)
source venv/bin/activate

# Activate the virtual environment (Windows)
venv\Scripts\activate
- `gradio`
- `transformers`
- `torch`

These dependencies are listed in the [requirements.txt](requirements.txt) file.

## Installation

### Step 1: Clone the repository
```bash
git clone <repository-url>
cd demoApp# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment (Mac/Linux)
source venv/bin/activate
Step 3: Install dependencies
Install the required Python libraries:

Usage
Run the application using the following command:

After running the script, a Gradio interface will launch, and a link will be provided to access the app in your browser.

Gradio will run on : http://127.0.0.1:7860
It will provide UI for this chat to interact.
Use shared=true for public access url.

#How It Works

  1.  The app uses the nlptown/bert-base-multilingual-uncased-sentiment model from Hugging Face.
  2. The predict_sentiment function processes the input text and returns the sentiment label along with the confidence score.
  3. Gradio provides a simple web interface for users to interact with the model.
Example
Input:
"I love this product!"

Output:
5 stars (confidence: 0.95)

License
This project is licensed under the MIT License. See the LICENSE file for details.


