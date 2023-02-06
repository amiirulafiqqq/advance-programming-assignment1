import smtplib

input_file = open ('food.csv','r') #open csv file file
output_file = open ('food_file_copy.csv','w') # create the same csv file
csv = input_file.read() #read content of source file

output_file.write(csv) #content of csv file are being copied to the new csv file
		
input_file.close()
output_file.close()
	
#email notification after csv copied completed

subject = 'CSV copy by Python'
body = 'Copy completed'
sender_email = 'muhammadamirulafiq@graduate.utm.my'
receiver_email = 'amiirulafiqqq@gmail.com'
password = input(str("Enter password:"))  #to make it automatically. Put the email password directly in here
	
message = 'subject: ' + subject+'\n\n' + body

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
server.sendmail(sender_email, receiver_email, message)

print("your file copy has finished.")
