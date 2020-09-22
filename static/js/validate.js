$(document).ready(function() {
    $('#registraionForm').validate({
        errorPlacement: function(label, element) {
            label.addClass('error-wrapper');
            label.insertAfter(element);
        },
        wrapper: 'div',
        rules: {
            fullname: {
                required: true,
                minlength: 5
            },
            username: {
                required: true,
                minlength: 3,
            },
            email: {
                required: true,
                email: true,
            },
            password: {
                required: true,
                minlength: 5,
            },
            alias: {
                required: true,
                minlength: 3,
            },
            school_password: {
                required: true,
                minlength: 5,
            }
        },
        messages: {
            fullname: {
                required: 'Заполните данное поле',
                minlength: 'Должно быть больше 5 букв'
            },
            username: {
                required: 'Введите имя пользователя',
                minlength: 'Должно быть более 3 символов'
            },
            email: {
                required: 'Введите Адресс электронной почты',
                email: 'Адресс электронной почты введен неправильно'
            },
            password: {
                required: 'Введите пароль',
                minlength: 'Пароль должен состоять из более 5 символов'
            },
            alias: {
                required: 'Введите EduName',
                minlength: 'EduName должен состоять из более 5 символов'
            },
            school_password: {
                required: 'Введите пароль школы',
                minlength: 'Должно состоять из более 5 символов'
            }
        },
    })
    $('#personalInfo').validate({
        errorPlacement: function(label, element) {
            label.addClass('error-wrapper');
            label.insertAfter(element);
        },
        wrapper: 'div',
        rules: {
            fullname: {
                required: true,
                minlength: 5,
            },
            username: {
                required: true,
                minlength: 3,
            },
        },
        messages: {
            fullname: {
                required: 'Заполните данное поле',
                minlength: 'Должно быть больше 5 букв'
            },
            username: {
                required: 'Введите имя пользователя',
                minlength: 'Должно быть более 3 символов'
            },
        }
    })
    $('#passwordInfo').validate({
        errorPlacement: function(label, element) {
            label.addClass('error-wrapper');
            label.insertAfter(element);
        },
        wrapper: 'div',
        rules: {
            password0: {
                required: true,
                minlength: 5,
            },
            password1: {
                required: true,
                minlength: 5
            },
            password2: {
                required: true,
                minlength: 5,
                equalTo: "#password1"
            }
        },
        messages: {
            password0: {
                required: 'Введите пароль',
                minlength: 'Должно быть больще 5 символов'
            },
            password1: {
                required: 'Введите пароль',
                minlength: 'Должно быть больще 5 символов'
            },
            password2: {
                required: 'Введите пароль',
                minlength: 'Должно быть больще 5 символов',
                equalTo: 'Введеный пароли не совпадают'
            }
        }
    })
    $('#studentRegistrationForm').validate({
        errorPlacement: function(label, element) {
            label.addClass('error-wrapper');
            label.insertAfter(element);
        },
        wrapper: 'div',
        rules: {
            fullname: {
                required: true,
                minlength: 5
            },
            username: {
                required: true,
                minlength: 3,
            },
            email: {
                required: true,
                email: true,
            },
            password: {
                required: true,
                minlength: 5,
            },
            alias: {
                required: true,
                minlength: 3,
            },
            grade: {
                required: true,
            },
            school_password: {
                required: true,
                minlength: 5,
            }
        },
        messages: {
            fullname: {
                required: 'Заполните поле',
                minlength: 'Должно быть больше 5 букв'
            },
            username: {
                required: 'Введите имя пользователя',
                minlength: 'Должно быть более 3 символов'
            },
            email: {
                required: 'Введите Адресс электронной почты',
                email: 'Адресс электронной почты введен неправильно'
            },
            password: {
                required: 'Введите пароль',
                minlength: 'Пароль должен состоять из более 5 символов'
            },
            alias: {
                required: 'Введите EduName',
                minlength: 'EduName должен состоять из более 5 символов'
            },
            grade: {
                required: 'Заполните поле'
            },
            school_password: {
                required: 'Введите пароль школы',
                minlength: 'Должно состоять из более 5 символов'
            }
        },
    })
    $("#loginForm").validate({
        errorPlacement: function(label, element) {
            label.addClass('error-wrapper');
            label.insertAfter(element);
        },
        wrapper: 'div',
        rules: {
            username: {
                required: true,
                minlength: 3,
            },
            password: {
                required: true,
                minlength: 5,
            },
        },
        messages: {
            username: {
                required: 'Заполните поле',
                minlength: 'Имя пользователя должно быть более 3-х символов'
            },
            password: {
                required: 'Заполните поле',
                minlength: 'Пароль должен быть более 5 символов'
            }
        }
    })
    $("#schoolRegisterForm").validate({
        errorPlacement: function(label, element) {
            label.addClass('error-wrapper');
            label.insertAfter(element);
        },
        wrapper: 'div',
        rules: {
            name: {
                required: true,
                minlength: 5,
            },
            email: {
                required: true,
                email: true,
            },
            password: {
                required: true,
                minlength: 5,
            },
            alias: {
                required: true,
                minlength: 3,
            },
        },
        messages: {
            name: {
                required: 'Заполните данное поле',
                minlength: "Название школы должно состоять из более 5 букв"
            },
            email: {
                required: 'Заполните данное поле',
                email: 'Адресс электронной почты введен неправильно'
            },
            password: {
                required: 'Заполните данное поле',
                minlength: 'Пароль должен состоять из более 5 символов'
            },
            alias: {
                required: 'Заполните данное поле',
                minlength: 'EduName должен состоять из более 5 символов'
            },
        }
    })
    $("#schoolLoginForm").validate({
        errorPlacement: function(label, element) {
            label.addClass('error-wrapper');
            label.insertAfter(element);
        },
        wrapper: 'div',
        rules: {
            alias: {
                required: true,
                minlength: 3,
            },
            password: {
                required: true,
                minlength: 5,
            },
        },
        messages: {
            alias: {
                required: 'Заполните данное поле',
                minlength: 'EduName должен состоять из более 5 символов'
            },
            password: {
                required: 'Заполните данное поле',
                minlength: 'Пароль должен состоять из более 5 символов'
            },
        },
    })
})