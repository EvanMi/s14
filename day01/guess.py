# -*- coding:utf-8 -*-
# Author: Evan Mi

age_of_old_boy = 56
count = 0
while count < 3:
    guess_age = int(input("guess age:"))
    if guess_age == age_of_old_boy:
        print("yes,you got it.he is %d" % age_of_old_boy)
        break
    elif guess_age > age_of_old_boy:
        print("think smaller than {0}...".format(guess_age))
    else:
        print("think bigger  than {_guess_age}...".format(_guess_age=guess_age))
    count += 1
else:
    print("you have tried too many times .. fuck off")
