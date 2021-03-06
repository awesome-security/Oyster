import platform
import socket


def get_sys_info():
    info = """
Machine: {}\nVersion: {}
Platform: {}\nNode: {}\nUname: {}\nSystem: {}
Processor: {}\n\nHost Name: {}\nFQDN: {}\n
""".format(
        platform.machine(),
        platform.version(),
        platform.platform(),
        platform.node(),
        platform.uname(),
        platform.system(),
        platform.processor(),
        socket.gethostname(),
        socket.getfqdn()
    )
    return info


class Plugin(object):
    """
    Gather basic system information and send it back to the server
    """

    version = 'v1.0'
    invocation = 'sysinfo'
    enabled = True

    def run(self, client, data):
        client.send_data(get_sys_info())

