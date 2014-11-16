// Global Scripts for theme demo

$(document).ready(function() {
  "use strict";


  // ====================================================================================
  // ------------------------------------------
  // Widget toggle
  // ------------

  // check and persist widget state
  if($.cookie('style-widget-state') === 'true') { 
    $('.style-widget').addClass('style-toggle-show');
    $('.style-tab').removeClass('ai-cogs');
    $('.style-tab').addClass('ai-arrow-left5');
  };
  // toggle widget
  $('.style-tab').on('click', function() {
    $(".style-widget").toggleClass("style-toggle-show");
    $.cookie('style-widget-state', $('.style-widget').hasClass('style-toggle-show'), {expires:365, path: '/'});
    $(this).toggleClass("ai-cogs ai-arrow-left5");
    return false;
  });

  // ====================================================================================
  // ------------------------------------------
  // Theme schemes
  // -------------

  // check for stylesheet cookie and set if present
  if($.cookie('css')){
      checkAndSetThemeScheme()
  }; // END if

  
  // toggle active stylesheet
  $('.theme-scheme-btn').on('click', function(e){
      e.preventDefault();

      var newStyle = ($(this).attr('rel'));
      // make absolute url
      var newStyle = newStyle.replace(/\W\../g, '');
      // set root for demo, else for root
      if (window.location.host == "pixelandkraft.com") {
        var newStyle = ("/" + "adapto/demo/" + newStyle);
      } else {
        var newStyle = ("/" + newStyle);
      };
      $('link#default-style-toggle').prop('href', newStyle);
  
      // set active class for styling preview color-chip
      var target = $('#theme-scheme-selection-wrap .color-box');
      if($(target).hasClass('color-box-activated')) { $(target).removeClass('color-box-activated') };
      $(this).addClass('color-box-activated');

      // set cookie after toggled
      $.cookie('css', newStyle, {expires:365, path: '/'});
      // create cookie for clicking correct color tile on load
      $.cookie('activatedColorScheme','#' + this.id, {expires:365, path: '/'});
      return false;
  }); // END click function


  // LIGHT/DARK TOGGLE
  if($.cookie('light-or-dark')) {
    $($.cookie('light-or-dark') + '-radio').attr('checked', true);
    $('#theme-schemes-light').hide();
    $('#theme-schemes-dark').hide();
    $($.cookie('light-or-dark')).show();
    } else {
    $('#theme-schemes-dark').hide();
  }; // END if

  $('[name=light-dark-radio]').change(function(){
      $('#theme-schemes-light').delay(250).toggle('fast');
      $('#theme-schemes-dark').delay(250).toggle('fast');
      // set cookie on toggle state
      $.cookie('light-or-dark', '#theme-schemes-' + this.value, {expires:365, path: '/'});
      
      var cookie = $.cookie('light-or-dark');
      // activate default style on toggle based on cookie
      if ( cookie === '#theme-schemes-light' ) {
          makeLight();
      } else if ( cookie === '#theme-schemes-dark' ) { 
          makeDark();
      };
  }) // END change function


  function checkAndSetThemeScheme() {
     var cssCookie = ($.cookie('css'));
      $('link#default-style-toggle').attr('href', cssCookie);

      var target = $('#theme-scheme-selection-wrap .color-box');
      var targetDiv = $($.cookie('activatedColorScheme'));

      if(target.hasClass('color-box-activated')) { target.removeClass('color-box-activated'); }
      targetDiv.addClass('color-box-activated');
  }; // END checkAndSetThemeScheme

  function makeDark() { $('#dark-color-blue-scheme-square').trigger('click'); };
  function makeLight() { $('#light-color-blue-scheme-square').trigger('click'); };

  // ====================================================================================
  // ------------------------------------------
  // Background noise toggle and options
  // -------------

  // hide by default bg noise options
  $('#bg-noise-options').hide('fast');

  // show/hide background noise options
  $("input[name$='bg-noise-toggle']").change(function(){
    var target = $('#bg-noise-options');

    if($("#bg-noise-off").is(':checked')){
      target.hide('fast');
    } else {
      target.show('fast');
    };

    // toggle cookie state true/false on div shown/hidden
    $.cookie('bg-noise-state', $("#bg-noise-on").is(':checked'), {expires:365, path: '/'});
    
  });

  // handle checkboxes
  $('input[name="bg-noise-option[]"]').on('change', function() {
    
    // toggle bg-noise class on check/uncheck
    var targetClass = $(this).attr('data-at');
    $('.' + targetClass).toggleClass('bg-noise');

    var check_array = [];
    // add to array
    $(':checked').each(function() {
        check_array.push($(this).attr('data-at'));
    });
    // stringify array object
    check_array = JSON.stringify(check_array);

    // set cookie
    $.cookie('chk_ar', check_array, {expires:365, path:'/'});

  });

  if( $.cookie('bg-noise-state') === 'true' ) {
    $('#bg-noise-on').trigger('click');
    checkBgNoise(); // initiate function to set bg noise checkboxes if cookie true
  };

  // call function 
  $("input[name$='bg-noise-toggle']").change(checkBgNoise);

  // create function
  function checkBgNoise() {

    // check for bg-noise array cookie here since both states need the value - exit if it's undefined
    var chk_ar = $.cookie('chk_ar');
    if (chk_ar == undefined) return;

    // check background noise option state,
    // if true, click 'on' to activate
    // then add classes and check checkboxes

    if( $.cookie('bg-noise-state') === 'true' ) {
      $('#bg-noise-on').trigger('click');

      // convert string to object
      chk_ar = $.parseJSON(chk_ar);

      // loop through and apply checks to matching sets
      $.each(chk_ar, function(index, value) {
        // add bg-noise class for activated areas
        $('.' + value).addClass('bg-noise');
        // check those areas
        $('input').filter('[data-at="'+value+'"]').prop('checked', true);
      });

    } else if ( $.cookie('bg-noise-state') === 'false' ) {

      // remove classes when selecting 'off'
      chk_ar = $.parseJSON(chk_ar);
      $.each(chk_ar, function(index, value) {
        // remove bg-noise added on toggling off noise
        $('.' + value).removeClass('bg-noise');
        // uncheck the boxes
        $('input').filter('[data-at="'+value+'"]').prop('checked', false);
      });      
    };

  }; // end function checkBgNoise


  // =========================================================================
  // ------------------------------------------
  // Toggle extra-header sizes
  // -------------

  // check if cookie is set
  if($.cookie('extra-header')){
    $('.extra-header').removeClass('header-hidden');
    $('.extra-header').addClass($.cookie('extra-header'));
    $($.cookie('extra-header-select-id')).prop('checked', true); // add selection to input with cookie value
    $('.extra-header').toggleClass('header-hidden', $('#headerOptionDefault').is(':checked'));
  };

  // extra-header function
  $('.trigger').on('change', function () {
    
    // hide/show header on default 'off' option
    $('.extra-header').toggleClass('header-hidden', $('#headerOptionDefault').is(':checked'));
    
    // cycle through options
    $('.trigger').each(function() {
      $('.extra-header').toggleClass('header-' + this.value, this.checked);
    });
    
    // set cookies, one for extra-header class and one for input value
    $.cookie('extra-header','header-' + this.value, {expires:365, path: '/'});
    $.cookie('extra-header-select-id', '#' + this.id, {expires:365, path: '/'});
  });


  // ====================================================================================
  // ------------------------------------------
  // Toggle header content options on header 
  // size selection
  // --------------

  // check if extra header is not off
  if($('#headerOptionDefault').is(':checked')){
    $('#extra-header-content-wrap').hide();
  } else {
    $('#extra-header-content-wrap').show();
  };

  $("input[name$='headerChoice']").change(function (){
    var target = $('#extra-header-content-wrap');
    if($("#headerOptionDefault").is(':checked')){
      target.hide('fast');
    } else {
      target.show('fast');
    }
  });

  // toggle extra-header content 
  $("input[name$='extra-header-content']").change(function() {
    $('.extra-header-' + $(this).val()).toggleClass('header-hidden');

        
    // if(('.extra-header-' + $(this).val()) == )
     // TODO: to get working --> $.cookie('extra-header-content', ('.extra-header-' + $(this).val()), {expires:365, path: '/'})
     // think i need to loop through the selection and save each one to a unique cookie
  });


  // ====================================================================================
  // ------------------------------------------
  // Boxed / Wide toggles
  // -------------
    
  // header & footer
  // ---

  // toggle
  $("input[name$='hfWidth']").change(function() {
    
      // make sure body is boxed
      if( $.cookie('body-boxed') !== 'true' ){
        $("#styleWidthBoxed").trigger('click'); // click 'wide' body
      };
    
      $('.site-footer, .header, .extra-header').toggleClass('boxed');
      $.cookie('footer-header-boxed', $('.site-footer, .header, .extra-header').hasClass('boxed'), {expires:365, path: '/'});  
    
  }); // end change function

  // check for state using cookie
  if($.cookie('footer-header-boxed') === 'true') { 
    $("#hfBoxed").trigger('click'); // click "boxed" header/footer
  };


  // body
  // ---
  
  // toggle
  $("input[name$='styleWidth']").change(function() {
  
      // turn off header & footer boxed when on
      if( $.cookie('footer-header-boxed') === 'true' ){
        $("#hfWide").trigger('click'); // click "wide" header/footer    
      };      

      $('.page-wrap').toggleClass('boxed'); 
      $.cookie('body-boxed', $('.page-wrap').hasClass('boxed'), {expires:365, path: '/'});

  }); // end change function

  // check for state using cookie
  if($.cookie('body-boxed') === 'true') { 
    $("#styleWidthBoxed").trigger('click');    
  };
  



  // ====================================================================================
  // ------------------------------------------
  // Space (on body) Toggles
  // -------------

  // call spaceToggled function on change
  //$('input[name$="spaceToggle"]').on('change', spaceToggleFunction );

  // toggle on change
  $('input[name$="spaceToggle"]').change(function() {

      var $body = $('body');
      var $tc = $(this).attr("data-ClassToToggle");

      // create an array for storing values in cookie to acces on page load for triggering click on the right radio
      // var $radioAndClass = [
      //     { 'radioClicked' : this.value, },
      // ];

      // if body is not checked, trigger click
      if( $.cookie('footer-header-boxed') !== 'true' && this.value !== 'spaceToggleOff' ){
          $("#hfBoxed").trigger('click'); // click "wide" header/footer
          $("#styleWidthBoxed").trigger('click'); // click "wide" body
      }; // end if

      function removeBoth() { 
          $body.removeClass('body-space-top body-space-bottom'); 
      }; // end function removeBoth

      // call function to remove classes
      removeBoth();

      // if selection is not 'off' - add classes
      if( this.value !== 'spaceToggleOff' ){ ($body).addClass($tc) };

      // if off - remove classes
      if( this.value === 'spaceToggleOff' ){ removeBoth() };

      // COOKIE SECTION
      // if selection is not 'off' - create cookie
      if( this.value !== 'spaceToggleOff' ) {
          // set cookie with the radio and class stored (as an array in a variable - that's why it has to be converted to a string here first, as cookies can only store strings)
          //$.cookie('spaceAdded', JSON.stringify($radioAndClass), {expires:365, path: '/'});

          $.cookie('spaceAdded', '#' + this.value, {expires:365, path: '/'});
      } // else remove cookie
      else {
          $.removeCookie('spaceAdded', {path: '/'});
      };

  });

  // check cookie on doc ready (remember this is already nested in doc ready) and trigger click if present
  if ( $.cookie('spaceAdded') ){
      var spaceCookie = $.cookie('spaceAdded');
      $(spaceCookie).trigger('click');
  };



  // ====================================================================================
  // ------------------------------------------
  // Boxed bg toggles
  // -------------

  // color
  var lastBgColor = "";

  if($.cookie('boxed-bg-color')){ 
    var cookie = $.cookie('boxed-bg-color');
    $('body').removeClass(lastBgColor).addClass(cookie);
    $('[data-id="'+cookie+'"]').addClass('color-box-activated');
  };

  $('.boxedBgSwitch').on('click', function(e){
      e.preventDefault();
      var $this = $(this);
      var target = $('#boxed-bg-color-selections .color-box');
      var bgClass = $this.data("id");

      // make sure 'boxed' is selected
      if($('#styleWidthWide').is(':checked')){
        $('#styleWidthBoxed').trigger('click');
      }

      // set active class for styling preview color-chip
      if($(target).hasClass('color-box-activated')) { $(target).removeClass('color-box-activated') };
      $this.addClass('color-box-activated');

      // if cookie remove already present class
      if($.cookie('boxed-bg-color')){ 
        $('body').removeClass($.cookie('boxed-bg-color')).addClass(bgClass);
      // else remove empty class (for cycle) and add selected
      } else {
        $('body').removeClass(lastBgColor).addClass(bgClass);
        lastBgColor = bgClass;
      };

      $.cookie('boxed-bg-color', bgClass, {expires:365, path: '/'})
  });

  // image
  var lastBgImg = "";

  if($.cookie('boxed-bg-image')){ 
    var patternCookie = $.cookie('boxed-bg-image');
    $('body').removeClass(lastBgImg).addClass(patternCookie);
    $('[data-id="'+patternCookie+'"]').addClass('color-box-pattern-activated');
  };

  $('.boxedBgImgSwitch').on('click', function(e){
      e.preventDefault();
      var $this = $(this);
      var target = $('#boxed-pattern-selections .color-box');
      var bgClass = $this.data("id");

      // make sure 'boxed' is selected
      if($('#styleWidthWide').is(':checked')){
        $('#styleWidthBoxed').trigger('click');
      }

      // set active class for styling preview color-chip
      if($(target).hasClass('color-box-pattern-activated')) { $(target).removeClass('color-box-pattern-activated') };
      $this.addClass('color-box-pattern-activated');
      
      // if cookie remove already present class
      if($.cookie('boxed-bg-image')){ 
        $('body').removeClass($.cookie('boxed-bg-image')).addClass(bgClass);
      // else remove empty class (for cycle) and add selected
      } else {
        $('body').removeClass(lastBgImg).addClass(bgClass);
        lastBgImg = bgClass;
      };

      $.cookie('boxed-bg-image', bgClass, {expires:365, path: '/'})
  });


  // ====================================================================================
  // ------------------------------------------
  // Show/Hide Core Widget Divs
  // -------------
  // toggle functionality added via data attributes
  // in the html. Create a cookie here to give it memory

  $('#style-widget [data-toggle="collapse"]').on('click', function() {

    if( $(this).has('[data-target="#wide-or-boxed-wrap"]') && 
        $(window).width()<1200 &&
        (!$(this).hasClass('expanded')) && // this checks for it NOT having the class 'expanded'
        $.cookie('alert-has-been-shown') !== 'true'

      ){ 
          alert("                          *** AHOY! ***\n
Your browser window must be wider to see the changes made with the site layout settings!\n\n
How large, exactly?\n
1200 pixels or wider.\n
(note: this is simply an initially warning and will not be shown again)");
          // create cookie to keep message from showing again
          $.cookie('alert-has-been-shown', ('true'), {expires:3, path: '/'})
    }; // end alert notice


    // toggle div class
    $(this).toggleClass('expanded collapsed');

    // call function to store value
    storeState();
  });

  function storeState() {
      var check_open_divs = [];
      var toggled_div = $('#style-widget [data-toggle="collapse"]:not(.collapsed)');

      // add to array
      $(toggled_div).each(function() {
        check_open_divs.push($(this).attr('data-target'));
      });
      // stringify array object
      check_open_divs = JSON.stringify(check_open_divs);

      // set cookie
      $.cookie('toggled-div-state', check_open_divs, {expires:365, path: '/'});
  }; // END function storeState

  // persist state of toggled open divs
  if( $.cookie('toggled-div-state') ) {
      activateDivStates();
  };

  function activateDivStates() {
    if( $.cookie('toggled-div-state') ) {
      
      var toggled_divs = ($.cookie('toggled-div-state'));

      toggled_divs = $.parseJSON(toggled_divs);

      $.each(toggled_divs, function(index, value) {
        $(this).collapse('show'); // 'this' here targets the ID 
        // now use string concatenation to target the data-target
        $('[data-target="'+value+'"]').removeClass('collapsed');
        $('[data-target="'+value+'"]').addClass('expanded');
      });
    };
  }; // END function activateDivStates
  function resetDivStates() {
    if( $.cookie('toggled-div-state') ) {
      var toggled_divs = ($.cookie('toggled-div-state'));

      toggled_divs = $.parseJSON(toggled_divs);

      $.each(toggled_divs, function(index, value) {
        $('[data-target="'+value+'"]').removeClass('expanded');
        $('[data-target="'+value+'"]').addClass('collapsed');
        $(this).collapse('hide'); // 'this' here targets the ID 
      });
    };
  }; // END function resetDivStates









  // ------------------------------------------
  // Reset button
  // -------------

  $('.resetThemeStyle').on('click', function (e){
    e.preventDefault();

    $('#defaultThemeScheme').trigger('click'); // click default stylesheet
    $('#theme-schemes-light-radio').prop('checked', true); // check defaults
    $('#theme-schemes-dark').hide();
    $('#theme-schemes-light').show(); // reset theme scheme choices
    $('#bg-noise-off').trigger('click'); // programmaticly resets all bgs
    $('.page-wrap').removeClass('bg-noise');
    $('#headerOptionDefault').trigger('click'); // click "off" for extra header
    $("#hfWide").trigger('click'); // click "wide" header/footer
    $("#styleWidthWide").trigger('click'); // click "wide" body
    
    $.removeCookie('extra-header', {path: '/'});
    $('.extra-header').addClass('header-hidden');
    $("input[name$='extra-header-content']").removeAttr('checked'); // remove all
    $(".extra-header ul").not('ul.extra-header-default-content').addClass('header-hidden'); // hide non-default header content
    $("ul.extra-header-default-content").removeClass('header-hidden'); // if header was hidden on customization, remove header-hidden class
    $('.default-extra-header-input').prop('checked', true); // check defaults
    $('body').removeClass(); // clear all classes added to body
    $('#boxed-bg-color-selections .color-box').removeClass('color-box-activated');
    $('#boxed-pattern-selections .color-box').removeClass('color-box-pattern-activated');

    $('#spaceToggleOff').trigger('click');

    // delete cookies
    $.removeCookie('chk_ar', {path:'/'});
    $.removeCookie('activatedColorScheme', {path:'/'});
    $.removeCookie('light-or-dark', {path: '/'});
    $.removeCookie('body-boxed', {path: '/'});
    $.removeCookie('footer-header-boxed', {path: '/'});
    $.removeCookie('spaceAdded', {path: '/'});
    $.removeCookie('boxed-bg-color', {path: '/'});
    $.removeCookie('boxed-bg-image', {path: '/'});

    makeLight(); // for reseting back to the light color scheme
    resetDivStates(); // calls function to close toggled open divs
    $.removeCookie('toggled-div-state', {path:'/'});

  });

  // top reset btn tooltip
  $('#resetWidgetMessage').tooltip();

  
}); // End Document Ready
/*!
 * jQuery Cookie Plugin v1.4.0
 * https://github.com/carhartl/jquery-cookie
 *
 * Copyright 2013 Klaus Hartl
 * Released under the MIT license
 */
(function (factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD. Register as anonymous module.
    define(['jquery'], factory);
  } else {
    // Browser globals.
    factory(jQuery);
  }
}(function ($) {

  var pluses = /\+/g;

  function encode(s) {
    return config.raw ? s : encodeURIComponent(s);
  }

  function decode(s) {
    return config.raw ? s : decodeURIComponent(s);
  }

  function stringifyCookieValue(value) {
    return encode(config.json ? JSON.stringify(value) : String(value));
  }

  function parseCookieValue(s) {
    if (s.indexOf('"') === 0) {
      // This is a quoted cookie as according to RFC2068, unescape...
      s = s.slice(1, -1).replace(/\\"/g, '"').replace(/\\\\/g, '\\');
    }

    try {
      // Replace server-side written pluses with spaces.
      // If we can't decode the cookie, ignore it, it's unusable.
      s = decodeURIComponent(s.replace(pluses, ' '));
    } catch(e) {
      return;
    }

    try {
      // If we can't parse the cookie, ignore it, it's unusable.
      return config.json ? JSON.parse(s) : s;
    } catch(e) {}
  }

  function read(s, converter) {
    var value = config.raw ? s : parseCookieValue(s);
    return $.isFunction(converter) ? converter(value) : value;
  }

  var config = $.cookie = function (key, value, options) {

    // Write
    if (value !== undefined && !$.isFunction(value)) {
      options = $.extend({}, config.defaults, options);

      if (typeof options.expires === 'number') {
        var days = options.expires, t = options.expires = new Date();
        t.setDate(t.getDate() + days);
      }

      return (document.cookie = [
        encode(key), '=', stringifyCookieValue(value),
        options.expires ? '; expires=' + options.expires.toUTCString() : '', // use expires attribute, max-age is not supported by IE
        options.path    ? '; path=' + options.path : '',
        options.domain  ? '; domain=' + options.domain : '',
        options.secure  ? '; secure' : ''
      ].join(''));
    }

    // Read

    var result = key ? undefined : {};

    // To prevent the for loop in the first place assign an empty array
    // in case there are no cookies at all. Also prevents odd result when
    // calling $.cookie().
    var cookies = document.cookie ? document.cookie.split('; ') : [];

    for (var i = 0, l = cookies.length; i < l; i++) {
      var parts = cookies[i].split('=');
      var name = decode(parts.shift());
      var cookie = parts.join('=');

      if (key && key === name) {
        // If second argument (value) is a function it's a converter...
        result = read(cookie, value);
        break;
      }

      // Prevent storing a cookie that we couldn't decode.
      if (!key && (cookie = read(cookie)) !== undefined) {
        result[name] = cookie;
      }
    }

    return result;
  };

  config.defaults = {};

  $.removeCookie = function (key, options) {
    if ($.cookie(key) !== undefined) {
      // Must not alter options, thus extending a fresh object...
      $.cookie(key, '', $.extend({}, options, { expires: -1 }));
      return true;
    }
    return false;
  };

}));
