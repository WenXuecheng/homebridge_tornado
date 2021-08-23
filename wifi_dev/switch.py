import requests

dev_name_and_ip={
    "esp-switch-wifi-dev-toplight":'',
}
name_to_dev_name = {
    "顶灯":"esp-switch-wifi-dev-toplight",
}



def option_dev_swtich(name,op,va,ip):
    global dev_name_and_ip
    global name_to_dev_name
    try:
        name = name_to_dev_name[name]
    except:
        name=name
    if name == "esp-switch-wifi-dev-toplight":
        if op == 'init':
            if ip != dev_name_and_ip["esp-switch-wifi-dev-toplight"]:
                dev_name_and_ip["esp-switch-wifi-dev-toplight"] = ip
                return ''
            return ''
        if op == 'open':
            url = 'http://' + dev_name_and_ip[name] + '/' + op
            try:
                res = requests.get(url,timeout=0.1)
                res_switch = {
                    "name_switch": name,
                    "option_switch": op,
                    "status_switch": bool(1-int(res.text.split(':')[1])),
                }
            except:
                res_switch = {
                    "name_switch": name,
                    "option_switch": op,
                    "status_switch": '',
                }
            return res_switch

        if op == 'close':
            url = 'http://' + dev_name_and_ip[name] + '/' + op
            try:
                res = requests.get(url,timeout=0.1)
                res_switch = {
                    "name_switch": name,
                    "option_switch": op,
                    "status_switch": bool(1-int(res.text.split(':')[1])),
                }
            except:
                res_switch = {
                    "name_switch": name,
                    "option_switch": op,
                    "status_switch": '',
                }
            return res_switch
        if op == 'get_status':
            url = 'http://' + dev_name_and_ip[name] + '/' + op
            try:
                res = requests.get(url,timeout=0.1)
                res_switch = {
                    "name_switch": name,
                    "option_switch": op,
                    "status_switch": bool(1-int(res.text.split(':')[1])),
                }
            except:
                res_switch = {
                    "name_switch": name,
                    "option_switch": op,
                    "status_switch": False,
                }
            return res_switch




