/*!
    * Start Bootstrap - SB Admin v6.0.0 (https://startbootstrap.com/templates/sb-admin)
    * Copyright 2013-2020 Start Bootstrap
    * Licensed under MIT (https://github.com/BlackrockDigital/startbootstrap-sb-admin/blob/master/LICENSE)
    */
    (function($) {
    "use strict";

    // Add active state to sidbar nav links
    var path = window.location.href; // because the 'href' property of the DOM element is the absolute path
        $("#layoutSidenav_nav .sb-sidenav a.nav-link").each(function() {
            if (this.href === path) {
                $(this).addClass("active");
            }
        });

    // Toggle the side navigation
    $("#sidebarToggle").on("click", function(e) {
        e.preventDefault();
        $("body").toggleClass("sb-sidenav-toggled");
    });
})(jQuery);



function ageCalculate(){
    //document.getElementById('age').InnerHtml
  // document.getElementById("demo").InnerHtml=4+5;
   //document.write="Hi";
   var geboortedatum =document.getElementById('geboortedatum').value;

//if(geboortedatum==""){
  //  alert("Choose correct geboortedatum.")
//}else{
  //  alert(geboortedatum);
  //  alert(Date());
    var d = new Date(geboortedatum);

   // document.getElementById("age").innerHTML = d;

//}

        var mdate = geboortedatum.toString();
        var yearThen = parseInt(mdate.substring(0,4), 10);
        var monthThen = parseInt(mdate.substring(5,7), 10);
        var dayThen = parseInt(mdate.substring(8,10), 10);
        
        var today = new Date();
        var birthday = new Date(yearThen, monthThen-1, dayThen);
     //   alert(today.valueOf() + " " + birthday.valueOf());
        var differenceInMilisecond = today.valueOf() - birthday.valueOf();
      //  alert(differenceInMilisecond);
        
        var year_age = Math.floor(differenceInMilisecond / 31536000000);
        var day_age = Math.floor((differenceInMilisecond % 31536000000) / 86400000);
        
        if ((today.getMonth() == birthday.getMonth()) && (today.getDate() == birthday.getDate())) {
            alert("Happy B'day!!!");
        }
        
        var month_age = Math.floor(day_age/30);
        
        day_age = day_age % 30;
        
        var tMnt= (month_age + (year_age*12));
        var tDays =(tMnt*30) + day_age;
        
        if (isNaN(year_age) || isNaN(month_age) || isNaN(day_age)) {
            document.getElementById("leeftijd").innerHTML = ("Invalid birthday - Please try again!");
        }
        else {
            document.getElementById("leeftijd").value = year_age;
        }

}