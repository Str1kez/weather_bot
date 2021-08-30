from aiogram import types


async def set_default_commands(dp):
    commands = [
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("help", "Вывести справку"),
        types.BotCommand("send_contact", "Отправить данные (просто вывод трех сообщений 😎"),
        types.BotCommand('menu', 'Показать меню'),
        types.BotCommand('close_menu', 'Убрать меню')
    ]
    await dp.bot.set_my_commands(commands)
