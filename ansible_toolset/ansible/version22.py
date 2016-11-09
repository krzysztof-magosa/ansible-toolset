from __future__ import absolute_import

from ansible_toolset.ansible.base import AnsibleAdapterBase
from ansible_toolset import utils
from ansible.parsing.vault import VaultEditor
from ansible.parsing.vault import is_encrypted

class AnsibleAdapter22(AnsibleAdapterBase):
    def init(self):
        self.vault_editor = VaultEditor(self.vault_password)

    def is_encrypted_vault(self, filename):
        return is_encrypted(utils.read_file_contents(filename))

    def encrypt_vault(self, filename):
        self.vault_editor.encrypt_file(filename)

    def decrypt_vault(self, filename):
        self.vault_editor.decrypt_file(filename)

    def vault_plaintext(self, filename):
        return self.vault_editor.plaintext(filename)
