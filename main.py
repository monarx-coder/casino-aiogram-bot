from aiogram import Bot,Dispatcher
import asyncio


TOKEN='8233544942:AAGVjsLseImKiS4zgNWbrEUEle-hcKzwbGA'

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    
    await dp.start_polling(bot)
    
if __name__ == '__main__':
	try:
		asyncio.run(main())
	except KeyboardInterrupt:
		print('Бот остановлен.')
