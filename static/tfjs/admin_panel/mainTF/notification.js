$(document).ready(function () {
    // console.log('data-table');
    $("#notification-table").DataTable({
        scrollY: "210px",
        scrollCollapse: true,
        paging: false,
        searching: false,
        info: false,
        "initComplete": function(settings, json) {
            $('body').find('.dataTables_scrollBody').addClass("scrollbar");
        },
    });
});


const deleteRowBtn = document.querySelectorAll(".dlt")

deleteRowBtn.forEach(btn=>{
    btn.addEventListener("click", ()=>{
        btn.parentElement.parentElement.classList.add("d-none")
    })
})