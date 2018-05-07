$(document).ready(function(){
  $('#new-task').on('click', function(){
    if ($('#form-new-task').css('display') == 'none') {
      $('#form-new-task').fadeIn();
    } else {
      $('#form-new-task').fadeOut();
    }
  });

  $('form button').on('click', function(){
    $('#todo-list, #concluded-list').html('<div class="loader"></div>');
    var name = $('#name').val();
    var description = $('#description').val();
    $.ajax({
      method: "POST",
      url: "/api/task/",
      data: { name: name, description: description },
      success: function(response) {
        loadTasks();
        markAsDone();
      }
    });
  });
  
  loadTasks();

  function loadTasks() {
    $.ajax({
      url: "/api/task/",
      success: function(response) {
          var todo = '';
          var concluded = '';

          $.each(response, function(index, value) {
            if (value[3] == 0) {
              todo += '<div class="alert alert-info todo-task" id="task-'+value[0]+'" role="alert">'+
                        '<strong>'+value[1]+'</strong><br>'+
                        value[2]+'<br>'+
                        new Date(value[4])+'<br>'+
                    '</div>';
            }

            if (value[3] == 1) {
              concluded += '<div class="alert alert-success" role="alert">'+
                        '<strong>'+value[1]+'</strong><br>'+
                        value[2]+'<br>'+
                        new Date(value[4])+
                    '</div>';
            }
          });

          $('#todo-list').html(todo);
          $('#concluded-list').html(concluded);
          markAsDone();
      }
    });

    function markAsDone() {
      $('.todo-task').on('click', function(){
        $('#todo-list, #concluded-list').html('<div class="loader"></div>');
        var id = $(this).attr('id').split('-')[1];
        $.ajax({
          url: "/api/task/done/"+id,
          success: function(response) {
            loadTasks();
          }
        });
      });
    }
  }
});