from __future__ import absolute_import

import ansible
from distutils.version import LooseVersion

ansible_version = LooseVersion(ansible.__version__)

if ansible_version >= LooseVersion("2.2.0.0"):
    from ansible_toolset.ansible.version22 import AnsibleAdapter22 as AnsibleAdapter
elif ansible_version >= LooseVersion("2.0.0.0"):
    from ansible_toolset.ansible.version20 import AnsibleAdapter20 as AnsibleAdapter
else:
    raise RuntimeError("This software is intended to be used with Ansible 2.0 or higher.")
