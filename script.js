// Event listener to show/hide the select options when the select box is clicked
const selectBox = document.querySelector('.form-group select');
const optionsList = document.querySelector('.select-options');

selectBox.addEventListener('click', () => {
  optionsList.style.display = optionsList.style.display === 'none' ? 'block' : 'none';
});

optionsList.addEventListener('click', (event) => {
  if (event.target.tagName === 'LI') {
    selectBox.value = event.target.textContent;
    optionsList.style.display = 'none';
  }
});




