// ajax for like-button without refresh browser

$(document).ready(function() {
    $(document).on('click', '.like-button', function(e) {
        e.preventDefault();

        var $this = $(this);
        var url = $this.attr('href');
        var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();

       $.ajax({
    url: url,
    type: 'POST',
    data: {
        csrfmiddlewaretoken: csrfToken
    },
    dataType: 'json',
    success: function(data) {
        if (data.is_liked) {
            $this.find('i').removeClass('far').addClass('fas');
        } else {
            $this.find('i').removeClass('fas').addClass('far');
        }
        $this.siblings('.likes-count').text(data.likes_count);
    },
    error: function(xhr) {
        if (xhr.status === 403) {
            document.getElementById('alert-container').classList.remove('d-none');
        } else {
            console.error("Error occurred: ", xhr.responseText);
             }
           }
       });
    });


// event listener for close alert
    document.addEventListener('DOMContentLoaded', function () {
        const closeButton = document.querySelector('.btn-close');
        if (closeButton) {
            closeButton.addEventListener('click', function () {
                document.getElementById('alert-container').classList.add('d-none');
            });
        }
    });
});
