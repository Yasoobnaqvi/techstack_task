document.addEventListener('DOMContentLoaded', function () {
    // Load user email from session
    const userEmail = sessionStorage.getItem('userEmail');
    if (userEmail) {
        document.getElementById('user-email').innerText = userEmail;
    }

    // Load products on page load
    loadProducts();
});

function loadProducts() {
    fetch('/api/products/')
        .then(response => response.json())
        .then(products => displayProducts(products));
}

function displayProducts(products) {
    const table = document.getElementById('product-table');
    table.innerHTML = ''; // Clear previous content

    // Create table header
    const headerRow = table.insertRow();
    ['ID', 'Name', 'Description', 'Price', 'Available Stock'].forEach(headerText => {
        const th = document.createElement('th');
        th.textContent = headerText;
        headerRow.appendChild(th);
    });

    // Create table rows
    products.forEach(product => {
        const row = table.insertRow();
        ['id', 'name', 'description', 'price', 'available_stock'].forEach(fieldName => {
            const cell = row.insertCell();
            cell.textContent = product[fieldName];
        });
    });
}

function searchProducts() {
    const searchInput = document.getElementById('search-input');
    const searchQuery = searchInput.value;

    fetch(`/api/products/search/?search=${searchQuery}`)
        .then(response => response.json())
        .then(products => displayProducts(products));
}

function logout() {
    // Clear session data
    sessionStorage.removeItem('userEmail');
    // Redirect to logout endpoint
    window.location.href = '/accounts/logout/';
}
