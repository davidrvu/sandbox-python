# DAVIDRVU - 2019

# pip install pyserial

import serial
import time
import datetime
import struct
import sys 

def serial_ports():
    # PARA VERLOS EN WINDOWS HAY QUE EJECUTAR: "devmgmt.msc"
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    print("ports = ")
    print(ports)
    result = []
    for port in ports:
        s = serial.Serial(port)
        print(s)        
        #try:
        #    s = serial.Serial(port)
        #    print(s)
        #    s.close()
        #    result.append(port)
        #except (OSError, serial.SerialException):
        #    print(port)
        #    pass
    return result



#print(serial_ports())

#print("asdads")
#sys.exit()


#ser = serial.Serial('/dev/ttyUSB0',57600)
ser = serial.Serial('Port_#0009.Hub_#0001',57600)
pack = [0xef01, 0xffffffff, 0x1]

def printx(l):
    for i in l:
        print(hex(i))
    print('')

def readPacket():
    time.sleep(1)
    w = ser.inWaiting()
    ret = []
    if w >= 9:
        s = ser.read(9) #partial read to get length
        ret.extend(struct.unpack('!HIBH', s))
        ln = ret[-1]
        
        time.sleep(1)
        w = ser.inWaiting()
        if w >= ln:
            s = ser.read(ln)
            form = '!' + 'B' * (ln - 2) + 'H'
            ret.extend(struct.unpack(form, s))
    return ret


def writePacket(data):
    pack2 = pack + [(len(data) + 2)]
    a = sum(pack2[-2:] + data)
    pack_str = '!HIBH' + 'B' * len(data) + 'H'
    l = pack2 + data + [a]
    s = struct.pack(pack_str, *l)
    ser.write(s)


def verifyFinger():
    data = [0x13, 0x0, 0, 0, 0]
    writePacket(data)
    s = readPacket()
    return s[4]
    
def genImg():
    data = [0x1]
    writePacket(data)
    s = readPacket()
    return s[4]    

def img2Tz(buf):
    data = [0x2, buf]
    writePacket(data)
    s = readPacket()
    return s[4]

def regModel():
    data = [0x5]
    writePacket(data)
    s = readPacket()
    return s[4]

def store(id):
    data = [0x6, 0x1, 0x0, id]
    writePacket(data)
    s = readPacket()
    return s[4]    
    

if verifyFinger():
    print('Verification Error')
    sys.exit(0)

print('Put finger')
sys.stdout.flush()

time.sleep(1)    
while genImg():
    time.sleep(0.1)

    print('.')
    sys.stdout.flush()

print('')
sys.stdout.flush()

if img2Tz(1):
    print('Conversion Error')
    sys.exit(0)

print('Put finger again')
sys.stdout.flush()

time.sleep(1)    
while genImg():
    time.sleep(0.1)
    print('.')
    sys.stdout.flush()

print('')
sys.stdout.flush()

if img2Tz(2):
    print('Conversion Error')
    sys.exit(0)

if regModel():
    print('Template Error')
    sys.exit(0)
id = 1
if store(id):
    print('Store Error')
    sys.exit(0)    

print("Enrolled successfully at id = " + str(id))