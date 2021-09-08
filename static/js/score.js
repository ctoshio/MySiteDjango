var total = 0;

function dealcard() {
  total = Math.floor(Math.random() * 1000001);
  document.getElementById('playerscards').value = total;
  document.getElementById('btn1').disabled = true;
}