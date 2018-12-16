function showReserveDetail(roomNumber , dayoftransaction , begin , end , reason , teacher , staff , resno , staff_result , teacher_result, teacher_reason, staff_reason) {
	document.getElementById("close-detail").style.display = "block";
	var roomNumberID = document.getElementById("room-number");
	var paragraph = document.getElementsByClassName("text-in-detail-box");
	var cancelBtn = document.getElementsByClassName("cancelReserve");
	document.getElementById("time-reserve").innerHTML = dayoftransaction;
	document.getElementById("date_begin").innerHTML = begin;
	document.getElementById("date_end").innerHTML = end;
	document.getElementById("reason").innerHTML = reason;
	document.getElementById("reservation").value = roomNumber;
	document.getElementById("resno").value = resno;
	document.getElementById("staff_result").innerHTML = staff_result;
	document.getElementById("teacher_result").innerHTML = teacher_result;

	if (teacher.length == 0) {
		document.getElementById("teacher").innerHTML = "ไม่มี";
	}
	else{
		document.getElementById("teacher").innerHTML = teacher;
	}
	
	if (staff.length == 0) {
		document.getElementById("staff").innerHTML = "ไม่มี";
	}
	else{
		document.getElementById("staff").innerHTML = staff;
	}
	
	if (teacher_reason.length == 0) {
		document.getElementById("teacher-approve-reason").innerHTML = "ไม่มี";
	}
	else{
		document.getElementById("teacher-approve-reason").innerHTML = teacher_reason;
	}

	if (staff_reason.length == 0) {
		document.getElementById("staff-approve-reason").innerHTML = "ไม่มี";
	}
	else{
		document.getElementById("staff-approve-reason").innerHTML = staff_reason;
	}

	roomNumberID.innerHTML = roomNumber;
	

	for(i=0;i<paragraph.length; i++) {
		paragraph[i].style.display = "block";
	}

	for(i=0;i<cancelBtn.length; i++) {
		cancelBtn[i].style.display = "block";
	}

	document.getElementById("detail-box").style.width = "50%";
	document.getElementById("detail-box").style.height = "auto";
	document.getElementById("detail-box").style.padding = "40px";
}

function exitReserveDetail() {
	document.getElementById("close-detail").style.display = "none";
	document.getElementById("room-number").style.display = "none";
	var paragraph = document.getElementsByClassName("text-in-detail-box");
	var cancelBtn = document.getElementsByClassName("cancelReserve");

	for(i=0;i<paragraph.length; i++) {
		paragraph[i].style.display = "none";
	}

	for(i=0;i<cancelBtn.length; i++) {
		cancelBtn[i].style.display = "none";
	}

	document.getElementById("detail-box").style.width = "0%";
	document.getElementById("detail-box").style.height = "0%";
	document.getElementById("detail-box").style.padding = "0";
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