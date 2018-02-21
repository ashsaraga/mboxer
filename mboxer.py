import mailbox
import csv

writer = csv.writer(open("output.csv", "wb"))

for message in mailbox.mbox('input.mbox'):
	writer.writerow([message['message-id'], message['subject'], message['from']])

print 'Mboxing complete! *high five*'
