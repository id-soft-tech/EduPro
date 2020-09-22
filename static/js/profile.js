let closeButton = document.querySelectorAll('.close');
        let modal = document.querySelector('.modal');
        let openModal = document.querySelector('.openModal');
        let openPasswordModal = document.querySelector('.openPasswordModal');
        let passwordModal = document.querySelector('.passwordModal');
    
        openModal.onclick = function() {
            modal.style.display = 'block';
        }
        openPasswordModal.onclick = function() {
            passwordModal.style.display = 'block';
        }
        for (let close of closeButton) {
            close.onclick = function() {
                modal.style.display = 'none';
                passwordModal.style.display = 'none';
            }
        }
        window.onclick = function(event) {
            if (event.target == modal || event.target == passwordModal) {
                modal.style.display = 'none';
                passwordModal.style.display = 'none';
            }
        }
        // Vue.js
        const personalInfo = new Vue({
            delimiters : ['[[',']]'],
            el: '#personalInfo',
            data: {
                fullname: '',
                username: '',
                errors: [],
            },
            methods: {
                checkForm: function(e) {
                    if (this.fullname || this.username) {
                        if (this.fullname.length > 5 || this.username.length > 2) {
                            return true;
                        }
                    }
                    this.errors = [];
                    if (this.fullname.length < 5) {
                        this.errors.push('Фамилия и имя должно быть больше 5 букв');
                    }
                    if (this.username.length < 2) {
                        this.errors.push('Имя пользователя должно быть больше 2 символов');
                    }
                    e.preventDefault();
                }
            },
        })
        const passwordInfo = new Vue({
            delimiters : ['[[',']]'],
            el: '#passwordInfo',
            data: {
                password0: '',
                password1: '',
                password2: '',
                errors: [],
            },
            methods: {
                checkForm: function(e) {
                    if (this.password0 && this.password1 && this.password2) {
                        if (this.password0.length > 5 && this.password1.length > 5 && this.password2.length > 5) {
                            return true;
                        }
                    }
                    this.errors = [];
                    if (this.password0.length <= 5 || this.password1.length <= 5 || this.password2.length <= 5) {
                        this.errors.push('Пароль должен состоять из более 5 символов');
                    }
                    e.preventDefault();
                }
            },
        })