# Find PI to the Nth Digit - Enter a number and have the program generate π (pi) up to that many decimal places. Keep a limit to how far the program will go.

#1st way:

def return_pie(n = 15):
    result = float(22/7)
    return round(result,n)

print(return_pie(50))

# print((4/1) - (4/3)+ (4/5) - (4/7) + (4/9) - (4/11) + (4/13)- (4/15) + (4/17)- (4/19) + (4/21)- (4/23) + (4/25)- (4/27) + (4/29)- (4/31) + (4/33))

def cal_pie(limit):
    num = 4
    result = 0
    cycle_start = True

    # if limit > 15:
    #     print("LIMIT can't be greater than 15.")
    #     limit = 15

    for denom in range(1, 10^limit, 2):
        # print(limit)
        if cycle_start:
            result = result + (num / denom)
        else:
            result = result - (num / denom)

        cycle_start = not cycle_start
    return round(result, limit)


print(cal_pie(1000000))

