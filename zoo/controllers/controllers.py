import time

from odoo import http


class Zoo(http.Controller):
    @http.route('/zoo/zoo', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/zoo/get_animal_status', auth='public', type='json', methods=['POST'])
    def get_animal_status(self, name, **kw):
        return http.request.env['zoo.animal'].search_read([('name', '=', name)], ['status'], limit=1)[0]['status']

    @http.route('/zoo/he_bit_me', auth='public')
    def he_bit_me(self, **kw):
        cr = http.request.env.cr
        cr.execute("update zoo_animal set name = 'bastard biter' where id = 1")
        # let's reflect some time on this new name ...
        time.sleep(1000)
        return "ok"
