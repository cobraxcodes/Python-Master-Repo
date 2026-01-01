day = 7
match day:
    case 1: 
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")


today = 7
match today:
    case 1: 
        print("Weekday")
    case 2:
        print("Weekday")
    case 3:
        print("Weekday")
    case 4:
        print("Weekday")
    case 5:
        print("Almost weekend!")
    case 6:
        print("Weekend")
    case 7:
        print("Day of the Lord")


operation = "div"
a = 1
b = 1

match operation:
    case "add":
        print(a + b);
    case "sub":
        print(a - b);
    case "mul":
        print(a * b);
    case "div":
        print(a / b);
    case _: 
        print("Invalid operations")
