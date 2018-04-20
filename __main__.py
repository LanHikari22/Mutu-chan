import sys
import discord
from discord.ext import commands
import asyncio
import time

# commands used (also initialize in on_ready())
from Commands.botcmd import BotCMD
from Commands.add import AddCMD
from Commands.gg import GGCMD

DEBUG = True
def dbg(str, file=None, active=True):
    """just a wrapper function to distinguish a DEBUG print from an actual print."""
    try:
        if DEBUG and active:
            if file is None:
                import sys
                print(str, file=sys.stderr)
            else:
                print(str, file=file)
    except: pass


if __name__ == '__main__':
    bot = commands.Bot(command_prefix='?', description="You are the reason why I still -- oops this is a song")
    bot_commands = [] # list of BotCMD objects that are available to this bot
    msgHistory = []

async def botmsg(string):
    """Just a simple abstraction that assumes global variables channel and bot"""
    msgHistory.append(await bot.send_message(destination=channel, content=string))

async def execute(message):
    """executes command passed in argv"""

    # obtain argv
    msg = message.content[message.content.index('>')+2:] # remove '<id> '
    argv = msg.split(' ')

    # execute appropriate command
    # First, control commands
    if argv[0] == 'help':
        await handle_help(user)
    else:
        for botcmd in bot_commands:
            error_code = botcmd.get_error_code(command=argv[0], argv=argv)
            if error_code == BotCMD.SUCCESS:
                await botcmd.execute(argv)
            elif error_code >= BotCMD.COMMAND_MATCH: # if command matches, argv error_codes are all > COMMAND_MATCH
                await botmsg(botcmd.get_error_msg(error_code))

async def handle_help(user):
    msg = "Hi %s! I'm QBot! Here's how to use me:\n" % user
    for botcmd in bot_commands:
        msg += "**%s**\t\t%s\n" % (botcmd.command, botcmd.get_help_format())
    msg += "**help**\n"
    await botmsg(msg)

def get_bot_command(bot_commands, command):
    """
    simpler helper that identifies a commandbot by its unique command id and returns it
    :returns: bot_command with specified command as id, or None
    """
    bot_command = None
    for botcmd in bot_commands:
        if botcmd.command == command:
            bot_command = botcmd
            break
    return bot_command


    # elif argv[0] == 'del':
    #     await botmsg("Error: This is currently unsupported. Give me more premissions if you really want it done.")
    #     if msgHistory:
    #         bot.delete_message(msgHistory.pop())


@bot.event
async def on_ready():
    global server, channel, member # I am sorry. How do you create async methods???

    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

    # gets server and channel we're interacting in....
    for s in bot.servers:
        server = s
    for c in server.channels:
        if c.name == "bot_testing":
            channel = c

    member = server.get_member(user_id=bot.user.id)
    # await bot.change_nickname(member,nickname='QuarkBot') # i'm sorry, you can't
    await bot.change_presence(game=discord.Game(name="QBot.cplx"))

    # initiate commands -- insert commands used by the bot here
    bot_commands.append(AddCMD(command='add',bot=bot,channel=channel))
    bot_commands.append(GGCMD(command='gg', bot=bot, channel=channel))



@bot.event
async def on_message(message):
    dbg("<on_message>")

    # obtain user
    global user # oops
    user = message.author
    user = str(user)[:-5]


    if not (message.mentions is not None and member in message.mentions):
        return

    # This is only executed at @<this_bot> so!

    # setup for bot commands that need message dependent data
    get_bot_command(bot_commands, 'gg').setUser(user)

    await execute(message) # executes commands in msg if any

    dbg("</on_message>\n")


async def my_background_task():
    global bot, server
    await bot.wait_until_ready()
    logfile = open("stats.log", "a")
    dbg(logfile)
    time_ref = time.time()
    while not bot.is_closed:
        try:
            logfile.write("[t=%is] numMembers: %i\n" % ((int(time.time()-time_ref), server.member_count)))
            # dbg("[t=%is] numMembers: %i\n" % ((int(time.time()-time_ref), server.member_count)))
        except: pass
        await asyncio.sleep(1)  # task runs every second

bot.loop.create_task(coro=my_background_task())
bot.run('MzQwODkxMjIwMzc5MTcyODk2.DGS_mw.dpKg0Z8V0NF0jESEOBltvxasxxE')
bot.logout()
