def Proverka():
    while True:
        num = int(input())
        if len(str(num)) != 6:
            print("Ошибка")
        else:
            return num


print("Введите меньший шестизначный номер билета: ")
N_ticket = Proverka()
print("Введите больший шестизначный номер билета: ")
M_ticket = Proverka()
if N_ticket > M_ticket:
    while N_ticket > M_ticket:
        print("fool")
        print("Введите меньший шестизначный номер билета: ")
        N_ticket = Proverka()
        print("Введите больший шестизначный номер билета: ")
        M_ticket = Proverka()

count_tickets = 0
for i in range(N_ticket, M_ticket + 1):
    j = str(i)
    if int(j[0]) + int(j[1]) + int(j[2]) == \
            int(j[3]) + int(j[4]) + int(j[5]):
        count_tickets += 1

print("Кол-во счастливых билетов равно: ", count_tickets)
