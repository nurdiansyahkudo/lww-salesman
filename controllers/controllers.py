# -*- coding: utf-8 -*-
# from odoo import http


# class LwwSalesman(http.Controller):
#     @http.route('/lww_salesman/lww_salesman', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/lww_salesman/lww_salesman/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('lww_salesman.listing', {
#             'root': '/lww_salesman/lww_salesman',
#             'objects': http.request.env['lww_salesman.lww_salesman'].search([]),
#         })

#     @http.route('/lww_salesman/lww_salesman/objects/<model("lww_salesman.lww_salesman"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('lww_salesman.object', {
#             'object': obj
#         })

