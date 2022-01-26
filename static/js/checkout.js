
console.log('hello ritel')
function checkout(){
    var name = document.forms["form"]["name"];
	var phone = document.forms["form"]["phone"];
	var reçu= document.forms["form"]["reçu"];

    if (reçu.value == "") {
		window.alert("أدخل صورة وصل الدفع رجاء");
		reçu.focus();
		return false;
	}
    else{
        
        window.alert("تمت العملية بنجاح سيتم تفعيل الدورات بعد التأكد من الوصل");
        location.reload()
    }
   
}