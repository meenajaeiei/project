
var header = document.getElementById("floor-side");
var floorSelected = header.getElementsByClassName("floor-number");
for (var i = 0; i < floorSelected.length; i++) {
	floorSelected[i].addEventListener("click", function() {
		var current = document.getElementsByClassName("active");
		if (current.length > 0) { 
			current[0].className = current[0].className.replace(" active", "");
			floorja = this.id;
		}
		this.className += " active";

	});
}

// function showFloor(floorNumber) {
// 	console.log(floorNumber);
	// document.getElementById(floorNumber).style.display = "block";
	// if (floorNumber=="floor1") {
	// 	document.getElementById("floor1-map").style.display = "block";
	// 	document.getElementById("floorM-map").style.display = "none";
	// 	document.getElementById("floor2-map").style.display = "none";
	// 	document.getElementById("floor3-map").style.display = "none";
	// } else if (floorNumber=="floorM") {
	// 	document.getElementById("floor1-map").style.display = "none";
	// 	document.getElementById("floorM-map").style.display = "block";
	// 	document.getElementById("floor2-map").style.display = "none";
	// 	document.getElementById("floor3-map").style.display = "none";
	// } else if (floorNumber=="floor2") {
	// 	document.getElementById("floor1-map").style.display = "none";
	// 	document.getElementById("floorM-map").style.display = "none";
	// 	document.getElementById("floor2-map").style.display = "block";
	// 	document.getElementById("floor3-map").style.display = "none";
	// } else {
	// 	document.getElementById("floor1-map").style.display = "none";
	// 	document.getElementById("floorM-map").style.display = "none";
	// 	document.getElementById("floor2-map").style.display = "none";
	// 	document.getElementById("floor3-map").style.display = "block";
	// }
// }

function showDetail(roomNumber) {
	document.getElementById("close-detail").style.display = "block";
	var roomNumberID = document.getElementById("room-number");
	var statusID = document.getElementById("status");
	var reservationID = document.getElementById("reservation");
	
	roomNumberID.innerHTML = roomNumber;
	roomNumberID.style.display = "block";
	statusID.style.display = "block";
	reservationID.style.display = "block";

	var status = statusID.innerText;
	if(status == "unavilable") {
		reservationID.disabled = true;
	}
	
	document.getElementById("detail-box").style.width = "40%";
	document.getElementById("detail-box").style.height = "50vh";
	



}

function exit() {
	document.getElementById("close-detail").style.display = "none";
	document.getElementById("room-number").style.display = "none";
	document.getElementById("status").style.display = "none";
	document.getElementById("reservation").style.display = "none";
	document.getElementById("detail-box").style.width = "0%";
	document.getElementById("detail-box").style.height = "0%";
}