document.addEventListener("DOMContentLoaded", function() {
    const editButtons = document.getElementsByClassName("btn-edit");
    const commentText = document.getElementById("id_body");
    const commentForm = document.getElementById("commentForm");
    const submitButton = document.getElementById("submitButton");
    const deleteModal = new mdb.Modal(document.getElementById("deleteModal"));
    const deleteButtons = document.getElementsByClassName("btn-delete");
    const deleteConfirm = document.getElementById("deleteConfirm");
   
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
            
            if (commentId) {
                deleteConfirm.href = `delete_comment/${commentId}`;
                deleteModal.show();
            } else {
                console.error("Comment ID not found.");
            }
        });
       
    }
        
});
    