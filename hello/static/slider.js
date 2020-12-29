var longitudeSlider = document.getElementById("longitudeSlider");
var latitudeSlider = document.getElementById("latitudeSlider");
var longitudeValue = document.getElementById("longitudeValue");
var latitudeValue = document.getElementById("latitudeValue");

longitudeValue.innerHTML = longitudeSlider.value;
latitudeValue.innerHTML = latitudeSlider.value;

var x = document.getElementById("x");
x.style.position = "absolute";
x.style.top = (((latitudeSlider.value + 90) / 180) * 100) + "%";
x.style.left = (((longitudeSlider.value - 180) / 360) * 100) + "%";
x.style.transform = "translate(-50%, -50%)";

longitudeSlider.oninput = function() {
    longitudeValue.innerHTML = this.value;
    x.style.left = (((this.value - 180) / 360) * 100) + "%";
}

latitudeSlider.oninput = function() {
    latitudeValue.innerHTML = this.value;
    x.style.top = (((this.value + 90) / 180) * 100) + "%";
}