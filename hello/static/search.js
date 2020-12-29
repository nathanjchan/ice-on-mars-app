var searchButton = document.getElementById("searchButton");
var searchText1 = document.getElementById("searchText1");
var searchText2 = document.getElementById("searchText2");
var searchText3 = document.getElementById("searchText3");

searchButton.onclick = function() {
  while (true) {
    searchText1.style.display = "block";
    setTimeout(function(){return;}, 1000);
    searchText1.style.display = "none";
    searchText2.style.display = "block";
    setTimeout(function(){return;}, 1000);
    searchText2.style.display = "none";
    searchText3.style.display = "block";
    setTimeout(function(){return;}, 1000);
    searchText3.style.display = "none";
  }
}