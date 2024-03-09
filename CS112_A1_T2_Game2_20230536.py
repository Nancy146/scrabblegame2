numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player1 = 0
player2 = 0
player1_picks = 0
player2_picks = 0

def player1_fun():
    global player1, player1_picks
    num1 = int(input("player1 turn: "))
    if num1 in numbers_list:
        if player1 + num1 > 15:
            print("This number will make the sum more than 15. Choose a smaller number.")
        else:
            numbers_list.remove(num1)
            player1 += num1
            player1_picks += 1
    else:
        print("the number is not in the list or has been picked, try another number")

def player2_fun():
    global player2, player2_picks
    num2 = int(input("player2 turn: "))
    if num2 in numbers_list:
        if player2 + num2 > 15:
            print("This number will make the sum more than 15.")
        else:
            numbers_list.remove(num2)
            player2 += num2
            player2_picks += 1
    else:
        print("the number is not in the list or has been picked, try another number")

def game():
    for _ in range(3):
        print(f"choose a number from {numbers_list}")
        player1_fun()
        if player1_picks == 3:
            if player1 == 15:
                print("player1 is the winner")
                return
        player2_fun()
        if player2_picks == 3:
            if player2 == 15:
                print("player2 is the winner")
                return
            else:
                print("draw")
                break

print("*Game Rules:-")
print("1-each player has to choose only 3 numbers from 1 to 9 to make the total 15")
print("2-the player who reach 15 first is the winner")
game()