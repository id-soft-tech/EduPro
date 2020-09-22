$(document).ready(function() {
    $(document).ready(function(){
            $('.toast').toast({delay: 5000});
            $('.toast').toast('show');
    });
    const addQuestionButtons = document.getElementsByClassName('addQuestionButton')

    let query;

    for (let questionButton of addQuestionButtons) {
        questionButton.onclick = function() {
            query = questionButton.getAttribute("data-test-id");
        }
    }
    $('.add_question_form').submit(function(e) {
        e.preventDefault()
        let $form = $(this)
        let $form_data = $form.serialize()
        let $valid_form_data = decodeURI($form_data)
        $.ajax({
            type: 'POST',
            url: 'teacher/' + query + '/adding_questions/',
            data: $valid_form_data,
            beforeSend: function() {
                $('.loading-button').toggle('active');
            },
            success: function() {
                $('#createQuestionModal').modal('hide');
            },
            complete: function() {
                $form.each(function(){
                    this.reset();   //Here form fields will be cleared.
                });
                $('.status').html('')
                $('.loading-button').toggle('active');
            },
            error: function(jqXHR, textStatus, errorThrown) {
                console.log(textStatus, errorThrown);
            }
        })
        $.ajax({
            type: 'GET', 
            url: 'teacher/' + query + '/adding_questions/',
            dataType: 'json',
            success: function(response) {
                console.log(response.test_left)
                let test_left = response.test_left
                if (test_left == 0) {
                    location.reload()
                }
            }
        })
    })
    // CHART FOR TESTS
    $.ajax({
        type: 'GET', 
        dataType: 'json',
        url: 'tested_pupils/',
        success: function(response) {
            createChart1(response)
        }
    })
    function createChart1(data) {
        let ctxL1 = document.getElementById("testChart").getContext('2d');
        let gradientFill1 = ctxL1.createLinearGradient(0, 0, 0, 290);
        gradientFill1.addColorStop(0, "rgba(0, 125, 250, 1)");
        gradientFill1.addColorStop(1, "rgba(0, 125, 250, 0.1)");
        let testChart = new Chart(ctxL1, {
            type: 'line',
            data: {
                labels: ['Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май'],
                datasets: [
                {
                    label: "Количество созданных тестирований",
                    data: data,
                    backgroundColor: gradientFill1,
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
    // CHART FOR ONLINE LESSONS
    $.ajax({
        type: 'GET', 
        dataType: 'json',
        url: 'homework/',
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