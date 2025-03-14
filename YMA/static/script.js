// Добавление задачи
function addTask(column) {
  const input = document.getElementById(`task-input-${column}`);
  const taskText = input.value.trim();
  if (taskText) {
      fetch('/add_task', {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
          },
          body: JSON.stringify({ column: column, task: taskText }),
      })
      .then(response => response.json())
      .then(data => {
          if (data.success) {
              location.reload(); // Перезагружаем страницу
          }
      });
  }
}

// Перемещение задачи в "Сделанные"
function completeTask(column, taskIndex) {
  fetch('/complete_task', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
      },
      body: JSON.stringify({ column: column, task_index: taskIndex }),
  })
  .then(response => response.json())
  .then(data => {
      if (data.success) {
          location.reload(); // Перезагружаем страницу
      }
  });
}