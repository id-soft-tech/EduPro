$(document).ready(function() {
    $.ajax({
        type: 'GET', 
        dataType: 'json',
        url: 'student_achievement/',
        success: function(response) {
            createChart2(response)
        }
    })

    function createChart2(data) {
        let ctxL2 = document.getElementById("lessonChart").getContext('2d');
        let gradientFill2 = ctxL2.createLinearGradient(0, 0, 0, 290);
        gradientFill2.addColorStop(0, "rgba(0, 125, 250, 1)");
        gradientFill2.addColorStop(1, "rgba(0, 125, 250, 0.1)");
        let lessonChart = new Chart(ctxL2, {
        type: 'line',
        data: {
            labels: ['Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май'],
            datasets: [
            {
                label: "Количество созданных домашних заданий",
                data: data,
                backgroundColor: gradientFill2,
                borderColor: [
                '#007DFA',
                ],
                borderWidth: 2,
                pointBorderColor: "#007DFA",
                pointBackgroundColor: "rgba(0, 125, 250, 1)",
            }
            ]
        },
        options: {
            responsive: true
        }
        });
    }
})