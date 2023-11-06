# -*- coding: utf-8 -*-
# from odoo import http


# class Zoo(http.Controller):
#     @http.route('/zoo/zoo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/zoo/zoo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('zoo.listing', {
#             'root': '/zoo/zoo',
#             'objects': http.request.env['zoo.zoo'].search([]),
#         })

#     @http.route('/zoo/zoo/objects/<model("zoo.zoo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('zoo.object', {
#             'object': obj
#         })
