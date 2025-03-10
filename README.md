# meme-coin-trading-bot
Installation & Setup
1.Clone the repository
    git clone https://github.com/Shivani01joshi/meme-coin-trading-bot.git
    cd solana-meme-coin-bot
2. Install dependencies
    pip install -r requirements.txt  # Python  
3. Run the bot
    python manage.py fetch_tokens


---------------------------------------------------------------------------------------------------

To design and build a meme coin trading bot for Solana using Python and Django, we’ll break the process into clear, actionable steps. Each step will include instructions, tools, and code snippets where applicable. Let’s begin:
Step 1: Set Up Your Development Environment
    Install Python:

    Download and install Python (version 3.8 or higher) from python.org.

    Verify installation: python --version.

    Install Django:

    Install Django using pip:
        pip install django

    Install necessary Python libraries:
        pip install solana pandas requests django-environ psycopg2-binary
2.Set Up PostgreSQL
    Install PostgreSQL:
        Install PostgreSQL 
    Create a database for your project:
        CREATE DATABASE memecoin_bot;
3.Create a Django Project:

    Create a new Django project:
        django-admin startproject memecoin_bot
        cd memecoin_bot
    Create a new Django app:
        python manage.py startapp trading_bot
4.Configure Django Settings:
    Update settings.py to connect to PostgreSQL

Step 2: Research and Choose APIs
1.DEX Screener API:

Use DEX Screener to monitor new meme coins on Solana.

API Endpoint: https://api.dexscreener.com/latest/dex/tokens/{token_address}.

2.Create a utils.py file in your Django app (e.g., trading_bot/utils.py).

This is a good place for reusable functions like API calls.
3. In a Service Layer
Create a services.py file in your Django app (e.g., trading_bot/services.py).

This is a good place for business logic and external API interactions.

4. Directly in a View or Management Command
If this function is only used in a specific view or management command, you can define it there.
5.Once the function is defined, you can call it from other parts of your Django project.
