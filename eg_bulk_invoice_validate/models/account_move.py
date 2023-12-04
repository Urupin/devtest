from odoo import models
from odoo.exceptions import UserError


class AccountMove(models.Model):
    _inherit = 'account.move'

    def invoice_bulk_validate(self):
        for record in self:
            if record.state in ['draft']:
                record.action_post()
            else:
                raise UserError('You can invoice bulk validate only draft invoice :{}'.format(record.name))


