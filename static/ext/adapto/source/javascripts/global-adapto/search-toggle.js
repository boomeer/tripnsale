$(document).ready(function() {

  // for toggling the search bar

  $("#search").click(function() {
    $("#searchBox").slideToggle("fast");
    $("#search .ai").toggleClass("ai-close");
  });

}); // End Document Ready