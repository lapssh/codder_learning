import {showThumbnails} from "./thumbnail.js";
import {generateImages} from "./data.js";
const IMG_NUMBER = 25;

let thumbnails = generateImages(IMG_NUMBER);

const serverUrl = "https://23.javascript.pages.academy/kekstagram/data";
function getImages() {
    fetch(serverUrl)
        .then((response) => response.json()
        .then((data) => {
        // console.log('взял с сервера: ',data);
        showThumbnails(data);
        // return data;
        }))
        .catch((err) => {
            alert('Извините, сервер в данный момент не доступен');
            showThumbnails(generateImages(IMG_NUMBER));
        });


};

function sendForm() {
    console.log('начинаю отправку формы');
    const sendUrl = 'https://23.javascript.pages.academy/kekstagram';
    const params = {
        method: 'POST',
        body: 'sdfsd',
    }
    // Данные для отправки
    const form = document.querySelector('.img-upload__form');
    fetch(sendUrl, params)
        .then((response) => {
            if (response.ok) {
                console.log('ответ с сервера - НОРМ!');
            }
        throw new Error(`${response.status} — ${response.statusText}`);})
        .then((response) => response.json())
        .then((answer) => console.log(answer))
        .catch((error) => console.log(error));
        // .then((json) => {
        //     console.log('Результат отправки формы:', response);})

    // let response = fetch(sendUrl, {
    //   method: 'POST',
    //   type: 'multipart/form-data',
    //   body: new FormData(form)
    // });
    // console.log(response);
    // let result = response.json();

    // alert(result.message);

};

export {getImages, sendForm};
