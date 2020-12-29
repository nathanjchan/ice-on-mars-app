var searchButton = document.getElementById("searchButton");
var searchText1 = document.getElementById("searchText1");
var searchText2 = document.getElementById("searchText2");
var searchText3 = document.getElementById("searchText3");

check();

searchButton.onclick = function() {
  while (true) {
    if (searchText1.style.display == "none") {
      searchText1.style.display = "block";
    } else {
      searchText1.style.display = "none";
    }
    setTimeout(check, 1000);
    if (searchText2.style.display == "none") {
      searchText2.style.display = "block";
    } else {
      searchText2.style.display = "none";
    }
    setTimeout(check, 1000);
    if (searchText3.style.display == "none") {
      searchText3.style.display = "block";
    } else {
      searchText3.style.display = "none";
    }
  }
}