from . import mb

@mb.route('/')
def hello_world():
    return 'Market place'
