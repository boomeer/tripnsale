// ------------------------------------------
// GLOBAL SCRIPTS - .MIX FILE
// ---------

// Plugins - Global
@import "global-plugins/headroom.js";
@import "global-plugins/jquery.headroom.js";
@import "global-plugins/retina-1.1.0.js";
@import "global-plugins/isotope.js";
@import "global-plugins/jquery.fitvids.js";
@import "global-plugins/double-tap-to-go.js";


// Adapto Custom - Global
@import "global-adapto/search-toggle.js";
@import "global-adapto/grid-list-toggle.js";
@import "global-adapto/smooth-scroll.js";


// initializers
$(document).ready(function() {

  // ini
  $("#header").headroom({
      "tolerance": 5,
      "offset": 0,
      "classes": {
        "initial": "animated",
        "pinned": "slideUp",
        "unpinned": "slideDown",
        "top": "headroom--top",
        "notTop": "headroom--not-top"
      }
  });

  // initialize double-tap-to-go for top nav on mobile
  // TODO: put this in a media query
  $( 'ul.nav li.dropdown:has(ul), li.dropdown-submenu:has(ul)' ).doubleTapToGo();

  // initialize tool tip for anything with class of 'tooltip-link'
  $('.tooltip-link').tooltip({ 
      html: true,
      title: function() {
        return $(this).html();
      }
  });

  // animations on hover function 
  // src: http://www.telegraphicsinc.com/2013/07/how-to-use-animate-css/
  function animationHover(element, animation){
    element = $(element);
    element.hover(
        function() {
            element.addClass('animated ' + animation);         
        },
        function(){
            //wait for animation to finish before removing classes
            window.setTimeout( function(){
                element.removeClass('animated ' + animation);
            }, 2000);          
        });
  };

  // for animatting only a section of hovered elelment
  function animationHoverTwo(hoverTarget, animationTarget, animation){
    animationTarget = $(animationTarget);
    hoverTarget = $(hoverTarget);

    hoverTarget.hover(
        function() {
            animationTarget.addClass('animated ' + animation);         
        },
        function(){
            //wait for animation to finish before removing classes
            window.setTimeout( function(){
                animationTarget.removeClass('animated ' + animation);
            }, 2000);          
        });
  };

  // initiate animates on hover
  $('.logo-top').each(function() {
      animationHoverTwo('.logo-top', '.logo-top .ai', 'bounceInDown');
      animationHoverTwo('.logo-top', '.logo-top', 'rubberBand');
  });
  $('.features--feature-wrap').each(function() {
      icon = $(this).children('i.ai');
      animationHoverTwo(this, icon, 'swing');
  });


}); // End Document Ready

