import bottle


@bottle.route('/hello')
def index():
    return {'status': True}


bottle.run(host='127.0.0.1', port=12580)
