var header = document.getElementById("floor-side");
var floorSelected = header.getElementsByClassName("floor-number");
var allRooms = document.querySelectorAll("g")[0];
for (var i = 0; i < floorSelected.length; i++) {
	floorSelected[i].addEventListener("click", function() {
		var current = document.getElementsByClassName("active");
		if (current.length > 0) { 
			current[0].className = current[0].className.replace(" active", "");
		}
		this.className += " active";

	});
}

function showFloor(floorNumber) {

	if(floorNumber == "floor-1" || floorNumber == "floor-m") {
		document.getElementById("floor-1-m-map").style.display = "block";
		document.getElementById("floor-2-map").style.display = "none";
		document.getElementById("floor-3-map").style.display = "none";
	} else if (floorNumber == "floor-2") {
		document.getElementById("floor-2-map").style.display = "block";
		document.getElementById("floor-1-m-map").style.display = "none";
		document.getElementById("floor-3-map").style.display = "none";
	} else {
		document.getElementById("floor-3-map").style.display = "block";
		document.getElementById("floor-1-m-map").style.display = "none";
		document.getElementById("floor-2-map").style.display = "none";
	}

}

function showDetail(roomNumber , roomstatus) {

	document.getElementById("close-detail").style.display = "block";
	var roomNumberID = document.getElementById("room-number");
	var statusID = document.getElementById("status");
	var datetime = document.getElementsByClassName("datetime");
	
	roomNumberID.innerHTML = roomNumber;
	statusID.innerHTML = roomstatus;
	
	for(i=0;i<datetime.length; i++) {
		datetime[i].style.display = "block";
	}
	roomNumberID.style.display = "block";
	statusID.style.display = "block";

	var status = statusID.innerText;
	
	document.getElementById("eiei").value = roomNumber;
	document.getElementById("detail-box").style.width = "40%";
	document.getElementById("detail-box").style.height = "55vh";
	



}

function exit() {
	document.getElementById("close-detail").style.display = "none";
	document.getElementById("room-number").style.display = "none";
	var datetime = document.getElementsByClassName("datetime");
	for(i=0;i<datetime.length; i++) {
		datetime[i].style.display = "block";
	}
	document.getElementById("status").style.display = "none";
	document.getElementById("detail-box").style.width = "0%";
	document.getElementById("detail-box").style.height = "0%";
}