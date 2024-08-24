
console.log("ajax loaded");
        
console.log(typeof $);


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
                
            });
        });
    });
