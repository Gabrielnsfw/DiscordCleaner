# Discord Server Cleaner

--------

This bot helps keep your Discord server clean by kicking inactive users after 3 months. Only admins can use the bot. The bot will send confirmation messages in embeds.

### Requirements

- Python 3.7+
- Discord.py

### Running the bot

1. Clone the repository:

```bash
git clone https://github.com/Gabrielnsfw/DiscordCleaner
```

2. Install the dependencies:

```bash
pip install -r requirements.txt
```

3. Replace `YOUR_BOT_TOKEN` with your bot token in `bot.py`:

```python

@bot.command()
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
    embed.set_footer(text='Made by ❤️ Gabriel.nsfw')

    await ctx.send(embed=embed)
```

4. Run the bot:

```bash
python bot.py
```

### Versions

This bot uses the following versions:

- Python: 3.10.4
- Discord.py: 1.7.3

### Contributing

Contributions are welcome! Please follow the following guidelines:

1. Fork the repository.
2. Make your changes.
3. Submit a pull request.

### License

This bot is licensed under the MIT License.
