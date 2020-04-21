jQuery(document).ready(function($) {
    'use strict';

    if ($("table.second").length) {

        $(document).ready(function() {
            var table = $('table.second').DataTable({
                "order": [[ 0, "xyz" ]],
                "pageLength": 15,
                lengthChange: false,
                buttons: ['copy', 'excel', 'pdf', 'print', ]
            });

            table.buttons().container()
                .appendTo('#example_wrapper .col-md-6:eq(0)');
        });
    }




});