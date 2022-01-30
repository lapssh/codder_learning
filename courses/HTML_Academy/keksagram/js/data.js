import {getRandomNumber} from "./util.js";

const MIN_LIKES = 15;
const MAX_LIKES = 200;

const NAMES = [
  'Ираид',
  'Валентин',
  'Олeг',
  'Мариан',
  'Игорь',
  'Анастас',
  'Агафон',
  'Михаил',
  'Алексей',
];

const SURNAMES = [
  'Берлунов',
  'Папанов',
  'Ювелев',
  'Юхтриц',
  'Куксов',
  'Турбин',
  'Мухоморов',
  'Афонин',
  'Саянков',
];

const MESSAGE = [
  'Всё отлично!',
  'В целом всё неплохо. Но не всё.',
  'Когда вы делаете фотографию, хорошо бы убирать палец из кадра. В конце концов это просто непрофессионально.',
  'Моя бабушка случайно чихнула с фотоаппаратом в руках и у неё получилась фотография лучше.',
  'Я поскользнулся на банановой кожуре и уронил фотоаппарат на кота и у меня получилась фотография лучше.',
  'Лица у людей на фотке перекошены, как будто их избивают. Как можно было поймать такой неудачный момент?!',
];

const DESCRIPTION = [
  'На кити щербацкой, который устраивала его содействовало: его сторонником.',
  'Приехал на свободу пред ним, и землевладельца, которые он будет женат.',
  'Сказал, стояло на свободу пред ним, и потому.',
  'Заявить свои права на стороне нынешнего успеха.',
  'Вронский; для того, чтобы не от русских виноторговцев.',
  'Эпизоды выборов так заняло его, что, кроме этого шального господина, женатого.',
  'Просто и потому, что ему кучу ни к чему нейдущих.',
  'Послал дарье александровне телеграмму такого милого тона.',
  'Баллотироваться, – простые, ровные ко всем отношения.',
  'Злобой наговорил ему кучу ни к будущему.',
];

function generateComments(numberOfComments) {
  const commentsPull = [];
  for (let i = 0; i < numberOfComments; i++) {
    let randomComment =
      {
        id: getRandomNumber(MIN_LIKES, MAX_LIKES),
        avatar: 'img/avatar-' + getRandomNumber(1, 6) + '.svg',
        message: MESSAGE[getRandomNumber(0, MESSAGE.length - 1)],
        name: NAMES[getRandomNumber(0, NAMES.length - 1)] + ' '
          + SURNAMES[getRandomNumber(0, SURNAMES.length - 1)]
      }
    commentsPull.push(randomComment);
  }

  return commentsPull;
}


function generateImages(numberOfImages) {
  const createPhotoDescription = [];
  for (let id = 1; id <= numberOfImages; id++) {
    createPhotoDescription.push({
      id: id,
      url: `photos/${id}.jpg`,
      description: DESCRIPTION[getRandomNumber(0, DESCRIPTION.length - 1)],
      likes: getRandomNumber(MIN_LIKES, MAX_LIKES),
      comments: generateComments(getRandomNumber(1, 20)),
    });
  }
  return createPhotoDescription;
}
export {generateImages};
