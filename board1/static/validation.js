function validateForm() {
    var firstName = document.getElementById("first_name").value;
    var lastName = document.getElementById("last_name").value;
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    var phoneNumber = document.getElementById("phone_number").value;

    // Check if any field is empty
    if (firstName.trim() === '' || lastName.trim() === '' || email.trim() === '' || password.trim() === '' || phoneNumber.trim() === '') {
        alert("All fields are required");
        return false;
    }

    // Check if email is in a valid format
    var emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(email)) {
        alert("Please enter a valid email address");
        return false;
    }

    // All validations passed
    return true;
}
