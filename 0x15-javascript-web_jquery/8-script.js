// This JQuery code fetches and lists the title for all movies by using this URL: https://swapi-api.alx-tools.com/api/films/?format=json
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
    $('UL#list_movies').append(...data.results.map(movie => `<li>${movie.title}</li>`));
});
