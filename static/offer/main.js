function TripsRefresh()
{        
    $(".tripsList").html("Загрузка...");
    $.post("/sale/filter/", {
        "from": $("#tripsFilterFrom").val(),
        "to": $("#tripsFilterTo").val(),
    }, function(res) {
        $(".tripsList").html(res);
    });
}


$(document).ready(function() {
    $("#tripsFilterApply").on("click", function() {
        TripsRefresh();
    });
    $("#tripsFilterFrom").on("input", function() {
        TripsRefresh();
    });

    $("#allPagesWrapper").fullpage({
        verticalCentered: false,
        resize : true,
        anchors:['main', 'trips', 'buys', 'footer'],
        scrollingSpeed: 700,
        slidesNavigation: true,
        slidesNavPosition: 'bottom',
        loopBottom: false,
        loopTop: false,
        loopHorizontal: true,
        autoScrolling: true,
        scrollOverflow: false,
        css3: true,
        paddingTop: '3em',
        paddingBottom: '10px',
        normalScrollElements: '',
        normalScrollElementTouchThreshold: 5,
        keyboardScrolling: true,
        touchSensitivity: 15,
        continuousVertical: false,
        animateAnchor: true,
        sectionSelector: '.section',
        slideSelector: '.slide',
        responsive: 0,

        //events
        onLeave: function(index, nextIndex, direction){},
        afterLoad: function(anchorLink, index){},
        afterRender: function(){},
        afterResize: function(){},
        afterSlideLoad: function(anchorLink, index, slideAnchor, slideIndex){},
        onSlideLeave: function(anchorLink, index, slideIndex, direction){}
    });
});
