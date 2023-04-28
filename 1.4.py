x = int(input('Введіть число яке хочете поділити: '))
y = int(input('Введіть число на яке хочете поділити: '))
sum_=x
for i in range(x):
    sum_=sum_-y

    print(sum_)
    if sum_<=y:
        print('Ділення завершено')
        break
