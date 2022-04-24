from audioop import mul
from ppadb.client import Client
import numpy
from PIL import Image
import time

adb = Client(host='127.0.0.1', port=5037)
devices = adb.devices()

if len(devices) == 0:
    print('no devices')
    quit()

device = devices[0]
print('success')

#get device width
device_width = 720.0
device_height = 1520
def conn_handler(conn):
    while True:
        data = conn.read(1024)
        if not data:
            break
        screen_info = data.decode('utf-8')
        start = screen_info.index(':')+2
        end = screen_info.index('x')
        global device_width
        device_width = float(screen_info[start:end])
        start = screen_info.index('x')+1
        global device_height
        device_height = screen_info[start:]
    conn.close()
device.shell('wm size',conn_handler)


# device.shell('input touchscreen swipe 500 500 500 500 400')
image = device.screencap()
with open('screen.png', 'wb') as f:
    f.write(image)

image = Image.open('screen.png')
image = numpy.array(image,dtype=numpy.uint8)

ninja_foot = int( int(device_height) * 1200.0 / 1520.0 )
print(ninja_foot)
while( sum(image[400,200,:3])/3 < 250 ):
    count = 0
    for i in range(719):
        if (sum(image[ninja_foot,i,:3]) < 100):
            first_black_pixel = i
            count = i
            break
    block_end = count
    for i in range(count,719):
        if (sum(image[ninja_foot,i,:3]) > 100):
            block_end = i
            count = i
            break
    distance = 0
    for i in range(count,719):
        if (sum(image[ninja_foot,i,:3]) < 100):
            distance = i-block_end
            break
    multiplier = 1.6
    # multiplier = (-1 * distance ) / 500.0 + 2.5 
    # interval = distance * multiplier

    distance = float(distance) / device_width
    if (distance < 25 / device_width):
        multiplier = 2.5
    elif (distance >= 25/ device_width and distance < 50/ device_width):
        multiplier = 2
    elif (distance >= 50/ device_width and distance < 100/ device_width):
        multiplier = 1.73
    elif (distance >= 100/ device_width and distance < 150/ device_width):
        multiplier = 1.71
    elif (distance >= 150 / device_width and distance < 200/ device_width):
        multiplier = 1.7
    elif (distance >= 200/ device_width and distance < 250/ device_width): #perfect
        multiplier = 1.65
    elif (distance >= 250/ device_width and distance < 300/ device_width):
        multiplier = 1.59
    elif (distance >= 300/ device_width and distance < 350/ device_width):
        multiplier = 1.57
    elif (distance >= 350/ device_width and distance < 400/ device_width):
        multiplier = 1.54
    else:
        multiplier = 1.53
    multiplier = multiplier * device_width   
    interval = distance * multiplier
    print(f'distance: {distance} , multiplier: {multiplier}')
    # print(str(interval)+' '+str(int(interval)))
    device.shell('input touchscreen swipe 500 500 500 500 '+str(int(interval)))
    time.sleep(3)
    image = device.screencap()
    with open('screen.png', 'wb') as f:
        f.write(image)
    image = Image.open('screen.png')
    image = numpy.array(image,dtype=numpy.uint8)
device.shell('input touchscreen swipe 595 1056 595 1056 100')
print('game over')
