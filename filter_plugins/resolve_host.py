import socket

def resolve_host(host):

    str(host)
    return socket.gethostbyname(host)


class FilterModule(object):
    def filters(self):
        return {
            'resolve_host': resolve_host,
		}
        
 
        
# ping -W1 -c1 aav.pgpool02|grep aav.pgpool02|cut -d'(' -f2|cut -d')' -f1
# dig +short sbb.ch