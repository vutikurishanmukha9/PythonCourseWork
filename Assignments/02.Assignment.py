# Assignment 2: WhatsApp Chat Data Analysis

chat = {}
n = int(input("Enter the Number of chats: "))
for i in range(n):
    name, mssg = input().split(':')
    if name in chat:
        chat[name].append((mssg, i))
    else:
        chat[name] = [(mssg, i)]

while True:
    print("\n1. Count total number of messages")
    print("2. Identify unique users in the chat")
    print("3. Count total words in the chat")
    print("4. Calculate average words per message")
    print("5. Find the longest message sent")
    print("6. Find the most active user")
    print("7. Get message count for a specific user")
    print("8. Find the most frequently used word by a specific user")
    print("9. Retrieve the first and last message sent by a user")
    print("10. Check if a user is present in the chat")
    print("11. Find commonly repeated words")
    print("12. Identify the user with the longest average message length")
    print("13. Count how many messages mention a specific user")
    print("14. Remove duplicate messages")
    print("15. Sort messages alphabetically")
    print("16. Extract all questions asked in the chat")
    print("17. Calculate the reply ratio between two users")
    print("18. Check for deleted messages")
    ch = int(input("Enter Your Choice: "))

    if ch == 1:
        print("Total number of messages:", sum(len(msgs) for msgs in chat.values()))

    elif ch == 2:
        print("Unique users in the chat:", list(chat.keys()))

    elif ch == 3:
        total_words = sum(len(mssg.split()) for msgs in chat.values() for mssg, _ in msgs)
        print("Total words in the chat:", total_words)

    elif ch == 4:
        total_msgs = sum(len(msgs) for msgs in chat.values())
        total_words = sum(len(mssg.split()) for msgs in chat.values() for mssg, _ in msgs)
        avg = total_words / total_msgs if total_msgs else 0
        print("Average words per message:", round(avg, 2))

    elif ch == 5:
        longest = ''
        for msgs in chat.values():
            for mssg, _ in msgs:
                if len(mssg) > len(longest):
                    longest = mssg
        print("Longest message sent:", longest)

    elif ch == 6:
        most_active = max(chat.items(), key=lambda item: len(item[1]))
        print("Most active user:", most_active[0], "with", len(most_active[1]), "messages")

    elif ch == 7:
        user = input("Enter username: ")
        print(f"{user} has sent", len(chat.get(user, [])), "messages")

    elif ch == 8:
        from collections import Counter
        user = input("Enter username: ")
        all_words = [word for mssg, _ in chat.get(user, []) for word in mssg.split()]
        if all_words:
            most_common = Counter(all_words).most_common(1)[0]
            print("Most frequently used word by", user, "is:", most_common[0])
        else:
            print("No messages from this user.")

    elif ch == 9:
        user = input("Enter username: ")
        msgs = chat.get(user, [])
        if msgs:
            print("First message:", msgs[0][0])
            print("Last message:", msgs[-1][0])
        else:
            print("User not found.")

    elif ch == 10:
        user = input("Enter username to check: ")
        print("User is present in the chat" if user in chat else "User not found.")

    elif ch == 11:
        from collections import Counter
        all_words = [word for msgs in chat.values() for mssg, _ in msgs for word in mssg.split()]
        word_counts = Counter(all_words)
        repeated = [word for word, count in word_counts.items() if count > 1]
        print("Repeated words:", repeated)

    elif ch == 12:
        def avg_len(msgs):
            return sum(len(mssg) for mssg, _ in msgs) / len(msgs) if msgs else 0
        user = max(chat.items(), key=lambda item: avg_len(item[1]))
        print("User with longest average message length:", user[0])

    elif ch == 13:
        mentioned_user = input("Enter user to check mentions: ")
        count = sum(1 for msgs in chat.values() for mssg, _ in msgs if mentioned_user in mssg)
        print(f"User '{mentioned_user}' mentioned in {count} messages.")

    elif ch == 14:
        for user in chat:
            unique_msgs = list(dict.fromkeys(chat[user]))
            chat[user] = unique_msgs
        print("Duplicate messages removed.")

    elif ch == 15:
        for user in chat:
            chat[user].sort(key=lambda x: x[0])
        print("Messages sorted alphabetically per user.")

    elif ch == 16:
        print("Questions in chat:")
        for user, msgs in chat.items():
            for mssg, _ in msgs:
                if mssg.strip().endswith('?'):
                    print(f"{user}: {mssg}")

    elif ch == 17:
        user1 = input("Enter first user: ")
        user2 = input("Enter second user: ")
        msg_count_1 = len(chat.get(user1, []))
        msg_count_2 = len(chat.get(user2, []))
        if msg_count_2 == 0:
            print("Reply ratio: Infinity (second user sent no messages)")
        else:
            print("Reply ratio (", user1, "/", user2, "):", round(msg_count_1 / msg_count_2, 2))

    elif ch == 18:
        deleted = []
        for user, msgs in chat.items():
            for mssg, _ in msgs:
                if mssg.lower() in ['deleted', 'message deleted', 'msg deleted']:
                    deleted.append((user, mssg))
        if deleted:
            print("Deleted messages found:")
            for user, msg in deleted:
                print(f"{user}: {msg}")
        else:
            print("No deleted messages found.")

    else:
        print("Invalid choice.")