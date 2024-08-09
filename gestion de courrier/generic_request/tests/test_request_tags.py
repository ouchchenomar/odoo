from ast import literal_eval

from odoo.tests.common import Form
from .common import RequestCase


class TestRequestTags(RequestCase):
    """Test request tags
    """
    def setUp(self):
        super(TestRequestTags, self).setUp()

        # Request service
        self.default_service = self.env.ref(
            'generic_service.generic_service_default')

        # Request category
        self.tech_categ = self.env.ref(
            'generic_request.request_category_demo_technical_configuration')
        # Tag categories
        self.tag_categ_severity = self.env.ref(
            'generic_request.tag_category_severity')
        self.tag_categ_priority = self.env.ref(
            'generic_request.tag_category_priority')
        self.tag_categ_platform = self.env.ref(
            'generic_request.tag_category_platform')

    def test_request_tags(self):
        # Enable services
        self.env.ref('base.group_user').write(
            {'implied_ids': [(4, self.env.ref(
                'generic_request.group_request_use_services').id)]})

        # PREPARE INIT TEST DATA
        # Add tag categories to the service
        self.default_service.write({
            'tag_category_ids': [(6, 0, self.tag_categ_severity.ids)]
        })

        # Add tag categories to the category
        self.tech_categ.write({
            'tag_category_ids': [(6, 0, self.tag_categ_platform.ids)]
        })

        # Add tag categories to the type
        self.access_type.write({
            'tag_category_ids': [(6, 0, self.tag_categ_priority.ids), ]
        })

        # Check request tags domain
        with Form(self.env['request.request']) as request_form:

            # Check default domain
            self.assertListEqual(
                literal_eval(request_form.tag_ids_domain),
                ['&', ('model_id.model', '=', 'request.request'),
                 ('category_id', '=', False),
                 ])

            # Check tags domain with service
            request_form.service_id = self.default_service
            service_tag_categs = self.default_service.tag_category_ids
            self.assertListEqual(
                literal_eval(request_form.tag_ids_domain),
                ['&', ('model_id.model', '=', 'request.request'),
                 ('category_id', 'in', service_tag_categs.ids),
                 ])

            # Check tags domain with category
            request_form.category_id = self.tech_categ
            expected_tags_categ_ids = self.env['generic.tag.category'].browse()
            expected_tags_categ_ids += self.default_service.tag_category_ids
            expected_tags_categ_ids += self.tech_categ.tag_category_ids
            self.assertListEqual(
                literal_eval(request_form.tag_ids_domain),
                ['&',
                 ('model_id.model', '=', 'request.request'),
                 ('category_id', 'in', expected_tags_categ_ids.ids),
                 ])

            # Check tags domain with type
            request_form.type_id = self.access_type
            expected_tags_categ_ids = self.env['generic.tag.category'].browse()
            expected_tags_categ_ids += self.default_service.tag_category_ids
            expected_tags_categ_ids += self.tech_categ.tag_category_ids
            expected_tags_categ_ids += self.access_type.tag_category_ids
            self.assertListEqual(
                literal_eval(request_form.tag_ids_domain),
                ['&',
                 ('model_id.model', '=', 'request.request'),
                 ('category_id', 'in', expected_tags_categ_ids.ids),
                 ])
            request_form.save()
