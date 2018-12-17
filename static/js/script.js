function showDetail(roomNumber , roomstatus, roomnote) {
	document.getElementById("reason").style.display = "block";
	document.getElementById("close-detail").style.display = "block";
	var roomNumberID = document.getElementById("room-number");
	var statusID = document.getElementById("status");
	var noteID = document.getElementById("room-note");
	var datetime = document.getElementsByClassName("datetime");
	var buttonID = document.getElementById("reserve");
	var paragraph = document.getElementsByClassName("text-in-detail-box");
	var select_teacher = document.getElementById("select-teacher");
	document.getElementById("demo").value =  roomNumber;

	for(i=0;i<paragraph.length; i++) {
		paragraph[i].style.display = "block";
	}

	roomNumberID.innerHTML = roomNumber;
	// if (roomstatus == "pending"){
	// 	statusID.innerHTML = roomstatus;
	// }
	// else
	statusID.innerHTML = roomstatus;
	noteID.innerHTML = roomnote;
	
	for(i=0;i<datetime.length; i++) {
		datetime[i].style.display = "inline-block";
	}

	
	roomNumberID.style.display = "block";
	statusID.style.display = "inline-block";
	buttonID.style.display = "block";
	noteID.style.display = "inline-block";
	select_teacher.style.display = "inline-block";
	if(roomstatus == "pending")
	{
		document.getElementById("reason").style.display = "none";
		buttonID.style.display = "none";
	}
	var status = statusID.innerText;

	document.getElementById("detail-box").style.width = "40%";
	document.getElementById("detail-box").style.height = "auto";
	document.getElementById("detail-box").style.padding = "40px";
}

function exit() {
	document.getElementById("reason").style.display = "none";
	document.getElementById("close-detail").style.display = "none";
	document.getElementById("room-number").style.display = "none";
	document.getElementById("select-teacher").style.display = "none";
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
	document.getElementById("detail-box").style.padding = "0";
}

