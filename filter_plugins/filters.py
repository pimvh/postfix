#!/usr/bin/python3

import ipaddress

from ansible.errors import AnsibleFilterError
from ansible.template import AnsibleUndefined


class FilterModule:
    """custom filter to check if something is a list"""

    def filters(self):
        return {
            "bracket_ipv6": self.bracket_ipv6,
        }

    def bracket_ipv6(self, obj):
        """Bracket an IPv6 network, leave IPv4 networks unmodified, e.g:
        ::1/128     -> [::1]/128
        127.0.0.1   -> 127.0.0.1"""

        if isinstance(obj, AnsibleUndefined):
            return []

        elif not isinstance(obj, str):
            raise AnsibleFilterError("This only works on a IPv4 or IPv6 network string")

        network, address = None, None

        try:
            network = ipaddress.ip_network(obj)
        except:
            pass

        try:
            address = ipaddress.ip_address(obj)
        except:
            pass

        if not network and not address:
            raise ValueError("Passed value is not an IP-address")

        elif isinstance(address, ipaddress.IPv6Address):
            return "[" + obj + "]"

        elif isinstance(network, ipaddress.IPv6Network):
            return "[" + obj.replace("/", "]/")

        else:
            return obj
