from .data import RAID, REPLYRAID
import random
from config import STUFF, DEV
import asyncio
from .data import KeshavX

hl = STUFF.COMMAND_HANDLER

LEGENDS = DEV.SUDO_USERS + [DEV.OWNER_ID] + KeshavX

async def raid(_, m):
    try:
        count = int(m.text.split()[1])
    except:
        return await m.reply(f"{hl}raid [count]")
    for c in range(0, count):
        raid = random.choice(RAID)
        if m.reply_to_message:
            if m.reply_to_message.from_user.id in LEGENDS:
                return await m.reply("CAN'T RAID THEM !")
            await m.reply_to_message.reply(raid)
        else:
            await _.send_message(m.chat.id, raid)
        await asyncio.sleep(0.02)

RAID_IDS = []
async def replyraid(_, m):
    global RAID_IDS
    try:
        if m.reply_to_message:
            id = m.reply_to_message.from_user.id
        else:
            x = m.text.split()[1]
            if str(x)[0] == "@":
                id = (await _.get_users(x)).id
            else:
                id = int(x)
    except:
        return await m.reply(f"{hl}replyraid [id|username|reply]")
    if id in LEGENDS:
        return await m.reply("CAN'T RAID THEM !")
    if id in RAID_IDS:
        return await m.reply("RAID IS ALREADY ACTIVATED TO THIS USER !")
    RAID_IDS.append(id)
    return await m.reply(f"RAID REPLY ACTIVATED TO USER <code>{id}</code>")
    
async def dreplyraid(_, m):
    global RAID_IDS
    try:
        if m.reply_to_message:
            id = m.reply_to_message.from_user.id
        else:
            x = m.text.split()[1]
            if str(x)[0] == "@":
                id = (await _.get_users(x)).id
            else:
                id = int(x)
    except:
        return await m.reply(f"{hl}dreplyraid [id|username|reply]")
    
    if not id in RAID_IDS:
        return await m.reply("RAID IS NOT ACTIVATED TO THIS USER !")
    RAID_IDS.remove(id)
    return await m.reply(f"RAID REPLY DEACTIVATED TO USER <code>{id}</code>")

async def raid_cwf(_, m):
    if m.from_user:
        if m.from_user.id in RAID_IDS:
            await m.reply(random.choice(REPLYRAID))
