from p4utils.mininetlib.network_API import NetworkAPI

net = NetworkAPI()

# Network general options
net.setLogLevel('info')
net.enableCli()


# Network definition
net.addP4Switch('s1')
net.addP4Switch('s2')
#net.addP4Switch('...')
net.setP4SourceAll('p4src/forwarding.p4') # p4 source file name

net.addHost('h1')
net.addHost('h2')
#net.addHost('...')

net.addLink('h1','s1')
net.addLink('s1','s2')
net.addLink('s2','h2')
#net.addLink('...', '...')

#set interface port number
net.setIntfPort('h1', 's1', 1)  # Set the number of the port on h1 facing s1
net.setIntfPort('s1', 'h1', 1)
net.setIntfPort('s1','s2',2)
net.setIntfPort('s2','s1',1)
net.setIntfPort('s2','h2',2)
net.setIntfPort('h2','s2',1)
#net.SetIntfPort('...', '...', '...')

# Assignment strategy
net.mixed() #ip assignment strategy. For more information, access: https://nsg-ethz.github.io/p4-utils/usage.html

# Nodes general options
net.enablePcapDumpAll()
net.enableLogAll()

# Start network
net.startNetwork() #this line actually start the topology with all configuration above
