document.addEventListener("DOMContentLoaded", function () {
    const filterDropdown = document.getElementById("filterDropdown");
    const searchInput = document.getElementById("productSearch");

    function applyFilters() {
        const selected = filterDropdown ? filterDropdown.value : "all";
        const searchTerm = searchInput ? searchInput.value.toLowerCase() : "";
        document.querySelectorAll('.cardproduct').forEach(card => {
            // Skip the Add Product card
            if (card.classList.contains('add-product-card')) return;

            const cardCategory = card.getAttribute('data-name');
            const cardName = card.querySelector("#name").textContent.toLowerCase();

            const matchesCategory = selected === "all" || cardCategory === selected;
            const matchesSearch = cardName.includes(searchTerm);

            card.style.display = (matchesCategory && matchesSearch) ? "" : "none";
        });
    }

    if (filterDropdown) {
        filterDropdown.addEventListener("change", applyFilters);
    }
    if (searchInput) {
        searchInput.addEventListener("input", applyFilters);
    }
    // Initial filter on page load
    applyFilters();
});



function confirmDelete(productId) {
    if (confirm("Are you sure you want to delete this product?")) {
        window.location.href = "products.php?delete_product=" + productId;
    }
};

const searchInput = document.getElementById("searchInput");
if (searchInput) {
    searchInput.addEventListener("keyup", function () {
        const filter = this.value.toLowerCase();

        const rows = document.querySelectorAll("table tbody tr:not([id^='edit-'])");

        rows.forEach(row => {
            const rowText = row.textContent.toLowerCase();
            const show = rowText.includes(filter);
            row.style.display = show ? "" : "none";

            const userId = row.querySelector("td")?.textContent.trim();
            const editRow = document.getElementById("edit-" + userId);
            if (editRow) editRow.style.display = "none";
        });
    });
}

document.addEventListener("DOMContentLoaded", () => {
    const productView = document.querySelector(".product-view");
    if (!productView) return;

    productView.addEventListener("click", function(e) {
        if (e.target.classList.contains("toggle-description")) {
            const button = e.target;
            const card = button.closest(".cardproduct");
            const shortDesc = card.querySelector(".short-description");
            const fullDesc = card.querySelector(".full-description");

            const isExpanded = card.classList.contains("expanded");

            if (isExpanded) {
                shortDesc.style.display = "inline";
                fullDesc.style.display = "none";
                button.textContent = "View Detail";
                card.classList.remove("expanded");
                document.querySelectorAll('.cardproduct-backdrop').forEach(b => b.remove());
            } else {
                shortDesc.style.display = "none";
                fullDesc.style.display = "inline";
                button.textContent = "Hide Detail";
                card.classList.add("expanded");
                // Add backdrop
                const backdrop = document.createElement('div');
                backdrop.className = 'cardproduct-backdrop';
                backdrop.onclick = function() {
                    card.classList.remove("expanded");
                    shortDesc.style.display = "inline";
                    fullDesc.style.display = "none";
                    button.textContent = "View Detail";
                    backdrop.remove();
                };
                document.body.appendChild(backdrop);
            }
        }
    });
});

document.addEventListener("DOMContentLoaded", function () {
    const productView = document.querySelector(".product-view");

    document.querySelectorAll(".cardproduct .stars button").forEach(button => {
        button.addEventListener("click", function () {
            const originalCard = this.closest(".cardproduct");

            // Blur background
            productView.classList.add("blurred");

            // Clone card and display as modal
            const focusedCard = originalCard.cloneNode(true);
            focusedCard.classList.add("focused-product");

            // Replace button with Close functionality
            const focusBtn = focusedCard.querySelector(".stars button");
            focusBtn.textContent = "Close";
            focusBtn.addEventListener("click", function () {
                document.body.removeChild(focusedCard);
                productView.classList.remove("blurred");
            });

            document.body.appendChild(focusedCard);
        });
    });
});

