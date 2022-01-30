import {showFullSize} from "./fullsize.js";
function showThumbnails(thumbnails) {
  const pictures = document.querySelector('.pictures');
  const templateFragment = document.querySelector('#picture');
  const template = templateFragment.content.querySelector(".picture");
  const fragment = document.createDocumentFragment();
  for (let thumbnail = 0; thumbnail < thumbnails.length; thumbnail++) {
    const element = template.cloneNode(true);
    const url = thumbnails[thumbnail].url;
    element.querySelector('img').src = thumbnails[thumbnail].url;
    element.querySelector('.picture__likes').textContent = thumbnails[thumbnail].likes;
    element.querySelector('.picture__comments').textContent = thumbnails[thumbnail].comments.length;
    element.addEventListener('click', function (evt) {
      showFullSize(evt, element, thumbnails[thumbnail].comments, thumbnails[thumbnail]);
    })
    fragment.appendChild(element);
  }
  pictures.appendChild(fragment);
}


export {showThumbnails};
