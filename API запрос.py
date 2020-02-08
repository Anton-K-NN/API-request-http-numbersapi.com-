'''
В этой задаче вам необходимо воспользоваться API сайта numbersapi.com

Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный математический факт об этом числе.

Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.

Пример запроса к интересному числу:
http://numbersapi.com/31/math?json=true

Пример запроса к скучному числу:
http://numbersapi.com/999/math?json=true

Пример входного файла:
31
999
1024
502

﻿Пример выходного файла:
Interesting
Boring
Interesting
Boring
'''


import requests
import re
import json
f=open('dataset_24476_3 (2).txt','r')
n=[]
for line in f:
    line=line.rstrip()
    n.append(line)
print(n)
for x in n:
    api_url="http://numbersapi.com/"
    api_url+=str(x)
    api_url+='/math?json=true'
    res=requests.get(api_url)
    data=json.loads(res.text)
    if data['found']==True:
        print('Interesting')
    else:
        print('Boring')

    '''
954
962
900
936
904
937
938
970
941
981
921
922
923
956
991'''