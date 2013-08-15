from evernote.api.client import EvernoteClient, NoteStore
import os

dev_token = "S=s1:U=69cac:E=14611178634:C=13eb9665a37:P=1cd:A=en-devtoken:V=2:H=80b1ea7e8a83bb999d4845be77e27e28"

def enml_to_html(enml):
	'''takes ENML markup and turns it into HTML markup, any media items will be hashed and the src will be added to the html tag'''
	pass


client = EvernoteClient(token=dev_token, sandbox=True)

userStore = client.get_user_store()
user=userStore.getUser()

note_store= client.get_note_store()

if not os.path.exists(user.username):
    os.makedirs(user.username)

notebooks=note_store.listNotebooks()
for notebook in notebooks:
	
	if not os.path.exists(user.username+'/'+notebook.name):
		os.makedirs(user.username+'/'+notebook.name)

	noteFilter=NoteStore.NoteFilter()
	noteFilter.notebookGuid=notebook.guid

	notes=note_store.findNotes(dev_token, noteFilter, 0, 100)

	for note in notes.notes:
		fullNote=note_store.getNote(dev_token, note.guid, True, False, False, False)


		if not os.path.exists(user.username+'/'+notebook.name+'/'+note.title):
			os.makedirs(user.username+'/'+notebook.name+'/'+note.title)
	
		if note.resources:
			for resource in note.resources:
				content=note_store.getResource(dev_token, resource.guid, True, False, True, False)

				try:
					f=open(user.username+'/'+notebook.name+'/'+note.title+'/'+content.attributes.fileName, 'w')
				except TypeError:
					f=open(user.username+'/'+notebook.name+'/'+note.title+'/'+content.guid, 'w') # need to go from mime (content.mime) to file extention

				f.write(content.data.body)
				f.close()

		#enml_to_html(enml) later
		
    	f=open(user.username+'/'+notebook.name+'/'+note.title+'/'+note.title+'.html', 'w')
    	f.write(fullNote.content)
    	f.close()