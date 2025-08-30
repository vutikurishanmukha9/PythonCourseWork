from collections import Counter

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

# Main menu loop
while True:
    print("\n" + "="*50)
    print("WHATSAPP CHAT ANALYSIS OPTIONS")
    print("="*50)
    print("1.  Count total messages")
    print("2.  Show unique users")
    print("3.  Count total words")
    print("4.  Average words per message")
    print("5.  Find longest message")
    print("6.  Find most active user")
    print("7.  Get user message count")
    print("8.  Find user's most common word")
    print("9.  Get user's first & last message")
    print("10. Check if user exists")
    print("11. Find repeated words")
    print("12. User with longest avg message")
    print("13. Count user mentions")
    print("14. Remove duplicate messages")
    print("15. Sort messages alphabetically")
    print("16. Extract questions")
    print("17. Calculate reply ratio")
    print("18. Check for deleted messages")
    print("0.  Exit")
    print("="*50)
    
    choice = int(input("Enter your choice: "))
    
    if choice == 0:
        print("Thank you for using WhatsApp Chat Analyzer!")
        break
        
    elif choice == 1:
        # Count total messages
        total_messages = 0
        for user_messages in chat.values():
            total_messages += len(user_messages)
        print("Total messages:", total_messages)
    
    elif choice == 2:
        # Show unique users
        users = list(chat.keys())
        print("Unique users:", users)
    
    elif choice == 3:
        # Count total words
        total_words = 0
        for user_messages in chat.values():
            for message in user_messages:
                total_words += len(message.split())
        print("Total words:", total_words)
    
    elif choice == 4:
        # Average words per message
        total_messages = 0
        total_words = 0
        
        for user_messages in chat.values():
            total_messages += len(user_messages)
            for message in user_messages:
                total_words += len(message.split())
        
        if total_messages > 0:
            average = total_words / total_messages
            print("Average words per message:", round(average, 2))
        else:
            print("No messages found")
    
    elif choice == 5:
        # Find longest message
        longest_message = ""
        for user_messages in chat.values():
            for message in user_messages:
                if len(message) > len(longest_message):
                    longest_message = message
        print("Longest message:", longest_message)
    
    elif choice == 6:
        # Find most active user
        most_active_user = ""
        max_messages = 0
        
        for user, user_messages in chat.items():
            message_count = len(user_messages)
            if message_count > max_messages:
                max_messages = message_count
                most_active_user = user
        
        print("Most active user:", most_active_user, "with", max_messages, "messages")
    
    elif choice == 7:
        # Get user message count
        username = input("Enter username: ")
        if username in chat:
            message_count = len(chat[username])
            print(username, "sent", message_count, "messages")
        else:
            print("User not found")
    
    elif choice == 8:
        # Find user's most common word
        username = input("Enter username: ")
        if username in chat:
            all_words = []
            for message in chat[username]:
                words = message.split()
                all_words.extend(words)
            
            if all_words:
                word_counter = Counter(all_words)
                most_common_word, count = word_counter.most_common(1)[0]
                print("Most common word by", username, "is:", most_common_word, "(" + str(count), "times)")
            else:
                print("No words found for this user")
        else:
            print("User not found")
    
    elif choice == 9:
        # Get user's first and last message
        username = input("Enter username: ")
        if username in chat and chat[username]:
            first_message = chat[username][0]
            last_message = chat[username][-1]
            print("First message:", first_message)
            print("Last message:", last_message)
        else:
            print("User not found or no messages")
    
    elif choice == 10:
        # Check if user exists
        username = input("Enter username: ")
        if username in chat:
            print("User exists in the chat")
        else:
            print("User not found")
    
    elif choice == 11:
        # Find repeated words
        all_words = []
        for user_messages in chat.values():
            for message in user_messages:
                words = message.split()
                all_words.extend(words)
        
        word_counter = Counter(all_words)
        repeated_words = []
        for word, count in word_counter.items():
            if count > 1:
                repeated_words.append(word)
        
        print("Repeated words:", repeated_words)
    
    elif choice == 12:
        # User with longest average message
        longest_avg_user = ""
        max_avg_length = 0
        
        for user, user_messages in chat.items():
            if user_messages:
                total_length = 0
                for message in user_messages:
                    total_length += len(message)
                avg_length = total_length / len(user_messages)
                
                if avg_length > max_avg_length:
                    max_avg_length = avg_length
                    longest_avg_user = user
        
        print("User with longest average message:", longest_avg_user)
    
    elif choice == 13:
        # Count user mentions
        mentioned_user = input("Enter user to check mentions: ")
        mention_count = 0
        
        for user_messages in chat.values():
            for message in user_messages:
                if mentioned_user in message:
                    mention_count += 1
        
        print("'" + mentioned_user + "' mentioned in", mention_count, "messages")
    
    elif choice == 14:
        # Remove duplicate messages
        for user in chat:
            unique_messages = []
            seen_messages = set()
            
            for message in chat[user]:
                if message not in seen_messages:
                    unique_messages.append(message)
                    seen_messages.add(message)
            
            chat[user] = unique_messages
        
        print("Duplicate messages removed")
    
    elif choice == 15:
        # Sort messages alphabetically
        for user in chat:
            chat[user].sort()
        print("Messages sorted alphabetically for each user")
    
    elif choice == 16:
        # Extract questions
        print("Questions found in chat:")
        questions_found = False
        
        for user, user_messages in chat.items():
            for message in user_messages:
                if message.strip().endswith('?'):
                    print(user + ": " + message)
                    questions_found = True
        
        if not questions_found:
            print("No questions found")
    
    elif choice == 17:
        # Calculate reply ratio
        user1 = input("Enter first user: ")
        user2 = input("Enter second user: ")
        
        count1 = 0
        count2 = 0
        
        if user1 in chat:
            count1 = len(chat[user1])
        if user2 in chat:
            count2 = len(chat[user2])
        
        if count2 == 0:
            print("Reply ratio: Infinity (second user sent no messages)")
        else:
            ratio = count1 / count2
            print("Reply ratio (" + user1 + "/" + user2 + "):", round(ratio, 2))
    
    elif choice == 18:
        # Check for deleted messages
        deleted_keywords = ['deleted', 'message deleted', 'msg deleted']
        deleted_found = False
        
        for user, user_messages in chat.items():
            for message in user_messages:
                if message.lower() in deleted_keywords:
                    print(user + ": " + message)
                    deleted_found = True
        
        if not deleted_found:
            print("No deleted messages found")
    
    else:
        print("Invalid choice! Please select 0-18")