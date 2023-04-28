x = int(input('Введіть ділене: '))
y = int(input('Введіть дільник: '))
sum_=x  
for i in range(x):
    sum_=sum_-y

    print(sum_)
    if sum_<=y:
        print('Ділення завершено')
        break
