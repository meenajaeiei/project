// var slideIndex = 1;
// showDivs(slideIndex);

// function plusDivs(n) {
//   showDivs(slideIndex += n);
// }

// function currentDiv(n) {
//   showDivs(slideIndex = n);
// }

// function showDivs(n) {
//   var i;
//   var x = document.getElementsByClassName("mySlides");
//   var dots = document.getElementsByClassName("demo");
//   if (n > x.length) {slideIndex = 1}    
//   if (n < 1) {slideIndex = x.length}
//   for (i = 0; i < x.length; i++) {
//      x[i].style.display = "none";  
//   }
//   for (i = 0; i < dots.length; i++) {
//      dots[i].className = dots[i].className.replace(" w3-white", "");
//   }
//   x[slideIndex-1].style.display = "block";  
//   dots[slideIndex-1].className += " w3-white";
// }

function showDetail(roomNumber , roomstatus) {

	document.getElementById("close-detail").style.display = "block";
	var roomNumberID = document.getElementById("room-number");
	var statusID = document.getElementById("status");
	var datetime = document.getElementsByClassName("datetime");
	var buttonID = document.getElementById("reserve");
	document.getElementById("demo").value =  roomNumber;
	roomNumberID.innerHTML = roomNumber;
	statusID.innerHTML = roomstatus;
	
	for(i=0;i<datetime.length; i++) {
		datetime[i].style.display = "inline-block";
	}
	roomNumberID.style.display = "inline-block";
	statusID.style.display = "inline-block";
	buttonID.style.display = "block";
	var status = statusID.innerText;

	document.getElementById("detail-box").style.width = "40%";
	document.getElementById("detail-box").style.height = "55vh";

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

