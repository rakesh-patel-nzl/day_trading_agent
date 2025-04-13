import asyncio

from browser_use.agent.service import Agent
from browser_use.browser.browser import Browser, BrowserConfig
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI

load_dotenv()

# Configure the browser to connect to your real Browser where you're already authenticated with Finviz & Blackbox Stocks
# noinspection SpellCheckingInspection
browser = Browser(
    config=BrowserConfig(
        # Specify the path to your Browser Executable (this is a Windows Example)
        chrome_instance_path='C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe',
        # MacOS might be something like this
        # chrome_instance_path='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        # Linux might be something like this
        # chrome_instance_path='/usr/bin/google-chrome',
    )
)

perplexity_prompt = f"""
Go to https://www.perplexity.ai/finance/NEM and extract information about their most recent earnings.
"""

# noinspection SpellCheckingInspection
blackboxstocks_prompt = f"""
go to https://members.blackboxstocks.com/options then click on 'Bullish Flow' and finally capture the list of symbols 
from the 'SYMBOL' column.
"""


# noinspection SpellCheckingInspection
async def main():
    agent = Agent(
        task=blackboxstocks_prompt,
        llm=ChatOpenAI(model="gpt-4o"),
        browser=browser,
        save_conversation_path="logs/conversation"      # Save chat logs
    )
    result = await agent.run()
    final_result = result.final_result()

    print('Results:')
    print(result)
    print('Final Result: {}'.format(final_result))


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
