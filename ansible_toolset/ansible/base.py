from __future__ import absolute_import

from ansible_toolset import utils

class AnsibleAdapterBase:
    def __init__(self, vault_password):
        self.vault_password = vault_password
        self.init()

    def init():
        pass

    def is_encrypted_vault(self, filename):
        raise NotImplementedError()

    def encrypt_vault(self, filename):
        raise NotImplementedError()

    def decrypt_vault(self, filename):
        raise NotImplementedError()
