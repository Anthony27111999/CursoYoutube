var tblClient;
 var modal_title;

function getData() {
    tblClient = $('#table').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "id"},
            {"data": "names"},
            {"data": "surnames"},
            {"data": "ci"},
            {"data": "date_birthday"},
            {"data": "gender"},
            {"data": "id"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    var buttons = '<a href="#" rel="edit" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                    buttons += '<a href="#" rel="delete" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                    return buttons;
                }
            },
        ],
        initComplete: function (settings, json) {

        }
    });
}

$(function () {

    modal_title = $('.modal-title');

    getData();

    $('.btnAdd').on('click', function () {
        $('input[name="action"]').val('add');
        modal_title.find('span').html('Creación de un cliente');
        console.log(modal_title.find('i'));
        modal_title.find('i').removeClass().addClass('fas fa-plus');
        $('form')[0].reset();
        $('#myModalClient').modal('show');
    });

    $('#table tbody')
        .on('click', 'a[rel="edit"]', function(){
        $('input[name="action"]').val('edit');
        modal_title.find('span').html('Edit de un cliente');
        let tr = tblClient.cell( $(this).closest('td, li')).index();
        let data = tblClient.row(tr.row).data();
        $('input[name="id"]').val(data.id)
        $('input[name="name"]').val(data.names)
        $('input[name="surname"]').val(data.surnames)
        $('input[name="ci"]').val(data.ci)
        $('input[name="date_birthday"]').val(data.date_birthday)
        $('input[name="address"]').val(data.address)
        $('input[name="gender"]').val(data.gender)
        $('#myModalClient').modal('show');
    })
        .on('click', 'a[rel="delete"]', function(){
        $('input[name="action"]').val('edit');
        modal_title.find('span').html('Edit de un cliente');
        let tr = tblClient.cell( $(this).closest('td, li')).index();
        let data = tblClient.row(tr.row).data();
        $('input[name="id"]').val(data.id)
        $('input[name="name"]').val(data.names)
        $('input[name="surname"]').val(data.surnames)
        $('input[name="ci"]').val(data.ci)
        $('input[name="date_birthday"]').val(data.date_birthday)
        $('input[name="address"]').val(data.address)
        $('input[name="gender"]').val(data.gender)
        $('#myModalClient').modal('show');
    });

    $('#myModalClient').on('shown.bs.modal', function () {
        $('form')[0].reset();
    });

    $('form').on('submit', function (e) {
        e.preventDefault();
        //var parameters = $(this).serializeArray();
        var parameters = new FormData(this);
        alert_jqueryConfirm(window.location.pathname, parameters, '¿Estas seguro de realizar la siguiente acción?', parameters, function () {
            $('#myModalClient').modal('hide');
            tblClient.ajax.reload();
            //getData();
        });
    });
});