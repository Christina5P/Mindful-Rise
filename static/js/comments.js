document.addEventListener("DOMContentLoaded", function() {
  
      console.log("everything loaded");
});

 // Event listeners för edit Buttons
 const editButtons = document.querySelectorAll('.btn-edit');

 for (let button of editButtons) {
     button.addEventListener("click", (e) => {
         let commentId = e.target.getAttribute("data-comment_id") || e.target.closest('button').getAttribute("data-comment_id");
         let commentContent = document.getElementById(`comment${commentId}`).innerText;
         commentText.value = commentContent;
         submitButton.innerText = "Update";
         const slug = window.slug;
         commentForm.setAttribute("action", `/post/${slug}/comment/${commentId}/edit/`);
         
         console.log("Editing comment ID:", commentId);
         console.log("Comment content:", commentContent);
         
         // Visa edit-formuläret
         showEditForm(commentId);
     });
 }
 

    // Event listeners för delete Buttons
    
     for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
            let commentId = e.target.getAttribute("data-comment_id");
	    document.addEventListener("DOMContentLoaded", function() {
            });
        });
    };
