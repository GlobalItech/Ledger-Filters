
from odoo import models, fields, api
import time

class general_ledger_filter_custom(models.TransientModel):
#     _name = "general.ledger.filter.custom"
    _inherit = "account.report.general.ledger"
    _description = "This filter is on accounts basis."
    
    account_ids=fields.Many2many('account.account',string="Accounts")
    
    def _print_report(self,data):
        data = self.pre_print_report(data)
        if self.account_ids:
            data['form'].update({'account_ids': self.account_ids.ids,})
        return super(general_ledger_filter_custom, self)._print_report(data)

class ReportGeneralLedger(models.AbstractModel):
    _inherit = 'report.account.report_generalledger'
    
    @api.model
    def render_html(self, docids, data=None):
        self.model = self.env.context.get('active_model')
        docs = self.env[self.model].browse(self.env.context.get('active_ids', []))

        init_balance = data['form'].get('initial_balance', True)
        sortby = data['form'].get('sortby', 'sort_date')
        display_account = data['form']['display_account']
        codes = []
        if data['form'].get('journal_ids', False):
            codes = [journal.code for journal in self.env['account.journal'].search([('id', 'in', data['form']['journal_ids'])])]

        obj_account = self.env['account.account']
        get_accounts = data['form']['account_ids'] if data['form'].has_key('account_ids') else 0
        if get_accounts:
            accounts = obj_account.browse(get_accounts)
        else:
            accounts =self.env['account.account'].search([]) 
            accounts = docs if self.model == 'account.account' else self.env['account.account'].search([])
        accounts_res = self.with_context(data['form'].get('used_context',{}))._get_account_move_entry(accounts, init_balance, sortby, display_account)
        docargs = {
            'doc_ids': docids,
            'doc_model': self.model,
            'data': data['form'],
            'docs': docs,
            'time': time,
            'Accounts': accounts_res,
            'print_journal': codes,
        }
        return self.env['report'].render('account.report_generalledger', docargs)