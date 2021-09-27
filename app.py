async def on_shutdown(*args):
    await db.drop_user_table()


async def on_startup(dispatcher):
    import middlewares
    import handlers
    from utils import on_startup_notify, set_default_commands

    # Устанавливаем дефолтные команды
    await set_default_commands(dispatcher)

    # Создаем таблицу, если нет
    await db.create_user_table()

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    from aiogram import executor
    from loader import dp, db

    executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown, skip_updates=True)
