$('p select[name=Browser]').change(function(e) {
  if ($('p select[name=Browser]').val() == '5') {
    $('#browserother').show();
  } else {
    $('#browserother').hide();
  }
});

$('p select[name=OS]').change(function() {
  if ($('p select[name=OS]').val() == 'otheros') {
    $('#osother').show();
  } else {
    $('#osother').hide();
  }
});
