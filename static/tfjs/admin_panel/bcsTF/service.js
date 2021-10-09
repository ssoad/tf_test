$(document).ready(function () {
    $("#sub-service-list").DataTable({
        scrollY: "410px",
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
        "initComplete": function (settings, json) {
            $('body').find('.dataTables_scrollBody').addClass("scrollbar");
        },
        "paging": false,
    });
    $("#reading-list").DataTable({
        scrollX: true,
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
})


const addServiceBtn = document.querySelector(".addService")
const addServiceFormCloses = document.querySelectorAll(".form-close")
const backToList = document.querySelector(".form-close-back")
const addServiceForm = document.querySelector(".add-form")
const tableContainer = document.querySelector(".table-container")
const formFirstPart = document.querySelectorAll("#div_id_category,#div_id_service_icon,#div_id_service_title,#div_id_short_description, #div_id_has_sub_service, #div_id_is_subscription_based")
const formSecondPart = document.querySelectorAll("#div_id_service_header, #div_id_service_body, #div_id_service_footer, .saveSubservice")
const serviceHeader = document.querySelector("#div_id_service_header")


addServiceBtn.addEventListener("click", () => {
    tableContainer.classList.add("d-none")
    addServiceForm.classList.remove("d-none")
    backToList.classList.remove("d-none")
    formSecondPart.forEach(item=>{
        item.classList.add("d-none")
    })
    const nextBtn = document.createElement("button")
    nextBtn.classList.add('btn', 'btn-primary', 'nextBtn', 'text-capitalize')
    nextBtn.textContent = "Next"
    serviceHeader.insertAdjacentElement("beforebegin", nextBtn)
    nextBtn.addEventListener("click",(e)=>{
        e.preventDefault()
        formSecondPart.forEach(item=>{
            item.classList.remove("d-none")
        })
        formFirstPart.forEach(item=>{
            item.classList.add("d-none")
        })
        nextBtn.classList.add("d-none")
    })
})

// console.log(nextForm)
// nextBtn("click", ()=>{

// })

addServiceFormCloses.forEach(addServiceFormClose => {
    addServiceFormClose.addEventListener("click", () => {
        addServiceForm.classList.add("d-none")
        backToList.classList.add("d-none")
        tableContainer.classList.remove("d-none")
    })
})


