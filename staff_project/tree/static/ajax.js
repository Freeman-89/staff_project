  $(document).on("click", ".jstree-clicked",function(){
    let clicked_element_title = $(this).attr("title")
    let title_list = clicked_element_title.split(" ")
    $.ajax({
        url: "/staff_list/" + title_list[0] + "/page/" + title_list[1] +"/",
        success: function (data) {
            $('.table_content').html(data.result);
        }
    });
  });