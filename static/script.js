$(document).ready(function () {
  $("#form").on("submit", function (e) {
    console.log("asdfsdfd");
    $("#form").hide();
    $.ajax({
      data: {
        user: $("#username").val(),
        subs: $("#file").val(),
      },
      type: "POST",
      url: "/submitted",
    }).done(function (data) {
      console.log(data);
      $("#loading").text(data.output).show();
    });
  });
});
