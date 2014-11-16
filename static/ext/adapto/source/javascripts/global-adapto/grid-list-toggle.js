$(document).ready(function() {

  // For grid/list display

  var elem=$('#dataDiv');      
  $('#viewControls').on('click',function(e) {
    if ($('#listView').hasClass('active')) {
      elem.fadeOut(200, function () {
      elem.removeClass('dataList').addClass('dataGrid');
      elem.fadeIn(200);
             });      
      }
    else if($('#gridView').hasClass('active')) {
    elem.fadeOut(200, function () {
    elem.removeClass('dataGrid').addClass('dataList');
    elem.fadeIn(200);
          });         
      }
  });

}); // End Document Ready