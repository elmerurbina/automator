document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("main");
    const successMessage = document.getElementById("success_message");

    form.addEventListener("submit", function (e) {
        e.preventDefault(); 

        const phoneNumber = document.getElementById("phone_number").value;
        const message = document.getElementById("message").value;
        const hour = document.getElementById("hour").value;
        const minute = document.getElementById("minute").value;

        if (phoneNumber && message && hour >= 1 && hour <= 24 && minute >= 0 && minute <= 59) {
            successMessage.style.display = "block";

            
            const formData = new FormData(form);

            console.log(formData);

            fetch('/send_message', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    alert('Message scheduled successfully!');
                } else {
                    alert('Error scheduling message.');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred.');
            });

        } else {
            successMessage.style.display = "none";
        }
    });
});