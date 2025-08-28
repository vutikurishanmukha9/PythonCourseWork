import EmailAutomation

subject = input("Enter the Subject: ")
body = input("Enter the Body of the Email: ")

choice = input("Do you want to send (1) Single Email or (2) Bulk Emails? Enter 1 or 2: ")

if choice == "1":
    recipient = input("Enter recipient email: ")
    EmailAutomation.send_email(recipient, subject, body)

elif choice == "2":
    csv_file = input("Enter path to CSV file with email addresses: ")
    EmailAutomation.send_bulk_emails(csv_file, subject, body)
else:
    print("Invalid choice! Please enter 1 or 2.")
