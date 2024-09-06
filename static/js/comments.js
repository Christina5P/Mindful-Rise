// Open edit form for comment edits

document.addEventListener("DOMContentLoaded", function() {
    const editButtons = document.querySelectorAll('.btn-edit');
  
    editButtons.forEach(button => {
      button.addEventListener("click", function() {
        const commentId = this.getAttribute("data-comment_id");
        const editForm = document.getElementById(`editForm${commentId}`);
        const commentText = document.getElementById(`comment${commentId}`);
  
        if (commentText && editForm) {
          if (editForm.style.display === "none") {
            editForm.style.display = "block";
            commentText.style.display = "none";
          } else {
            editForm.style.display = "none";
            commentText.style.display = "block";
          }
        }
      });
    });
  });


// to push delete Modal
$(document).ready(function() {
    const deleteConfirm = document.getElementById("deleteConfirm");

    $('.btn-delete').on('click', function() {
        const deleteUrl = $(this).data("delete-url"); 
        deleteConfirm.setAttribute('href', deleteUrl); 


        const deleteModalElement = document.getElementById("deleteModal");
        const deleteModal = new mdb.Modal(deleteModalElement);
        deleteModal.show(); 
    });
});
