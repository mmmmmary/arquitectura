document.addEventListener('DOMContentLoaded', function () {
    // Comprobar si el header ya existe
    if (!document.querySelector('header')) {
        const headerHTML = `
            <header>
                <div class="logo">
                    <img src="/static/myapp/img/logo.png" alt="Logo" style="height: 60px;">
                </div>
                <div class="navbar-container">
                    <nav class="navbar">
                        <div class="dropdown">
                            <a href="#">Categorías</a>
                            <div class="dropdown-menu">
                                <a href="#">Géneros Musicales</a>
                                <a href="#">Bandas</a>
                                <a href="#">Épocas</a>
                            </div>
                        </div>
                        <a href="#Puntos">Puntos</a>
                        <a href="#productos">Todos los productos</a>
                        <div class="searchbar">
                            <input type="text" placeholder="Buscar...">
                            <button type="button">Buscar</button>
                        </div>
                    </nav>
                </div>
                <div class="iconos">
                    <i class="fas fa-shopping-cart"></i>
                    <div class="dropdown">
                        <i class="fas fa-user" onclick="toggleUserDropdown()"></i>
                        <div class="dropdown-menu" id="userDropdown">
                            <a href="/login/">Iniciar Sesión</a> <!-- Usa la ruta absoluta -->
                            <a href="/register/">Crear Cuenta</a>
                        </div>
                    </div>
                </div>
            </header>
        `;
        document.body.insertAdjacentHTML('afterbegin', headerHTML);
    }

    // Comprobar si el footer ya existe
    if (!document.querySelector('footer')) {
        const footerHTML = `
            <footer>
                <div class="logo">
                    <img src="/static/myapp/img/logo.png" alt="Logo" style="height: 80px;">
                </div>
                <div class="social-icons">
                    <a href="https://facebook.com" target="_blank"><i class="fab fa-facebook-f"></i></a>
                    <a href="https://twitter.com" target="_blank"><i class="fab fa-twitter"></i></a>
                    <a href="https://instagram.com" target="_blank"><i class="fab fa-instagram"></i></a>
                    <a href="https://linkedin.com" target="_blank"><i class="fab fa-linkedin-in"></i></a>
                </div>
            </footer>
        `;
        document.body.insertAdjacentHTML('beforeend', footerHTML);
    }
});

// Función para mostrar/ocultar el dropdown de usuario
function toggleUserDropdown() {
    const dropdown = document.getElementById("userDropdown");
    dropdown.classList.toggle("show"); // Alternar la clase para mostrar/ocultar
}

// Cerrar el dropdown si se hace clic fuera de él
window.onclick = function(event) {
    const dropdown = document.getElementById("userDropdown");
    if (!event.target.matches('.fas.fa-user') && !event.target.matches('.dropdown-menu a')) {
        if (dropdown.classList.contains('show')) {
            dropdown.classList.remove('show');
        }
    }
}
