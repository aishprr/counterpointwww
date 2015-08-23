
$(document).ready(function() {

    var nav = $(".navbar");

    var navbarOpts = [
        {"scrollTo": "header", "elem": $("#header")},
        {"scrollTo": "aboutUs", "elem": $("#aboutUs")},
        {"scrollTo": "schedule", "elem": $("#schedule")},
        {"scrollTo": "contactUs", "elem": $("#contactUs")},
        {"scrollTo": "members", "elem": $("#members")},
        {"scrollTo": "join", "elem": $("#join")},
        {"scrollTo": "follow", "elem": $("#follow")}
    ];

    //at the start it is at the top 
    var selectedMenu = "header";
    //not scrolling
    var scrollingNow = false;

    $(window).scroll(function() {
        
        var scrollHeight = $(this).scrollTop();
        var middleScreenHeight = scrollHeight + ($(this).height() / 2);
        //Need number of options in meni
        var navbarOptsLen = navbarOpts.length;

        for(var i = 0; i < navbarOptsLen; i++) {

            console.log(navbarOpts[i]["scrollTo"])
            console.log(navbarOpts[i]["elem"].offset())
            
            var topOffset = navbarOpts[i]["elem"].offset().top;
            //I want height of each element
            var height = navbarOpts[i]["elem"].height();

            if(middleScreenHeight >= topOffset && middleScreenHeight <= (topOffset + height)) {
                
                if(selectedMenu != navbarOpts[i]["scrollTo"] && !scrollingNow) {
                    
                    var scrollTo = navbarOpts[i]["scrollTo"];
                    
                    //I need to make the active one active
                    $(".navbar-nav li").removeClass("active");
                    $(".navbar-nav li a[scrollTo='"+scrollTo+"']").parent().addClass("active");
                    selectedMenu = scrollTo;
                }
            }
        }
    });


    $(".navbar-nav li a").click(function(event) {

        //When I click, scroll to the thing
        var scrollTo = $(this).attr('scrollTo');
        var elem = $("#"+scrollTo);

        scrollingNow = true;
        
        //scroll the shit
        $('html, body').animate({
            scrollTop: elem.offset().top - nav.height()
        }, 400, function() {
            scrollingNow = false;
        });

        //make new point as active
        $(".navbar-nav li").removeClass("active");
        $(this).parent().addClass("active");
        
        //Don't do the shit that usually happens.. which is just jumping
        //uggh so long to get this 
        event.preventDefault();
    });

    $(document).click(function(event) {
        
        if($(window).width() < 768){

            if (!$(event.target).closest('.navbar-inverse, .navbar-fixed-top').length && !$(event.target).class('.drawer')) {
                $(".navbar-toggle").click();
            }
        }
    })

})
