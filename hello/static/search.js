var searchButton = document.getElementById("searchButton");
var searchText = document.getElementById("searchText");

searchButton.onclick = function() {
    if (searchText.style.display == "none") {
      searchText.style.display = "block";
    } else {
      searchText.style.display = "none";
    }
  }