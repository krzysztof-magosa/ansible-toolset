# Ansible Toolset
[![PyPI version](https://badge.fury.io/py/ansible-toolset.svg)](https://badge.fury.io/py/ansible-toolset)

[![asciicast](https://asciinema.org/a/91811.png)](https://asciinema.org/a/91811)

## Setup
### Install
You can install `ansible-toolset` from PIP like other python package.
```
$ pip install ansible-toolset
```

At the moment `ansible-toolset` supports only Ansible 2.0 and 2.1.  
Support for Ansible 2.2 will be added in upcoming days.  
There is no plan to support Ansible 1.x.

### Configuration

Create file containing your Ansible Vault password.
```
$ echo "my_secret_password" > ~/.ansible-vault-password
```

Prevent other users of your computer from being able to see your password.
```
$ chmod 0600 ~/.ansible-vault-password
```

Set environment variable so Ansible knows where to find password file.  
You may want to add this line to your shell profile file.
```
$ export ANSIBLE_VAULT_PASSWORD_FILE=~/.ansible-vault-password
```

## Commands
### Vault

To create new vault you can use `ansible-vault` directly.  
This command is provided for consistency and convenience.
```
$ ats-vault create path/to/some/secret/file.yml
```


Decrypt all existing vaults below current directory.
```
$ ats-vault open
```

Encrypt all previously decrypted vaults.
```
$ ats-vault close
```

Grep vaults (including closed ones) against some word:
```
$ ats-vault grep word
```

Grep vaults (including closed ones) against python regex:
```
$ ats-vault rgrep 'word\d+'
```

`ats-vault` stores previous encrypted content in SQLite database.
When you close wallet without doing changes, original content is restored.
It prevents `git` from seeing changes in files which is opposite to `ansible-vault` behavior
which produces different result every time, even if secrets were not changed.
