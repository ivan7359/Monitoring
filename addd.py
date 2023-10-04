# Чтение из файла
def reading_file(file, memory):
    result = []
    f = open(file, 'r')
    if(memory == True):
        a = f.readline()
        b = f.readline()
        result.append(a)
        result.append(b)
    else:
        a = f.readline()
        result.append(a)
    f.close()
    return result

# Парсинг CPU
def parsing_CPU(a):
    a = a.split()
    a = a[0:3]
    a[0] = a[0] + '- средняя загрузка CPU за 1 мин \n'
    a[1] = a[1] + '- средняя загрузка CPU за 5 мин \n'
    a[2] = a[2] + '- средняя загрузка CPU за 15 мин \n'
    return a

# Парсинг Memory
def parsing_Memory(a):
    b = a[0].split()
    c = a[1].split()
    b[1] = str(int(b[1]) // 1000000)
    b[2] = 'GB'
    c[1] = str(int(c[1]) // 1000000)
    c[2] = 'GB'
    a[0] = ' '.join(b) + '\n'
    a[1] = ' '.join(c) + '\n'
    return a

# Парсинг SSD
def parsing_SSD(a):
    a = 'Free space: ' + str(int(a) // 1024) + ' MB'
    return a
        

# Запись
def writing_file(a):
    f = open('/mnt/c/users/ivanh/monitoring/file.txt', 'a')
    for i in a:
        f.write(i)
    f.write('\n')
    f.close()

result = reading_file('/proc/loadavg', False)
result = parsing_CPU(result[0])
writing_file(result)

result = reading_file('/proc/meminfo', True)
result = parsing_Memory(result)
writing_file(result)

result = reading_file('/sys/block/sda/size', False)
result = parsing_SSD(result[0])
writing_file(result)