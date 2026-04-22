# day=int(input("Enter not of day in the week "))
# match day:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")


day=int(input("Enter the day of the week "))
match day:
    case 1|2|3|4|5:
        print("i hate Working day")
    case 6|7:
        print("i love weekends")
    case _:
        print("No match")