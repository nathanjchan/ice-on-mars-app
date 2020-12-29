var longitudeSlider = document.getElementById("longitudeSlider");
var latitudeSlider = document.getElementById("latitudeSlider");
var longitudeValue = document.getElementById("longitudeValue");
var latitudeValue = document.getElementById("latitudeValue");

longitudeValue.innerHTML = longitudeSlider.value;
latitudeValue.innerHTML = latitudeSlider.value;

var x = document.getElementById("x");
x.style.position = "absolute";
x.style.top = "50%";
x.style.bottom = "50%";
x.style.transform = "translate(-50%, -50%)";

longitudeSlider.oninput = function() {
    longitudeValue.innerHTML = this.value;
}

latitudeSlider.oninput = function() {
    latitudeValue.innerHTML = this.value;
}