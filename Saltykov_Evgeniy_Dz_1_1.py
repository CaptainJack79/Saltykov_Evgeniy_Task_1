duration = int(input('Введите время в секундах: '))

days = duration // 3600 // 24
hours: int = duration // 3600 - days * 24
minutes = duration // 60 % 60
seconds = duration % 60

print(days, "дн,",  hours, "час,", minutes, "мин,", seconds, "сек.", sep=" ")