document.addEventListener("DOMContentLoaded", () => {
    const editButtons = document.getElementsByClassName("btn-edit");
    const commentText = document.getElementById("id_body");
    const commentForm = document.getElementById("commentForm");
    const submitButton = document.getElementById("submitButton");
    //const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    const deleteButtons = document.getElementsByClassName("btn-delete");
    const deleteConfirm = document.getElementById("deleteConfirm");
    const likeIcons = document.querySelectorAll('.like-icon');
    //const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    console.log("everything loaded");
        
    
    // event listeners for edit Buttons
    for (let button of editButtons) {
        button.addEventListener("click", (e) => {
            let commentId = e.target.getAttribute("data-comment_id");
            let commentContent = document.getElementById(`comment${commentId}`).innerText;
            commentText.value = commentContent;
            submitButton.innerText = "Update";
            const slug = window.slug;
            commentForm.setAttribute("action", `/post/${slug}/comment/${commentId}/edit/`);
            console.log("Editing comment ID:", commentId);
            console.log("Comment content:", commentContent);
        });
    }
    // event listeners for delete Buttons
    for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
            let commentId = e.target.getAttribute("data-comment_id");
            deleteConfirm.href = `delete_comment/${commentId}`;
            deleteModal.show();
        });
    }
   
    
    /*event listeners for span likeIcons
    likeIcons.forEach(icon => {
        icon.addEventListener('click', function() {
            const postId = this.getAttribute('data-post-id');
            const form = this.closest('.like-form');
            const likeCountElement = document.getElementById(`like-count-${postId}`);
            const iconElement = this.querySelector('i'); // Hämta ikonen direkt här
    
            fetch(form.action, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': csrfToken
                },
                body: JSON.stringify({})
            })
            .then(response => response.json())
            .then(data => {
                console.log('Received data:', data);
                if (data.success) {
                    likeCountElement.textContent = data.new_like_count;
                    console.log("Like icons found:", likeIcons.length);
    
                    // Byt ikonens klass här
                    if (iconElement.classList.contains('far')) {
                        iconElement.classList.remove('far');
                        iconElement.classList.add('fas');
                    } else {
                        iconElement.classList.remove('fas');
                        iconElement.classList.add('far');
                    }
                } else {
                    console.error('Något gick fel.');
                }
            })
            .catch(error => console.error('Fel:', error));
        });
    });*/
    
});