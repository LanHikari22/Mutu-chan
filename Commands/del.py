from Commands.botcmd import BotCMD
import discord
from discord.ext.commands import Bot


# TODO in progress
class DelCMD(BotCMD):

    # access to bot -- to send message.
    bot = None
    channel = None
    # needs history of sent messages
    msgHistory = None

    def __init__(self, command: str, bot:Bot, channel:discord.Channel, msgHistory:list):
        super().__init__(command)
        self.bot = bot
        self.channel = channel
        self.msgHistory = msgHistory



    @staticmethod
    def get_help_format():
        return ""

    @staticmethod
    def get_help_doc():
        return "deletes one of the previous messages sent by this bots"

    def get_error_code(self, command, argv=None):
        if self.command != command:
            return self.COMMAND_MISMATCH
        if argv:
            if len(argv) < 3: return self.MISSING_ARGS
            validity_status = 0b0000 # so far, a success!
            try:
                if not argv[1].isnumeric():
                    validity_status |= self.ARG1_FAILURE
                if not argv[2].isnumeric():
                    validity_status |= self.ARG2_FAILURE
            except Exception as e:
                return self.INVALID_ARGV_FORMAT
            return validity_status
        else:
            return self.COMMAND_MATCH

    def get_error_msg(self, error_code: int):
        error_msg = super().get_error_msg(error_code)
        if error_code == self.MISSING_ARGS:
            error_msg = "I don't know what I'm supposed to add..."
        elif error_code == self.ARG1_FAILURE:
            error_msg = "I don't think the first argument is a number..."
        elif error_code == self.ARG2_FAILURE:
            error_msg = "I don't think the second argument is a number..."
        elif error_code == self.BOTH_FAILURE:
            error_msg = "Are you... Are you really adding numbers?"
        return error_msg

    async def execute(self, argv):
        await self.bot.send_message(destination=self.channel,
                content="Um. I think I can do this... Let's see...\n%s plus %s equals %s, I think??" %
               (int(argv[1]), int(argv[2]), int(argv[1]) + int(argv[2])))