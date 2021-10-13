
// console.log($("#subscription-list"));

$(document).ready(function () {
    $("#subscription-list").DataTable({
        scrollX: true,
        scrollCollapse: true,
        info: false,
        columnDefs: [{
            orderable: false,
            targets: -1
        }],
        sorting: false,
        searching: false,
        // oLanguage: {
        //     sSearch: `_INPUT_ <i class="bi bi-search"></i>`,
        //     sSearchPlaceholder: "Search...",
        // },
        "paging": false,
    });

});

const plugAndPlay = document.querySelector(".plugAndPlay")
const selectElement = document.querySelectorAll('.form-check-input');
const manage = document.querySelector(".managed")
selectElement.forEach(select=>{
    select.addEventListener("change",()=>{
        if(select.value== "option1"){
            manage.classList.add("d-none")
            plugAndPlay.classList.remove("d-none")
        }else{
            manage.classList.remove("d-none")
            plugAndPlay.classList.add("d-none")
        }
    })
})

const addFeature = document.querySelector(".add-feature")
const featureInput = document.querySelector(".feature-input")
const featureContainer = document.querySelector(".featureInputContainer")

addFeature.addEventListener("click", (e)=>{
    e.preventDefault()
    const desabledInput = document.createElement("input")
    desabledInput.setAttribute("disabled", "true")
    desabledInput.setAttribute("name", "feature")
    desabledInput.classList.add("featureInputDesabled")
    desabledInput.setAttribute("type", "text")
    desabledInput.setAttribute("value", featureInput.value)
    featureInput.value = ""
    featureContainer.appendChild(desabledInput)
})

let packageChart = document.getElementById("package-chart").getContext("2d");

let revenuePieChart = new Chart(packageChart, {
    type: "pie",
    data: {
        labels: ["CUSTOM", "BASIC", "ADVANCE", "MEDIUM"],
        datasets: [{
            label: "Subscribed client",
            backgroundColor: ['#182F59','#5BBC2E','#FFD500', '#DC143C'],
            data: [45, 25, 10, 20],
        },  ],
    },
      
    options: {
        responsive: true,
        legend: {
            display: true,
            labels: {
                fontColor: "black",
                boxWidth:15,
            },
            // maxWidth: 30,
            position: "left",
        },        
    },
});