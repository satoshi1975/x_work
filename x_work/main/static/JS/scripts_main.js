// var textarea = document.querySelector('textarea');

// textarea.addEventListener('keyup', function(){
//   if(this.scrollTop > 0){
//     this.style.height = this.scrollHeight + "px";
//   }
// });
const tx = document.getElementsByTagName("textarea");
for (let i = 0; i < tx.length; i++) {
  tx[i].setAttribute("style", "height:" + (tx[i].scrollHeight) + "px;overflow-y:hidden;");
  tx[i].addEventListener("input", OnInput, false);
}

function OnInput() {
  this.style.height = 0;
  this.style.height = (this.scrollHeight) + "px";
}



$(document).ready(function() {
  $("#input-b5").fileinput({showCaption: false, dropZoneEnabled: false});
});






function setScrollTrigger(element, distance) {
 var offset = element.getBoundingClientRect().top;
 
 window.addEventListener('scroll', function() {
   if (window.scrollY > offset) {
   
     element.style.position = 'fixed';
     element.style.top = 0;
   } else {
    
     element.style.position = 'absolute';
     element.style.top = 130 + 'px';
    }
  });
}

var element = document.getElementById('employer-card');
 setScrollTrigger(element, 0);
