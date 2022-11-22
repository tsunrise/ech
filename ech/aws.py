import boto3
from .profile import get_server_info
from dataclasses import dataclass
import colorama

def colored_state(state: str):
    green_states = ["running", "pending"]
    yellow_states = ["stopping"]
    red_states = ["stopped",  "terminated"]
    if state in green_states:
        return colorama.Fore.GREEN + state + colorama.Fore.RESET
    elif state in yellow_states:
        return colorama.Fore.YELLOW + state + colorama.Fore.RESET
    elif state in red_states:
        return colorama.Fore.RED + state + colorama.Fore.RESET
    else:
        return state


@dataclass
class StartInstanceResult:
    previous_state: str
    current_state: str

    def __str__(self) -> str:
        return f"Instance state changed from {colored_state(self.previous_state)} to {colored_state(self.current_state)}"

def start_instance(alias: str):
    # Get server info from config file
    server = get_server_info(alias)
    # Start instance
    session = boto3.session.Session(profile_name=server.profile, region_name=server.region)
    result = session.client('ec2').start_instances(InstanceIds=[server.id], DryRun=False)
    return StartInstanceResult(result["StartingInstances"][0]["PreviousState"]["Name"], result["StartingInstances"][0]["CurrentState"]["Name"])

@dataclass
class InstanceDescription:
    alias: str
    id: str
    dns: str

    def __str__(self):
        return f"{self.alias} ({self.id}): {self.dns}"

def describe_instance(alias: str):
    # Get server info from config file
    server = get_server_info(alias)
    # Describe instance
    session = boto3.session.Session(profile_name=server.profile, region_name=server.region)
    result = session.client('ec2').describe_instances(InstanceIds=[server.id], DryRun=False)
    dns = result["Reservations"][0]["Instances"][0]["PublicDnsName"]
    return InstanceDescription(alias, server.id, dns)
    
@dataclass
class StopInstanceResult:
    previous_state: str
    current_state: str

    def __str__(self) -> str:
        return f"Instance state changed from {colored_state(self.previous_state)} to {colored_state(self.current_state)}"

def stop_instance(alias: str):
    # Get server info from config file
    server = get_server_info(alias)
    # Stop instance
    session = boto3.session.Session(profile_name=server.profile, region_name=server.region)
    result = session.client('ec2').stop_instances(InstanceIds=[server.id], DryRun=False)
    return StopInstanceResult(result["StoppingInstances"][0]["PreviousState"]["Name"], result["StoppingInstances"][0]["CurrentState"]["Name"])


