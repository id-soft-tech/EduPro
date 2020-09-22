$(document).ready(function(){
    window.onload = initilize;
    let saveAnswerButton;
    let form = document.querySelector('#solve_test_form');
    let test_id = form.getAttribute('data-test-id');
    function initilize() {
        saveAnswerButton = document.getElementById('save_answer')
        saveAnswerButton.onclick = save_answer;
    }
    function save_answer() {
        let answer = $('input:radio[name=option]:checked').val();
        let question_id = form.getAttribute('data-question-id');

        let request = new XMLHttpRequest();
        let url = '/student/'+ test_id +'/' + question_id +'/save_answer?answer=' + answer

        request.open('GET', url, true)
        request.send()
    }
    let timer_wrapper = document.querySelector('#timer')
    function timer() {
        $.ajax({
            url: '/student/' + test_id + '/get_timer/',
            dataType: 'json',
            type: 'GET',
            success: function(response) {
                time = response['time']
                if (response['isfinished']) {
                    window.location.href = '/';
                }else {
                    timer_wrapper.innerHTML = Math.floor(time / 60) + ' : ' + ((time % 60 >= 10) ? Math.floor(time%60) : '0' + Math.floor(time%60));
                }
            }
        })
    }
    setInterval(timer, 1000);
})