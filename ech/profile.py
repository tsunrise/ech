from typing import Optional
import toml
from dataclasses import dataclass
import os

@dataclass
class ServerInfo:
    alias: str
    id: str
    region: str
    profile: str
    user: str
    key: Optional[str]

def get_server_info(alias):
    home_dir = os.path.expanduser("~")
    config_file = os.path.join(home_dir, "awsh.toml")
    # Read config file from "~/awsh.toml"
    with open(config_file, "r") as f:
        config = toml.load(f)
        servers = config["servers"]
        server = servers[alias]
        if "profile" not in server:
            server["profile"] = "default"
        if "user" not in server:
            server["user"] = "ubuntu"
        return ServerInfo(alias, server["id"], server["region"], server["profile"], server["user"], server.get("key"))