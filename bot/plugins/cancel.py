from pyrogram import filters as Filters
from pyrogram.types import CallbackQuery

from ..utubebot import UtubeBot


@UtubeBot.on_callback_query(
    Filters.create(lambda _, __, query: query.data.startswith("cncl+"))
)
async def cncl(c: UtubeBot, q: CallbackQuery) -> None:
    _, pid = q.data.split("+")
    if not c.download_controller.get(pid, False):
        await q.answer("Ваш процесс в настоящее время не активен! ", show_alert=True)
        return
    c.download_controller[pid] = False
    await q.answer("Ваш процесс скоро будет отменен! ", show_alert=True)
