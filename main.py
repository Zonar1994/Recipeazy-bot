import discord
import openai

client = discord.Client(intents=discord.Intents().all())
openai.api_key = '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'
# Define the virtual chef's name
chef_name = 'Virtual Chef'

# Handle incoming messages from users
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Generate a response using ChatGPT
    prompt = f'{chef_name}: {message.content}'
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7
    )

    # Send the response back to the user
    await message.channel.send(f'{message.author}: {response.choices[0].text}')

# Run the bot
client.run('MTA4NTg2NDQ0NDgxNjUyNzQxMA.G0wAqt.fxXsX-q2Yr75tlmvtOq-q65vtuLluNQZ1PRDBU')
