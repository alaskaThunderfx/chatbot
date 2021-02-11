action = list(" " * 9)


def board():
    print('---------')
    print('|', action[0], action[1], action[2], '|')
    print('|', action[3], action[4], action[5], '|')
    print('|', action[6], action[7], action[8], '|')
    print('---------')


win = []
xwin = ["X", "X", "X"]
owin = ["O", "O", "O"]
turn = 0

board()

while xwin not in win and owin not in win and " " in action:
    coordinates = []
    nums = [i for i in input("Enter coordinates:").split() if i.isalpha() is False]
    if len(nums) == 2:
        if int(nums[0]) < 4 and int(nums[1]) < 4:
            if action[((int(nums[0]) - 1) * 3 + (int(nums[1]) + 2)) - 3] == " ":
                for i in nums:
                    coordinates.append(int(i))
                if turn == 0:
                    turn += 1
                    action[((coordinates[0] - 1) * 3 + (coordinates[1] + 2)) - 3] = "X"
                    board()
                    win = [action[0:3], action[3:6], action[6:9], action[0:8:3],
                           action[1:8:3], action[2:9:3], action[0:9:4], action[2:7:2]]
                else:
                    turn -= 1
                    action[((coordinates[0] - 1) * 3 + (coordinates[1] + 2)) - 3] = "O"
                    board()
                    win = [action[0:3], action[3:6], action[6:9], action[0:8:3],
                           action[1:8:3], action[2:9:3], action[0:9:4], action[2:7:2]]
            else:
                print("This cell is occupied! Choose another one!")
        else:
            print("Coordinates should be from 1 to 3!")
    else:
        print("You should enter numbers!")
if xwin in win:
   print("X wins")
elif owin in win:
    print("O wins")
else:
    print("Draw")
