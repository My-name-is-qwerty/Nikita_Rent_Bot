import asyncio
from handlers import message_handler
from aiogram import Bot, Dispatcher
from config_data.Config import Config, load_config


async def main() -> None:

    """ Загружаем конфиг в переменную config """
    config: Config = load_config()

    """ Инициализируем бот и диспетчер """
    bot: Bot = Bot(token=config.tg_bot.token)
    dp: Dispatcher = Dispatcher()

    """ Регистриуем роутеры в диспетчере """
    dp.include_router(message_handler.router)

    """ Пропускаем накопившиеся апдейты и запускаем polling """
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())


