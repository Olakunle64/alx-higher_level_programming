$(document).ready(function () {
  function fetcher (language) {
    $.post(`https://hellosalut.stefanbohacek.dev/?lang=${language}`, function (data) {
      $('DIV#hello').text(data.hello);
    });
  }

  $('INPUT#btn_translate').click(function () {
    const language = $('INPUT#language_code').val();
    fetcher(language);
  });

  $('INPUT#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      const language = $('INPUT#language_code').val();
      fetcher(language);
    }
  });
});
