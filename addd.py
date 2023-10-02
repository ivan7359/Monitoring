# CPU
# Чтение из файла
def reading_file(file):
    f = open(file, 'r')
    a = f.readline().split()
    f.close()
    return a

# Парсинг
def parsing(a):
    a = a[0:3]
    a[0] = a[0] + '- средняя загрузка CPU за 1 мин \n'
    a[1] = a[1] + '- средняя загрузка CPU за 5 мин \n'
    a[2] = a[2] + '- средняя загрузка CPU за 15 мин \n'
    return a

# Запись
def writing_file(a):
    f = open('/mnt/c/monitoring/file.txt', 'w')
    for i in a:
        f.write(i)
    f.close()

result = reading_file('/proc/loadavg')
result = parsing(result)
writing_file(result)

