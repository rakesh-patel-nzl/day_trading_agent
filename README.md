# day_trading_agent

Just trying out [browser-use](https://browser-use.com/). In this test script, we navigate to the [BlackBox Stocks Options Page](https://members.blackboxstocks.com/) and retrieve a list of stocks with "Bullish Flow."

Browser-Use makes use of APIs from some of the most common LLMs. It recommends GPT-4o. However, it also supports Anthropic, Azure OpenAI, Gemini, DeepSeek, and Ollama. Ollama can be used as a local model (free), while all the other models are paid.

The aim of this project is to:
1. Determine if it is possible to extract data from BlackBox Stocks using a local browser with saved credentials.
2. Assess how much it would cost to run queries using ChatGPT's GPT-4o model (the recommended model).

---

## Setup Python on Windows

I am using Windows as an example here since most people likely have a Windows PC (I am guessing). Personally, I use a MacBook Pro.

### Download the Installer
- Visit the official [Python website](https://www.python.org/). Make sure you download a version higher than 3.11.
- Select the appropriate Windows installer (e.g., Windows x86-64 executable installer) for your system architecture.

### Run the Installer
- Double-click the downloaded installer file.
- Accept the license agreement and proceed.
- Ensure the box "Add Python to PATH" is checked in the installer. This allows you to run Python commands from the command line without specifying the full path.
- Customize the installation if desired (I usually install the binaries under `C:\`, something like `C:\Python313-64`).
- Complete the installation.
- Verify the installation by opening a command prompt and typing:

      python --version

---

## Download the Source Code
- You can download the `day_trading_agent.py` and `requirements.txt` files from here, or you can use Git to clone this repository.
- If you don't have a specific folder for scripts, create one—for example: `C:\Projects`.

---

## Setup Dependencies and Run the Agent

### Steps:
1. Open a command prompt and navigate to your projects folder (e.g., `C:\Projects`).
2. Copy over the `day_trading_agent.py` file and `requirements.txt` file into this folder.
3. Create a `.env` file in this folder with your OpenAI API key (the key below is not real):

       OPENAI_API_KEY='sk-proj-ZfPrH6eD ........'

4. Create a Python virtual environment and activate it:

       python -m venv venv
       venv\Scripts\activate.bat

5. Install dependencies listed in `requirements.txt`:

       pip install -r requirements.txt

6. Install Playwright:

       playwright install

7. Create a logs directory:

       mkdir logs

8. Run the agent:

       python day_trading_agent.py

