$(document).ready(function () {
    $("#subscription-list").DataTable({
        scrollCollapse: true,
        info: false,
        columnDefs: [{
            orderable: false,
            targets: -1
        }],
        sorting: false,
        oLanguage: {
            sSearch: `_INPUT_ <i class="bi bi-search"></i>`,
            sSearchPlaceholder: "Search...",
        },
        "paging": false,
    });

});