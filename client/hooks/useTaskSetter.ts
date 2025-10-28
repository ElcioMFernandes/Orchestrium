import { TypeCreateTask } from "@/types/task";

const useTaskSetter = (id: string) => {
  function createTask(task: TypeCreateTask) {
    // Implement logic to create a new task
  }

  function updateTask(task: TypeCreateTask) {
    // Implement logic to update an existing task
  }

  function deleteTask(id: string) {
    // Implement logic to delete a task
  }

  return { createTask, updateTask, deleteTask };
};

export default useTaskSetter;
