import shutil as sh
import math


"""Задания 4, 9, 10"""


def disc_space():
    total_mb = sh.disk_usage(".").total / (1024 * 1024)
    used_mb = sh.disk_usage(".").used / (1024 * 1024)
    free_mb = sh.disk_usage(".").free / (1024 * 1024)
    print(f'Общий объем диска: {math.ceil(total_mb)} МБ. '
          f'Занято: {math.ceil(used_mb)} МБ, '
          f'свободно: {math.ceil(free_mb)} МБ')

def path(cmd):
    return sh.which(cmd) if sh.which(cmd) else 'Команда не найдена'

def move_file(src, dst):
    try:
        sh.move(src, dst)
        print(f'Файл {src} перемещен в {dst}')
    except FileNotFoundError:
        print('Файл не найден')


move_file('/Users/vlad/Desktop/Новая папка/report.txt',
          '/Users/vlad/Desktop/Новая папка/report_old.txt')
disc_space()
print(path('python'))