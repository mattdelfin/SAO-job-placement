/*function toggleCard() {
  var card = document.getElementById("cardContainer");
  if (card.style.display === "none" || card.style.display === "") {
      card.style.display = "block";
  } else {
      card.style.display = "none";
  }
}*/

function toggleCard() {
  var card = document.getElementById("cardContainer");
  console.log("Toggling card visibility"); // Debugging
  if (card.style.display === "none" || card.style.display === "") {
      card.style.display = "block";
  } else {
      card.style.display = "none";
  }
}