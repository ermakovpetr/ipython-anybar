from anybar import AnyBar
from IPython.core.magic import register_line_magic


class LineWatcher(object):

    def __init__(self):
        self.start_flag = False
        self.anybar = None

    def connect(self, host='localhost', port='1738'):
        if self.anybar:
            self.anybar.change('green')
        self.anybar = AnyBar(port=int(port), address=host)
        print('Connect to {host}:{port}'.format(host=host, port=int(port)))

    def start(self):
        self.start_flag = True
        if self.anybar:
            self.anybar.change('red')

    def stop(self):
        if self.start_flag:
            self.start_flag = False
            if self.anybar:
                self.anybar.change('green')


antbar_watcher = None


def load_ipython_extension(ip):
    global antbar_watcher
    antbar_watcher = LineWatcher()
    ip.events.register('pre_run_cell', antbar_watcher.start)
    ip.events.register('post_run_cell', antbar_watcher.stop)


def unload_ipython_extension(ip):
    ip.events.unregister('pre_run_cell', antbar_watcher.start)
    ip.events.unregister('post_run_cell', antbar_watcher.stop)
    if antbar_watcher:
        del antbar_watcher


@register_line_magic
def ipython_anybar_connect(line):
    parametrs = line.strip().split()
    if len(parametrs) == 2:
        antbar_watcher.connect(*parametrs)
    elif len(parametrs) == 1:
        antbar_watcher.connect(port=parametrs[0])
    else:
        antbar_watcher.connect()
