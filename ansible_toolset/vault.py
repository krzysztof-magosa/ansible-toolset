from __future__ import absolute_import

import os
from ansible_toolset.models import *


class VaultManager:
    def __init__(self, ansible):
        self.ansible = ansible

    def is_encrypted(self, filename):
        return self.ansible.is_encrypted_vault(filename)

    def encrypt(self, filename):
        # in case somebody use ansible-vault manually in meantime.
        if self.is_encrypted(filename):
            return
        vault = Vault.get(filename=filename)

        if os.path.getmtime(filename) > vault.mtime:
            self.ansible.encrypt_vault(filename)
        else:
            with open(filename, "w") as handler:
                handler.write(vault.contents)

        Vault.delete().where(Vault.filename==filename).execute()


    def decrypt(self, filename):
        with open(filename, "r") as handler:
            contents = handler.read()

        self.ansible.decrypt_vault(filename)

        vault, _ = Vault.get_or_create(filename=filename)
        vault.contents = contents
        vault.mtime = os.path.getmtime(filename)
        vault.save()


    def is_known(self, filename):
        return Vault.select().where(Vault.filename==filename).exists()

    def list_vaults(self, open=False, closed=False):
        for root, _, files in os.walk("."):
            for basename in files:
                filename = os.path.realpath(os.path.join(root, basename))

                if closed and self.is_encrypted(filename):
                    yield dict(path=filename, state='closed')
                elif open and self.is_known(filename):
                    yield dict(path=filename, state='open')

    def open(self):
        for item in self.list_vaults(closed=True):
            self.decrypt(item["path"])

    def close(self):
        for item in self.list_vaults(open=True):
            self.encrypt(item["path"])

    def list(self):
        return self.list_vaults(open=True, closed=True)
