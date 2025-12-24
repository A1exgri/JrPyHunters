import dotenv
import os

dotenv.load_dotenv()

BOT_TOKEN = os.getenv('TOKEN')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
PROXY = os.getenv('PROXY')
ADMIN_ID = int(os.getenv('ADMIN_ID'))
