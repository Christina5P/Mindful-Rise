
window.addEventListener("load", function() {
    window.cookieconsent.initialise({
        palette: {
            popup: { background: "#afdbf6" },
            button: { background: "#f4f4f4" }
        },
        theme: "edgeless",
        content: {
            header: "We use cookies",
            message: "This website uses cookies to ensure you get the best experience.",
            dismiss: "I agree",
        }
    });
});
