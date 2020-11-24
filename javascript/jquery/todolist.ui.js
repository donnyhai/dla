if(typeof window.todoList === "undefined") {
  window.todoList = {};
}



window.todoList.ui = (function() {
  console.log("todolistui aufgerufen");

  var initHomePage = function() {

    console.log("inithomepage aufgerufen");

    var bindButtonEvents = function() {
      $("new_task-button").on("Click", function() {
        console.log("newtaskbutton aufgerufen");
        showNewTaskPage();
      });

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

    };
    bindButtonEvents();
  };

  initHomePage();

  var showHomePage = function() {
    $.mobile.changePage("#home-page", {
      transition: "slideup",
      reverse: true,
      changeHash: true
    });
  };

  var initNewTaskPage = function() {
    var bindButtonEvents = function() {
      $("cancel_new_task_save-button").on("Click", function() {
        showHomePage();
      });

      $("save_new_task-button").on("Click", function() {
        addNewTask($("add_task_name").val(), $("add_task_description").val());
      });

    }
    bindButtonEvents();
  };

  var showNewTaskPage = function() {
    alert("showNewTaskPage")

    $.mobile.changePage("#new_task-page", {
      transition: "slideup",
      reverse: false,
      changeHash: true
    });
  };

  var initEditTaskPage = function() {

  };

  var showEditTaskPage = function() {

  };

  var addNewTask = function(name, description) {

  }



  var refreshTask = function() {

  };

  var deleteAllTasks = function() {

  };

  var deleteTask = function(id) {

  };


  $(document).on("pagecreate", "#home-page", initHomePage);
  $(document).on("pagecontainershow", "#home-page", showHomePage);

  $(document).on("pagecreate", "#new_task-page", initNewTaskPage);
  $(document).on("pagecontainershow", "#new_task-page", showNewTaskPage);

  $(document).on("pagecreate", "#edit_task-page", initEditTaskPage);
  $(document).on("pagecontainershow", "#edit_task-page", showEditTaskPage);



})()
