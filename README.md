# Pieces-ChatBot-Loadtest

This repo holds all code related to a pieces chatbot for a simple load test.

## How to run the chatbot

1. Clone the repo
2. Run `python -m venv .venv` to create a virtual environment
3. Run `source .venv/bin/activate` to activate the virtual environment (on Windows, run `.venv\Scripts\activate`)
4. Run `pip install -r requirements.txt` to install the required packages
5. Create a `.env` file in the root directory and add the following variables:

    ```bash
    PIECES_INSTANCE_HOST=your_instance_host (default is localhost)
    PIECES_INSTANCE_PORT=your_instance_port (default is 1000 for Windows / MacOS and 5323 for Linux)
    ```

6. Run `streamlit run app.py` to start the chatbot

Now you can open `http://localhost:8501/` in your browser to check the connection the piecesOS and start chatting with the chatbot.

## Gratifications

- [Streamlit](https://streamlit.io/)
- [Pieces](https://pieces.app)
- Special thanks to [Shivay](https://github.com/shivay-at-pieces) and his [Chatbot Demo](https://github.com/pieces-app/pieces-copilot-streamlit-example)
