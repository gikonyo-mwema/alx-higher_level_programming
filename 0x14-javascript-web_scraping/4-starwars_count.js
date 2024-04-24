#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, function (error, response, body) {
  if (error) {
    console.error('Error:', error);
    return;
  }
  const films = JSON.parse(body).results;
  let count = 0;
  films.forEach(film => {
    film.characters.forEach(character => {
      if (character.endsWith('/18/')) {
        count++;
      }
    });
  });
  console.log(count);
});
