
#for x in range(1, 21):
 #   print("x=",x, "x2=", x*x)

#2students = ["Михаил", "Олег", "Маша", "Кирилл", "Гоша" ,"Сеня","Немой"]


#for i in range(0, len(students)) :
 #   print (students[i])

#word = "test"

#for x in range(0, len(students)) :
 #   print (students[x])

#for s in word :
#    print (s)

#for student in students :
 #   print (student)

#nums = [1,2,3,4,5,6,7,8,9,10]

#for n in nums :
#    if (n % 2 == 1) :
##        print (n)

#employee_list = ["John Snow", "Piter Pen", "Drakula", "IvanIV", "Moana", "Juilet"]
#print(employee_list[1])
##print(employee_list[-2])


#def dev_by_three(number):
 #   return "Да" if number % 3==0 else "Нет"

#num = int(input("Введите число: "))
#result = dev_by_three(num)
#print(f"Делится ли на три {num} - {result}")


#import math


#def min_boxes(items):
#    return math.ceil ( items / 5 )
#num_items = int(input("Введите количество предметов :" ))
#print(f"Минимальное количество коробок : {min_boxes(num_items)}")


#n = int(input("Введите число: "))

#def check_divisibility(n):
 #   for i in range(1,n+1):
 #          print(f"{i} - Делится  и на 2 , и на 4 " )
  #      elif i % 2 == 0:
  #      else:
   #         print(i)


#check_divisibility(n)

#def quarter_of_year(month):
#    if 1 <= month <= 3:
#       return "I квартал"
 #   if 4 <= month <= 6:
 #       return "II квартал"
 #   if 7 <= month <= 9:
#        return "III квартал"
#    if 10 <= month <= 12:
#        return "IV квартал"
#    return "Неверный номер месяца"

#month = int(input("Введите номер месяца (1-12): "))
#print(quarter_of_year(month))


#lst = [17, 34, 9, 21, 13, 48, 24, 7, 81, 29, 16, 12, 42]

#result = [x for x in lst if x > 15 and x % 3 == 0]

#print(result)

count = 1
for i in range(8, 80, 8):
    print(count, ' * 8 = ', i)
    count += 1