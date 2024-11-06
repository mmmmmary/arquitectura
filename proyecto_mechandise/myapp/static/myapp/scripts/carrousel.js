let currentSlide = 0;

// Cambia al slide anterior
function prevSlide() {
  const slides = document.querySelectorAll(".slide");
  currentSlide = (currentSlide === 0) ? slides.length - 1 : currentSlide - 1;
  updateSlidePosition();
}

// Cambia al siguiente slide
function nextSlide() {
  const slides = document.querySelectorAll(".slide");
  currentSlide = (currentSlide === slides.length - 1) ? 0 : currentSlide + 1;
  updateSlidePosition();
}

// Actualiza la posición de los slides
function updateSlidePosition() {
  const slidesContainer = document.querySelector(".slides");
  slidesContainer.style.transform = `translateX(-${currentSlide * 100}%)`;
}

// Inicia el carrusel en el primer slide
updateSlidePosition();

