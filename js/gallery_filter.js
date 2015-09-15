$("body").ready(function(){
    $(".filter_link").click(function(){
        var filter = this.attributes["data-tag"].value;

        if ($(this).hasClass("filtering")) {
            $(".example").show();
            $(this).removeClass("filtering");
        } else {
            $(".filter_link.filtering").removeClass("filtering");
            $(this).addClass("filtering");
            $(".example").each(function(){
                var $el = $(this);
                var tags = $el.attr("data-tags").split(",");
                var should_show = false;
                for (var t = 0; t < tags.length; t++ ) {
                    if (tags[t] == filter) {
                        should_show = true;
                    }
                }
                if (should_show) {
                    $el.show();
                } else {
                    $el.hide();
                }
            });
        }

    });
});