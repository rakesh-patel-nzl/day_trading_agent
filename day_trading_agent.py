# day_trading_agent.py
# Copyright (c) 2025 Rakesh Patel
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
# FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

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
