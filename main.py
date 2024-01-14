import discord
from discord.ext import commands
import datetime


# Bitchass create an instance of the bot
bot = commands.Bot(command_prefix='!')

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------GABRIELLLLLLLLLLLLLLLLLLLLL------')

@bot.hybrid_command(name='kick_inactive_users')
@commands.has_permissions(administrator=True)
async def kick_inactive_users(ctx):
    guild = ctx.guild
    current_time = int(datetime.datetime.now().timestamp())

    inactive_users = []
    for member in guild.members:
        last_activity = member.last_activity
        if last_activity is None:
            continue

        inactive_time = current_time - last_activity.timestamp()
        if inactive_time / 86400 >= 90:  # 90 days = 3 months
            inactive_users.append(member)

    for user in inactive_users:
        await user.kick('Inactive for more than 3 months.')

    embed = discord.Embed(
        title='Inactive Users Kicked',
        description=f'{len(inactive_users)} users were kicked for being inactive.',
        color=0x00FF00
    )
    embed.set_footer(text=f'Made by ❤️ Gabriel.nsfw')

    await ctx.send(embed=embed)

bot.run('YOUR_BOT_TOKEN')
