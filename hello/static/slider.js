var longitudeSlider = document.getElementById("longitudeSlider");
var latitudeSlider = document.getElementById("latitudeSlider");
var longitudeValue = document.getElementById("longitudeValue");
var latitudeValue = document.getElementById("latitudeValue");

longitudeValue.innerHTML = longitudeSlider.value;
latitudeValue.innerHTML = latitudeSlider.value;

var x = document.getElementById("x");
x.style.position = "absolute";
x.style.top = "50%"
x.style.left = "50%"
x.style.transform = "translate(-50%, -60%)";

longitudeSlider.oninput = function() {
    longitudeValue.innerHTML = this.value;
    if (this.value > 180) {
        x.style.left = ((this.value - 180) / 360) * 100 + "%";
    } else {
        x.style.left = ((this.value + 180) / 360) * 100 + "%";
    }
}

latitudeSlider.oninput = function() {
    latitudeValue.innerHTML = this.value;
    x.style.top = (-(this.value - 90) / 180) * 100 + "%";
}