import subprocess
import re

def IPAddress():
    data = subprocess.getoutput("ifconfig")
    allIp = re.findall("inet [.\d]+", data)

    if allIp:
        if len(allIp) == 3:
            address = re.match("inet ([.\d]+)", allIp[0]).group(1)

        else:
            address = re.match("inet ([.\d]+)", allIp[0]).group(1)

    return address
