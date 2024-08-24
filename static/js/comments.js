document.addEventListener("DOMContentLoaded", function() {
    const deleteModal = new mdb.Modal(document.getElementById("deleteModal"));
    const deleteButtons = document.getElementsByClassName("btn-delete");
    const deleteConfirm = document.getElementById("deleteConfirm");
   
    console.log("everything loaded");
        
   
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
