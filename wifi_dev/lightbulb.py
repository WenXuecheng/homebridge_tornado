import requests

dev_name_and_ip={
    "esp-lightbulb-wifi-dev-table-lamp":'',
}
name_to_dev_name = {
    "台灯":"esp-lightbulb-wifi-dev-table-lamp",
}



def option_dev_lightbulb(name,op,va,ip):
    global dev_name_and_ip
    global name_to_dev_name
    try:
        name = name_to_dev_name[name]
    except:
        name=name
    if name == "esp-lightbulb-wifi-dev-table-lamp":
        if op == 'init':
            if ip != dev_name_and_ip["esp-lightbulb-wifi-dev-table-lamp"]:
                dev_name_and_ip["esp-lightbulb-wifi-dev-table-lamp"] = ip
                return {"ip_status":"changed"}
            return {"ip_status":"unchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchangedchanged"}
        if op == 'set_brightness':
            res_lightbulb = {
                "name_lightbulb": name,
                "option_lightbulb": op,
                "status_lightbulb": '',
                "brightness_lightbulb": va,
            }
            return res_lightbulb
        if op == 'open':
            url = 'http://' + dev_name_and_ip[name] + ':6236/' + op + '/none'
            try:
                res = requests.get(url)
                res_lightbulb = {
                    "name_lightbulb": name,
                    "option_lightbulb": op,
                    "status_lightbulb": bool(1-int(res.text.split(':')[1])),
                    "brightness_lightbulb": 100,
                }
            except:
                res_lightbulb = {
                    "name_lightbulb": name,
                    "option_lightbulb": op,
                    "status_lightbulb": True,
                    "brightness_lightbulb": 100,
                }
            return res_lightbulb

        if op == 'close':
            url = 'http://' + dev_name_and_ip[name] + ':6236/' + op + '/none'
            try:
                res = requests.get(url)
                res_lightbulb = {
                    "name_lightbulb": name,
                    "option_lightbulb": op,
                    "status_lightbulb": bool(1 - int(res.text.split(':')[1])),
                    "brightness_lightbulb": 0,
                }
            except:
                res_lightbulb = {
                    "name_lightbulb": name,
                    "option_lightbulb": op,
                    "status_lightbulb": False,
                    "brightness_lightbulb": 0,
                }
            return res_lightbulb
        if op == 'get_status':
            url = 'http://' + dev_name_and_ip[name] + ':6236/' + op +'/none'
            try:
                res = requests.get(url)
                res_lightbulb = {
                    "name_lightbulb": name,
                    "option_lightbulb": op,
                    "status_lightbulb": bool(1-int(res.text.split(':')[1])),
                    "brightness_lightbulb": '',
                }
            except:
                res_lightbulb = {
                    "name_lightbulb": name,
                    "option_lightbulb": op,
                    "status_lightbulb": False,
                    "brightness_lightbulb": '',
                }
            return res_lightbulb

        if op == 'get_brightness':
            url = 'http://' + dev_name_and_ip[name] + ':6236/' + op +'/none'
            try:
                res = requests.get(url)
                res_lightbulb = {
                    "name_lightbulb": name,
                    "option_lightbulb": op,
                    "status_lightbulb": bool(1-int(res.text.split(':')[1])),
                    "brightness_lightbulb": '',
                }
            except:
                res_lightbulb = {
                    "name_lightbulb": name,
                    "option_lightbulb": op,
                    "status_lightbulb": False,
                    "brightness_lightbulb": '',
                }
            return res_lightbulb




