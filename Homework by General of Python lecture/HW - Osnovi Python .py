#!/usr/bin/env python
# coding: utf-8

# ## Задание №1
# ### Фразы
# 

# In[26]:


phrase_1= 'Насколько проще было бы писать программы, если бы не заказчики'
print (phrase_1)
phrase_2= '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'
print (phrase_2)
if len(phrase_1)>len(phrase_2):
    print('Фраза 1 длиннее фразы 2')
phrase_1=input('введите фразу 1 - ')
phrase_2=input('введите фразу 2 - ')
if len(phrase_1)<len(phrase_2):
    print('Фраза 2 длиннее фразы 1')
else:
    print('НЕВЕРНО, НЕПОДХОДЯЩАЯ ФРАЗА')
phrase_1=input('введите фразу 1 - ')
phrase_2=input('введите фразу 2 - ')
if len(phrase_1)==len(phrase_2):
    print('Фразы равной длины')
else:
    print('НЕВЕРНО, НЕПОДХОДЯЩАЯ ФРАЗА')


# In[ ]:


phrase_1 = 'Насколько проще было бы писать программы, если бы не заказчики'
phrase_2 = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'
if len(phrase_1)>len(phrase_2):
    print('Фраза 1 длиннее фразы 2')
phrase_1 = '640Кб должно хватить для любых задач. Билл Гейтс (по легенде)'
phrase_2 = 'Насколько проще было бы писать программы, если бы не заказчики'
if len(phrase_1)<len(phrase_2):
    print('Фраза 2 длиннее фразы 1')
phrase_1 = 'Насколько проще было бы писать программы, если бы не заказчики'
phrase_2 = 'Насколько проще было бы писать программы, если бы не заказчики'
if len(phrase_1)==len(phrase_2):
    print('Фразы равной длины')


# ## Задание №2
# ### Годы

# In[ ]:


year=int (input('year = '))
if year % 400 == 0:
    print('високосный')
elif year % 4 == 0:
    print('високосный год')
elif year % 100 == 0:
    print('обычный год')
else:
    print('обычный год')


# ## Задание №3
# ### Знак зодиака

# In[ ]:


date=int (input ('Введите дату '))
month=(input ('Введите месяц '))
if date >=21 and month=='Январь' or date<=19 and month=='Февраль':
    print ('Ваш знак зодиака: Водолей')
elif date >=20 and month =='Февраль' or date <=20 and month =='Март':
    print ('Ваш знак зодиака: Рыба')
elif date >=22 and month=='Декабрь' or date<=20 and month=='Январь':
    print ('Ваш знак зодиака: Козерог')
elif date >=22 and month=='Ноябрь' or date<=21 and month=='Декабрь':
    print ('Ваш знак зодиака: Стрелец')
elif date >=23 and month=='Октябрь' or date<=21 and month=='Ноябрь':
    print ('Ваш знак зодиака: Скорпион')
elif date >=23 and month=='Сентябрь' or date<=22 and month=='Октябрь':
    print ('Ваш знак зодиака: Весы')
elif date >=24 and month=='Август' or date<=22 and month=='Сентябрь':
    print ('Ваш знак зодиака: Дева')
elif date >=23 and month=='Июль' or date<=23 and month=='Август':
    print ('Ваш знак зодиака: Лев')
elif date >=22 and month=='Июнь' or date<=22 and month=='Июль':
    print ('Ваш знак зодиака: Рак')
elif date >=22 and month=='Май' or date<=21 and month=='Июнь':
    print ('Ваш знак зодиака: Близнецы')
elif date >=21 and month=='Апрель' or date<=21 and month=='Май':
    print ('Ваш знак зодиака: Телец')
elif date >=20 and month=='Март' or date<=19 and month=='Апрель':
    print ('Ваш знак зодиака: Овен')


# ## Задание №4
# ### Упаковка
# 

# In[ ]:


width= int (input ('введите ширину '))
length= int (input ('введите длину '))
height= int (input ('введите высоту '))
if width<15 and length<15 and height<15:
    print ('Коробка №1')
elif ((width<50 and width>15 or
       length<50 and length>15) and 
  (height<50 and height>15)):
        print ('Коробка №2')
elif height>200:
    print ('Упаковка для лыж')
else:
    print ('Стандартная коробка №3')


# ## Задание №5
# ### Счастливый билет

# In[3]:


x= int (input ('ВВЕДИТЕ НОМЕР БИЛЕТА '))
q=x//100000
w=(x%100000)//10000
e=(x%10000)//1000
r=(x%1000)//100
t=(x%100)//10
y=(x%10)//1
if q+w+e==r+t+y:
    print ('Счастливый билет')
else:
    print ('Неасчастливый билет')


# ## Задание №6
# ### Площадь фигуры

# In[25]:


k=(input ('Введите тип фигуры: '))
if k==('Круг'):
    d=int(input ('Введите диаметр: '))
    print ('Площадь круга', (3.14*(d/2)**2))
elif k==('Прямоугольник'):
    a=int(input ('Введине сторону а: '))
    b=int(input ('Введине сторону b: '))
    print ('Площадь Прямоугольника', (a*b))
elif k==('Треугольник'):
    a=int(input ('Введине сторону а: '))
    b=int(input ('Введине сторону b: '))
    c=int(input ('Введине сторону c: '))
    p= a/2+b/2+c/2
    print ('Площадь Треугольника', (p*(p-2)*(p-b)*(p-c))**0.5)
else:
    print ('ВВЕДЕНЫ НЕВЕРНАЯ ФИГУРА ИЛИ НЕУЧТЕН РЕГИСТР')

