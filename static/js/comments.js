document.addEventListener("DOMContentLoaded", () => {
    const editButtons = document.getElementsByClassName("btn-edit");
    const commentText = document.getElementById("id_body");
    const commentForm = document.getElementById("commentForm");
    const submitButton = document.getElementById("submitButton");
    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
    const deleteButtons = document.getElementsByClassName("btn-delete");
    const deleteConfirm = document.getElementById("deleteConfirm");
    const likeIcons = document.querySelectorAll('.like-icon');

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

    
    // event listeners for span likeIcons

     likeIcons.forEach(icon => {
        icon.addEventListener('click', function() {
            const postId = this.getAttribute('data-post-id');
            const form = this.closest('.like-form');

            fetch(form.action, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': form.querySelector('[name=csrfmiddlewaretoken]').value,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ post_id: postId })
            })
            .then(response => {
                if (response.ok) {
                    // Ändra ikonen baserat på gillande-status
                    const iconElement = this.querySelector('i');
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
    });
});

