from . import ub

@ub.route('/')
def hello_world():
    return 'Hello World! How are you doing?'
