$('a').each(function() {
  var a = new RegExp('/' + window.location.host + '/');
  if(!a.test(this.href)) {
    $(this).click(function(event) {
      event.preventDefault();
      event.stopPropagation();
      if (this.target == "_self" || /^mailto:/.test(this.href))  {
        window.open(this.href, "_self");
      } else {
        window.open(this.href, '_blank');
      }
    });
  }
});
