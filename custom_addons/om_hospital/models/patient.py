from odoo import fields, api, models

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Patient Master"

    name = fields.Char(string="name", required=True)
    date = fields.Date(string="DOB")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")