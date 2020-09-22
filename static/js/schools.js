$(document).ready(function() {
    let numberOfTeachers;
    let numberOfStudents;
    $.ajax({
        type: 'GET',
        dataType: 'json',
        url: 'list_teachers/',
        success: function(response) {
            let j = JSON.parse(response)
            numberOfTeachers = j.length
        }
    })
    $.ajax({
        type: 'GET',
        dataType: 'json',
        url: 'list_students/',
        success: function(response) {
            let j = JSON.parse(response)
            numberOfStudents = j.length
            defineChar();
        }
    })
    // Create chart instance
    function defineChar() {
        var ctxP = document.getElementById("labelChart").getContext('2d');
        var myPieChart = new Chart(ctxP, {
        plugins: [ChartDataLabels],
        type: 'pie',
        data: {
            labels: ["Ученики", "Учителя",],
            datasets: [{
                data: [numberOfStudents, numberOfTeachers],
                backgroundColor: ["#949FB1", "#4D5360"],
                hoverBackgroundColor: ["#A8B3C5", "#616774"]
            }]
        },
        options: {
            responsive: true,
            legend: {
            position: 'right',
            labels: {
                padding: 20,
                boxWidth: 10
            }
            },
            plugins: {
            datalabels: {
                formatter: (value, ctx) => {
                    let sum = 0;
                    let dataArr = ctx.chart.data.datasets[0].data;
                    dataArr.map(data => {
                        sum += data;
                    });
                    let percentage = (value * 100 / sum).toFixed(2) + "%";
                    return percentage;
                    },
                    color: 'white',
                    labels: {
                    title: {
                        font: {
                        size: '16'
                        }
                }
                }
            }
            }
        }
        });
    }
})