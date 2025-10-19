const API_KEY = 'YOUR_API_KEY_HERE';  // ჩასვით თქვენი TMDb API გასაღები
const BASE_URL = 'https://api.themoviedb.org/3';
const IMG_BASE = 'https://image.tmdb.org/t/p/w200';

async function fetchMovies() {
  const url = `${BASE_URL}/movie/popular?api_key=${API_KEY}&language=en-US&page=1`;
  const response = await fetch(url);
  if (!response.ok) {
    throw new Error('Წვდომა API-ზე ვერ ხერხდება');
  }
  const data = await response.json();
  return data.results;
}

async function displayMovies() {
  try {
    const movies = await fetchMovies();
    const container = document.getElementById('movies-container');
    movies.forEach(movie => {
      const div = document.createElement('div');
      div.className = 'movie';
      div.innerHTML = `
        <img src="${IMG_BASE + movie.poster_path}" alt="${movie.title}" />
        <div class="movie-details">
          <h2 class="movie-title">${movie.title}</h2>
          <p class="movie-overview">${movie.overview}</p>
        </div>
      `;
      container.appendChild(div);
    });
  } catch (error) {
    console.error('ფილმების ჩვენება ვერ მოხერხდა:', error);
  }
}

displayMovies();
