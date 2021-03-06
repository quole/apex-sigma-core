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

import arrow
import discord

from sigma.core.mechanics.command import SigmaCommand


async def afk(cmd: SigmaCommand, message: discord.Message, args: list):
    afk_data = await cmd.db[cmd.db.db_cfg.database]['AwayUsers'].find_one({'UserID': message.author.id})
    if args:
        afk_reason = ' '.join(args)
    else:
        afk_reason = 'No reason stated.'
    in_data = {
        'UserID': message.author.id,
        'Timestamp': arrow.utcnow().timestamp,
        'Reason': afk_reason
    }
    if afk_data:
        title = 'Your status has been updated'
        await cmd.db[cmd.db.db_cfg.database]['AwayUsers'].update_one({'UserID': message.author.id}, {'$set': in_data})
    else:
        title = 'You have been marked as away'
        await cmd.db[cmd.db.db_cfg.database]['AwayUsers'].insert_one(in_data)
    url = None
    for piece in afk_reason.split():
        if piece.startswith('http'):
            suffix = piece.split('.')[-1]
            if suffix in ['gif', 'jpg', 'jpeg', 'png']:
                url = piece
                afk_reason = afk_reason.replace(piece, '')
                break
    if not afk_reason:
        afk_reason = 'See image below.'
    response = discord.Embed(color=0x66CC66)
    response.add_field(name=f'✅ {title}.', value=f'Reason: **{afk_reason}**')
    if url:
        response.set_image(url=url)
    await message.channel.send(embed=response)
