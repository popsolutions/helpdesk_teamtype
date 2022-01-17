# Copyright 2021 Pop Solutions
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Helpdesk Team Types',
    'summary': """
        Helpdesk Team Types""",
    'version': '12.0.22.01',
    'license': 'AGPL-3',
    'author': 'Pop Solutions,Odoo Community Association (OCA)',
    'website': 'www.popsolutions.co',
    'depends': [
        'helpdesk_mgmt',
        'helpdesk_type'
    ],
    'data': [
        'views/helpdesk_ticket_templates_inherited.xml'
    ],
    'demo': [
    ],
    'development_status': 'Beta',
    'installable': True,
}
