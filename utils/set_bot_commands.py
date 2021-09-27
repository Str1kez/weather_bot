from aiogram import types


async def set_default_commands(dp):
    commands_user = [
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("help", "Вывести справку"),
        types.BotCommand("send_contact", "Отправить данные (просто вывод трех сообщений 😎"),
        types.BotCommand('menu', 'Показать меню'),
        types.BotCommand('close_menu', 'Убрать меню'),
        types.BotCommand('get_shops', 'Вывести ссылки на магазы со шмотом'),
        types.BotCommand('here', 'Отправь геолокацию'),
        types.BotCommand('recent', 'Последние 3 запроса'),
        types.BotCommand('close_recent', 'Закрыть меню запросов')
    ]
    commands_group = [
        types.BotCommand("start", "Запустить бота"),
        types.BotCommand("help", "Вывести справку"),
        types.BotCommand('weather', 'Ответь на название города')
    ]
    await dp.bot.set_my_commands(commands_user)
