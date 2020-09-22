const submitHwButtons = document.getElementsByClassName('submitHomework');
const sendHomeworkButtons = document.getElementsByClassName('sendHomeworkButton');

let hw_id;
for (let sendHwButton of sendHomeworkButtons) {
    sendHwButton.onclick = function() {
        hw_id = sendHwButton.getAttribute('data-hw-id');
        $.ajax({
            url: '/student/' + hw_id + '/instantiate_student_homework/',
            type: 'GET',
            dataType: 'json',
        })
    }
}

for (let submitHwButton of submitHwButtons) {
    submitHwButton.onclick = function() {
        $.ajax({
            url: '/student/' + hw_id + '/submit_homework/',
            type: 'GET',
            dataType: 'json',
            success: function(response) {
                if (response['isdone'] == true) {
                    window.location.reload();
                }
            }
        })
    }
}
// DROPZONE CONFIGURATIONS
let homeworkDropzone = document.querySelector('#homeworkDropzone');
let requestUsername = homeworkDropzone.getAttribute('data-username');
let now = new Date();
let year = now.getFullYear();
let month = now.getMonth();
let date = now.getDate()
let hours = now.getHours();
let minutes = now.getMinutes();
let seconds = now.getSeconds();

Dropzone.options.homeworkDropzone = {
    addRemoveLinks: true, 
    dictDefaultMessage: "Перетащите или нажмите для отправки фотографий",
    dictFallbackMessage: "К сожалению, ваш браузер не поддерживает Drag'n'Drop",
    dictFallbackText: "Пожалуйста, воспользуйтесь старой доброй формой для загрузки",
    dictFileTooBig: "Файл слишком большой. Максимальный допустимый размер файла 10 MB",
    dictInvalidFileType: "Вы не можете загружать файлы этого типа.",
    dictResponseError: "Произошла ошибка при загрузке файла. Попробуйте еще раз. Если ошибка будет повторяться - передайте эту информацию администратору сайта: Код ошибки {{statusCode}}",
    dictCancelUpload: "Отменить загрузку",
    dictCancelUploadConfirmation: "Уверены, что хотите прервать загрузку?",
    dictRemoveFile: "Удалить файл",
    renameFile: function(file) {
        let file_comp = file.name.split('.');
        let type = file_comp[1];
        let file_name = `${requestUsername}_${file_comp[0]}_${year}${month}${date}${hours}${minutes}${seconds}.${type}`;
        return file_name;
    },
    removedfile: function(file) {
        let file_comp = file.name.split('.');
        let type = file_comp[1];
        let file_name = `${requestUsername}_${file_comp[0]}_${year}${month}${date}${hours}${minutes}${seconds}.${type}`;
        $.ajax({
            url: '/student/' + file_name + '/delete_upload/',
            type: 'GET',
            success: function(response) {
                console.log('Success!!')
            }
        })
        return file.previewElement.remove();
    },
    maxFilesize: 10,
    maxFiles: 10,
    acceptedFiles: 'image/jpg',
    acceptedFiles: '.jpeg, .jpg, .png',
    dictMaxFilesExceeded: `Превышен лимит количества файлов. Вы можете загрузить не более 10 файлов`,
}

//
