$(document).ready(function() {
    const changingQuestionButtons = document.getElementsByClassName('changingQuestion');
    let query;
    for (let changeButton of changingQuestionButtons) {
        changeButton.onclick = function() {
            query = changeButton.getAttribute('data-question-test-id');
        }
    }
    $('.changeQuestion').submit(function(e) {
            e.preventDefault();
            let $form = $(this)
            let $form_data = $form.serialize();
            let $valid_form_data = decodeURI($form_data);
            $.ajax({
                type: 'POST',
                url: '/teacher/' + query + '/changing_question/',
                data: $valid_form_data,
                beforeSend: function() {
                    $('.loading-button').toggle('active');
                },
                success: function() {
                    $('.modal').modal('hide')
                    location.reload()
                },
                complete: function() {
                    $('.loading-button').toggle('active');
                }
            })
        }
    )
})