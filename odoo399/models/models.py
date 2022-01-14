# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class odoo399(models.Model):
#     _name = 'odoo399.odoo399'
#     _description = 'odoo399.odoo399'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
from odoo import models, fields, api

class zapatilla399(models.Model):
	_name = 'odoo399.zapatilla399'
	_description = 'model zapatilla399'

	name = fields.Char('Id',required=True)
	modelo = fields.Char(string='Modelo',required=True)
	marca = fields.Char(string='Marca',required=True)

class sudaderas(models.Model):
	_name = 'odoo399.sudaderas'
	_description = 'model sudaderas'

	name = fields.Char('Id',required=True)
	talla = fields.Char(string='Talla',required=True)
	color = fields.Char(string='Color',required=True)

class abrigos(models.Model):
	_name = 'odoo399.abrigos'
	_description = 'model abrigos'

	name = fields.Char('Id',required=True)
	material = fields.Char(string='Material',required=True)
	marca = fields.Char(string='Marca',required=True)

