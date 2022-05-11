# https://scribblinganything.tistory.com/244?category=987545

# If you access the new wifi and should insert the password, you can insert the SSID address and password of wifi to access and below is code for it

import os
os.system("netsh wlan show networks interface=Wi-Fi")
Selected_SSID = input('insert the SSID you want to access :')
Selected_PW = input('insert the password od SSID you want to access :')
config =
'''<?xml version=\"1.0\?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>'''+Selected_SSID+'''</name>
    <SSIDConfig>
        <SSID>
            <name>'''+Selected_SSID+'''</name>
        </SSID>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>auto</connectionMode>
    <MSM>
        <securtiy>
            <authEncryption>
                <authentication>WPA2PSK</authentication>
                <encryption>AES</encryption>
                <useOneX>false</useOneX>
            </authEncryption>
            <sharedKey>
                <keyType>passPhrase</keyType>
                <protected>false</protected>
                <keyMaterial>'''+Selected_PW+'''</keyMaterial>
            </sharedKey>
        </securtiy>
    </MSM>
</WLANProfile>'''

with oepn(Selected_SSID+".xml", 'w') as file:
    file.write(config)
    os.system('netsh wlan add profile filename=\''+Selected_SSID+'.xml\''+'interface=Wi-Fi')
try:
    os.system('netsh wlan connect name=\''+Selected_SSID+'\' ssid=\''+Selected_SSID+'\' interface=Wi-Fi')
except:
    print("Error")



'''
 annotation : In the above code, to connect the wireless internet profile,
utilize the methode which insert the XML access profile information and transmit the XML.
The way of accessing the XML is originated from google searching and insert the SSID and password
into that XML, then through the 'netsh' sheel, the connection is accomplished.
'''
