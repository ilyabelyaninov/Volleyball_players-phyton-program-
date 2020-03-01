from Volleyball import *

volleyball_players = []
volleyball_players.append(Volleyball_player(datetime.date(1998, 5, 2), True, 'Max Maximov', 195, 87, 'VC_Kuzbass','Russia'))
while True:
    command = input("Write a command \r\n")

    if command == "ADD":
        new_volleyball_player = Volleyball_player()
        new_volleyball_player.add()
        volleyball_players.append(new_volleyball_player)
    if command == "EXIT":
        break
    if command.upper() == "SHOW":
        for volleyball_player in volleyball_players:
            print(volleyball_player.show())