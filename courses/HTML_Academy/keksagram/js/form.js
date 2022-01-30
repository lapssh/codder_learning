import {sendForm} from "./fetch.js";

const re = /^#[A-Za-zА-Яа-я0-9]{1,19}$/;
const form = document.querySelector('.img-upload__form');
const NONE_EFFECT = 'none';
const scaleValue = document.querySelector('.scale__control--value');
const scaleUp = document.querySelector('.scale__control--bigger');
const scaleDown = document.querySelector('.scale__control--smaller');
const picturePreview = document.querySelector('.img-upload__preview img');
const sliderElement = document.querySelector('.effect-level__slider');
const sliderValue = form.querySelector('.effect-level__value');
let currentEffect = ''; // в начале работы программы эффектов нет. просто объявляю переменную
const effectNames = {
    chrome: {
        name: 'grayscale',
        min: 0,
        max: 1,
        step: 0.1,
    },
    sepia: {
        name: 'sepia',
        min: 0,
        max: 1,
        step: 0.1,
    },
    marvin: {
        name: 'invert',
        min: 0,
        max: 100,
        step: 1,
        unit: '%',
    },
    phobos: {
        name: 'blur',
        min: 0,
        max: 3,
        step: 0.1,
        unit: 'px',
    },
    heat: {
        name: 'brightness',
        min: 1,
        max: 3,
        step: 0.1,
    },
};

const turnEffectLevel = (effectName) => {
    const {
        min,
        max,
        step,
        name: filterName,
        unit = '',
    } = effectNames[effectName];

    if (sliderElement.noUiSlider) {
        sliderElement.noUiSlider.off();
        sliderElement.noUiSlider.updateOptions({
            range: {
                min,
                max,
            },
            start: max,
            step,
        });
    } else {
        noUiSlider.create(sliderElement, {
            range: {
                min: 0,
                max: 1,
            },
            start: 1,
            step: 0.1,
            connect: 'lower',
            format: {
                to: (value) => {
                    if (Number.isInteger(value)) {
                        return value.toFixed(0);
                    }
                    return value.toFixed(1);
                },
                from: (value) => parseFloat(value),
            },
        });
    }

    sliderElement.noUiSlider.on('update', (_, handle, unencoded) => {
        const value = unencoded[handle];
        sliderValue.value = value;
        picturePreview.style.filter = `${filterName}(${value}${unit})`;
    });

};

const destroyEffectLevel = () => {
    if (sliderElement.noUiSlider) {
        sliderElement.noUiSlider.off();
        sliderElement.noUiSlider.destroy();
    }
    sliderValue.value = '';
    picturePreview.style.filter = '';
};

const filterChangeHandler = (evt) => {
    currentEffect = evt.target.value;
    if (evt.target.matches('.effects__radio')) {
        picturePreview.classList = `img-upload_preview effects_preview--${evt.target.value}`;
        if (currentEffect === NONE_EFFECT) {
            destroyEffectLevel();
        } else {
            turnEffectLevel(currentEffect);
        }
    }

};
const initForm = () => {
    scaleValue.value = 100 + '%';
    scaleUp.addEventListener('click', function () {
        calculateScale(scaleValue.value, 'up');
    })
    scaleDown.addEventListener('click', function () {
        calculateScale(scaleValue.value, 'down');
    })
    form.addEventListener('change', filterChangeHandler);
};


const setScale = (value) => {
    scaleValue.value = value + '%';
    picturePreview.style.transform = "scale(" + value / 100 + ")";
}


const calculateScale = (value, button) => {
    let intValue = Number(value.replace('%', ''));
    if (button === 'up') {
        intValue += 25;

    }
    if (button === 'down') {
        intValue -= 25;
    }
    if (intValue > 100) {
        intValue = 100
    }
    if (intValue < 25) {
        intValue = 25
    }
    setScale(intValue);
}

const setDefaultForm = () => {
    console.log('устанавливаем значения по-умолчанию');
    setScale(100);
}


const openModalForm = () => {
    setDefaultForm();

    document.querySelector('.img-upload__overlay').classList.remove('hidden');
    document.querySelector('body').classList.add('modal_open');


};

const closeModalForm = () => {
    document.querySelector('.img-upload__overlay').classList.add('hidden');
    document.querySelector('body').classList.remove('modal_open');

};


const setElementError = (element, errorMessage) => {
    console.log('вызвана setElementError');
    if (errorMessage) {
        element.classList.add('text__invalid');
    } else {
        element.classList.remove('text__invalid');
    }
    element.setCustomValidity(errorMessage);
    element.reportValidity();
}

const validateHashtags = (evt, hashtagsArea) => {
    console.log('валидация хэш-тега: ', hashtagsArea);
    let customValidityError = []; // описание ошибок
    // разбиваем текстовый  ввод на отдельные хэш-теги через пробел
    let hashtags = hashtagsArea.split(' ');
    console.log(hashtags);

    // ПРОВЕРКА №1 - нельзя указать больше пяти хэш-тегов;
    if (hashtags.length > 5) {
        customValidityError.push('Указано больше 5 хэш-тегов');
    }

    // ПРОВЕРКА №2 - проверка повторений хэш-тегов
    let uniqueHashTags = []
    for (let i = 0; i < hashtags.length; i++) {
        if (!hashtags[i].match(re)) {
            customValidityError.push('Хэш-тег ' + hashtags[i] + ' не прошёл валидацию');
        } else {
            if (uniqueHashTags.includes(hashtags[i].toLowerCase())) {
                customValidityError.push('Хэш-тег ' + hashtags[i] + ' встретился больше одного раза');
            }
            uniqueHashTags.push(hashtags[i].toLowerCase());
        }
    }
    const hashtagForm = document.querySelector('.text__hashtags');
    setElementError(hashtagForm, customValidityError);
    console.log(customValidityError);

}

const validateForm = (evt) => {
    evt.preventDefault();
    console.log('запущена форма валидации');
    // валидация комментариев

    const hashtagsArea = document.querySelector('.text__hashtags');
    hashtagsArea.value = '#ghbdtn #hello #ХэшТег2 #сказачноебали';
    validateHashtags(evt, hashtagsArea.value);
}

const formImg = document.querySelector('.img-upload__start');
formImg.addEventListener('click', function () {
    openModalForm();
})

const formClose = document.querySelector('.img-upload__cancel');
formClose.addEventListener('click', function () {
    closeModalForm();
})

const submit = document.querySelector('.img-upload__submit');
submit.addEventListener('click', function (evt) {
    // validateForm(evt);
    // evt.preventDefault();
    // sendForm();
    console.log('базовая отправка формы');
})

export {initForm};
