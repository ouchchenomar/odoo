from odoo import models, fields, tools


class RequestTimesheetReport(models.Model):
    _name = "request.timesheet.report"
    _description = "Request Timesheet Report"
    _auto = False
    _order = 'date DESC, id DESC'

    date = fields.Date(readonly=True)

    user_id = fields.Many2one('res.users', readonly=True)
    activity_id = fields.Many2one('request.timesheet.activity', readonly=True)
    amount = fields.Float(readonly=True)

    request_id = fields.Many2one(
        'request.request', readonly=True)
    request_type_id = fields.Many2one(
        'request.type', readonly=True)
    request_category_id = fields.Many2one(
        'request.category', readonly=True)
    request_kind_id = fields.Many2one(
        'request.type', readonly=True)
    request_author_id = fields.Many2one(
        'res.partner', readonly=True)
    request_partner_id = fields.Many2one(
        'res.partner', readonly=True)
    request_stage_type_id = fields.Many2one(
        'request.stage.type', readonly=True)
    request_stage_id = fields.Many2one(
        'request.stage', readonly=True)
    request_channel_id = fields.Many2one(
        'request.channel', readonly=True)
    request_closed = fields.Boolean(readonly=True)
    request_service_id = fields.Many2one(
        'generic.service', readonly=True)

    def _get_request_fields(self):
        """ Get list of fields to read from request.
            Return: [(request_field, select_as_field)]
        """
        return [
            ('id', 'request_id'),
            ('type_id', 'request_type_id'),
            ('category_id', 'request_category_id'),
            ('kind_id', 'request_kind_id'),
            ('author_id', 'request_author_id'),
            ('partner_id', 'request_partner_id'),
            ('stage_type_id', 'request_stage_type_id'),
            ('stage_id', 'request_stage_id'),
            ('closed', 'request_closed'),
            ('channel_id', 'request_channel_id'),
            ('service_id', 'request_service_id'),
        ]

    def init(self):
        # pylint: disable=sql-injection
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute(
            """
                CREATE or REPLACE VIEW %(view_name)s as (
                SELECT
                    rtr.id,
                    rtr.date,
                    rtr.date_start,
                    rtr.date_end,
                    rtr.user_id,
                    rtr.activity_id,
                    rtr.amount,
                    %(request_fields)s
                FROM request_timesheet_line AS rtr
                LEFT JOIN request_request AS rr ON rr.id = rtr.request_id
            )""" % {
                'view_name': self._table,
                'request_fields': ", ".join((
                    "rr.%s AS %s" % r for r in self._get_request_fields()
                )),
            })  # nosec

    def action_view_related_request(self):
        if self.request_id:
            return self.request_id.get_formview_action()
        return False
