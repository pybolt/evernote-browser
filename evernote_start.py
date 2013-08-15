from evernote.api.client import EvernoteClient, NoteStore
import os

dev_token = "S=s1:U=69cac:E=14611178634:C=13eb9665a37:P=1cd:A=en-devtoken:V=2:H=80b1ea7e8a83bb999d4845be77e27e28"
client = EvernoteClient(token=dev_token, sandbox=True)
userStore = client.get_user_store()
user=userStore.getUser()

note_store= client.get_note_store()

#get a list of all the notebooks
notebook_list=note_store.listNotebooks()

def get_notes(notebook):
	'''get a list of all the notes form a give notebooks, returns a list of notes'''
	notebookFilter=NoteStore.NoteFilter()
	notebookFilter.notebookGuid=notebook.guid
	notes=note_store.findNotes(dev_token, notebookFilter, 0, 100)
	return notes.notes

def get_resources(note):
	'''get the list of resources from a given note, returns a list of resoucres'''
	if note.resources:
		resources=[]
		for resource in note.resources:
			resources.append(note_store.getResource(dev_token, resource.guid, True, False, True, False))
		return resources
	else:
		return None


user=userStore.getUser()

if not os.path.exists(user.username):
    os.makedirs(user.username)


for notebook in notebook_list:
	
	if not os.path.exists(user.username+'/'+notebook.name):
		os.makedirs(user.username+'/'+notebook.name)

	for note in get_notes(notebook):

		if not os.path.exists(user.username+'/'+notebook.name+'/'+note.title):
			os.makedirs(user.username+'/'+notebook.name+'/'+note.title)

		#get resources
		if get_resources(note):	
			for resource in get_resources(note):
				try:
					f=open(user.username+'/'+notebook.name+'/'+note.title+'/'+resource.attributes.fileName, 'w')
				except TypeError:
					f=open(user.username+'/'+notebook.name+'/'+note.title+'/'+resource.guid, 'w') # need to go from mime (resource.mime) to file extention

				f.write(resource.data.body)
				f.close()

		#write the note in html
		fullNote=note_store.getNote(dev_token, note.guid, True, False, False, False)
		f=open(user.username+'/'+notebook.name+'/'+note.title+'/'+note.title+'.html', 'w')
    	f.write(fullNote.content)
    	f.close()







