$(document).ready(function () {
    $("#blogList").DataTable({
        scrollX: true,
        scrollCollapse: true,
        paging: false,
        searching: true,
        info: false,
        sorting: false,
        oLanguage: {
            sSearch: `_INPUT_ <i class="bi bi-search"></i>`,
            sSearchPlaceholder: "Search...",
        },
    });

});
