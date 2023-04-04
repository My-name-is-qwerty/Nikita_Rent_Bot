from aiogram.types import Message, InputMediaPhoto
import asyncio
from aiogram.filters import CommandStart
from aiogram import Router, F, Bot
from config_data.Config import Config, load_config
from aiogram.types.input_media import InputMedia
from aiogram.methods.send_media_group import SendMediaGroup

config: Config = load_config()
bot: Bot = Bot(token=config.tg_bot.token)

router: Router = Router()


@router.message(CommandStart())
async def start_command(message: Message):
    await bot.send_message(chat_id=message.from_user.id, text="Hello World!")


# @router.message(F.photo[0].file_id)
# async def send_photo(message: Message):
#     await bot.send_photo(chat_id=-1001821547478, photo=message.photo[0].file_id, caption=message.caption)


mediagroups = {}


@router.message(F.photo[-1].file_id.as_("photo_id"), F.media_group_id.as_("album_id"))
async def collect_and_send_media_group(message: Message, photo_id: str, album_id: int):
    if album_id in mediagroups:
        mediagroups[album_id].append(photo_id)
        return

    mediagroups[album_id] = [photo_id]
    await asyncio.sleep(1)


    new_album = [InputMediaPhoto(media=file_id) for file_id in mediagroups[album_id]]
    # await message.answer_media_group(media=new_album)
    await bot.send_media_group(chat_id=-1001821547478, media=new_album)
    print(mediagroups)


