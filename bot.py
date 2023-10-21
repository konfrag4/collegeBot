import discord
import respnoses

async def send_message(message, user_message, is_priv):
    try:
        response = respnoses.handle_response(user_message)
        await message.author.send(response) if is_priv else await message.channel.send(response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = "TOKEN"
    intents = discord.Intents.all()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        #is_priv = isinstance(message.channel, discord.DMChannel)
        #await send_message(message, message.content, is_priv)
        print(f"{username} said {user_message} in {channel}")

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, True)
        else:
            await send_message(message, user_message, False)

    client.run(TOKEN)
