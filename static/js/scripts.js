document.addEventListener("DOMContentLoaded", function () {
    const tabs = document.querySelectorAll('.tabs a');

    tabs.forEach(tab => {
        tab.addEventListener('click', function (e) {
            e.preventDefault();  // Prevent the default link action
            const url = this.getAttribute('href');

            // Fetch content dynamically (using Fetch API)
            fetch(url)
                .then(response => response.text())
                .then(html => {
                    document.querySelector('.container').innerHTML = html;
                })
                .catch(error => {
                    console.error('Error loading the page:', error);
                });
        });
    });
});