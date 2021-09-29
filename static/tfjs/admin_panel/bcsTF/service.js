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


const forms = document.querySelectorAll('.needs-validation')
forms.forEach((form) => {
    form.addEventListener("submit", (event) => {
        event.preventDefault()
        if (!form.checkValidity()) {
            event.stopPropagation()
            console.log(form);
        }

        form.classList.add('was-validated')
        form.classList.add('d-none')
        form.nextElementSibling.classList.remove("d-none")

    })
}, false)



tinymce.init({
    selector: '.title-container',
    plugins: 'image code lists',
    menubar: false,
    statusbar: false,
    toolbar: 'undo redo | image code | bold italic alignleft aligncenter alignright alignjustify| bullist numlist outdent indent',

    /* without images_upload_url set, Upload tab won't show up*/
    images_upload_url: 'postAcceptor.php',

    /* we override default upload handler to simulate successful upload*/
    images_upload_handler: function (blobInfo, success, failure) {
        setTimeout(function () {
            /* no matter what you upload, we will turn it into TinyMCE logo :)*/
            success('http://moxiecode.cachefly.net/tinymce/v9/images/logo.png');
        }, 2000);
    },
    content_style: 'body { font-family:Helvetica,Arial,sans-serif; font-size:14px }'
});

const addServiceBtn = document.querySelector(".addService")
const addServiceFormCloses = document.querySelectorAll(".form-close")
const backToList = document.querySelector(".form-close-back")
const addServiceForm = document.querySelector(".add-form")
const tableContainer = document.querySelector(".table-container")

addServiceBtn.addEventListener("click", () => {
    tableContainer.classList.add("d-none")
    addServiceForm.classList.remove("d-none")
    backToList.classList.remove("d-none")
})
addServiceFormCloses.forEach(addServiceFormClose => {
    addServiceFormClose.addEventListener("click", () => {
        addServiceForm.classList.add("d-none")
        backToList.classList.add("d-none")
        tableContainer.classList.remove("d-none")
    })
})