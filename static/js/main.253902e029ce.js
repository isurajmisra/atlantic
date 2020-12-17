//$(function () {
//    $("#datepicker").datepicker({
//          autoclose: true,
//          todayHighlight: true
//    }).datepicker('update', new Date());
//  });
//function datepickerShow(){
//    $("#date-div").css("display","block");
//}

//function datepickerHide(){
//  $("#date-div").css("display","none");
//}

function travelUpToShow(){
  $("#travelUpTo").css("display","block")
}
function travelUpToHide(){
  $("#travelUpTo").css("display","none")
}

$(function () {
  $("#51").click(function () {
  if ($(this).is(":checked")) {
    $("#travelUpTo").css("display","block");
  } else {
  $("#travelUpTo").css("display","none");
  }
});
  });
//import { subjectList } from '.addSubject.js';
//const { subjectList } = require('./addSubject.js')
$(function(){
  $("#submitQuestions").click(function(e) {
    var allChecked = true;
      e.preventDefault();
      data = {}
      if($('#questionPage').length){
      var t = $('#questionPage').val();
      data['userType'] = t;
      }

      if($("#pincode").length){
      let pincode = $("#pincode");
      if (pincode.val().length == 6 && pincode.hasClass('form-control is-valid'))
      {
        data['pincode'] = pincode.val();
        $("#pincodeErrorMsg").css("display","none");
      }
      else{
        allChecked = false;
        $("#pincodeErrorMsg").css("display","inline-block");
      }
      }

      if($("#age").length){
      if($("#age").val().length==2){
        data["age"] =$("#age").val();
        $("#ageErrorMsg").css("display","none");
      }
      else{
        allChecked = false;
        $("#ageErrorMsg").css("display","inline-block");
      }
      }
      if($("#searchSubject").length){
      if(subjectList.length){
      data['subject'] = subjectList ;
      data['subject'] = subjectList ;
      }
      else{
      allChecked = false;
        $("#subjectErrorMsg").css("display","inline-block");
      }
      }
       if($("#gradesRadio").length){
       if($("input[name='grades']").is(":checked")){
       data['grades'] = $("input[name='grades']:checked").val();
       $("#gradesErrorMsg").css("display","none");
       }
       else{
       allChecked = false;
       $("#gradesErrorMsg").css("display","inline");
       }
       }
        if($("#gradesCheckbox").length){
       if($("input[name='grades']").is(":checked")){
       grades = []
        $("input[name='grades']:checked").each(function(){
        grades.push($(this).val());
        });
        data['grades']=grades;
       $("#gradesErrorMsg").css("display","none");
       }
       else{
       allChecked = false;
       $("#gradesErrorMsg").css("display","inline");
       }
       }
       if($("#edBoard").length){
       if($("#edBoard :selected").val() !== ''){
       data['edBoard'] = $("#edBoard option:selected").val();
       $("#edBoardErrorMsg").css("display","none");
       }
       else{
       allChecked = false;
       $("#edBoardErrorMsg").css("display","inline");
       }
       }

//      if($("#reason").length){
//      if($("input[name='reason']").is(":checked")){
//      if($("#14").is(":checked")){
//      var text = $("#reasonText").val();
//      data["reason"] = text;
//      $("#reasonErrorMsg").css("display","none");
//      }
//      else{
//        data["reason"] = $("input[name='reason']:checked").val()
//        $("#reasonErrorMsg").css("display","none");
//      }
//      }
//      else{
//        allChecked = false;
//        $("#reasonErrorMsg").css("display","inline-block");
//      }
//      }
//
//      if($("#time").length){
//      if($("input[name='time']").is(":checked")){
//        data["time"] = $("input[name='time']:checked").val()
//        $("#timeErrorMsg").css("display","none");
//      }
//      else{
//        allChecked = false;
//        $("#timeErrorMsg").css("display","inline-block");
//      }
//      }
//
//      if($("#session").length){
//      if($("input[name='session']").is(":checked")){
//        data["session"] = $("input[name='session']:checked").val()
//        $("#sessionErrorMsg").css("display","none");
//      }
//      else{
//        allChecked = false;
//        $("#sessionErrorMsg").css("display","inline-block");
//      }
//      }
//
//      if($("#joiningDate").length){
//      if($("input[name='joiningDate']").is(":checked")){
//      if($("#44").is(':checked')){
//      var dateObject = $("#datepicker").datepicker('getDate')
//       data["joiningDate"] = dateObject;
//       $("#joiningDateErrorMsg").css("display","none");
//      }
//      else{
//       data["joiningDate"] = $("input[name='joiningDate']:checked").val()
//        $("#joiningDateErrorMsg").css("display","none");
//      }
//
//      }
//      else{
//        allChecked = false;
//        $("#joiningDateErrorMsg").css("display","inline-block");
//      }
//      }

      if($("#howToMeet").length){
      if($("input[name='howToMeet']").is(":checked")){

          if($("#51").is(":checked")){
          data['tutorPlace'] = true;
          data['willingToTravel']=$("#willingToTravel").val();
          }
           if($("#52").is(":checked")){
          data['myPlace']=true;
          }
          if($("#53").is(":checked")){
          data['onlineTutoring']=true;
          }
        $("#howToMeetErrorMsg").css("display","none");
      }
      else{
        allChecked = false;
        $("#howToMeetErrorMsg").css("display","inline-block");
      }
      }
//       if($("#anythingElse").length){
//       data['anythingElse'] = $("#anythingElse").val();
//       }

      if (allChecked == true)
      {
        fetch('/forward_request/', {
          method: "POST",
          body: JSON.stringify(data),
          headers: {"Content-type": "application/json; charset=UTF-8",
          "X-CSRFToken": $("[name='csrfmiddlewaretoken']").val()}
        })
        .then(response => response.json()).then(response=>{
        console.log(response.message);
        if (response['user'] == "True"){
        window.location = "/new_request/";
        }
        else{
           window.location = "/registration/";
        }


        })

        .catch(err => console.log(err));
     
      }
      else{
        allChecked = true;
        return false
      }

  })
})
function checkError(){
    if($("input[name='howToMeet']").is(":checked")){
    $("#howToMeetErrorMsg").css("display","none");
    }
    if($("input[name='grades']").is(":checked")){
    $("#gradesErrorMsg").css("display","none");
    }
}



