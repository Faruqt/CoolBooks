from . import cb

@cb.route('/')
def hello_world():
    return 'Catlogue world?'
