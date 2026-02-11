def covert_ms (ms):
    if ms<1000:
        print(f"just {ms} millisecond/s")
    total_ms = ms//1000
    hours = total_ms//3600
    minutes = (total_ms%3600)//60
    seconds =( total_ms%3600)%60
    final=[]
    if hours>0:
        final.append(f"{hours} hour/s")
    if minutes>0:
        final.append(f"{minutes} minute/s")
    if seconds>0:
        final.append(f"{seconds} second/s")

    return " ".join(final)


def main():
    print("This program converts milliseconds into hours, minutes, and seconds ")
    print("-"*70)
    print('To exit the program, please type "exit"')
    while True:
        val = input("Please enter the milliseconds (should be greater than zero):") 
        if val.lower() == "exit":
            print("Exiting the program... Good Bye")
            break
        if not val.isdigit() or int(val) <= 0:
            print("Not Valid Input !!!")
            continue

        print(covert_ms(int(val)))

if __name__ == "__main__":
    main()
