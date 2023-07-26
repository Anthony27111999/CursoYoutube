function message_error(obj) {
    let html = '';
    if (typeof obj === 'object') {
        html += '<ul>';
        $.each(obj, function (key, value) {
            html += '<li>' + key + ': ' + value + '</li>';
        });

        html += '</ul>';
    } else {
        html = '<p>' + obj + '</p>';
    }


    Swal.fire({
        title: 'Error!',
        html: html,
        icon: 'error',
        confirmButtonText: 'Cool'
    })

}

function alert_jqueryConfirm(url, parameters, callback) {
    $.confirm({
        theme: 'material',
        title: 'Confirmación',
        icon: 'fa fa-info',
        content: '¿Estas seguro de realizar la siguiente accion?',
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
                    $.ajax({
                        url: url,
                        type: 'POST',
                        data: parameters,
                        dataType: 'json'
                    }).done(function (data) {
                        if (!data.hasOwnProperty('error')) {
                            callback();
                            return false;
                        }
                        message_error(data)
                    }).fail(function (jqXHR, textStatus, errorThrown) {
                        alert('Error - ' + textStatus + ' - ' + errorThrown)
                    }).always(function (data) {
                        console.log('paso')
                    })
                },
                danger: {
                    text: "No",
                    btnClass: 'btn-red',
                    action: function () {

                    }
                },
            }
        }
    })
}
