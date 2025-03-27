document.addEventListener('click', event => {
  if(event.target.hasAttribute("data-open-media-card-dialog")){
    const dialog = document.querySelector('#media-card-dialog');
    dialog.showModal();
  }
});