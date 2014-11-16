$(document).ready(function() {

// For Smooth Scrolling
  // using the html-5 data-toggle to avoid conflicts with other scripts -- thus, explicitly setting a "smoothScroll" data-toggle class the links I want to smoothly scroll to their destination

  $('[data-toggle="smoothScroll"]').bind('click', function(e) {
  e.preventDefault(); //prevent the "normal" behaviour which would be a "hard" jump
        
  var target = $(this).attr("href"); //Get the target
       
  // Animated scrolling by getting top-position of target-element and set it as scroll target
  $('html, body').stop().animate({ scrollTop: $(target).offset().top}, 400, function() {
      location.hash = target;  //attach the hash (#jumptarget) to the pageurl
    });     
    return false;
  });

}); // End Document Ready