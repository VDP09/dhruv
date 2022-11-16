first = input('give me the first number\n')
second = input('give me the second number\n')
third = input('give me the third number\n')

if first > second and third > first:
    one = third
    two = first
    three = second
else:
    if first > third and second > first:
        one = second
        two = first
        three = third
    else:
        if second > first and third > second:
            one = third
            two = second
            three = first
        else:
            if second > third and first > second:
                one = first
                two = second
                three = third
            else:
                if third > second and first > third:
                    one = first
                    two = third
                    three = second
                else:
                    if third > first and second > third:
                        one = second
                        two = third
                        three = first


print(one, two, three)