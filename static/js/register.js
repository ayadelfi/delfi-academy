var infos =  document.getElementById('info');
if (infos != null){
	window.alert("اسم المستخدم مستعمل من قبل")
}
var infoss =  document.getElementById('infos');
if (infoss != null){
	window.alert("تأكد من وجود الحساب")
}
console.log(infos);
function GEEKFORGEEKS() {
	var username = document.forms["RegForm"]["username"];
	var phone = document.forms["RegForm"]["phone"];
	var password1= document.forms["RegForm"]["password1"];
	var password2= document.forms["RegForm"]["password2"];
    

	if (username.value == "") {
		window.alert("أدخل اسم المستخدم رجاء");
		username.focus();
		return false;
	}

	if (phone.value == "") {
		window.alert(
		  "أدخل رقم الهاتف رجاء");
		phone.focus();
		return false;
	}

	if (password1.value == "") {
		window.alert("أدخل كلمة السر");
		password1.focus();
		return false;
	}
	if (password2.value == "") {
		window.alert("أكد كلمة السر");
		password2.focus();
		return false;
	}
	if (password2.value !== password1.value) {
		window.alert("كلمات السر غير متطابقة");
		password2.focus();
		return false;
	}
	



	return true;
}
