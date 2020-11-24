if(typeof window.todoList === "undefined") {
  window.todoList = {};
}



window.todoList.ui = (function() {

  var initHomePage = function() {
    var bindButtonEvents = function() {
      $("new_task-button").on("Click", function() {
        showNewTaskPage();
      })

      $("task_title").on("Click", function() {
        showEditTaskPage();
      });

      $("complete_task").on("Click", function() {
        refreshTask();
      });

      $("cancel_new_task_save-button").on("Click", function() {
        showEditTaskPage();
      });

      $("save_new_task-button").on("Click", function() {
        showEditTaskPage();
      });

      $("delete_all_tasks-button").on("Click", function() {
        deleteAllTasks();
      });

    }
    bindButtonEvents();
  };

  var showHomePage = function() {

  };

  var initNewTaskPage = function() {

  };

  var showNewTaskPage = function() {

  };

  var initEditTaskPage = function() {

  };

  var showEditTaskPage = function() {

  };




  var refreshTask = function() {

  };

  var deleteAllTasks = function() {

  };

  var deleteTask = function() {

  };


  $(document).on("pagecreate", "#home-page", initHomePage);
  $(document).on("pagecontainershow", "#home-page", showHomePage);

  $(document).on("pagecreate", "#new_task-page", initNewTaskPage);
  $(document).on("pagecontainershow", "#new_task-page", showNewTaskPage);

  $(document).on("pagecreate", "#edit_task-page", initEditTaskPage);
  $(document).on("pagecontainershow", "#edit_task-page", showEditTaskPage);



})()
