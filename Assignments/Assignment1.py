chat = {}
n = int(input("Enter the Number of Chats: "))
for _ in range (n):
    name,msg = input().split(":")
    chat[name] = msg
print(chat)