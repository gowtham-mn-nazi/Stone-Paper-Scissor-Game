let win = 0, loss = 0, draw = 0;

function playGame(choice) {
  fetch('/play', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ choice: choice })
  })
  .then(response => response.json())
  .then(data => {
    document.getElementById('user-choice').textContent = data.user;
    document.getElementById('computer-choice').textContent = data.computer;
    document.getElementById('result-text').textContent = data.result;

    // Update counters
    if (data.result.includes("win")) {
      win++;
    } else if (data.result.includes("lose")) {
      loss++;
    } else {
      draw++;
    }

    // Display counts
    document.getElementById('win-count').textContent = win;
    document.getElementById('loss-count').textContent = loss;
    document.getElementById('draw-count').textContent = draw;
  });
}