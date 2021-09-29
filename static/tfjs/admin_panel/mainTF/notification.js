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

const checkEmpty = (btn, textArea, error) => {
    btn.addEventListener('click', () => {
        if (textArea.value == "") {
            error.classList.remove("d-none")
        }
        setTimeout(()=> {
            error.classList.add("d-none")
        }, 1000)
    })
}


const sendBtn = document.querySelector('.sendBtn')
const addBtn = document.querySelector('.addBtn')
const sendNotification = document.querySelector('.sendNotification')
const addNotification = document.querySelector('.addNotification')
const sendError = document.querySelector('.sendError')
const addError = document.querySelector('.addError')

checkEmpty(sendBtn, sendNotification, sendError);
checkEmpty(addBtn, addNotification, addError);

const deleteRowBtn = document.querySelectorAll(".dlt")

deleteRowBtn.forEach(btn=>{
    btn.addEventListener("click", ()=>{
        btn.parentElement.parentElement.classList.add("d-none")
    })
})