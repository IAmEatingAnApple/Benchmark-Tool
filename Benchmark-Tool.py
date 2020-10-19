import time
import os
from colorama import Back, Style

def bench():
	count = 1
	start = time.time()
	print("Бенчмарк начат. Ожидайте...")
	time.sleep(1)
	while count <= 1000000:
		print(count)
		count = count + 1
	end = time.time()
	bentime = end - start
	bentime = round(bentime, 2)
	res = count / bentime
	res = round(res, 1)
	os.system('cls' if os.name=='nt' else 'clear')
	print(Back.GREEN + Style.DIM + f"Бенчмарк окончен! Ваш результат: {res}")
	print(f"Время бенчмарка: {bentime} секунд" + Style.RESET_ALL)

def main():
	input('Нажмите Enter для начала теста')
	bench()

main()