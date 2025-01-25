# Text Summarizer

## Description

This project uses the `Google/pegasus-cnn_dailymail` model for text summarization, fine-tuned on the SAMSum dataset. It can summarize dialogues and PDF documents, providing summaries in bullet points.

## Features

*   **Summarization:** Summarizes dialogues and PDF documents.
*   **Bullet Points:** Provides summaries in bullet points.
*   **Long Document Handling:** Handles long documents by chunking them.
*   **Streamlit App:** Includes a Streamlit app for easy summarization of uploaded PDFs.

## Usage 

This project offers two main ways to summarize text:

* **Dialogue Summarization:** Summarize conversations or dialogues.
* **PDF Summarization:**  Summarize the content of PDF documents.

(You can add a brief example of how to use each feature here, or direct users to a separate "Examples" section or your project's documentation.)

## Requirements

*   Python 3.7 or higher
*   PyTorch
*   Transformers
*   Datasets
*   Sacrebleu
*   Rouge-score
*   Py7zr
*   Accelerate
*   Pymupdf
*   Streamlit

## Installation

1.  Clone the repository: `git clone [your repository link]`
2.  Install the required packages: `pip install -r requirements.txt`

## Running the Streamlit App

1.  Navigate to the project directory.
2.  Run the command: `streamlit run text_summarizer.py`
3.  Upload a PDF file in the app and get the summarized bullet points.

## Future Enhancements

*   Fine-tune the model on a larger dataset for better performance.
*   Add support for other document formats.
*   Improve the user interface of the Streamlit app.

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests.

## Acknowledgments

*   Google for the Pegasus model.
*   Hugging Face for the Transformers library.
