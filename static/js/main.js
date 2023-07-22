


var spinner = function () {
  setTimeout(function () {
      if ($('#spinner').length > 0) {
          $('#spinner').removeClass('show');
      }
  }, 1);
};
spinner();

// mobile_navnbar-start
function hamburger() {

    var hamburger = $(".hamburger")
    var header_menu = $(".header__menu")
    if (document.querySelector(".is-active")) {
        hamburger.removeClass("is-active")
        header_menu.removeClass("is-open")
    } else {
        hamburger.addClass("is-active")

        header_menu.addClass("is-open")
    }



}
// mobile_navnbar-end


// first_dropdown_start

$("#dropdownMenuFutures").click(function () {

  if (document.querySelector(".show")) {
    $(".dropdown").removeClass('show')

  } else {
    $(".dropdown").addClass('show')
    
    
  }



})
// $(document).on("click", function(event){
//     var $trigger = $(".dropdown");
//     if($trigger !== event.target && !$trigger.has(event.target).length){
//         $(".dropdown#dropmenu_first").removeClass('show')
//         $(".dropdown-menu#dropmenu_frst").removeClass('show')
//         $("#dropdownMenuFutures").attr("aria-expanded","false")
//     }
// });

// // first_dropdown_end

// // first_dropdown_second

// $("#dropdownMenuUsecases").click(function () {

//   if (document.querySelector(".show")) {
//     $(".dropdown#dropmenu_second").removeClass('show')
//     $(".dropdown-menu#dropmenu_scnd").removeClass('show')
//     $("#dropdownMenuUsecases").attr("aria-expanded","false")
//   } else {
//     $(".dropdown#dropmenu_second").addClass('show')
//     $(".dropdown-menu#dropmenu_scnd").addClass('show')
//     $("#dropdownMenuUsecases").attr("aria-expanded","true")
//   }



// })
// $(document).on("click", function(event){
//     var $trigger = $(".dropdown");
//     if($trigger !== event.target && !$trigger.has(event.target).length){
//         $(".dropdown#dropmenu_second").removeClass('show')
//         $(".dropdown-menu#dropmenu_scnd").removeClass('show')
//         $("#dropdownMenuUsecases").attr("aria-expanded","false")
//     }
// });

// first_dropdown_end

// $('.dropdown').on('click', function() {
//     // Hide all other dropdowns
//     $('.dropdown-menu').not(this).hide();
//   });



$(window).scroll(function () {

   
        

        if ($(this).scrollTop() > 45) {
           
            $('.header').addClass('bg-light shadow')
            $('.header').css({'top': 0,'height':77});
            $('.header__wrapper').addClass('nav_scroll')
          
        } else {
            $('.header').removeClass('bg-light shadow')
            $('.header').css({'top': 0,'height':100});
            $('.header__wrapper').removeClass('nav_scroll')
        }

});


// Swiper



$('[data-toggle="counter-up"]').counterUp({
    delay: 10,
    time: 2000
});

$('.counter').counterUp({
    delay: 10,
    time: 2000
  });
  $('.counter').addClass('animated fadeInDownBig');
  $('h3').addClass('animated fadeIn');



  controlVideoVolume.addEventListener('click', function() {
    if (bannerVideo.muted) {
        bannerVideo.muted = false;
 
    } else {
        bannerVideo.muted = true;
   
    }
  });



  var swiper1 = new Swiper(".mySwiper", {
    slidesPerView: 1,
    spaceBetween: 30,
    loop: true,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
  
  });

//   var swiper2 = new Swiper(".testimonials", {
//     slidesPerView: 3,
//     spaceBetween: 30,
//     loop: true,
//     pagination: {
//       el: ".swiper-pagination",
//       clickable: true,
//     }, breakpoints: {  
//   '1200': {
//     slidesPerView: 3,
//     spaceBetween: 30,},
//   '400': {
//     slidesPerView: 1,
//     spaceBetween: 30, },
    
//   '300': {
//     slidesPerView: 1,
//     spaceBetween:30, },
// }
  
//   });
  
  
//   var swiper3 = new Swiper(".swiper-container-strategy", {
    
//     spaceBetween: 30,
//     loop: true,
//     breakpoints: {  
//   '1200': {
//     slidesPerView: 3,
//     spaceBetween: 40,},
//   '640': {
//     slidesPerView: 1,
//     spaceBetween: 30, },
// },
//     pagination: {
//       el: ".swiper-pagination",
//       clickable: true,
//     },
  
//   });
  
//   var swiper4 = new Swiper(".swiper-container-features", {
//     slidesPerView: 5,
//     spaceBetween: 30,
//     loop: true,
//     pagination: {
//       el: ".swiper-pagination",
//       clickable: true,
//     },
//     navigation: {
//       nextEl: ".features__carousel-btn--next",
//       prevEl: ".features__carousel-btn--prev",
//     },
//     breakpoints: {  
//   '1200': {
//     slidesPerView: 5,
//     spaceBetween: 30,},
//   '640': {
//     slidesPerView: 1,
//     spaceBetween: 30, },
    
//   '400': {
//     slidesPerView: 1,
//     spaceBetween:30, },
// }

  
//   });

//   var swiper5 = new Swiper(".swiper-container-pricing", {
//     slidesPerView: 5,
//     spaceBetween: 30,
    
//     pagination: {
//       el: ".swiper-pagination",
//       clickable: true,
//     },
//     navigation: {
//       nextEl: ".features__carousel-btn--next",
//       prevEl: ".features__carousel-btn--prev",
//     },
//     breakpoints: {  
//   '1200': {
//     slidesPerView: 7,
//     spaceBetween: 0,
//     loop: false,
//     noSwiping: true,
//   },
//   '800': {
//     slidesPerView: 3,
//     spaceBetween: 30, },
    
//   '400': {
//     slidesPerView: 1,
//     spaceBetween:30, },
// }

  
//   });
//   var swiper5 = new Swiper(".swiper-container-partners", {
//     slidesPerView: 5,
//     spaceBetween: 30,
    
//     pagination: {
//       el: ".swiper-pagination",
//       clickable: true,
//     },
//     navigation: {
//       nextEl: ".features__carousel-btn--next",
//       prevEl: ".features__carousel-btn--prev",
//     },
//     breakpoints: {  
//   '1200': {
//     slidesPerView: 7,
//     spaceBetween: 0,
//     loop: false,
//     noSwiping: true,
//   },
//   '800': {
//     slidesPerView: 3,
//     spaceBetween: 30, },
    
//   '400': {
//     slidesPerView: 1,
//     spaceBetween:30, },
// },autoplay: {
//   delay: 1000,
// },

  
//   });
  controlVideoVolume.addEventListener('click', function() {
  if (bannerVideo.muted) {
      bannerVideo.muted = false;
      $("#unmuted").css('display','block')
      $("#muted").css('display','none')

  } else {
      bannerVideo.muted = true;
      $("#muted").css('display','block')
      $("#unmuted").css('display','none')
  }
});

$('[data-toggle="counter-up"]').counterUp({
  delay: 10,
  time: 2000
});
