# importing libraries

import xlsxwriter
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch


# makeing client

api_id = ""  # Refactor this wtih a dynamic variable
# Refactor this wtih a dynamic variable
api_hash = ""

# Refactor this wtih a dynamic variable
target_group = "group name"
client = TelegramClient('test', api_id, api_hash)
client.connect()
print(f"Connected : {client.is_connected()}")
# Age be error 'Key is not registered khordi' ba with boro mesle khate payini
# with client:
#     print(client.get_dialogs()

workbook = xlsxwriter.Workbook(target_group+'.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write(0, 0, 'User name')
worksheet.write(0, 1, 'User ID')
worksheet.write(0, 2, 'User Phone Number')
print('excel file created')

print('starting getting users')

queryKey = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
channel = target_group
all_participants = []
row = 1
column = 0
for key in queryKey:
    offset = 0
    limit = 100
    print(key+' has started')
    while True:
        participants = client(GetParticipantsRequest(
            channel, ChannelParticipantsSearch(key), offset, limit,
            hash=0
        ))
        if not participants.users:
            break
        for user in participants.users:
            try:
                # if re.findall(r"\b[a-zA-Z]", user.first_name)[0].lower() == key:
                all_participants.append(user)
                if user.phone != None:
                    worksheet.write(row, column, user.username)
                    column += 1
                    worksheet.write(row, column, user.first_name)
                    column += 1
                    worksheet.write(row, column, user.phone)
                    row += 1
                    column = 0
                    print(str(row)+'/'+str(len(all_participants)))
            except:
                pass
        offset += len(participants.users)
        if offset >=9999:
            break



            
        # users.append(participants.users)


print('\nDone')
workbook.close()
