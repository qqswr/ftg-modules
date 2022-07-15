from telethon.tl import types

from .. import loader, utils
from telethon.tl.types import TypeChannelParticipantsFilter, ChannelParticipantsAdmins


class WelcomeMod(loader.Module):
    """Автоварн юзеров за Leave/AFK с использованием Group Help"""
    strings = {'name': 'AutoWarn'}

    async def client_ready(self, client, db):
        self.db = db

    async def wcmd(self, message):
        """ переключатель режима судной ночи(вкл/выкл автоварн короче)"""
        state = self.db.get("AutoWarn", "ids", [])

        if message.chat_id not in state:
            state.append(message.chat_id)
            self.db.set("AutoWarn", "ids", state)
            await message.respond("<b>Автоварн включен в этом чате!</b>")
            await message.delete()
            return
        state.remove(message.chat_id)
        self.db.set("AutoWarn", "ids", state)
        await message.respond("<b>Автоварн выключен в этом чате!</b>")
        await message.delete()
        return

    async def watcher(self, message):
        """почему это называется watcher???"""
        # admins_list = []

        # self.db.set("admins", "ids", admins_list)
        # admin_ids = self.db.get("admins", "ids", [])
        # fromid = message.from_id
        # sud_state = self.db.get("AutoWarn", "sud_state", [])
        # if message.chat_id not in sud_state:
        #     return
        # if message.from_id in admin_ids:
        #     return
#                                   былины  |   баку black |  баку   | true black | true  |   mafia russia
        if message.sender_id not in [606933972, 1044037207, 1050428643, 761250017, 468253535, 1520369962]:
            return
        if ('бу-у-у-у-ду' in message.raw_text.split()) or ('пообещал' in message.raw_text.split()):
            for usr in message.entities:
                if hasattr(usr, 'user_id'):
                    uid = usr.user_id
                    # if uid in admin_ids:
                    #     return
                    # else:
                    await message.respond(f"/mute 1h {str(uid)} AFK")

        if ('гнетущей' in message.raw_text.split()) or ('убежал' in message.raw_text.split()):
            msgs = []
            x = await message.client.get_messages(message.chat_id, 15)
            for msg in x:
                msgs.append(msg.raw_text)

            if msgs.count(message.raw_text) > 1:
                pass
            # elif uid in admin_ids:
            #     return
            else:
                for usr in message.entities:
                    if hasattr(usr, 'user_id'):
                        uid = usr.user_id
                        await message.respond(f"\warn {str(uid)} Лив из игры")
