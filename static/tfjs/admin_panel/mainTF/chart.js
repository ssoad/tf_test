let userChart = document.getElementById("user-chart").getContext("2d");
let infoChart = document.getElementById("info-chart").getContext("2d");
let userLineChart = new Chart(userChart, {
    type: "line",
    data: {
        labels: ["1:00pm", "2:00pm", "3:00pm", "4:00pm", "5:00pm"],
        datasets: [{
            label: "New User",
            backgroundColor: "black",
            borderColor: "black",
            data: [5, 45, 41, 50, 42],
            fill: false,
        },
     ],
    },
    options: {
        responsive: true,
        legend: {
            display: false,
            labels: {
                fontColor: "black",
            },
            position: "top",
        },
        title: {
            display:true,
            position: "top",
            align: 'start',
            text: "Users site visits in last 5 hours",
        },
        tooltips: {
            mode: "index",
            intersect: false,
        },
        hover: {
            mode: "nearest",
            intersect: true,
        },
        scales: {
            xAxes: [{
                gridLines: {
                    display: false
                }
            }],
            yAxes: [{
                gridLines: {
                    display: false
                }
            }]
        },
    },
});
let infoLineChart = new Chart(infoChart, {
    type: "line",
    data: {
        labels: ["text", "text", "text", "text", "text"],
        datasets: [{
            label: "Free",
            backgroundColor: "black",
            borderColor: "black",
            data: [5, 45, 41, 50, 42],
            fill: false,
        }, {
            label: "Regular",
            backgroundColor: "#182f59",
            borderColor: "#182f59",
            data: [75, 35, 45, 55, 15],
            fill: false,
        },{
            label: "Premium",
            backgroundColor: "red",
            borderColor: "red",
            data: [50, 5, 50, 9, 25],
            fill: false,
        },{
            label: "Maximum",
            backgroundColor: "green",
            borderColor: "#5BBC2E",
            data: [180, 3, 27, 30, 10],
            fill: false,
        }, ],
    },
    options: {
        responsive: true,
        legend: {
            display: true,
            labels: {
                fontColor: "black",
                boxWidth: 20,
                boxHeight: 20,
            },
            position: "top",
        },
        title: {
            display: false,
            position: "top",
            align: 'start',
            text: "all users",
        },
        tooltips: {
            mode: "index",
            intersect: false,
        },
        hover: {
            mode: "nearest",
            intersect: true,
        },
        scales: {
            xAxes: [{
                gridLines: {
                    display: false
                }
            }],
            yAxes: [{
                gridLines: {
                    display: false
                }
            }]
        },
    },
});
//console.log(window.innerWidth);
//
//if(window.innerWidth <=769){
//   infoLineChart.options.legend.display=false;
//}