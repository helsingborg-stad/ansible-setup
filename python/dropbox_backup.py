import os
import sys
import time
import dropbox
import getopt
import ntpath


# CONSTANS
# ##########################
ACCESS_TOKEN = os.environ['DROPBOX_ACCESS_TOKEN']
USAGE_EXAMPLE = 'usage: dropbox_backup.py [-h for help] [-f absolute path to the file to save to dropbox]'


# FUNCTIONS
# ##########################


# (listof String) -> Dict
# get the cmd params and produce a dict with the validated arguments
def validate_args(argv):
    try:
        opts, args = getopt.getopt(argv,'f:')
        return dict((x, y) for x, y in opts)
    except Exception as e:
        print ('ERROR: {}\n'.format(e))
        print ('{}\n'.format(USAGE_EXAMPLE))
        sys.exit()


# String DropboxClient -> Boolean
# produce true if successfull in pushing file to dropbox
def push_to_dropbox(filename, client):

    try:
        f = open(filename, 'rb')
        response = client.put_file(ntpath.basename(filename), f)

        print ('uploaded:', response['path'], response['size'], '\n')

    except Exception as e:
        print ('ERROR: {}\n'.format(e))


def main(args):
    print ('Dropbox backup script v0.0.1\n')
    start = time.perf_counter()

    # Check that the input is correct and get values given
    cmdargs = validate_args(args)

    # Create dropbox client
    client = dropbox.client.DropboxClient(ACCESS_TOKEN)

    # Push file to dropbox
    push_to_dropbox(cmdargs['-f'], client)

    # Report run time
    end = time.perf_counter()
    total_time = time.strftime("%H:%M:%S", time.gmtime(end-start))
    print ('Runtime: {}'.format(total_time))


if __name__ == "__main__":
    main(sys.argv[1:])
