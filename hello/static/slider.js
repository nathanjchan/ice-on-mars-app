var longitudeSlider = document.getElementById("longitudeSlider");
var latitudeSlider = document.getElementById("latitudeSlider");
var longitudeValue = document.getElementById("longitudeValue");
var latitudeValue = document.getElementById("latitudeValue");

longitudeValue.innerHTML = longitudeSlider.value;
latitudeValue.innerHTML = latitudeSlider.value;

longitudeSlider.oninput = function() {
    longitudeValue.innerHTML = this.value;
}

latitudeSlider.oninput = function() {
    latitudeValue.innerHTML = this.value;
}