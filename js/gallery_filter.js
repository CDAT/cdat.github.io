$("body").ready(function(){
    function gethash(url) {
        var halves = url.split("#");
        return halves[1];
    }
    function hashchanged(e){

        var new_hash, old_hash;
        new_hash = gethash(e.newURL);
        old_hash = gethash(e.oldURL);

        $(".filter_link.filtering").removeClass("filtering");
        // Grab the correct link
        if (new_hash === "") {
            return;
        }
        var a = $(".filter_link[href='#" + new_hash + "']");
        a.addClass("filtering");
        $(".example").each(function(){
            var $el = $(this);
            var tags = $el.attr("data-tags").split(",");
            var should_show = false;
            for (var t = 0; t < tags.length; t++ ) {
                if (tags[t] == new_hash) {
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

    window.onhashchange = hashchanged;
    hashchanged({oldURL:"#", newURL:location.hash});

    // Allow filter to be removed
    $(".filter_link").click(function(e){
        if ($(this).hasClass("filtering")) {
            $(".example").show();
            $(this).removeClass("filtering");
            location.hash = "#";
            e.preventDefault();
        }
    });
});