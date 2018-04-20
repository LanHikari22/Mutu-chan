from Commands.botcmd import BotCMD
import discord
from discord.ext.commands import Bot


class GGCMD(BotCMD):

    # access to bot -- to send message.
    bot = None
    channel = None

    # username, cuz i like referring to users. gg user!
    user = None

    def __init__(self, command: str, bot:Bot, channel:discord.Channel):
        super().__init__(command)
        self.bot = bot
        self.channel = channel

    def setUser(self, user):
        """execute when user is available on_message()"""
        self.user = user

    @staticmethod
    def get_help_format():
        return ""

    @staticmethod
    def get_help_doc():
        return "says gg to user"

    def get_error_code(self, command, argv=None):
        if self.command != command:
            return self.COMMAND_MISMATCH
        return self.SUCCESS

    def get_error_msg(self, error_code: int):
        error_msg = super().get_error_msg(error_code)

    async def execute(self, argv):
        await self.bot.send_message(destination=self.channel, content="gg %s!" % self.user)