// console.log($("#subscription-list"));
const baseUrl = "http://127.0.0.1:8000/api/"

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


let packageChart = document.getElementById("package-chart").getContext("2d");

let revenuePieChart = new Chart(packageChart, {
    type: "pie",
    data: {
        labels: ["CUSTOM", "BASIC", "ADVANCE", "MEDIUM"],
        datasets: [{
            label: "Subscribed client",
            backgroundColor: ['#182F59', '#5BBC2E', '#FFD500', '#DC143C'],
            data: [45, 25, 10, 20],
        }, ],
    },

    options: {
        responsive: true,
        legend: {
            display: true,
            labels: {
                fontColor: "black",
                boxWidth: 15,
            },
            // maxWidth: 30,
            position: "left",
        },
    },
});
const packageDetails = document.querySelector(".package-details")
const subscriptionService = document.querySelector("#serviceName")
const showSubscription = (url)=>{
    fetch(url)
    .then(response => response.json())
    .then(result => {
        let divHtml
        result.map(subscription => {
            // console.log(subscription);
            const div = document.createElement("div")
            div.classList.add("package", "bg-lightgreen", "shadow", "p-3", "rounded")
            divHtml = `
            <h3 class="fw-bold fs-4">${subscription.package_name}</h3>
            <table class="mx-auto mb-3">
            <tbody>`
            subscription.feature_subscription?.map((item, index)=>{
                divHtml += `<tr>
                <td>${item}</td>
                <td>✓</td>
                </tr>`

            })
            
            
            divHtml += `
            </tbody>
            </table>
            <div class="info-btn">
            <p class="mb-0">
            <i class="bi bi-person-fill"></i> Max workstations
            </p>
            <p class="mb-0 fw-bold">${subscription.workstations}</p>
            </div>
            <div class="info-btn">
            <p class="mt-2">
            <i class="bi bi-person-fill"></i> Max servers
            </p>
            <p class="mb-0 fw-bold">${subscription.servers}</p>
            </div>
            <div class="info-btn">
            <p class="mt-2">
            <i class="bi bi-person-fill"></i> Max websites
            </p>
            <p class="mb-0 fw-bold">${subscription.websites}</p>
            </div>
            <div class="mt-2 info-btn">
            <p class="mb-0">
            <i class="icofont-tag"></i> Price
            </p>
            <p class="mb-0 fw-bold">${subscription.price}$ <span class="fw-bolder">/${parseInt(subscription.duration) > 1 && subscription.duration}</span>
            </p>
            </div>
            <button class="mt-3 btn bg-navy px-5 py-1 text-uppercase" data-bs-toggle="modal"
            data-bs-target="#subscribeModal-2">Edit</button>
            `
            div.innerHTML = divHtml
            packageDetails.appendChild(div)
        })
        
    })
}
console.log(subscriptionService.value);
window.addEventListener("load", ()=>{
    packageDetails.innerHTML = ""
    showSubscription(`${baseUrl}bcs/package/${subscriptionService.value}`)
})

subscriptionService.addEventListener("change", () => {
    packageDetails.innerHTML = ""
    showSubscription(`${baseUrl}bcs/package/${subscriptionService.value}`)
})