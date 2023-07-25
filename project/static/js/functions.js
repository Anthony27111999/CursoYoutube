function message_error(obj) {
    let html = '';
    if (typeof obj === 'object') {
        html += '<ul>';
        $.each(obj, function (key, value) {
            html += '<li>' + key + ': ' + value + '</li>';
        });

        html += '</ul>';
    }
    else{
            html = '<p>'+ obj +'</p>';
        } 
    

    Swal.fire({
        title: 'Error!',
        html: html,
        icon: 'error',
        confirmButtonText: 'Cool'
    })

}

function  alert_jqueryConfirm(){
    $.confirm({
        theme: 'material',
        title: 'Confirmación',
        icon: 'fa fa-info',
        content: '',
        columnClass: 'medium',
        typeAnimated: true,
        cancelButtonClass: 'btn-primary',
        draggable: true,
        dragWindowBorder: false,
        buttons: {
            info: {
                text: "Si",
                btnClass: 'btn-primary',
                action: function () {

                }
            },
            danger: {
                text: "No",
                btnClass: 'btn-red',
                action: function () {

                }
            },
        }
    })
}