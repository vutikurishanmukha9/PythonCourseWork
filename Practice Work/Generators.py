# def IPL(RCB):
#     for players in RCB:
#         yield players
# RCB = ['Kohli','Salt','Padikkal','Rajat','Jitesh','Tim David','Krunal','Bhuvineshwar kumar','Hazzle wood','Yash dayal','suyash Sharma']
# players = IPL(RCB)
# while True:
#     Next_Player = input("[O]ut / [N]ot OUT:  ").upper()
#     if Next_Player == 'O':
#         print(next(players))
#     else:
#         break
# try:
#     print(next(players))
# except StopIteration:
#     print("No more players left!")
#     break

def IPL(RCB):
    for player in RCB:
        yield player

RCB = [
    'Kohli', 'Salt', 'Padikkal', 'Rajat', 'Jitesh', 
    'Tim David', 'Krunal', 'Bhuvineshwar Kumar', 
    'Hazlewood', 'Yash Dayal', 'Suyash Sharma'
    ]
    
players = IPL(RCB)
print("\n--- IPL Match Simulator ---")
print("Press 'O' when a player is Out, 'N' to stop.\n")

while True:
    Next_Player = input("[O]ut / [N]ot OUT:  ").upper()
    
    if Next_Player == 'O':
        try:
            print("Next Player:", next(players))
        except StopIteration:
            print("All players are out! No more players left.")
            break
    elif Next_Player == 'N':
        print("Match simulation stopped.")
        break
    else:
        print("Invalid input. Please press 'O' or 'N'.")
