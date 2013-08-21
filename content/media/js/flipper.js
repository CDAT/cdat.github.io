function flipit(id){
  $(".flipbox").flippy({
    direction: "right",
    duration: "750",
    verso: "<div><center><pre><code>if(x<2){<br/> x=10;<br/> }</code></pre><br/><a class=\"btn\" href=\"#\" onclick=\"javascript:back('image')\">back</a></center></div>",
  });
  e.preventDefault();
}

function back(image){
  $(".flipbox").flippy({
    direction: "right",
    duration: "750",
    verso: "<div><center><img src=\"media/images/gallery/CelinesCaliforniaPlot.png\" class=\"thumbnail\" /><div class=\"carousel-caption\"><p>Caption text here <a class=\"btn\" href=\"#\" onclick=\"javascript:flipit('1')\">See code</a></p></div></center></div>",
  });
  e.preventDefault();
}

