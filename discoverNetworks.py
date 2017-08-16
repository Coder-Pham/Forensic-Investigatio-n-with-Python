import subprocess

# results = subprocess.check_output(["netsh", "wlan", "show", "network"])
results = subprocess.check_output(["netsh", "wlan", "show", "all"])
#results = results.decode("ascii")      # needed in python 3
results = results.replace("\r","")
wireless = results.split("\n")

out_file = wireless[1]
out_file = out_file.replace(':','-')
out_file = out_file.replace('/',' ')
out_file = out_file + '.txt'
out_data = open(out_file, 'w')
# TIM INFO CAN THIET
for x in range(len(wireless)):
    if wireless[x] == '======================= SHOW NETWORKS MODE=BSSID ====================== ':
        break
wireless = wireless[x:]

for x in range(len(wireless)):
    out_data.write(wireless[x])
    out_data.write('\n')
out_data.close()

#STILL DEVELOPING ...