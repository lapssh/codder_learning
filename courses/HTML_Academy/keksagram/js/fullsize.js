const COMMENTS_STEP = 5;

const bigPicture = document.querySelector('.big-picture');
const bigPictureImg = bigPicture.querySelector('.big-picture__img');
const bigPictureCancel = bigPicture.querySelector('.big-picture__cancel');
// const submitSend = document.querySelector('.img-upload__submit');

const likes = document.querySelector('.likes-count');
const description = document.querySelector('.social__caption');
let socialComments = document.querySelector('.social__comments');
const pageBody = document.querySelector('body');
let titleComments = document.querySelector('.social__comment-count'); // заголовок комментариев

const buttonLoadComments = document.querySelector(".social__comments-loader");

const renderComment = (comment) => {
    const templateComment = document.createElement("li");
    templateComment.classList.add('social__comment');
    const avatar = document.createElement("img");
    avatar.src = comment.avatar;
    avatar.alt = comment.name;
    templateComment.appendChild(avatar);
    const commentText = document.createElement("p");
    commentText.textContent = comment.message;
    templateComment.appendChild(commentText);
    socialComments.appendChild(templateComment);
};

const initComments = (evt) => {
  // обнуляем блок с комментариями
  socialComments.innerHTML = '';
};

const getNextComments = (comments) => {
  let displayedCommentsCount = socialComments.querySelectorAll('.social__comment').length;
  for (let i = displayedCommentsCount; i < displayedCommentsCount + COMMENTS_STEP; i++) {
        if (comments[i])
        {
            renderComment(comments[i]);
            // показать пипку
            buttonLoadComments.classList.remove('hidden');
        }

        else {
            // убрать пипку
            buttonLoadComments.classList.add('hidden');
        }
  }
  let numberComments = socialComments.querySelectorAll('.social__comment').length;
  titleComments.innerHTML = `${numberComments} из <span class="comments-count">${comments.length}</span> комментариев`
};


function showFullSize(evt, element, commentsList, photo) {
    // листенер на submit

    // submitSend.addEventListener('click', sendForm());

    // отключаем прокрутку главного окна
    pageBody.classList.add('modal-open');

    const target = evt.target;

    // подстановка url картинки на большом изображении
    const img = bigPictureImg.querySelector('img');
    img.src = target.src;

    // подстановка колличества лайков
    likes.textContent = element.querySelector('.picture__likes').textContent;

    // подстановка колличества комментариев
    const comments = document.querySelector('.comments-count');
    comments.textContent = element.querySelector('.picture__comments').textContent;

    // подстановка описания
    description.textContent = photo['description'];

    initComments();
    // commentsList.innerHTML = '';
    getNextComments(commentsList);

    //  вывод модального окна
    bigPicture.classList.remove('hidden');
    buttonLoadComments.addEventListener('click', () => {
        getNextComments(commentsList);
    });
    document.addEventListener('keydown', function (evt) {
        // Проверяем, что код клавиши равен 27
        if (evt.keyCode === 27) {
            bigPictiure.classList.add('hidden');

            // включаем обратно прокрутку главного окна
            document.body.classList.remove('modal-open');
        }
    });

    bigPictureCancel.addEventListener('click', function () {
        socialComments.innerHTML = '';
        commentsList ='';
        bigPicture.classList.add('hidden');
        // включаем обратно прокрутку главного окна
        document.body.classList.remove('modal-open');
    })
}

export {showFullSize};
