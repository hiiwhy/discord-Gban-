import interactions
import requests

Token = ""
bot = interactions.Client(token=Token)

@bot.command(
    name="gban",
    description="グローバルBANを実行します",
    options = [
        interactions.Option(
            name="user",
            description="gbanするuser",
            type=interactions.OptionType.USER,
            required=True,
        ),
        interactions.Option(
            name="password",
            description="パスワード",
            type=interactions.OptionType.STRING,
            required=True,
        ),
    ],
)
async def gban(ctx: interactions.CommandContext,user,password):
    if password == '123':
        await ctx.send('実行します', ephemeral=True)
        for guild in bot.guilds:
            headers = {
                'authorization': f'Bot {Token}',
            }
            json_data = {
                'delete_message_days': '0',
            }
            requests.put(f'https://discord.com/api/v9/guilds/{guild.id}/bans/{user}',headers=headers, json=json_data)
    else:
        await ctx.send('パスワードが違います', ephemeral=True)

bot.start()