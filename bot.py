import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import datetime
import random
import re

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

BOT_TOKEN = os.environ.get("BOT_TOKEN")

NOTICE_CHANNEL_IDS = os.environ.get("NOTICE_CHANNEL_IDS").split(",")
DIFF_JST_FROM_UTC = 9


prefix_list = ['.', '．' '。']


class BotMain(commands.Bot):
    def __init__(self, command_prefix, **options):
        super().__init__(command_prefix, **options)


    async def on_ready(self):
        print('on ready.')


    async def on_voice_state_update(self, member, before, after):
        for channel_str in NOTICE_CHANNEL_IDS:
          channel = bot.get_channel(int(channel_str))
          guild = before.channel.guild if after.channel is None else after.channel.guild
          if guild is channel.guild:
          # 通知チャンネルと同じサーバーにのみ反応させる
            now = datetime.datetime.utcnow() + datetime.timedelta(hours=DIFF_JST_FROM_UTC)
            now_str = now.strftime('%Y-%m-%d %H:%M:%S')
            if before.channel is None and after.channel:
                await channel.send(f'{now_str} - {member.name} が{after.channel.name} に参加したよ。')
            elif after.channel is None and before.channel:
                await channel.send(f'{now_str} - {member.name} が{before.channel.name} から出たよ。')
            elif after.channel is not before.channel:
                await channel.send(f'{now_str} - {member.name} が{before.channel.name} から {after.channel.name}に移動したよ。')


    async def on_message(self, message):
        pattern = "^([0-9]*)d([0-9]+)"
        if not message.content or len(message.content) < 1:
            return
        content = message.content.lower()
        if content[0] in prefix_list and not message.author.bot:
            match = re.match(pattern, content[1:])
            if match:
                multiply = match.group(1)
                dice = match.group(2)
                if multiply and int(multiply) > 0:
                    max_num = int(dice)
                    numbers = []
                    amount = 0
                    for i in range(int(multiply)):
                        number = random.randint(1, max_num)
                        amount += number
                        numbers.append(f"{i+1}:`{number}`")

                    result = "\n".join(numbers)
                    await message.channel.send(f'ダイスの目の合計は`{amount}`です。\n{result}')
                else:
                    max_num = int(dice)
                    number = random.randint(1, max_num)
                    await message.channel.send(f'ダイスの目は`{number}`です。')
            else:
                if len(content) > 1:
                    await message.channel.send('コマンドの書式間違っています。\n`数字(ダイスを振る数)d数字(使うダイスの種類)` \n例)\n2d6 6面ダイスを2個\nd12 12麺ダイスを1個\n2d10 10面ダイスを2個\nd100 100面ダイスを1個')


bot = BotMain(prefix_list)


if __name__ == '__main__':
    bot.run(os.environ.get("BOT_TOKEN"))

