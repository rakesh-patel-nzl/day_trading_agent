# day_trading_agent
Just trying out [brower-use](https://browser-use.com/). In this test script, we got to 
[BlackBox Stocks Options Page](https://members.blackboxstocks.com/) and get a list of stocks with "Bullish Flow".

Browser Use makes use of APIs from some of the most commom LLMs. It recommends GPT-4o. However, they also support
Anthropic, Azure OpenAI, Gemini, DeepSeek and Ollama. Ollama can be used as a local model (free). All the other 
models are paid ones. 

The aim of this project is to:
1. See if it is possible to extract data from Blackbox Stocks, using a local browser which has the credentials saved
2. See how much it would cost to run queries using ChatGPT GPT-4o model (the recommended model)

## Setup Python on Windows
I am using Windows as an example here as most people would have a Windows PC (I am guessing). Personally, I use 
MacBook Pro. 

### Download the Installer
- Visit the official [Python website](https://www.python.org/). Make sure you download a version that is higher than 3.11
- Select the appropriate Windows installer (e.g., Windows x86-64 executable installer) for your system architecture. 

### Run the Installer
- Double-click the downloaded installer file. 
- Accept the license agreement and proceed. 
- Make sure the box "Add Python to PATH" is checked in the installer. This allows you to run Python commands from the command line without specifying the full path.
- Customize the installation if desired (I usually install the binaries under C:\, something like C:\Python313-64)
- Then install
- Verify the installation by opening a command prompt and type:

       python --version

## Download the source code
- You can just download the day_trading_agent.py and requirements.txt files from here, or you can use Git to clone this repo
- If you don't have a specific folder that you use for scripts, create one ... something like C:\Projects

## Setup dependencies and run the agent
- Open a command prompt and navigate your projects folder (eg C:\Projects)
- copy over the day_trading_agent.py file and requirements.txt file here
- create a .env file here with your OpenAPI API KEY (the key below is not real)

      OPENAI_API_KEY='sk-proj-ZfPrH6eD ........'
- create a Python virtual environment and then activate it:

      python -m venv venv
      venv/Scripts/activate.bat

- copy over the requirements.txt file and pip install the required libraries:

      python -m venv venv
      venv/Scripts/activate.bat

- install Playwright:

      playwright install

- create a logs directory:

      mkdir logs

- run the agent:

      python day_trading_agent.py


