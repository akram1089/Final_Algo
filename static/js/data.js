
//     var swiper_container_disposal = new Swiper(".swiper-container-disposal", {
      
//       loop: true,
//       pagination: {
//         el: ".swiper-pagination",
//         clickable: true,
//       }, breakpoints: {  
//     '1200': {
//       slidesPerView: 3,
//       spaceBetween: 30,},
//     '400': {
//       slidesPerView: 1,
//       spaceBetween: 30, },
      
//     '300': {
//       slidesPerView: 1,
//       spaceBetween:30, },
//   }
    
//     });
    
var swiper = new Swiper(".swiper-container-disposal", {
    spaceBetween: 30,
    slidesPerView: 2,
    loop: true,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
  });
      
//     var swiper4 = new Swiper(".swiper-container-disposal", {
//       slidesPerView: 5,
//       spaceBetween: 30,
//       loop: true,
//       pagination: {
//         el: ".swiper-pagination",
//         clickable: true,
//       },
//       navigation: {
//         nextEl: ".features__carousel-btn--next",
//         prevEl: ".features__carousel-btn--prev",
//       },
//       breakpoints: {  
//     '1200': {
//       slidesPerView: 5,
//       spaceBetween: 30,},
//     '900': {
//       slidesPerView: 1,
//       spaceBetween: 30, },
    
//     '400': {
//       slidesPerView: 1,
//       spaceBetween:30, },
//   }

  
//     });





  var disposal_desc_js=[
      {
          id:1,
          main_desc:`
          
           <p>A range of order types. Market price, stop price, target price each with their own
                                  trigger price. You have the option to:</p>
                              <ul>
                                  <li><span>Submit all positions at one go or enter most illiquid position first or in order of list of positions</span>
                                  </li>
                                  <li><span>Reverse entered positions if some balance positions unfilled</span></li>
                              </ul>
          `
      },
      {
          id:2,
          main_desc:`
              <p>Built-in price execution algorithms allow you to get better execution prices. You
                                  have an option to choose:</p>
                              <ul>
                                  <li><span>Avg of Bid/Ask</span></li>
                                  <li>
                                      <span>One Tick above top price which you can update as per the time you set</span>
                                  </li>
                                  <li><span>Market Price</span></li>
                              </ul>
          `
      },
      {
          id:3,
          main_desc:`
          
   <p>When strategies have multiple positions of large quantities executing one after
                                  another will leave you unhedged for a bit. To prevent this, it’s best to execute all
                                  positions in smaller tranches. By doing this the smaller quantity of all positions
                                  will be completed before moving on to the next tranche. This is possible in 2
                                  ways:</p>
                              <ul>
                                  <li><span>As a Percentage or total size</span></li>
                                  <li><span>Max Lots per execution</span></li>
                              </ul>

          `
      },
      {
          id:4,
          main_desc:`
          <p>A trailing stop is a stop order that can be set to increase in tandem with your
                                  profit. You have the following options:</p>
                              <ul>
                                  <li>
                                      <span>To move the trailing stop to cost at a specified profit level and then</span>
                                  </li>
                                  <li><span>To move the trailing stop by a certain amount with every increase in profit</span>
                                  </li>
                              </ul>
      `
          
      },
      {
          id:5,
          main_desc:`
          <p>There is a choice to reactivate a strategy, manually or automatically, once it has
                                  entered and exited. Your options are:</p>
                              <ul>
                                  <li>
                                      <span>Automatically every hour / day / week / month / quarter / 6 months / year</span>
                                  </li>
                                  <li><span>Manually</span></li>
                              </ul>
          

          `
      },
      {
          id:6,
      main_desc:`
      <p>The positions entered in this block are automatically taken at the end of every day
                                  and reversed automatically at the beginning of the next day. This feature could be
                                  used to protect your short option positions from any possible black swan events.</p>
                          </div>
     `
      },
      {
          id:7,
          main_desc:`
          <p>If your strategy requires you to not trade in (for instance) the first fifteen or the
                                  last fifteen minutes of the exchange opening, that can be set here.</p>

`
      },{
          id:8,
          main_desc:`
          <p>For futures and options strategies if you need to close out open positions in
                                  contracts that are about to expire in favour of contracts that are expiring later,
                                  you can do it automatically here.</p>
          `
      }
  ]

  
  document.getElementById("disposal__desc").innerHTML=disposal_desc_js[0].main_desc
  function disposal(dispo) {

     
    const Filtered_about = disposal_desc_js.filter((Curr_dest) => {
      return Curr_dest.id === dispo
    })
    Filtered_about.map((x)=>{
      document.getElementById("disposal__desc").innerHTML=x.main_desc
      
    })
  
  
}


$(document).ready(function() {

$('[data-btn-id]:first-child').addClass('is-active')
// Filter button click event
$('[data-btn-id]').click(function() {
var btnId = $(this).attr('data-btn-id');
filterResults(btnId);
changeButtonColor($(this));
});

// Initial filtering (optional)
filterResults(1)
// Function to filter results
function filterResults(btnId) {
// Clear previous results


// Filter elements based on btnId


}

// Function to change button color
function changeButtonColor(button) {
// Reset color of all buttons
$('[data-btn-id]').removeClass('is-active');


// Add color to the clicked button
button.addClass('is-active');

}
});





