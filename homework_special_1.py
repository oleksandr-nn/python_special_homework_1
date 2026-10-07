#Розминка
a=17
b=5
print(a+b,"/",a-b,"/",a*b,"/",a/b)
print(a//b,"/",a%b)
# / - ділення з результатом у вигляді флоат
# // - ділення з виділенням цілої частини
result_1=2**10
print("2**10 is equal to:",result_1)
result_2=10**3
print("10**3 is equal to:",result_2)
# ;)
price=249.99
count=3
score=price*count
print("your score is:",score)
# ;)
a=type(7/2) #флоат бо 3.5 - дробове
b=type(7//2)#iнт бо ціла чистина 3
c=type(7.0//2)#флоат бо 7.0 - дробове число
print(a)
print(b)
print(c)
# ;)
name="Python"
print(name*3)
hi="Привіт"
wrld="світ"
print(hi+wrld)

# Обчислення
n_pupils=28
n_ranges=6
print("Кількість рядів:",n_pupils//n_ranges,"//",
      "Залишиться учнів:", n_pupils%n_ranges)
# ;)
time=3725
print(time,"in minutes will be",time/60,
      "//","in hours will be",time/60**2)
# ;)
min_1=150
print(min_1,"in hours is equal to:",min_1/60,
      "in seconds is equal to:",min_1*60,)
# ;)
c=36.6
print(c,"in Fahrenheit is:",c*9/5+32)
# ;)
a=12.5
b=8
print("area is:",a*b,"//",
      "perimeter is:",(a+b)*2)
# ;)
r=7
pi=3.14159
print("area is:",pi*r**2,"//",
      "lenght is:",2*r*pi)
# ;)
sum=1200
discount=0.15
print("price is:",sum-(sum*discount))
# ;)
salary=25000
tax=0.195
print("your final salary is:",
      salary-(salary*tax))
# ;)
v=90
t=2.5
print("distance is:",v*t)
# ;)
a=10
b=11
c=8
print((a+b+c)/2)
# ;)
n=7
if n%2==1:
      print("Число непарне")
elif n%2==0:
      print("Число парне")
# ;)
n=473
print("Остання цифра:",n%10)
# ;)
n=473
q=n//100
w=(n%100)//10
e=(n%100)%w
print("Сотні:",n//100)
print("Десятки:",(n%100)//10)
print("Одиниці:",(n%100)%7)
# ;)
n=859
r=n//100
t=(n%100)//10
y=(n%100)%t
print("Сума цифр:",r+t+y)
# ;)
num=123
rev=0
while num>0:
      dg=num%10
      rev=rev*10+dg
      num=num//10
print("Reversed number:",rev)
# ;)
a=144
print("Корінь=",a**0.5)
# ;)
y=365
print("Кількість секунд=",365*24*60*60)

#Типи даних
x="5"
y="3"
print(x+y)# виведе 53, бо це срінг
print(int(x)+int(y))# перевели в інт, виведе 8
# ;)
nn=9.99
print(int(nn))# виведе 9, бо інт відкидає дробову частину
# ;)
print(True+True+True)# буде 3, бо True=1(False=0)
print(True*10)# буде 10
# ;)
a=5
b=10
b-=a
a+=a
print(a,b)
# ;)
deposit=10000
rate=0.12
years=3
sum=deposit*(1+rate)**years
print("sum is:",sum)
# ;)
strng="-"
print(strng*20)
print("Результат:",str(2**20))







