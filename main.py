from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
import asyncio
import config

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command('start'))
async def start_command(message: Message):
    print(message)


@dp.message()
async def all_messages(message: Message, bot: Bot):
    msg_text = f'User {message.from_user.full_name} sent message: \n{message.text}'
    await message.answer(text=msg_text)
    # await bot.send_message(chat_id=, text=msg_text)


async def stat_bot():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(stat_bot())
