import wmi

ip = 'ip'
username = "username"
password = "Password"
SW_SHOWNORMAL = 1
print("Establishing connection to %s" % ip)
c = wmi.WMI(ip, user=username, password=password)
process_startup = c.Win32_ProcessStartup.new()
process_startup.ShowWindow = SW_SHOWNORMAL
process_id, result = c.Win32_Process.Create(CommandLine="gpresult /r", ProcessStartupInformation=process_startup)
if result == 0:
    print("Process started successfully: %d" % process_id)
else:
    raise RuntimeError("Problem creating process: %d" % result)

for share in c.Win32_Share():
    print(share.Name, share.Path)
