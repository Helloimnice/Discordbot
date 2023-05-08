import discord
import os
from discord.ext import commands
import random


load_dotenv()
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
bot = commands.Bot(command_prefix='!', intents=intents)

#creating a dictionary
quotes = [
    "Imagination is more important than knowledge. - Albert Einstein",
    "Don't cry because it's over, smile because it happened. - Dr. Seuss",
    "Be the change that you wish to see in the world. - Mahatma Gandhi",
    "In three words I can sum up everything I've learned about life: it goes on. - Robert Frost",
    "Believe you can and you're halfway there. - Theodore Roosevelt"
]

@bot.event
async def on_ready():
    print('The bot is online!')


class MyHelpCommand(commands.HelpCommand):
    async def send_bot_help(self, mapping):
        embed = discord.Embed(title="Help", description="List of available commands:")
        for cog, commands in mapping.items():
            category = getattr(cog, "qualified_name", "No Category")
            if len(commands) > 0:
                command_list = [f"`{c.name}` - {c.help}" for c in commands if not c.hidden]
                if command_list:
                    joined_commands = "\n".join(command_list)
                    embed.add_field(name=category, value=joined_commands, inline=False)
        await self.get_destination().send(embed=embed)

bot.help_command = MyHelpCommand()

@bot.command(name="kick")
async def kick(ctx, member: discord.Member,*,reason: str = None):
    """
    kick a member from the server.
    Optionally specify a reason for the ban.
    """
    if ctx.author.guild_permissions.administrator:
        if ctx.guild.me.guild_permissions.kick_members:
            await member.kick(reason=reason)
            await ctx.send(f'{member.mention} has been kicked!')
        else:
            await ctx.send("The bot does not have permission to kick members.")
    else:
        await ctx.send("You don't have permission to kick members.")



@bot.command(name = 'ban')
async def ban(ctx, member: discord.Member,*,reason: str = None):
    """
    ban a member from the server.
    Optionally specify a reason for the ban.
    """
    if ctx.author.guild_permissions.administrator:
        if ctx.guild.me.has_permissions.kick_members:
            await member.ban(reason=reason)
            await ctx.send(f'{member.mention} has been ban!')
        else:
            await ctx.send("The bot don't have permission!")
    else:
        await ctx.send("are you dumb, you aint got permisson!")

@bot.command()
async def quote(ctx,*, reason: str = None):
    """
    Good quotes if your feeling down
    """
    random_quote = random.choice(quotes)
    await ctx.send(random_quote)

bot.run('token')
