$(function() {

  //h1要素を隠す
  //$('h1').hide();  

  //
  $('img').fadeOut(1500);

  //
  //$('p').slideUp(1500);

  $('#hide-text').click(function() {
    $('#text').slideUp();
  });

  $('#language-wrapper').hover(
    function() {
      $('.language-text').fadeIn();
    },
    function() {
      $('.language-text').fadeOut();
  });

});

