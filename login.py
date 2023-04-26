print("login v2 asdasd")

def Time(minutes):
    count = 0
    hour = 0
    minute = minutes % 60
    while count < minutes:
        count += 1
        if count % 60 == 0:
            hour += 1

    print(f'cantidad de horas {hour} con {minute} minutos')
Time(900)