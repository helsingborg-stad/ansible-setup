import os
import sys
import time
import getopt

from dropbox_backup import pull, push, list


# CONSTANS
# ##########################
LIST_OPTIONS_HELP = {
    '[-l --latest]': 'get the latest file from dropbox'
}

PUSH_OPTIONS_HELP = {
    '[-f <file_path> --file <file_path>]': 'the file to send to dropbox'
}

PULL_OPTIONS_HELP = {
    '[-f <file_path> --file <file_path>]': 'the file to get from dropbox',
    '[-t <file_path> --to <file_path>]': 'where to put the file in your filesystem'
}

VALID_ACTIONS = {
    'push': {
        'opt': 'f:',
        'opt_long': ['file='],
        'help': 'push - send a backup to dropbox',
        'help_opt': PUSH_OPTIONS_HELP,
        'f': push
    },
    'pull': {
        'opt': 'f:t:',
        'opt_long': ['file=', 'to='],
        'help': 'pull - get a backup from dropbox',
        'help_opt': PULL_OPTIONS_HELP,
        'f': pull
    },
    'list': {
        'opt': 'l',
        'opt_long': ['latest'],
        'help': 'list - list the files avilable in dropbox',
        'help_opt': LIST_OPTIONS_HELP,
        'f': list
    }
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

# String ->
# produce helptext of valid actions to the command line
def print_valid_options(action_name):
    if action_name in VALID_ACTIONS:
        print (VALID_ACTIONS[action_name]['help'])
        print ()
        for k, v in VALID_ACTIONS[action_name]['help_opt'].items(): print (k, v)
    else:
        for k, v in VALID_ACTIONS.items(): print (v['help'])

    print ()


# (listof String) -> Dict
# get the cmd params and produce a dict with the validated arguments
def validate_args(argv, opt, opt_long):
    try:
        opts, args = getopt.getopt(argv, opt, opt_long)
        return dict((x, y) for x, y in opts)
    except Exception as e:
        print ('ERROR: {}\n'.format(e))
        print_valid_options('no_action')
        sys.exit()


# String -> String
# produce a valid action, otherwhise throw exception/help and end application
def get_action(action):
    if action not in VALID_ACTIONS:
        print_valid_options('no_action')
        sys.exit()

    return action


def main(args):

    # Get valid action
    action_name = args.pop(0)
    action = VALID_ACTIONS[get_action(action_name)]

    # Give help
    if ( '-h' in args ):
        print_valid_options(action_name)
        sys.exit()

    # Do designated action
    action['f'](validate_args(args, action['opt'], action['opt_long']))

if __name__ == "__main__":
    main(sys.argv[1:])
