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
    

    // function that increment and decrement qty on product detail page
    $(document).ready(function () {
        const quantityInput = $('#quantity-shower');
        const incrementButton = $('.increment-button');
        const decrementButton = $('.decrement-button');

        incrementButton.on('click', function (e) {
            e.preventDefault();
            quantityInput[0].stepUp();
        });
    
        decrementButton.on('click', function (e) {
            if (quantityInput.val() > 1) {
                e.preventDefault();
                quantityInput[0].stepDown();
            }
        });
    });

    // function that increment and decrement qty on cart page
    $(document).ready(function () {
        $('.increment-button-cart').on('click', function (e) {
            e.preventDefault();
            const productId = $(this).data('item-id');
            const quantityInput = $('#quantity-shower-cart_' + productId);
            if (quantityInput.length) {
                quantityInput[0].stepUp();
            }
        });
    
        $('.decrement-button-cart').on('click', function (e) {
            e.preventDefault();
            const productId = $(this).data('item-id');
            const quantityInput = $('#quantity-shower-cart_' + productId);
            if (quantityInput.length && quantityInput.val() > 1) {
                quantityInput[0].stepDown();
            }
        });
    });

    // function that handles submits cart qty form
    $(document).ready(function () {
        $('.update-entry').on('click', function (e) {   
            var form = $('.update-qty-cart-form')
            form.submit();
        });
    });

    // Function to retrieve the CSRF token from the cookie
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // Remove entry from cart and reload
    $(document).ready(function() {
        $('.remove-entry').on('click', function(e) {
            e.preventDefault();
            var item_id = $(this).data('item-id');
            var size = $(this).data('size');

            // Get the CSRF token from the cookie
            var csrftoken = getCookie('csrftoken');

            $.ajax({
                type: 'POST',
                url: '/cart/remove/' + item_id + '/',
                data: {
                    'product_size': size,
                    csrfmiddlewaretoken: csrftoken
                },
                headers: {
                    'X-CSRFToken': csrftoken
                },
                success: function(data) {
                    // Reload the page after successful removal
                    location.reload();
                },
                error: function(error) {
                    console.log(error);
                }
            });
        });
    });

    // Update entry in cart
    $(document).ready(function() {
        $('.update-entry').click(function(e) {
            e.preventDefault();
            
            var formId = $(this).data('form-id');
            $('#' + formId).submit();
        });
    });

    // Display thank you message after subscribing for newsletter 
    $(document).ready(function() {
        // Intercept form submission
        $(".subscribe-form").submit(function(e) {
            // Display the thank-you message
            showThankYouMessage();
        });
    
        function showThankYouMessage() {
            // Hide the form
            $(".subscribe-form").hide();
    
            // Display the thank-you message
            $("<h3>Thank you for subscribing!</h3>").insertBefore(".subscribe-form");
    
            // Set a timeout to show the form again and remove the thank-you message after 2 seconds
            setTimeout(function() {
                $(".subscribe-form").show();
                $("h3:contains('Thank you for subscribing!')").remove();
            }, 2000);
        }
    });
});