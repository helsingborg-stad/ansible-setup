import os
import dropbox
import ntpath


# CONSTANS
# ##########################
ACCESS_TOKEN = os.environ['DROPBOX_ACCESS_TOKEN']


# FUNCTIONS
# ##########################

# -> DropboxClient
# produce a dropbox client
def get_dropbox_client():
    return dropbox.client.DropboxClient(ACCESS_TOKEN)


# PushParam -> Boolean
# produce true if successfull in pushing file to dropbox
def push(args):
    try:
        f = open(args['-f'], 'rb')
        client = get_dropbox_client()
        response = client.put_file(ntpath.basename(args['-f']), f)

        print ('uploaded:', response['path'], response['size'], '\n')
        return True

    except Exception as e:
        print ('ERROR: {}\n'.format(e))
        return False


# PullParam -> Boolean
# produce true if successfull in pushing file to dropbox
def pull(args):
    try:
        if (os.path.isfile(args['-t'])):
            raise Exception('-t: file {} allready exists'.format(args['-t']))

        client = get_dropbox_client()
        f, metadata = client.get_file_and_metadata('{}'.format(args['-f']))
        out = open(args['-t'], 'wb')
        out.write(f.read())
        out.close()

        print ('pulled down:', args['-t'], metadata['size'], '\n')
        return True
    except Exception as e:
        print ('ERROR: {}\n'.format(e))
        return False


# ->
# produce true if successfull in pushing file to dropbox
def list():
    try:
        client = get_dropbox_client()
        for f in client.metadata('/')['contents']:
            print ('{} | {} | {}'.format(f['path'], f['size'], f['client_mtime']))

        print ('\n')

    except Exception as e:
        print ('ERROR: {}\n'.format(e))
        return False
