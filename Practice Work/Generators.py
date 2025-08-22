def IPL(RCB):
    for players in RCB:
        yield players
RCB = ['Kohli','Salt','Padikkal','Rajat','Jitesh','Tim David','Krunal','Bhuvineshwar kumar','Hazzle wood','Yash dayal','suyash Sharma']
players = IPL(RCB)
while True:
    Next_Player = input("[O]ut / [N]ot OUT:  ").upper()
    if Next_Player == 'O':
        print(next(players))
    else:
        break