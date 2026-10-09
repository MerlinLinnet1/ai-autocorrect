# AI Autocorrect Tool

A Python-based autocorrect application that uses TextBlob
to correct spelling mistakes through a simple web interface.

## Features
- Accepts text from users
- Suggests spelling corrections
- Displays original and corrected text
- Simple web interface using Streamlit

## Technologies Used
- Python
- TextBlob
- Streamlit

## How to Run

1. Install Python 3.11 or later.
2. Install the required libraries:

   pip install -r requirements.txt

3. Run the application:

   python -m streamlit run app.py

4. Open the local URL shown in the terminal.

## Limitations

TextBlob may incorrectly change words that are already
correct. It may also fail to detect errors that depend
on sentence context.

## Future Improvements
- Context-aware correction using a pretrained language model
- Improved correction suggestions
- Automated testing
- Online deployment
