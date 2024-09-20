document.addEventListener('DOMContentLoaded', () => {
    const productForm = document.getElementById('product-form');
    const errorContainer = document.createElement('div');
    errorContainer.classList.add('alert', 'alert-danger', 'mb-4');
    productForm.parentNode.insertBefore(errorContainer, productForm.nextSibling);
    errorContainer.style.display = 'none'; // Hide the error container initially

    productForm.addEventListener('submit', async function(event) {
        event.preventDefault(); // Prevent the default form submission

        // Clear previous error message
        errorContainer.style.display = 'none';
        errorContainer.innerHTML = '';

        const formData = new FormData(this);
        const data = Object.fromEntries(formData.entries());

        try {
            const response = await fetch('/api/products/add/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            });

            if (response.ok) {
                await loadProducts(); // Reload the products after adding
                this.reset(); // Reset the form
            } else if (response.status === 400) {
                const errorData = await response.json();
                if (errorData.non_field_errors) {
                    errorContainer.innerHTML = errorData.non_field_errors.join(', '); // Show non-field errors
                } else {
                    const fieldErrors = Object.entries(errorData);
                    const messages = fieldErrors.map(([field, messages]) => `${field}: ${messages.join(', ')}`);
                    errorContainer.innerHTML = messages.join('<br>'); // Show field-specific errors
                }
                errorContainer.style.display = 'block'; // Show the error message
            } else {
                const errorData = await response.json();
                console.error('Error adding product:', errorData);
            }
        } catch (error) {
            console.error('Error:', error);
        }
    });

    async function loadProducts() {
        const response = await fetch('/api/products/list');
        const products = await response.json();

        const productBody = document.getElementById('product-body');
        productBody.innerHTML = ''; // Clear the table

        products.forEach(product => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${product.title}</td>
                <td>${product.description}</td>
                <td>${product.price}</td>
            `;
            productBody.appendChild(row);
        });
    }

    // Load products when the page loads
    loadProducts();
});