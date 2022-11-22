from .aws import *
from sshconf import read_ssh_config
import os
import warnings

DEFAULT_IDENTITY_FILE = "~/aws.pem"

def bind_instance(alias: str):
    server_info = get_server_info(alias)
    if server_info.key is None:
        server_info.key = DEFAULT_IDENTITY_FILE
    result = describe_instance(alias)
    # Bind server to config file
    home_dir = os.path.expanduser("~")
    config_file = os.path.join(home_dir, ".ssh", "config")
    c  = read_ssh_config(config_file)
    if result.dns:
        try:
            c.set(alias, Hostname=result.dns, User=server_info.user, IdentityFile=server_info.key)
        except:
            c.add(alias, Hostname=result.dns, User=server_info.user, IdentityFile=server_info.key)
    else:
        warnings.warn(f"Instance {alias} has no public DNS name")
    c.save()
    # Return result
    return result