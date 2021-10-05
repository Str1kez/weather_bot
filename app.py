async def on_shutdown(*args):
    await db.gino.drop_all()


async def on_startup(dispatcher):
    import middlewares
    import handlers
    import filters
    from utils import on_startup_notify, set_default_commands
    from data.config import PG_URI

    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    await db.set_bind(PG_URI)
    # Создаем таблицу, если нет
    # await db.create_user_table()
    await db.gino.create_all()

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    from aiogram import executor
    from loader import dp, db

    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown, skip_updates=True)
