from aiogram.types import Message
import data

async def get_stat(message: Message):
    stat = data.get_stats()
    text = "TOP 10 talik\n\n"
    r = 1
    user_r = 0
    for i in stat:
        if i[0] == message.from_user.id: user_r = r
        user = data.get_user(i[0])
        if user and user.status == 1:
            if r <= 10: 
                text += f"{r}. {user.name} - {i[1] * 2} Notcoin\n"
            r += 1
        
    if r > 10 or user_r == 0: text += f"\n\nSiz {user_r}-o'rindasiz!" if user_r else "\n\nSiz hali Notcoin to'plamagansiz!"
    
    await message.answer(text)