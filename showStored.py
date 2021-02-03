import subprocess
import re

show_stored = True
show_surrounding = True
content = ""

if show_stored == True:
    command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()
    profile_names = (re.findall("All User Profile     : (.*)\r", command_output))

    wifis = []

    if len(profile_names) != 0:
        for name in profile_names:
            profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output = True).stdout.decode()
            wifi_name = name
            profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output = True).stdout.decode()
            password = re.search("Key Content            : (.*)\r", profile_info_pass)
            if password == None:
                wifi_pass = None
            else:
                wifi_pass = password[1]
            wifis.append([wifi_name, wifi_pass])

    accountnum = 1
    for wifi in wifis:
        content += f"===============ACCOUNT {accountnum}===============\n"
        content += f"ssid: {wifi[0]}\n"
        content += f"password: {wifi[1]}\n\n"
        accountnum += 1
        
print(content)
     
