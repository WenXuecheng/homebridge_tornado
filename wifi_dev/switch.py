import requests
import config
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
            with open(config.settings["wifi_dev_path"]+'/devs/esp-switch-wifi-dev-toplight','w+') as fd:
                fd.write(ip)
            return None;
        if op == 'open':
            with open(config.settings["wifi_dev_path"]+'/devs/esp-switch-wifi-dev-toplight','r') as fd:
                url = 'http://' + fd.read() + '/' + op
                res = requests.get(url)
                res_switch = {
                    "name_switch": name,
                    "option_switch": op,
                    "status_switch": res.split(':')[1],
                }
                return res_switch
        if op == 'close':
            with open(config.settings["wifi_dev_path"]+'/devs/esp-switch-wifi-dev-toplight','r') as fd:
                url = 'http://' + fd.read() + '/' + op
                res = requests.get(url)
                res_switch = {
                    "name_switch": name,
                    "option_switch": op,
                    "status_switch": res.split(':')[1],
                }
                return res_switch
        if op == 'get_status':
            with open(config.settings["wifi_dev_path"]+'/devs/esp-switch-wifi-dev-toplight','r') as fd:
                url = 'http://' + fd.read() + '/' + op
                res = requests.get(url)
                res_switch = {
                    "name_switch": name,
                    "option_switch": op,
                    "status_switch": res.split(':')[1],
                }
                return res_switch



