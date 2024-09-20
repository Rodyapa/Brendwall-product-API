document.getElementById('product-form').addEventListener('submit', async function(event) {
    event.preventDefault(); // Prevent the default form submission

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
window.onload = loadProducts;