var subjects = ["All Subjects", "Maths", "English", "Physics", "Science", "Chemistry", "Hindi",
 "Calculus", "Algebra", "Geometry", "Mechanical", "Computer",
 "Music", "Law", "Fine-Arts", "Dancing", "Engineering", "Sports", "Business",
  "Language", "English Speaking", "English Grammar", "English Literature", "Hindi Grammar", "Sanskrit", "Urdu", "Punjabi", "Biology", "Botany",
  "Agriculture", "Commerce", "History", "Computer Science"]
function autocomplete(inp, arr) {
  /*the autocomplete function takes two arguments,
  the text field element and an array of possible autocompleted values:*/
  var currentFocus;
  /*execute a function when someone writes in the text field:*/
  inp.addEventListener("input", function(e) {
      var a, b, i, val = this.value;
      /*close any already open lists of autocompleted values*/
      closeAllLists();
      if (!val) { return false;}
      currentFocus = -1;
      /*create a DIV element that will contain the items (values):*/
      a = document.createElement("DIV");
      a.setAttribute("id", this.id + "autocomplete-list");
      a.setAttribute("class", "autocomplete-items");
      /*append the DIV element as a child of the autocomplete container:*/
      this.parentNode.appendChild(a);
      /*for each item in the array...*/
      for (i = 0; i < arr.length; i++) {
        /*check if the item starts with the same letters as the text field value:*/
        if (arr[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
          /*create a DIV element for each matching element:*/
          b = document.createElement("DIV");
          /*make the matching letters bold:*/
          b.innerHTML = "<strong>" + arr[i].substr(0, val.length) + "</strong>";
          b.innerHTML += arr[i].substr(val.length);
          /*insert a input field that will hold the current array item's value:*/
          b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
          /*execute a function when someone clicks on the item value (DIV element):*/
              b.addEventListener("click", function(e) {
              /*insert the value for the autocomplete text field:*/
              inp.value = this.getElementsByTagName("input")[0].value;
              /*close the list of autocompleted values,
              (or any other open lists of autocompleted values:*/
              closeAllLists();
          });
          a.appendChild(b);
        }
      }
  });
  /*execute a function presses a key on the keyboard:*/
  inp.addEventListener("keydown", function(e) {
      var x = document.getElementById(this.id + "autocomplete-list");
      if (x) x = x.getElementsByTagName("div");
      if (e.keyCode == 40) {
        /*If the arrow DOWN key is pressed,
        increase the currentFocus variable:*/
        currentFocus++;
        /*and and make the current item more visible:*/
        addActive(x);
      } else if (e.keyCode == 38) { //up
        /*If the arrow UP key is pressed,
        decrease the currentFocus variable:*/
        currentFocus--;
        /*and and make the current item more visible:*/
        addActive(x);
      } else if (e.keyCode == 13) {
        /*If the ENTER key is pressed, prevent the form from being submitted,*/
        e.preventDefault();
        if (currentFocus > -1) {
          /*and simulate a click on the "active" item:*/
          if (x) x[currentFocus].click();
        }
      }
  });
  function addActive(x) {
    /*a function to classify an item as "active":*/
    if (!x) return false;
    /*start by removing the "active" class on all items:*/
    removeActive(x);
    if (currentFocus >= x.length) currentFocus = 0;
    if (currentFocus < 0) currentFocus = (x.length - 1);
    /*add class "autocomplete-active":*/
    x[currentFocus].classList.add("autocomplete-active");
  }
  function removeActive(x) {
    /*a function to remove the "active" class from all autocomplete items:*/
    for (var i = 0; i < x.length; i++) {
      x[i].classList.remove("autocomplete-active");
    }
  }
  function closeAllLists(elmnt) {
    /*close all autocomplete lists in the document,
    except the one passed as an argument:*/
    var x = document.getElementsByClassName("autocomplete-items");
    for (var i = 0; i < x.length; i++) {
      if (elmnt != x[i] && elmnt != inp) {
      x[i].parentNode.removeChild(x[i]);
    }
  }
}
/*execute a function when someone clicks in the document:*/
document.addEventListener("click", function (e) {
    closeAllLists(e.target);
});
}
var tags = document.getElementById("tags")
if(tags){
autocomplete(tags, subjects);
}

$(function() {
        $(".zip-form").submit(function(e){
        e.preventDefault();
        var q = $("#tags").val()
        if(subjects.includes(q)){
        fetch(`/search?q=${q}`, {
          method: "GET",
        })
        .then(response => response.json()).then(response=>{
        console.log(response.message);
        window.location = "/request/";
        })
        .catch(err => console.log(err));
        }
        else{
        return
        }
        });
    });



function appendSearch(){
    $("#searchDiv").css("display","flex");
    $("#buttonDiv").css("display","none");
}