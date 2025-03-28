import discord

TOKEN = "MTM1NDk3Nzc4MDI2NTI1NTAwNA.GZgNlP.IVbn5dUInbPQj_FsCftGQOvK-LlkrlwMcZXtxw"  # ใส่โทเคนของคุณ

intents = discord.Intents.default()
intents.messages = True  # เปิดให้บอทอ่านข้อความได้

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'✅ บอทออนไลน์แล้ว! ชื่อบอท: {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower() == "hello":
        await message.channel.send("สวัสดี!")

print("⏳ กำลังรันบอท...")  # เช็คว่าบอทเริ่มรันไหม
client.run(TOKEN)

