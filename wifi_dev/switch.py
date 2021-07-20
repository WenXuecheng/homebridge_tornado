import requests

dev_name_and_ip={
    "esp-switch-wifi-dev-toplight":'',
}
name_to_dev_name = {
    "顶灯":"esp-switch-wifi-dev-toplight",
}



def option_dev_swtich(name,op,va,ip):
    global dev_name_and_ip
    try:
        name = name_to_dev_name[name]
    except:
        name=name
    if name == "esp-switch-wifi-dev-toplight":
        if op == 'init':
            if ip == '':
                dev_name_and_ip["esp-switch-wifi-dev-toplight"] = 'sadfdsafsdf';
            dev_name_and_ip["esp-switch-wifi-dev-toplight"] = ip;
            return None;
        if op == 'open':
            url = 'http://' + dev_name_and_ip[name] + '/' + op
            res = requests.get(url)
            res_switch = {
                "name_switch": name,
                "option_switch": op,
                "status_switch": res.split(':')[1],
            }
            return res_switch
        if op == 'close':
            url = 'http://' + dev_name_and_ip[name] + '/' + op
            res = requests.get(url)
            res_switch = {
                "name_switch": name,
                "option_switch": op,
                "status_switch": res.split(':')[1],
            }
            return res_switch
        if op == 'get_status':
            url = 'http://' + dev_name_and_ip[name] + '/' + op
            res = requests.get(url)
            res_switch = {
                "name_switch": name,
                "option_switch": op,
                "status_switch": res.split(':')[1],
            }
            return res_switch




