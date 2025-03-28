let currentMediaNum = 0;

const lastMedia = document.querySelector('.media-cards .media-card:last-child');
const maxMediaNum = Number(lastMedia.dataset.mediaNum);

document.addEventListener('click', event => {
  if(event.target.hasAttribute('data-open-media-card-dialog')){
    const dialog = document.querySelector('#media-card-dialog');
    const image = document.querySelector('#media-display__image');

    image.src = event.target.src;
    currentMediaNum = Number(event.target.dataset.mediaNum);
    dialog.style.display = 'block';
  }
});


document.addEventListener('click', event => {
  if(event.target.hasAttribute('data-close-media-card-dialog')){
    const dialog = document.querySelector('#media-card-dialog');
    dialog.style.display = 'none';
  }
});


document.addEventListener('keydown', event => {
  if(event.key === 'Escape'){
    const dialog = document.querySelector('#media-card-dialog');
    dialog.style.display = 'none';
  }
});


document.addEventListener('click', event => {
  if(event.target.hasAttribute('data-change-media-right')){
    if(currentMediaNum === maxMediaNum) return;
    currentMediaNum++;
    const newImage = document.querySelector(`[data-media-num="${currentMediaNum}"]`);
    const currentImage = document.querySelector('#media-display__image');
    currentImage.src = newImage.src;
  }
});

document.addEventListener('click', event => {
  if(event.target.hasAttribute('data-change-media-left')){
    if(currentMediaNum === 1) return;
    currentMediaNum--;
    const newImage = document.querySelector(`[data-media-num="${currentMediaNum}"]`);
    const currentImage = document.querySelector('#media-display__image');
    currentImage.src = newImage.src;
  }
});