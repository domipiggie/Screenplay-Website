// classList - shows/gets all classes
const navToggle = document.querySelector('.nav-toggle');
const links = document.querySelector('.links');

// contains - checks classList for specific class
// add - add class
// remove - remove class
// toggle - toggles class

navToggle.addEventListener('click', () => {
  //   console.log(links.classList);
  //   console.log(links.classList.contains('links'));
  //   if (links.classList.contains('show-links')) {
  //     links.classList.remove('show-links');
  //   } else {
  //     links.classList.add('show-links');
  //   }

  //OR
  links.classList.toggle('show-links');
});