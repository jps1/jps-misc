import json, os, threading
from smallReproInterop import *
import jnius

failures = []
partial_workaround = False

class ThingCreator(threading.Thread):
    def __init__(self, x, js_json):
        threading.Thread.__init__( self )
        self.name = 'thing #' + str(x)
        self.js_json = js_json
        
    def run(self):
        global partial_workaround
        
        t = Thing(self.name)
        
        print('(py) adding ' + self.name + ' js to ' + t.getName())
        if partial_workaround:
            blah = json.dumps( self.js_json, sort_keys=True, indent=4)
            t.AddJsonString(self.name + ' js', blah)
        else:
            t.AddJsonString(self.name + ' js', json.dumps( self.js_json, sort_keys=True, indent=4) )
        
        nit = t.GetNumOfJsonStrings()
        if nit != 1 :
            global failures
            failures.append(self.name)
       
        jnius.detach()
        
def mymain():

    all_threads = []

    js_json = json.loads( open( os.path.join(os.pardir, 'sample.json')).read() )

    thread_count = 3

    for x in range(1, thread_count+1):
        thread = ThingCreator(x, js_json)
        all_threads.append(thread)
        thread.start()
 
    for thr in all_threads:
        thr.join()
    
    global failures
    if len(failures) is not 0:
        print('-----------------------------------------------------------------')
        print('# of JsonStrings is not right for: ' + str(failures))
        print('-----------------------------------------------------------------')


if __name__ == '__main__':
    mymain()
        