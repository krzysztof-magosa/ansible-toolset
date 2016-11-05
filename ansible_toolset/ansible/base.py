from __future__ import absolute_import

class AnsibleAdapterBase(object):
    def __init__(self, vault_password):
        self.vault_password = vault_password
        self.init()

    def init(self):
        pass

    def is_encrypted_vault(self, filename):
        raise NotImplementedError()

    def encrypt_vault(self, filename):
        raise NotImplementedError()

    def decrypt_vault(self, filename):
        raise NotImplementedError()

    def vault_plaintext(self, filename):
        raise NotImplementedError()
