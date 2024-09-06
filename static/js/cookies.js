// script for cookies alert

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
        },
  
        
        onStatusChange: function(status) {
            if (this.hasConsented()) {
            document.cookie = "authToken=token123; path=/; max-age=" + 60 * 60 * 24; 
            }
        }
    });
});


