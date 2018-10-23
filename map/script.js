function showDetail(roomNumber) {

	document.getElementById("close-detail").style.display = "block";
	var roomNumberID = document.getElementById("room-number");
	var statusID = document.getElementById("status");
	var datetime = document.getElementsByClassName("datetime");
	var buttonID = document.getElementById("reserve");
	roomNumberID.innerHTML = roomNumber;
	
	for(i=0;i<datetime.length; i++) {
		datetime[i].style.display = "inline-block";
	}
	roomNumberID.style.display = "inline-block";
	statusID.style.display = "inline-block";
	buttonID.style.display = "block";
	var status = statusID.innerText;

	document.getElementById("detail-box").style.width = "45%";
	document.getElementById("detail-box").style.height = "62vh";


}

function exit() {
	document.getElementById("close-detail").style.display = "none";
	document.getElementById("room-number").style.display = "none";
	var datetime = document.getElementsByClassName("datetime");
	for(i=0;i<datetime.length; i++) {
		datetime[i].style.display = "none";
	}
	document.getElementById("status").style.display = "none";
	document.getElementById("reserve").style.display = "none";
	document.getElementById("detail-box").style.width = "0%";
	document.getElementById("detail-box").style.height = "0%";
}

function clickAccept() {
	var checkBox = document.getElementById("acceptCondition");
	var confirmBtn = document.getElementById("confirmReserve");
	if (checkBox.checked == false){
    	confirmBtn.style.pointerEvents = "none";
    	confirmBtn.style.background = "gray";
  	} else {
  		confirmBtn.style.pointerEvents = "visible";
    	confirmBtn.style.background = "#28a745";
  	}
}
