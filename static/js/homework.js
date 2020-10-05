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
let FILENAME = {}
Dropzone.options.homeworkDropzone = {
    addRemoveLinks: true, 
    dictDefaultMessage: "Перетащите или нажмите для отправки фотографий",
    dictFallbackMessage: "К сожалению, ваш браузер не поддерживает Drag'n'Drop",
    dictFallbackText: "Пожалуйста, воспользуйтесь старой доброй формой для загрузки",
    dictFileTooBig: "Файл слишком большой. Максимальный допустимый размер файла 10 MB",
    dictInvalidFileType: "Вы не можете загружать файлы этого типа.",
    dictResponseError: "Произошла ошибка при загрузке файла. Попробуйте еще раз. Если ошибка будет повторяться - передайте эту информацию администратору сайта: Код ошибки {{statusCode}}",
    dictCancelUpload: "Отменить загрузку",
    dictUploadCanceled: 'Загрузка файла было отменено',
    dictCancelUploadConfirmation: "Уверены, что хотите прервать загрузку?",
    dictRemoveFile: "Удалить файл",
    dictRemoveFileConfirmation:  "Вы уверены, что хотите удалить этот файл?",
    success: function(file, response) {
        console.log(response['photoName'], file.name)
        FILENAME[file.name] = response['photoName']
    },
    removedfile: function(file) {
        file_name = FILENAME[file.name]
        $.ajax({
            url: '/student/' + file_name + '/delete_upload/',
            type: 'GET',
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
