document.addEventListener('click', event => {
  if(event.target.hasAttribute("data-open-media-card-dialog")){
    const dialog = document.querySelector('#media-card-dialog');
    const image = document.querySelector('#media-display__image');

    image.src = event.target.src;
    dialog.style.display = 'block';
  }
});


document.addEventListener('click', event => {
  if(event.target.hasAttribute("data-close-media-card-dialog")){
    const dialog = document.querySelector('#media-card-dialog');
    console.log('Works?');
    dialog.style.display = 'none';
  }
});


document.addEventListener('keydown', event => {
  if(event.key === 'Escape'){
    const dialog = document.querySelector('#media-card-dialog');
    dialog.style.display = 'none';
  }
});