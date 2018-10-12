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
	console.log(floorNumber);

	//set all block map to gray
	for(i=0; i<allRooms.childElementCount; i++){
		allRooms.children[i].style.fill = "gray";
		allRooms.children[i].style.pointerEvents = "none";
	}

	//set selected floor to change color active
	var floor = document.getElementsByClassName(floorNumber);
	for(i=0; i<floor.length; i++) {
		floor[i].style.fill = "#ffbacd";
		floor[i].style.pointerEvents = "auto";
	}

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
		reservationID.click(false);
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