# coin toss

favourable_outcomes = int(input("enter the number of favourable out "))
number_flip = int(input("pleas enter the number of times you want to flip the coin "))
total_outcomes = number_flip * 2
probability = favourable_outcomes / total_outcomes
print("probability is :-")
print(probability)


#tables (number)

n = int(input("enter the  number you want the table of "))
answer = 1

while answer <= 10:
    print(n, 'X', answer, "=", n*answer)
    answer = answer + 1


#1 to 100

number = 100

while number >= 1:
    print(number)
    number = number - 1


#counting

num_1 = int(input("please enter the first number:- "))
num_2 = int(input("please enter the second number:-  "))

while num_1 >= num_2:
    print(num_1)
    num_1 = num_1 - 1
while num_1 <= num_2:
    print(num_1)
    num_1 = num_1 + 1


    
    
