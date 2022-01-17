odoo.define('helpdesk_ticket_teamtyoe.js', function (require) {
    "use strict";

    require('web.dom_ready');
    var ajax = require('web.ajax');

    $(document).ready(function(){
        $("select[name='team_id']").trigger('change');
    });

    $("#type_id").hide();

    $("select[name='team_id']").on("change", function (){
        var team = this;
        var teamsel = team.options[team.selectedIndex];

        var typeids = teamsel.getAttribute('type_ids');
        if (typeids == null)
            typeids = '';

        typeids = typeids.replace('helpdesk.ticket.type', '');
        typeids = typeids.replace('(', '');
        typeids = typeids.replace(')', '');
        typeids = ' ' + typeids + ',';

        var type = document.getElementById("type_id");

        Array.from(type.getElementsByTagName('option')).forEach(function(element){
            element.hidden = (typeids.indexOf(' ' + element.value + ',') == -1);
        });

        type.selectedIndex = -1;
        $("#type_id").show();
    });
});
