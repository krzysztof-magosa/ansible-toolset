from __future__ import absolute_import

import os
from ansible_toolset import consts as C

class ErrorMessage(Exception):
    pass

def read_file_contents(filename):
    with open(filename, "rb") as fh:
        data = fh.read()

    return data


def get_ansible_vault_password():
    password_file = os.getenv(C.ANSIBLE_VAULT_PASSWORD_FILE_ENV)
    if not password_file:
        raise RuntimeError("You must set {} environment variable.".format(C.ANSIBLE_VAULT_PASSWORD_FILE_ENV))

    return read_file_contents(password_file).rstrip('\n')
