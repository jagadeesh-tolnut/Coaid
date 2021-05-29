(function ($) {
    "use strict";
    
    // Initiate the wowjs
    new WOW().init();
    
    
    // Back to top button
    $(window).scroll(function () {
        if ($(this).scrollTop() > 200) {
            $('.back-to-top').fadeIn('slow');
        } else {
            $('.back-to-top').fadeOut('slow');
        }
    });
    $('.back-to-top').click(function () {
        $('html, body').animate({scrollTop: 0}, 1500, 'easeInOutExpo');
        return false;
    });
    
    
    // Sticky Navbar
    $(window).scroll(function () {
        if ($(this).scrollTop() > 0) {
            $('.navbar').addClass('nav-sticky');
        } else {
            $('.navbar').removeClass('nav-sticky');
        }
    });
    
    
    // Dropdown on mouse hover
    $(document).ready(function () {
        function toggleNavbarMethod() {
            if ($(window).width() > 992) {
                $('.navbar .dropdown').on('mouseover', function () {
                    $('.dropdown-toggle', this).trigger('click');
                }).on('mouseout', function () {
                    $('.dropdown-toggle', this).trigger('click').blur();
                });
            } else {
                $('.navbar .dropdown').off('mouseover').off('mouseout');
            }
        }
        toggleNavbarMethod();
        $(window).resize(toggleNavbarMethod);
    });


        
})(jQuery);
window.onload = function () {
    var chart = new CanvasJS.Chart("chartContainer",
    {
      title: {
        text: "Monthly Downloads"
      },
        data: [
      {
        type: "area",
        dataPoints: [//array

        { x: new Date(2012, 00, 1), y: 2600 },
        { x: new Date(2012, 01, 1), y: 3800 },
        { x: new Date(2012, 02, 1), y: 4300 },
        { x: new Date(2012, 03, 1), y: 2900 },
        { x: new Date(2012, 04, 1), y: 4100 },
        { x: new Date(2012, 05, 1), y: 4500 },
        { x: new Date(2012, 06, 1), y: 8600 },
        { x: new Date(2012, 07, 1), y: 6400 },
        { x: new Date(2012, 08, 1), y: 5300 },
        { x: new Date(2012, 09, 1), y: 6000 }
        ]
      }
      ]
    });

    chart.render();
  }

