﻿# Apex Sigma: The Database Giant Discord Bot.
# Copyright (C) 2018  Lucia's Cipher
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import discord

from sigma.core.mechanics.command import SigmaCommand


async def togglestatus(cmd: SigmaCommand, message: discord.Message, args: list):
    if cmd.bot.cfg.pref.status_rotation:
        cmd.bot.cfg.pref.status_rotation = False
        response = discord.Embed(color=0x77B255, title=f'✅ Status rotation **disabled**.')
    else:
        cmd.bot.cfg.pref.status_rotation = True
        response = discord.Embed(color=0x77B255, title=f'✅ Status rotation **enabled**.')
    await message.channel.send(embed=response)
