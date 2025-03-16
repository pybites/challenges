from dotenv import load_dotenv
from pathlib import Path

# use python-dotenv to set environment variables
# sourcing .env file containing VARIABLE=VALUE
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
