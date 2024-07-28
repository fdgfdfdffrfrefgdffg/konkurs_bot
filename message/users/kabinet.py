from aiogram.types import Message
from bot_config import BOT_URL
import data
import keyboards.inline as iBtns

async def answer_task(message: Message):
    text = f"✅ Vazifa:\n\n"
    text += "Do'stlaringizni botga taklif qiling va har bitta do'stingiz uchun 2 ta Notcoin oling. Botdan kamida 100 ta Notcoin yechib olishingiz mumkin.\n\n"
    text += f"{BOT_URL}?start={message.from_user.id}"
    await message.answer(text)

async def answer_balans(message: Message):
    balans = len(data.get_ref_count(message.from_user.id))
    user = data.get_user(message.from_user.id)
    text = F"SIZNING MA'LUMOTLARINGIZ:\n\nIsm-familya: {user.name}\nBalans: {balans * 2} Notcoin\nTelefon raqam: {user.phone}\n\n1 Notcoin - 100 UZS"
    await message.answer(text, reply_markup=iBtns.withdraw_btn(message.from_user.id))
