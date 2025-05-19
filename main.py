from pyrogram import Client, filters
from pyrogram.types import Message
import os

# إعدادات العميل
API_ID = os.getenv("API_ID")  # سيتم إضافته لاحقًا في Render
API_HASH = os.getenv("API_HASH")  # سيتم إضافته لاحقًا في Render
SESSION_NAME = "my_session"

# إنشاء عميل Pyrogram
app = Client(SESSION_NAME, api_id=API_ID, api_hash=API_HASH)

# قائمة الأغاني
SONGS = [
    "https://example.com/song1.mp3",  # ستستبدل هذا بروابطك لاحقًا
]

# أمر /start
@app.on_message(filters.command("start"))
async def start_command(client, message: Message):
    await message.reply("مرحبًا! استخدم /play لتشغيل أغنية.")

# أمر /play
@app.on_message(filters.command("play"))
async def play_command(client, message: Message):
    chat_id = message.chat.id
    if SONGS:
        song = SONGS[0]
        await client.send_audio(chat_id, song)
        await message.reply(f"يتم تشغيل: {song}")
    else:
        await message.reply("لا توجد أغاني متاحة!")

# تشغيل البوت
if __name__ == "__main__":
    app.run()
