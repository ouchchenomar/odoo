/* eslint-disable no-use-before-define */
odoo.define('crnd_wsd.tour_request_new_priority_complex_selection', function (require) {
    'use strict';

    var tour = require('web_tour.tour');

    tour.register('crnd_wsd_tour_request_new_complex_selection', {
        test: true,
        url: '/requests/new',
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
            content: "Select request impact priority",
            trigger: "select[name='request_impact_priority']",
            run: function () {
                $("#request_impact_priority").val('1');
            },
        },
        {
            content: "Select request urgency priority",
            trigger: "select[name='request_urgency_priority']",
            run: function () {
                $("#request_urgency_priority").val('3');
            },
        },
        {
            content: "Write request text",
            trigger: "#request_text",
            run: function () {
                $("#request_text").trumbowyg(
                    'html', "My request test tour");
            },
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
    ]);
    return {};
});
