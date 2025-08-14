import discord
import os

intents = discord.Intents.default()
intents.messages = True
intents.dm_messages = True

client = discord.Client(intents=intents)

BOT_OWNER_ID = 1282714989223743581  # replace with your Discord ID

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    # Only respond to DMs
    if isinstance(message.channel, discord.DMChannel):
        user_info = f"User: {message.author} (ID: {message.author.id})"
        message_content = f"Message: {message.content}"
        
        owner = await client.fetch_user(BOT_OWNER_ID)
        await owner.send(f"{user_info}\n{message_content}")

client.run(os.environ['BOT_TOKEN'])
