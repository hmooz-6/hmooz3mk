#Bovonos
import threading ,amino, requests, json

client=amino.Client()
print ("By Bovonos")
client.login(email=input("Email: "),password="hamza#$1234")
nfo=client.get_from_code('http://aminoapps.com/p/hhxbvm')
uId=nfo.objectId
co=nfo.path[1:nfo.path.index("/")]
client.join_community(comId=co)
sent=amino.SubClient(comId=co,profile=client.profile)
def invc():
	return sent.join_chat(chatId=uId)and sent.leave_chat(chatId=uId)


while True:
	threading.Thread(target=invc).start()
	
