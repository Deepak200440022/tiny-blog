const container = document.getElementById('searchForm');
const input = document.getElementById('searchInput');
const placeholder = document.getElementById('placeholder');
const icon = document.getElementById('searchIcon');

function updatePlaceholderVisibility() {
  placeholder.classList.toggle('hidden', input.value.trim() !== '');
}

function updateVisualState() {
  const isEmpty = input.value.trim() === '';
  updatePlaceholderVisibility();

  if (container.classList.contains('active')) {
    input.style.color = 'black';
  } else if (container.classList.contains('submitted') && !isEmpty) {
    input.style.color = '#888';
  } else {
    input.style.color = 'black';
  }
}

function finalizeSearch() {
  if (input.value.trim() === '') return;
  container.classList.remove('active', 'hovered');
  container.classList.add('submitted');
  updateVisualState();
  input.blur();
  container.requestSubmit();
}

input.addEventListener('focus', () => {
  container.classList.add('active');
  container.classList.remove('hovered', 'submitted');
  updateVisualState();
});

input.addEventListener('keydown', (e) => {
  if (e.key === 'Enter') finalizeSearch();
});

icon.addEventListener('click', finalizeSearch);

input.addEventListener('input', updatePlaceholderVisibility);

container.addEventListener('mouseenter', () => {
  if (!container.classList.contains('active')) {
    container.classList.add('hovered');
  }
});

container.addEventListener('mouseleave', () => {
  if (!container.classList.contains('active')) {
    container.classList.remove('hovered');
  }
});

updatePlaceholderVisibility();
