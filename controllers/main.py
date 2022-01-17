import logging
import werkzeug
import odoo.http as http
import base64
from odoo.addons.helpdesk_mgmt.controllers.main import HelpdeskTicketController
from openerp.http import request

_logger = logging.getLogger(__name__)

class HelpdeskTicketControllerInherited(HelpdeskTicketController):

    @http.route()
    def create_new_ticket(self, **kw):
        team = http.request.env['helpdesk.ticket.team'].search([('active', '=', True)])
        type = http.request.env['helpdesk.ticket.type'].search([])
        email = http.request.env.user.email
        name = http.request.env.user.name
        return http.request.render('helpdesk_mgmt.portal_create_ticket', {
            'team': team, 'type': type, 'type_data_x': type, 'email': email, 'name': name})

    @http.route()
    def submit_ticket(self, **kw):
        vals = {
            'partner_name': kw.get('name'),
            'company_id': http.request.env.user.company_id.id,
            'type_id': kw.get('type_id'),
            'team_id': kw.get('team_id'),
            'partner_email': kw.get('email'),
            'description': kw.get('description'),
            'name': kw.get('subject'),
            'attachment_ids': False,
            'channel_id':
                request.env['helpdesk.ticket.channel'].
                sudo().search([('name', '=', 'PORTAL')]).id,
            'partner_id': request.env.user.partner_id.id,
        }
        new_ticket = request.env['helpdesk.ticket'].sudo().create(
            vals)
        new_ticket.message_subscribe(
            partner_ids=request.env.user.partner_id.ids)
        if kw.get('attachment'):
            for c_file in request.httprequest.files.getlist('attachment'):
                data = c_file.read()
                if c_file.filename:
                    request.env['ir.attachment'].sudo().create({
                        'name': c_file.filename,
                        'datas': base64.b64encode(data),
                        'datas_fname': c_file.filename,
                        'res_model': 'helpdesk.ticket',
                        'res_id': new_ticket.id
                    })
        return werkzeug.utils.redirect("/my/tickets")
