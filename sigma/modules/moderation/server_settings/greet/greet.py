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


async def greet(cmd: SigmaCommand, message: discord.Message, args: list):
    if not message.author.permissions_in(message.channel).manage_guild:
        embed = discord.Embed(title='⛔ Access Denied. Manage Server needed.', color=0xBE1931)
    else:
        active = await cmd.db.get_guild_settings(message.guild.id, 'Greet')
        if active is False and active is not None:
            await cmd.db.set_guild_settings(message.guild.id, 'Greet', True)
            embed = discord.Embed(color=0x77B255, title='✅ Greeting Messages Enabled')
        else:
            await cmd.db.set_guild_settings(message.guild.id, 'Greet', False)
            embed = discord.Embed(color=0x77B255, title='✅ Greeting Messages Disabled')
    await message.channel.send(None, embed=embed)