// plugin.js
document.addEventListener("DOMContentLoaded", function() {
    const categorySelect = document.getElementById('categorySelect');
    const subCategorySelect = document.getElementById('subCategorySelect');
    const currentSubCategory = window.currentSubCategory || "";

    const subCategories = {
        "PC Components": [
            "Processors",
            "Motherboards",
            "Memory Modules",
            "Graphics Cards",
            "Storage SSD & HDD",
            "PC Cases",
            "Power Supply"
        ],
        "Peripherals": [
            "Headsets",
            "Mice",
            "Keyboards",
            "Monitors"
        ],
        "Desktops": [
            "Intel",
            "AMD"
        ],
        "Laptops": [
            "Intel",
            "AMD"
        ]
    };

    function populateSubCategories(category) {
        subCategorySelect.innerHTML = "";
        (subCategories[category] || []).forEach(function(sub) {
            const option = document.createElement("option");
            option.value = sub;
            option.textContent = sub;
            if (sub === currentSubCategory) option.selected = true;
            subCategorySelect.appendChild(option);
        });
    }

    // Initial population
    populateSubCategories(categorySelect.value);

    // Update sub-categories when category changes
    categorySelect.addEventListener("change", function() {
        // When changing category, clear currentSubCategory so first option is selected
        window.currentSubCategory = "";
        populateSubCategories(this.value);
    });
});

// Add this to your JS (e.g., at the end of pccomponent.php or in plugin.js)
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.add-to-cart-btn').forEach(function(btn) {
        btn.addEventListener('click', function() {
            const product_id = this.getAttribute('data-product-id');
            const product_name = this.getAttribute('data-product-name');
            const photo_name = this.getAttribute('data-photo-name');
            const price = this.getAttribute('data-price');

            fetch('cart_actions.php', {
                method: 'POST',
                headers: {'Content-Type': 'application/x-www-form-urlencoded'},
                body: `add_to_cart=1&product_id=${encodeURIComponent(product_id)}&product_name=${encodeURIComponent(product_name)}&photo_name=${encodeURIComponent(photo_name)}&price=${encodeURIComponent(price)}`
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Optional: Show a notification
                    showPopupNotification('Added to cart!');
                } else {
                    alert('Failed to add to cart.');
                }
            });
        });
    });

    // Optional: Popup notification
    function showPopupNotification(message) {
        let popup = document.createElement('div');
        popup.className = 'popup-notification show';
        popup.innerHTML = `<i class="fa fa-check-circle"></i> <span>${message}</span>`;
        document.body.appendChild(popup);
        setTimeout(() => {
            popup.classList.remove('show');
            setTimeout(() => popup.remove(), 300);
        }, 1500);
    }
});

document.addEventListener("DOMContentLoaded", function () {
    // Show edit row when Edit is clicked
    document.querySelectorAll('.editBtn').forEach(function(btn) {
        btn.addEventListener('click', function() {
            const userId = btn.getAttribute('data-id');
            // Hide all edit rows first
            document.querySelectorAll("tr[id^='edit-']").forEach(row => row.style.display = "none");
            // Show the selected edit row
            const editRow = document.getElementById('edit-' + userId);
            if (editRow) editRow.style.display = "";
        });
    });

    // Hide edit row when Cancel is clicked
    document.querySelectorAll('.cancelBtn').forEach(function(btn) {
        btn.addEventListener('click', function() {
            const userId = btn.getAttribute('data-id');
            const editRow = document.getElementById('edit-' + userId);
            if (editRow) editRow.style.display = "none";
        });
    });
});

document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll('.location-name').forEach(function(loc) {
        loc.addEventListener('click', function() {
            const mapUrl = this.getAttribute('data-map');
            const mapFrame = document.getElementById('dynamic-map');
            if (mapUrl && mapFrame) {
                mapFrame.src = mapUrl;
            }
        });
    });
});

// Handle ng collapsible sections sa plus thing
        document.querySelectorAll('.faq-question, .terms-question, .privacy-question').forEach(question => {
            question.addEventListener('click', () => {
                const item = question.parentElement;
                item.classList.toggle('active');
            });
        });