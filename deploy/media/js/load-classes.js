;(function($) {
    $.ajax({
        url: "http://www.bloomyogastudio.com/calendar.php",
        dataType: 'text',
        success: function(data) {
            console.log(data);
        }
    });
})(jQuery);