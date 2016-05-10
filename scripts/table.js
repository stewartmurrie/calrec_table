$(function() {
  table = [];
  $.ajax({
    url: "shared/table.json",
    dataType: "json",
    success: function(response) {
      table = response;
    },
    async: false
  });
});
