function flipit(id){
  $(".flipbox").flippy({
    direction: "right",
    duration: "750",
    verso: "<div><center><pre><code>if(x<2){<br/> x=10;<br/> }</code></pre><br/><a class=\"btn\" href=\"#\" onclick=\"javascript:back()\">back</a></center></div>",
  });
}

function back(){
 $(".flipbox").flippyReverse();
}

