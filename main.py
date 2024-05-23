import os
import time
import json

class Task:
  """
  Clase que representa una tarea
  """
  def __init__(self,
               title: str,
               description: str = "",
               status: bool = False):
    """
    Inicializa una nueva tarea.
    @params[in] title -> Título de la tarea (str)
    @params[in] description -> Descripción detallada de la tarea (str)
    @params[in] status -> Indica si la tarea está completada o pendiente (bool)
    """
    self.__title = title
    self.__description = description
    self.__status = status                
    if not title:
      raise ValueError('Title can not be an empty string')

class TaskManager:
  """
  Clase que gestiona una lista de tareas.
  """
  def __init__(self):
    """
    Inicializa el administador de tareas
    """
    self.__data_path = "./tasks.json"
    self.__tasks = []                     
    self._load_tasks_from_file()
  
  def add_task(self, task):
    """
    Agrega una tarea a la lista.
    @params[in] task -> Tarea a agregar (Task)
    @return None
    """
    self.__tasks.append(task.__dict__)
    self._save_tasks_to_file()

  def delete_task(self, index):
    """
    Elimina una tarea dado su índice en la lista.
    @params[in] index -> Índice de la posición de la tarea en la lista (int)
    @return None
    """
    if 0 <= index < len(self.__tasks):
      del self.__tasks[index]
      self._save_tasks_to_file()
    else:
      raise IndexError ("Index is not valid")

  def get_tasks(self):
    """
    Obtiene la lista de tareas.
    @return Lista de tareas (list<Task>)
    """
    return self.__tasks

  def mark_completed(self, index):
    """
    Marca una tarea como completada.
    @params[in] index -> Índice de la posición de la tarea en la lista (int)
    @return None
    """
    if 0 <= index < len(self.__tasks):
      self.__tasks[index]["_Task__status"] = True
      self._save_tasks_to_file()
    else:
      raise IndexError("Index is not valid")

  """
  Funciones privadas => Sólo se pueden llamar desde dentro de la clase
  """
  def _create_task_file(self):
    """
    Crea un nuevo archivo para almacenar las tareas.
    """
    with open(self.__data_path, "w") as file:
      json.dump([], file, indent=2)

  def _save_tasks_to_file(self):
    """
    Guarda las tareas en el archivo.
    """
    with open(self.__data_path, "w") as file:
      json.dump(self.__tasks, file, default=lambda obj:obj.__dict__, indent=2)

  def _load_tasks_from_file(self):
    """
    Carga las tareas desde el archivo.
    """
    try:  
      with open(self.__data_path, "r") as file:
        self.__tasks = json.load(file)
    except FileNotFoundError:
      print("File not found! Creating a new file...")
      self._create_task_file()

def clear_terminal() :
  os.system("cls||clear")

def main():
  task_manager = TaskManager()
  # Bucle infinito para evitar cerrar la app al ingresar la primera opción a elegir
  while True:
    clear_terminal()
    print('TASK-MANAGER made by Edgar Joel Martin Melian')
    print('=' * 60)
    print(' [1] Add new task')
    print(' [2] Delete task')
    print(' [3] Show all tasks')
    print(' [4] Mark a task as complete')
    print(' [0] Exit')
    print('')
    option = input('option > ')
    if option == '0':
      clear_terminal()
      break
    elif option == '1':
      clear_terminal()
      try:
        print('Enter task data')
        print('')
        task_title = input('[Title] > ')
        task_description = input('[Description] > ')
        task_manager.add_task(Task(task_title, task_description))

        print('')
        print('\033[1;32mNew task added\033[0m')
      except Exception as error:
        print('')
        print(f'\033[1;31m[Error!]: {error}\033[0m')
      print('')
      input('Press (ENTER) to go back to the menu')
    elif option == '2':
      clear_terminal()
      try:
        print('Enter the index of the Task to delete')
        print('')
        index_task = int(input('index > '))
        task_manager.delete_task(index_task)
        print('')
        print(f'\033[1;32mTask with index "{index_task}" deleted! \033[0m')
      except Exception as error:
        print('')
        print(f'\033[1;31m[Error!]: {error}\033[0m')
      print('')
      input('Press (ENTER) to go back to the menu')
    elif option == '3':
      clear_terminal()
      print('TASKS')
      print('=' * 60)
      tasks = task_manager.get_tasks()
      task_index = 0
      if (len(tasks) == 0):
        print('No tasks :)')
      else:
        for task in tasks:
          status_color = ('\033[0;31m', '\033[0;32m')[task["_Task__status"]]
          print(f'{task_index}: ({status_color}{("Incompleted", "Completed")[task["_Task__status"]]}\033[0m) {task["_Task__title"]}')
          if (task["_Task__description"] != ""):
            print(f'     {task["_Task__description"]}')
          task_index += 1
      print('=' * 60)
      print('')
      input('Press (ENTER) to go back to the menu')
    elif option == '4':
      clear_terminal()
      try:
        print('Enter the index of the Task to mark as completed')
        print('')
        index_task = int(input('index > '))
        task_manager.mark_completed(index_task)
        print('')
        print(f'\033[1;32mTask with index "{index_task}" marked as COMPLETED! \033[0m')
      except Exception as error:
        print('')
        print(f'\033[1;31m[Error!]: {error}\033[0m')
      print('')
      input('Press (ENTER) to go back to the menu')
    else:
      print('')
      print(f'\033[1;31m[Error!]: Invalid option! Try again\033[0m')
      time.sleep(1)

if __name__ == "__main__":
  main()