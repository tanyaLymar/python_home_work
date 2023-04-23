"""
Задание 5.
Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.
Подсказки:
--- используйте модуль chardet, иначе задание не засчитается!!!
"""


# websites = ['yandex.ru', 'youtube.com']
# print(os.name)
#
#
# def ping_website(website):
#     ARGS = ['ping', website]
#     WS_PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)
#     for line in WS_PING.stdout:
#         result = chardet.detect(line)
#         print(line.decode(encoding=result['encoding']))
#
#
# if __name__ == '__main__':
#     with ThreadPoolExecutor(max_workers=len(websites)) as executor:
#         results = executor.map(ping_website, websites)

import subprocess
import chardet

web_address_list = ['yandex.ru', 'youtube.com']

def ping_website(adresses):
    for address in adresses:
        print(f'Пинг сайта: {address}')
        command = ['ping']
        command.append(address)
        res_ping = subprocess.Popen(command, stdout=subprocess.PIPE)
        for line in res_ping.stdout:
            line_encode = chardet.detect(line)
            print(line.decode(line_encode['encoding']))

ping_website(web_address_list)