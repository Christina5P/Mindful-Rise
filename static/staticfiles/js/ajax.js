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
                if (data.status === 'liked') {
                    $this.html('<i class="fas fa-heart" style="color: red;"></i>');
                } else if (data.status === 'unliked') {
                    $this.html('<i class="far fa-heart" style="color: red;"></i>');
                }

                // Uppdatera antalet gillningar
                $this.closest('.like-section').find('.likes-count').text(data.likes_count);
            },
            error: function(xhr, status, error) {
                console.error("Error occurred: ", error);
            }
        });
    });
});
