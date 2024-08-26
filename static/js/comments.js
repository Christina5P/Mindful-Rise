
console.log("comment loaded");

$(document).ready(function() {
    const deleteConfirm = document.getElementById("deleteConfirm");

    $('.btn-delete').on('click', function() {
        console.log("Delete button clicked!"); // Kontrollera om detta visas i konsolen
        //const commentId = $(this).data("comment_id");
        const deleteUrl = $(this).data("delete-url"); // Hämta delete-url från data-attributet
        deleteConfirm.setAttribute('href', deleteUrl); // Sätt rätt URL på deleteConfirm-länken

         // const postSlug = $(".my-5").data("post-slug");
        // const deleteUrl = `{% url 'comment_delete' post.slug '' %}${commentId}/`; // Skapa URL för att radera kommentaren
        deleteConfirm.setAttribute('href', deleteUrl); // Sätt rätt URL på deleteConfirm-länken

        const deleteModalElement = document.getElementById("deleteModal");
        const deleteModal = new mdb.Modal(deleteModalElement);
        deleteModal.show(); // Öppnar modalen
    });
});
