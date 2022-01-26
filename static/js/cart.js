console.log("home ys");
console.log("home ys")
var updateBtns = document.getElementsByClassName('update-cart')

for(var i=0 ; i<updateBtns.length ; i++){
    updateBtns[i].addEventListener('click',function(){
        var productID= this.dataset.product
        var action=this.dataset.action
        console.log('productID' ,productID,'action', action)
        console.log('user' ,user)
        if(user === 'AnonymousUser'){
            console.log('Not logged in')
            
            window.alert("عليك بتسجيل الدخول أولا ")


        }
        else{
            updateUserOrder(productID,action)
            window.alert("الدورة في السلة الأن")
            
        }
    })
}
function updateUserOrder(productID,action){
    console.log('user is logged')
    var url = '/update_item/'
    fetch(url,{
        method:'POST',
        headers:{
            'Content-type':'application/json',
            'X-CSRFToken':csrftoken

        },
        body:JSON.stringify({'productID': productID, 'action': action})
        }
    )
    .then((response) =>{
        return response.json()

    })
    .then((data) =>{
        console.log('data',data)
        location.reload()

    })
  
  
    

}