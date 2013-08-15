from evernote.api.client import EvernoteClient, NoteStore

dev_token = "S=s1:U=69cac:E=14611178634:C=13eb9665a37:P=1cd:A=en-devtoken:V=2:H=80b1ea7e8a83bb999d4845be77e27e28"
client = EvernoteClient(token=dev_token, sandbox=True)
userStore = client.get_user_store()
user=userStore.getUser()
print user.username

note_store= client.get_note_store()

notebooks=note_store.listNotebooks()
for notebook in notebooks:
    print "  * ", notebook.name

fil=NoteStore.NoteFilter()
fil.notebookGuid=notebook.guid
notes=note_store.findNotes(dev_token, fil, 0,100)
n=0
'''f=open('newtest.html','w')
for note in notes.notes:
    fullNote=note_store.getNote(dev_token, note.guid, True, False, False, False)
    print fullNote.content
    f.write(fullNote.content)

res=notes.notes[1].resources[0] #resource class type!?
#how do i download the resource?!
#http://dev.evernote.com/start/core/resources.php#downloading

res3guid=notes.notes[3].resources[0].guid

res4=note_store.getResource(dev_token, res3guid, True, False, True, False)
fileContent=res4.data.body


f=open('test.jpg','w')
f.write(fileContent)
f.close()
#picture is distorted: hex appears to be out of order :/
'''