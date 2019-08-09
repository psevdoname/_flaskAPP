from flask import Flask, Response
import time as t

app=Flask(__name__)

def what_time():
    t.sleep( 1 )
    s = t.ctime(t.time())
    return  s
@app.route('/time')
def time():
    def eventStream():
        while True:
            yield what_time() + '\n'
    return Response(eventStream(), mimetype='text/event-stream')

def bootapp():
    
    app.run(port=8080, debug=True)

if __name__=='__main__':
    bootapp()

