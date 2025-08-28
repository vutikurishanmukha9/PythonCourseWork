import smtplib                                          #Simple mail transfer Protocol for sending emails
import os                                               #For file path and file existance existence checks
import csv                                              #To Read email Address from the CSV file
from email.mime.multipart import MIMEMultipart          #For creating multipart email  messages
from email.mime.text import MIMEText                    #For adding plain text to email body

