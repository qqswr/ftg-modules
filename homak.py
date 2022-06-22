from .. import loader
from random import choice as какаша


def register(cb):
	cb(ChatinfoMod())

class HamsterPickMod(loader.Module):
	"""Случайный хомяк из @pic."""
	strings = {'name': 'homak'}

	async def pickhcmd(self, event):
		await event.edit('<b>Лови хомяка!</b>')
		reslt=await event.client.inline_query('pic',какаша(['hamster','хомяк']))
		await reslt[reslt.index(какаша(reslt))].click(event.to_id)		

		


		