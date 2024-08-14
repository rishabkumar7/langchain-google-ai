# Discover the Power of LangChain

Welcome to the repository for the "Discover the Power of LangChain" talk presented at Google Developer Group. This project demonstrates how to leverage LangChain to build a Stoic assistant that answers questions and provides guidance based on Stoic philosophy.

## Table of Contents

- [Introduction](#introduction)
- [Setup](#setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project showcases the integration of various LangChain components to create a Stoic assistant. The assistant uses language models, embeddings, and vector stores to provide insightful responses to user queries.

## Setup

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. **Install the required dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

3. **Set up environment variables:**

    Copy the `.env.example` file to `.env` and fill in the required API keys.

    ```sh
    cp .env.example .env
    ```

    Update the `.env` file with your API keys:

    ```env
    PINECONE_API_KEY=your_pinecone_api_key
    PINECONE_ENV=your_pinecone_env
    OPENAI_API_KEY=your_openai_api_key
    GOOGLE_API_KEY=your_google_api_key
    ```

## Usage

1. **Run the main application:**

    ```sh
    python main.py
    ```

    This will invoke the 'ask_stoic` function and print the response to the console.

2. **Run the Streamlit app:**

    ```sh
    streamlit run streamlit.py
    ```

    This will start a Streamlit web application where you can interact with the Stoic assistant.

## Project Structure

- `app.py`: Contains the main logic for querying the language model and vector store.
- `knowldge-base/knowledge_base.py`: Handles loading and processing of documents, and setting up the Pinecone vector store.
- `main.py`: Entry point for running the application.
- `streamlit.py`: Streamlit application for interacting with the Stoic assistant.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE]() file for details.

## Author

- Twitter: [@rishabincloud](https://x.com/rishabincloud)
- LinkedIn: [rishabkumar7](https://linkedin.com/in/rishabkumar7)
