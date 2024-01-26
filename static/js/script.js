$(function(){

    /*---------------------------------------
      Constants
    -----------------------------------------*/
    //const timeout3Seconds = setTimeout(3000);
    
    
    
    /*---------------------------------------
      Functions
    -----------------------------------------*/


    //functions that handles sthe sorting dropdown 
    $("#soring-products-selector").change(function() {
        var selector = $(this);
        var currentUrl = new URL(window.location);
        var selectedValue = selector.val();
    
        if (selectedValue !== "reset") {
            var [sort, direction] = selectedValue.split("_");
    
            currentUrl.searchParams.set("sort", sort);
            currentUrl.searchParams.set("direction", direction);
        } else {
            currentUrl.searchParams.delete("sort");
            currentUrl.searchParams.delete("direction");
        }
    
        window.location.replace(currentUrl);
    });

    $(document).ready(function () {
        // Show/hide the button based on scroll position
        $(window).scroll(function () {
            if ($(this).scrollTop() > 100) {
                $('#scrollToTopButton').fadeIn();
            } else {
                $('#scrollToTopButton').fadeOut();
            }
        });
    
        // Scrolling to top when the button is clicked
        $('#scrollToTopButton').click(function () {
            $('html, body').animate({ scrollTop: 0 }, 500);
        });
    });
    

    // function that increment and decrement qty
    $(document).ready(function () {
        const quantityInput = $('#quantity-shower');
        const incrementButton = $('#increment-button');
        const decrementButton = $('#decrement-button');

        incrementButton.on('click', function () {
            quantityInput[0].stepUp();
        });
    
        decrementButton.on('click', function () {
            if (quantityInput.val() > 1) {
                quantityInput[0].stepDown();
            }
        });
    });

});