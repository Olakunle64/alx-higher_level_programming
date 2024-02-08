$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const language = $('INPUT#language_code').val();
    $.post(`https://hellosalut.stefanbohacek.dev/?lang=${language}`, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
