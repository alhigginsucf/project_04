function getCookie(c_name)
{
    if (document.cookie.length > 0)
    {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1)
        {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
}
$(document).ready( () => {
  console.log('ready');
  $.ajaxSetup({
      headers: { "X-CSRFToken": getCookie("csrftoken") }
  });
  $('#showfb').click( () => {
    console.log('inside showfb')
    var url = "/getStockInfo/FB"
    $.ajax( {
        type: "GET",
        url: url,
        success: function( data) {
            alert("retrived data = "+ JSON.stringify( data))
        }
    })
})

});

