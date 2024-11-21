// Pega os slides e os botões
const slides = document.querySelectorAll('.slide');
const nextButton = document.getElementById('next');
const prevButton = document.getElementById('prev');

let currentIndex = 0; // Índice do slide atual

// Função para mostrar o slide baseado no índice
function showSlide(index) {
  slides.forEach((slide, i) => {
    slide.classList.toggle('ativo', i === index);
  });
}

// Evento para avançar no carrossel
nextButton.addEventListener('click', () => {
  currentIndex = (currentIndex + 1) % slides.length; // Vai para o próximo
  showSlide(currentIndex);
});

// Evento para voltar no carrossel
prevButton.addEventListener('click', () => {
  currentIndex = (currentIndex - 1 + slides.length) % slides.length; // Volta para o anterior
  showSlide(currentIndex);
});

// Inicializa o primeiro slide
showSlide(currentIndex);
