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
let infoLineChart = new Chart(infoChart, {});
let getChartData = type => {

    fetch(`http://127.0.0.1:8000/api/main/main_admin_${type}_chart/`)
        .then(response => {
            return response.json()
        })
        .then(data => {
            infoLineChart.destroy();
            infoLineChart = new Chart(infoChart, {
                type: "line",
                data: {
                    labels: data.x_axis,
                    datasets: [{
                        label: "Subscribed client",
                        backgroundColor: "#182F59",
                        borderColor: "#182F59",
                        data: data.datas.for_subscription,
                        fill: false,
                    }, {
                        label: "non- subscribed client",
                        backgroundColor: "#5BBC2E",
                        borderColor: "#5BBC2E",
                        data: data.datas.for_unsubscription,
                        fill: false,
                    }, {
                        label: "total client",
                        backgroundColor: "#111125",
                        borderColor: "#111125",
                        data: data.datas.total_count,
                        fill: false,
                    },],
                },
                options: {
                    responsive: true,
                    legend: {
                        display: true,
                        labels: {
                            fontColor: "black",
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

        });
}

getChartData('all');
//console.log(window.innerWidth);
//
//if(window.innerWidth <=769){
//   infoLineChart.options.legend.display=false;
//}