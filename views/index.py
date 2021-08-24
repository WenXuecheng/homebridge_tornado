import tornado.web
from tornado.web import RequestHandler
from tornado.websocket import WebSocketHandler
import urllib.parse as up
from wifi_dev import switch
from wifi_dev import lightbulb
import config
class StaticFileHandler(tornado.web.StaticFileHandler):
    def __init__(self, *args, **kwargs):
        super(StaticFileHandler, self).__init__(*args, **kwargs)
        self.xsrf_token

class HomeHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('home.html')

class ChatHandler(WebSocketHandler):
    users = []
    def open(self):
        self.users.append(self)
        for user in self.users:
            user.write_message(u"[%s]登陆了"%(self.request.remote_ip))

    def on_message(self, message):
        for user in self.users:
            user.write_message(u"[%s]说:%s"%(self.request.remote_ip, message))

    def on_close(self):
        self.users.remove(self)
        for user in self.users:
            user.write_message(u"[%s]退出了"%(self.request.remote_ip))

    def check_origin(self, origin):
        return True

class SwitchHandler(RequestHandler):
    def get(self, name, option, value,*args, **kwargs):
        name = up.unquote(name)
        option = up.unquote(option)
        value = up.unquote(value)
        res = switch.option_dev_swtich(name,option,value,str(self.request.remote_ip))
        self.finish(res)

class LightbulbHandler(RequestHandler):
    def get(self, name, option, value,*args, **kwargs):
        name = up.unquote(name)
        option = up.unquote(option)
        value = up.unquote(value)
        res = lightbulb.option_dev_lightbulb(name, option, value, str(self.request.remote_ip))
        self.finish(res)

class Fanv2Handler(RequestHandler):
    def get(self, name, option, value,*args, **kwargs):
        name = up.unquote(name)
        option = up.unquote(option)
        value = up.unquote(value)
        if name == '风扇':
            if value != 'none':
                if option == 'set_RotationSpeed':
                    res = {
                        "name_fanv2": name,
                        "option_fanv2": option,
                        "RotationSpeed":value,
                        "status_fanv2": '',
                        'SwingMode':'',

                    }
                    self.write(res)
            else:
                if option == 'get_RotationSpeed':
                    res = {
                        "name_fanv2": name,
                        "option_fanv2": option,
                        "RotationSpeed":50,
                        "status_fanv2": '',
                        'SwingMode':'',
                    }
                    self.write(res)
                if option == 'get_status':
                    res = {
                        "name_fanv2": name,
                        "option_fanv2": option,
                        "RotationSpeed":'',
                        "status_fanv2": True,
                        'SwingMode':'',
                    }
                    self.write(res)
                if option == 'open':
                    res = {
                        "name_fanv2": name,
                        "option_fanv2": option,
                        "RotationSpeed":'',
                        "status_fanv2": '',
                        'SwingMode':'',
                    }
                    self.write(res)
                if option == 'close':
                    res = {
                        "name_fanv2": name,
                        "option_fanv2": option,
                        "RotationSpeed":'',
                        "status_fanv2": '',
                        'SwingMode':'',
                    }
                    self.write(res)

                if option == 'get_SwingMode':
                    res = {
                        "name_fanv2": name,
                        "option_fanv2": option,
                        "RotationSpeed":'',
                        "status_fanv2": '',
                        'SwingMode':1,
                    }
                    self.write(res)

                if option == 'SwingMode':
                    res = {
                        "name_fanv2": name,
                        "option_fanv2": option,
                        "RotationSpeed":'',
                        "status_fanv2": '',
                        'SwingMode':'',
                    }
                    self.write(res)

                if option == 'NoSwingMode':
                    res = {
                        "name_fanv2": name,
                        "option_fanv2": option,
                        "RotationSpeed":'',
                        "status_fanv2": '',
                        'SwingMode':'',
                    }
                    self.write(res)

        elif name == 'room1_swtich_light':
            self.write(name + ',' + option)
        else:
            pass

class WindowCoveringHandler(RequestHandler):
    def get(self, name, option, value,*args, **kwargs):
        name = up.unquote(name)
        option = up.unquote(option)
        value = up.unquote(value)
        if name == '窗帘':
            if value != 'none':
                if option == 'set_TargetPosition':
                    res = {
                        "name_lightbulb": name,
                        "option_lightbulb": option,
                        "TargetPosition":value,
                        "CurrentPosition": '',
                        "PositionState": '',
                    }
                    self.write(res)
            else:
                if option == 'get_CurrentPosition':
                    res = {
                        "name_windowcovering": name,
                        "option_windowcovering": option,
                        "TargetPosition":'',
                        "CurrentPosition": 50,
                        "PositionState": '',
                    }
                    self.write(res)
                if option == 'get_PositionState':
                    res = {
                        "name_windowcovering": name,
                        "option_windowcovering": option,
                        "TargetPosition":'',
                        "CurrentPosition": '',
                        "PositionState": 2,
                    }
                    self.write(res)

                if option == 'get_TargetPosition':
                    res = {
                        "name_windowcovering": name,
                        "option_windowcovering": option,
                        "TargetPosition":50,
                        "CurrentPosition": '',
                        "PositionState": '',
                    }
                    self.write(res)


        elif name == 'room1_swtich_light':
            self.write(name + ',' + option)
        else:
            pass

class TestHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render(config.settings['views_path']+'/test.html')