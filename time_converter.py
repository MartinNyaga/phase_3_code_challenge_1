def time_converter(hour, minute, period):
    if hour == 12 and period == "am":
        hour = 0
    elif hour !=12 and period =="pm":
        hour += 12
    return(f"{hour:02d} : {minute:02d}")

hour = int(input("Hour: "))
minute = int(input("Minute: "))
period = input("Period: ")

print(time_converter(hour, minute, period))