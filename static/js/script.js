$(function(){

    /*---------------------------------------
      Constants
    -----------------------------------------*/
    //const timeout3Seconds = setTimeout(3000);
    
    
    
    /*---------------------------------------
      Functions
    -----------------------------------------*/

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
    
});