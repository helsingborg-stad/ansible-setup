import os
import sys
import time
import getopt

from dropbox_backup import pull, push, list


# CONSTANS
# ##########################
USAGE_EXAMPLE = 'usage: dropbox_backup.py [-h for help] [-f absolute path to the file to save to dropbox]'
VALID_ACTIONS = {
                    'push': {'opt': 'f:', 'help': 'push - send a backup to dropbox', 'f': push},
                    'pull': {'opt': 'f:t:', 'help': 'pull - get a backup from dropbox', 'f': pull},
                    'list': {'opt': '', 'help': 'list - list the files avilable in dropbox', 'f': list}
                }


# DATADEF
# ##########################

# PushParam is dict(-f=String)
    # -f     - the file to pushed to dropbox
    # interp. the parameters to perform a push to dropbox

PUSH1 = { '-f': '/path/to/file.txt' }
PUSH3 = { '-f': '/path/to/file.sql' }


# PullParam is dict(-f=String)
    # -f     - the file to pull from dropbox
    # -t     - the absolute path to were to store the file pulled from dropbox
    # interp. the parameters to perform a pull from dropbox

PULL1 = { '-f': 'file.txt', '-t': '' }
PULL3 = { '-f': 'file.sql', '-t': '/path/to/put/file' }


# FUNCTIONS
# ##########################

# (listof String) -> Dict
# get the cmd params and produce a dict with the validated arguments
def validate_args(argv, opt):
    try:
        opts, args = getopt.getopt(argv, opt)
        return dict((x, y) for x, y in opts)
    except Exception as e:
        print ('ERROR: {}\n'.format(e))
        print ('{}\n'.format(USAGE_EXAMPLE))
        sys.exit()


# ->
# produce helptext of valid actions to the command line
def print_valid_options():
    for k, v in VALID_ACTIONS.items():
        print (v['help'])
    print ()


# String -> String
# produce a valid action, otherwhise throw exception/help and end application
def get_action(action):
    if action not in VALID_ACTIONS:
        print_valid_options()
        sys.exit()

    return action


def main(args):
    print ('Dropbox backup script v0.0.1\n')
    start = time.perf_counter()

    # Get valid action
    action = VALID_ACTIONS[get_action(args.pop(0))]

    # Do designated action
    action['f'](validate_args(args, action['opt']))

    # Report run time
    end = time.perf_counter()
    total_time = time.strftime("%H:%M:%S", time.gmtime(end-start))
    print ('Runtime: {}'.format(total_time))


if __name__ == "__main__":
    main(sys.argv[1:])
