function wishList(){
    var list = document.getElementById("toast");
  list.classList.add("show");
  list.innerHTML = '<i class="far fa-heart wish"></i> Product added to List';
  setTimeout(function(){
    list.classList.remove("show");
  },3000);
}

