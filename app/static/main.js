function generateJoke() {
  fetch("/api/dadjoke")
    .then((response) => response.json())
    .then((data) => {
      if (data.error) {
        alert(`Failed to generate joke: ${data.error}`);
      } else {
        const jokeContainer = document.getElementById("joke-container");
        jokeContainer.innerHTML = data.joke;
      }
    })
    .catch((error) => {
      alert(`Failed to generate joke: ${error}`);
    });
}
