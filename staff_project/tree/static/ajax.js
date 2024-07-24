  $(document).on("click", ".jstree-clicked",function(){
    let clicked_element_id = $(this).attr("id")
    $.ajax({
        url: "/staff_list/" + clicked_element_id + "/",
        success: function (data) {
            $('.table_content').html(data.result);
        }
    });
  });