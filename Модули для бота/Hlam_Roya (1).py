from .. import loader

class AMod(loader.Module):
    strings = {"name": "ForwardM"}

    async def watcher(self, message):
        if message.sender_id != (await message.client.get_me()).id:
            return
        if message.text == "хлам":
            await message.client.forward_messages(1735806236, (await message.get_reply_message()))
            await message.delete() # изменение строки для удаления сообщения после пересылки