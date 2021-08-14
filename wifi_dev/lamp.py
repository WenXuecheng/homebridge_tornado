import requests

dev_name_and_ip={
    "esp-lamp-wifi-dev-table-lamp":'',
}
name_to_dev_name = {
    "台灯":"esp-switch-wifi-dev-table-lamp",
}



def option_dev_swtich(name,op,va,ip):
    global dev_name_and_ip
    try:
        name = name_to_dev_name[name]
    except:
        name=name
    if name == "esp-switch-wifi-dev-table-lamp":
        if op == 'init':
            if ip != dev_name_and_ip["esp-switch-wifi-dev-table-lamp"]:
                dev_name_and_ip["esp-switch-wifi-dev-table-lamp"] = ip
                return 'ip changed'
            return 'init ok'
        if op == 'open':
            url = 'http://' + dev_name_and_ip[name] + '/' + op + '/none'
            try:
                res = requests.get(url)
                res_lamp = {
                    "name_lamp": name,
                    "option_lamp": op,
                    "status_lamp": bool(1-int(res.text.split(':')[1])),
                }
            except:
                res_lamp = {
                    "name_lamp": name,
                    "option_lamp": op,
                    "status_lamp": '',
                }
            return res_lamp

        if op == 'close':
            url = 'http://' + dev_name_and_ip[name] + '/' + op + '/none'
            try:
                res = requests.get(url)
                res_lamp = {
                    "name_lamp": name,
                    "option_lamp": op,
                    "status_lamp": bool(1-int(res.text.split(':')[1])),
                }
            except:
                res_lamp = {
                    "name_lamp": name,
                    "option_lamp": op,
                    "status_lamp": '',
                }
            return res_lamp
        if op == 'get_status':
            url = 'http://' + dev_name_and_ip[name] + '/' + op +'/none'
            try:
                res = requests.get(url)
                res_lamp = {
                    "name_lamp": name,
                    "option_lamp": op,
                    "status_lamp": bool(1-int(res.text.split(':')[1])),
                }
            except:
                res_lamp = {
                    "name_lamp": name,
                    "option_lamp": op,
                    "status_lamp": False,
                }
            return res_lamp




