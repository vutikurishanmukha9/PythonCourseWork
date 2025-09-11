print("=== WhatsApp Chat Analyzer ===")
chat = {}
n = int(input("Enter the number of chats: "))

for i in range(n):
    user_input = input("Enter name:message format: ")
    name, message = user_input.split(':', 1)
    name = name.strip()
    message = message.strip()
    
    if name in chat:
        chat[name].append(message)
    else:
        chat[name] = [message]

while True:
    print("\n" + "="*50)
    print("WHATSAPP CHAT ANALYSIS")
    print("="*50)
    print("1. Count total messages")
    print("2. Show unique users")
    print("3. Count total words")
    print("4. Average words per message")
    print("5. Find longest message")
    print("6. Most active user")
    print("7. User message count")
    print("8. User's most used word")
    print("9. User's first & last message")
    print("10. Check if user exists")
    print("11. Find repeated words")
    print("12. User with longest avg message")
    print("13. Count user mentions")
    print("14. Remove duplicate messages")
    print("15. Sort messages alphabetically")
    print("16. Extract questions")
    print("17. Reply ratio between users")
    print("18. Check for deleted messages")
    print("0. Exit")
    print("="*50)
    
    choice = int(input("Choose option: "))
    
    if choice == 0:
        print("Goodbye!")
        break
        
    elif choice == 1:
        total = 0
        for messages in chat.values():
            total += len(messages)
        print("Total messages:", total)
    
    elif choice == 2:
        print("Unique users:", list(chat.keys()))
    
    elif choice == 3:
        total_words = 0
        for messages in chat.values():
            for msg in messages:
                total_words += len(msg.split())
        print("Total words:", total_words)
    
    elif choice == 4:
        total_msgs = 0
        total_words = 0
        for messages in chat.values():
            total_msgs += len(messages)
            for msg in messages:
                total_words += len(msg.split())
        
        if total_msgs > 0:
            avg = total_words / total_msgs
            print("Average words per message:", round(avg, 2))
        else:
            print("No messages found")
    
    elif choice == 5:
        longest = ""
        for messages in chat.values():
            for msg in messages:
                if len(msg) > len(longest):
                    longest = msg
        print("Longest message:", longest)
    
    elif choice == 6:
        top_user = ""
        max_msgs = 0
        for user, messages in chat.items():
            if len(messages) > max_msgs:
                max_msgs = len(messages)
                top_user = user
        print("Most active user:", top_user, "with", max_msgs, "messages")
    
    elif choice == 7:
        user = input("Enter username: ")
        if user in chat:
            print(user, "sent", len(chat[user]), "messages")
        else:
            print("User not found")
    
    elif choice == 8:
        user = input("Enter username: ")
        if user in chat:
            word_count = {}
            for msg in chat[user]:
                for word in msg.split():
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1
            
            if word_count:
                most_used = ""
                max_count = 0
                for word, count in word_count.items():
                    if count > max_count:
                        max_count = count
                        most_used = word
                print("Most used word by", user + ":", most_used, "(" + str(max_count) + " times)")
            else:
                print("No words found")
        else:
            print("User not found")
    
    elif choice == 9:
        user = input("Enter username: ")
        if user in chat and chat[user]:
            print("First message:", chat[user][0])
            print("Last message:", chat[user][-1])
        else:
            print("User not found or no messages")
    
    elif choice == 10:
        user = input("Enter username: ")
        if user in chat:
            print("User exists in the chat")
        else:
            print("User not found")
    
    elif choice == 11:
        word_count = {}
        for messages in chat.values():
            for msg in messages:
                for word in msg.split():
                    if word in word_count:
                        word_count[word] += 1
                    else:
                        word_count[word] = 1
        
        repeated = []
        for word, count in word_count.items():
            if count > 1:
                repeated.append(word)
        print("Repeated words:", repeated)
    
    elif choice == 12:
        longest_avg_user = ""
        max_avg = 0
        
        for user, messages in chat.items():
            if messages:
                total_length = 0
                for msg in messages:
                    total_length += len(msg)
                avg_length = total_length / len(messages)
                
                if avg_length > max_avg:
                    max_avg = avg_length
                    longest_avg_user = user
        
        print("User with longest average message:", longest_avg_user)
    
    elif choice == 13:
        mentioned_user = input("Enter user to check mentions: ")
        mention_count = 0
        
        for messages in chat.values():
            for msg in messages:
                if mentioned_user in msg:
                    mention_count += 1
        
        print("'" + mentioned_user + "' mentioned in", mention_count, "messages")
    
    elif choice == 14:
        for user in chat:
            unique = []
            seen = set()
            for msg in chat[user]:
                if msg not in seen:
                    unique.append(msg)
                    seen.add(msg)
            chat[user] = unique
        print("Duplicate messages removed")
    
    elif choice == 15:
        for user in chat:
            chat[user].sort()
        print("Messages sorted alphabetically for each user")
    
    elif choice == 16:
        print("Questions found:")
        found = False
        for user, messages in chat.items():
            for msg in messages:
                if msg.strip().endswith('?'):
                    print(user + ":", msg)
                    found = True
        if not found:
            print("No questions found")
    
    elif choice == 17:
        user1 = input("Enter first user: ")
        user2 = input("Enter second user: ")
        
        count1 = 0
        count2 = 0
        
        if user1 in chat:
            count1 = len(chat[user1])
        if user2 in chat:
            count2 = len(chat[user2])
        
        if count2 == 0:
            print("Reply ratio: Cannot calculate (second user sent no messages)")
        else:
            ratio = count1 / count2
            print("Reply ratio (" + user1 + "/" + user2 + "):", round(ratio, 2))
    
    elif choice == 18:
        deleted_words = ['deleted', 'message deleted', 'msg deleted']
        found = False
        
        for user, messages in chat.items():
            for msg in messages:
                if msg.lower() in deleted_words:
                    print(user + ":", msg)
                    found = True
        
        if not found:
            print("No deleted messages found")
    
    else:
        print("Invalid choice! Please select 0-18")