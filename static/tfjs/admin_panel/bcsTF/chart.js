let userChart = document.getElementById("user-chart").getContext("2d");
let infoChart = document.getElementById("info-chart").getContext("2d");
let userLineChart = new Chart(userChart, {
    type: "line",
    data: {
        labels: ["1:00pm", "2:00pm", "3:00pm", "4:00pm", "5:00pm"],
        datasets: [{
            label: "Subscribed client",
            backgroundColor: "black",
            borderColor: "black",
            data: [5, 45, 41, 50, 42],
            fill: false,
        }, ],
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
            display: true,
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
            label: "Subscribed client",
            backgroundColor: "#182F59",
            borderColor: "#182F59",
            data: [5, 45, 41, 50, 42],
            fill: false,
        }, {
            label: "non- subscribed client",
            backgroundColor: "#5BBC2E",
            borderColor: "#5BBC2E",
            data: [75, 35, 45, 55, 15],
            fill: false,
        }, {
            label: "total client",
            backgroundColor: "#111125",
            borderColor: "#111125",
            data: [50, 5, 50, 9, 25],
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
            position: "left",
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