function showDetail(roomNumber , roomstatus) {

	document.getElementById("close-detail").style.display = "block";
	var roomNumberID = document.getElementById("room-number");
	var statusID = document.getElementById("status");
	var datetime = document.getElementsByClassName("datetime");
	var buttonID = document.getElementById("reserve");
	var paragraph = document.getElementsByClassName("text-in-detail-box");
	document.getElementById("demo").value =  roomNumber;

	for(i=0;i<paragraph.length; i++) {
		paragraph[i].style.display = "block";
	}

	roomNumberID.innerHTML = roomNumber;
	statusID.innerHTML = roomstatus;
	
	for(i=0;i<datetime.length; i++) {
		datetime[i].style.display = "inline-block";
	}

	
	roomNumberID.style.display = "block";
	statusID.style.display = "inline-block";
	buttonID.style.display = "block";
	var status = statusID.innerText;

	document.getElementById("detail-box").style.width = "40%";
	document.getElementById("detail-box").style.height = "59vh";

}

function exit() {
	document.getElementById("close-detail").style.display = "none";
	document.getElementById("room-number").style.display = "none";
	var paragraph = document.getElementsByClassName("text-in-detail-box");
	var datetime = document.getElementsByClassName("datetime");

	for(i=0;i<paragraph.length; i++) {
		paragraph[i].style.display = "none";
	}

	for(i=0;i<datetime.length; i++) {
		datetime[i].style.display = "none";
	}
	document.getElementById("status").style.display = "none";
	document.getElementById("reserve").style.display = "none";
	document.getElementById("detail-box").style.width = "0%";
	document.getElementById("detail-box").style.height = "0%";
}



function showReserveDetail(roomNumber) {
	document.getElementById("close-detail").style.display = "block";
	var roomNumberID = document.getElementById("room-number");
	var paragraph = document.getElementsByClassName("text-in-detail-box");
	roomNumberID.innerHTML = roomNumber;

	for(i=0;i<paragraph.length; i++) {
		paragraph[i].style.display = "block";
	}

	document.getElementById("detail-box").style.width = "45%";
	document.getElementById("detail-box").style.height = "auto";
}

function exitReserveDetail() {
	document.getElementById("close-detail").style.display = "none";
	document.getElementById("room-number").style.display = "none";
	var paragraph = document.getElementsByClassName("text-in-detail-box");

	for(i=0;i<paragraph.length; i++) {
		paragraph[i].style.display = "none";
	}

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


