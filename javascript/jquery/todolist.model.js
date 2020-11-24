if(typeof window.todoList === "undefined") {
  window.todoList = {};
}



window.todoList.model = (function() {

  var model = {
    tasks: {},
  };

  var addTask = function(name, description) {};

  var deleteTask = function(id) {};

  var reset = function(){};

  var getTask = function(){};

  var getTasks = function(){};


  return(
    addtask: addtask,
    deleteTask: deleteTask,
    reset: reset,
    getTask: getTask,
    getTasks: getTasks,
  );




})()
