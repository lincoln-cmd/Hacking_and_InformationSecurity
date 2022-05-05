# https://scribblinganything.tistory.com/190?category=987545

'''
finding wifi password
'''

import subprocess
import re
import os

os.system('chcp 437')
# chcp 437 : english
# chcp 949 : korean
#os.system('netsh wlan show profiles') # 'netsh' can be operated by os.system

network_profiles = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], capture_output = True)
# capture_output : get result values as 'return'
print("###")
print(network_profiles)
SSID_names = (re.findall(' : (.*)\r', network_profiles.stdout.decode()))
print("###")
print(SSID_names)
id_pw = {}
o_num, err_msg, err_filename)
FileNotFoundError: [Errno 2] No such file or directory: 'netsh'



if SSID_names:
    for SSID_name in SSID_names:
        SSID_info = subprocess.run(['netsh', 'wlan', 'show', 'profile', SSID_name], capture_output = True).stdout.decode()
        if re.findall('Security key          : Present', SSID_info):
            password_visible = subprocess.run(['netsh', 'wlan', 'show', 'profile', SSID_name, 'key=clear'], capture_output = True).stdout.decode()
            password = re.findall("Key Content             : (.*)\r", password_visible)
            id_ps[SSID_nave] = password

        else:
            print('There are not any saved SSID')
        print("###")
        print(id_pw)
