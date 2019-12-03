$('#danger').hide();
$('#update_danger').hide();
updateList();

function updateList() {
    $.ajax({
        url: '/visitors/all',
        type: 'get',
        dataType: 'json',
        success: function (data) {
            let rows = '';
            data.visitors.forEach(visitor => {
                rows += `
        <tr>
            <td>${visitor.id}</td>
            <td>${visitor.name}</td>
            <td>${visitor.email}</td>
            <td>${visitor.title}</td>          
            <td>
                <button id="deletebtn" class="btn deleteBtn btn-danger" data-id="${visitor.id}">Delete</button>
                <button id="update-btn" class="btn updateBtn btn-warning" data-id="${visitor.id}">Update</button>
            </td>  
        </tr>`;
            });
            $('#myTable > tbody').append(rows);
            $('.deleteBtn').each((i, elm) => {
                $(elm).on("click", (e) => {
                    $("#myDeleteModal").modal('show');
                    $('.crud-delete').click(function () {
                        deleteVisitor($(elm));
                    });
                })
            })
            $('.updateBtn').each((i, elm) => {
                $(elm).on("click", (e) => {

                    $("#myUpdateModal").modal('show');
                    $('.crud-update').click(function () {
                        updateVisitor($(elm));
                    });
                })
            })
        }
    });
}

$('.crud-submit').click(function () {
    var nameInput = $('input[name="name"]').val().trim();
    var emailInput = $('input[name="email"]').val().trim();
    var titleInput = $('input[name="title"]').val().trim();
    var formdata = {
        'name': nameInput,
        'email': emailInput,
        'title': titleInput
    };
    $.ajax({
        dataType: 'json',
        type: 'POST',
        url: 'new/',
        data: formdata,
        success: function (data) {
            if (data.is_valid == true) {
                $("#myModal").modal('hide');
                $('#danger').hide();
                updateList();
            } else {
                $('#danger').show(1000);
            }

        }
    },)
});

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function deleteVisitor(el) {
    visitorId = $(el).data('id');
    $.ajax({
        url: `/visitors/delete/${visitorId}`,
        type: 'post',
        dataType: 'json',
        success: function (data) {
            $(el).parents()[1].remove();
            $("#myDeleteModal").modal('hide');
        }
    });
}

function updateVisitor(el) {
    console.log("burdayım");
    var visitorId = $(el).data('id');
    var nameInput = $('input[name="update_name"]').val().trim();
    var emailInput = $('input[name="update_email"]').val().trim();
    var titleInput = $('input[name="update_title"]').val().trim();
    var formdata = {
        'id': visitorId,
        'name': nameInput,
        'email': emailInput,
        'title': titleInput
    };
    $.ajax({
        url: `/visitors/update/${visitorId}`,
        type: 'post',
        dataType: 'json',
        data: formdata,
        success: function (data) {
            if (data.is_valid == true) {
                $("#myUpdateModal").modal('hide');
                $('#update_danger').hide();
                updateList();
            } else {
                $('#update_danger').show(1000);
            }

        }
    });

}


function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');
console.log(csrftoken);