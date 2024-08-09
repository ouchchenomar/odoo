odoo.define('crnd_wsd.tour_request_author_no_phone', function (require) {
    'use strict';

    var tour = require('web_tour.tour');

    tour.register('crnd_wsd_tour_request_author_no_phone', {
        test: true,
        url: '/web/session/logout?redirect=/requests/new',
    }, [
        {
            content: "Check that we in request creation process on step 'type'",
            trigger: ".wsd_request_new form#request_category",
        },
        {
            content: "Select request category SaAS / Support",
            trigger: "h4:has(label:containsExact('SaAS / Support'))" +
                ":contains() input[name='category_id']",
            run: 'click',
        },
        {
            content: "Check that we in request creation process on step 'type'",
            trigger: ".wsd_request_new form#request_type",
        },
        {
            content: "Check category selected",
            trigger: "#request-selection-box #request-category" +
                " span:containsExact('SaAS / Support')",
        },
        {
            content: "Select request type Generic Question",
            trigger: "h4:has(label:containsExact('Generic Question'))" +
                ":contains() input[name='type_id']",
            run: 'click',
        },
        {
            content: "Check category selected",
            trigger: "#request-selection-box #request-category" +
                " span:containsExact('SaAS / Support')",
        },
        {
            content: "Check type selected",
            trigger: "#request-selection-box #request-type" +
                " span:containsExact('Generic Question')",
        },
        {
            content: "Write some request text",
            trigger: "#request_text",
            run: function () {
                $("#request_text").trumbowyg(
                    'html', "<p>My request without my phone</p>");
            },
        },
        {
            content: "Enter e-mail address",
            trigger: "input[name='request_author_email']",
            run: 'text Test_author@email.com',
        },
        {
            content: "Click 'Create' button",
            trigger: "button[type='submit']",
        },
        {
            content: "Wait for congratulation page loaded",
            trigger: "#wrap:has(h3:contains(" +
                "'Your request has been submitted')):contains()",
        },
        {
            content: "Click on request name ot open it",
            trigger: ".wsd_request a.request-name",
        },
        {
            content: "Wait for request page loaded",
            trigger: "#wrap:has(h3:contains('Req-')):contains()",
        },
    ]);
    return {};
});