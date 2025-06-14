jQuery(document).ready(function () {
  jQuery("ul#ticker01").liScroll({
    travelocity: 0.07,
  });
});

window.addEventListener('DOMContentLoaded', async (e) => {
  const wrapper = document.querySelector('[wrapper]'),
    wrapper_item = wrapper.querySelectorAll('[div]'),
    left_button = document.querySelector('[left]'),
    right_button = document.querySelector('[right]'),
    secondLeft = document.querySelector('[secondLeft]'),
    secondRight = document.querySelector('[secondRight]');

  let currentStep = 0;
  const maxStep = wrapper_item.length - 1;

  function updateTransform() {
    wrapper_item.forEach(item => {
      item.style.transform = `translateX(-${currentStep * 100}%)`;
    })
  }

  right_button.addEventListener('click', () => {
    if (currentStep < maxStep) {
      currentStep++;
      updateTransform();
    }
  });

  secondRight.addEventListener('click', () => {
    if (currentStep < maxStep) {
      currentStep++;
      updateTransform();
    }
  });

  left_button.addEventListener('click', () => {
    if (currentStep > 0) {
      currentStep--;
      updateTransform();
    }
  });

  secondLeft.addEventListener('click', () => {
    if (currentStep > 0) {
      currentStep--;
      updateTransform();
    }
  });

  updateTransform();

  const toggleBtn = document.getElementById('userToggle');
  const dropdown = document.getElementById('userDropdown');

  toggleBtn.addEventListener('click', function () {
    dropdown.classList.toggle('hidden');
  });

  // Agar boshqa joy bosilsa yopilsin
  document.addEventListener('click', function (e) {
    if (!toggleBtn.contains(e.target) && !dropdown.contains(e.target)) {
      dropdown.classList.add('hidden');
    }
  });

  
})