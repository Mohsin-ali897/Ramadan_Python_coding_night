import click
import json
import os
TODO_FILE = 'todo.json'

#? apple 
#? for loading task

def load_task():
    if os.path.exists(TODO_FILE):
        # return []
        with open(TODO_FILE, 'r') as file:
            return json.load(file)


#? for saving task
def save_tasks(Tasks):
    with open(TODO_FILE, 'w') as file:
        json.dump(Tasks, file, indent=4) 


@click.group()
def cli():
    '''simple Todo List Manager'''
    pass

@click.command()
@click.argument('task')
def add(task):
    '''Add a new Task to the list'''
    Tasks = load_task()
    Tasks.append({'task':task, 'done':False})
    save_tasks(Tasks)
    click.echo(f'Task added successfully : {task}')

@click.command()
def list():
    '''List All the Tasks'''
    tasks = load_task()
    if not tasks:
        click.echo('No Task found.')
        return
    for ind , task in enumerate(tasks,1):
        status = 'truty' if task['done'] else 'falsy'
        click.echo(f'{ind}. {task['task']} [{status}]')

@click.command()
@click.argument('task_number', type=int)
def complete(task_number):
    '''Mark a task as complete'''
    tasks = load_task()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]['done'] = True
        save_tasks(tasks)
        click.echo(f'Task {task_number} marked as a completed')
    else:
        click.echo(f'Invalid Task number: {task_number}')

@click.command()
@click.argument('task_number', type=int)

def remove(task_number):
    '''Remove Task from The List'''
    tasks = load_task()
    if 0 < task_number <= len(tasks):
        remove_tasks = tasks.pop(task_number - 1)
        save_tasks(tasks)
        click.echo(f'Removed Task : {remove_tasks['task']}')
    else:
        click.echo(f'Invalid Task Number {task_number}')
          


cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)
cli.add_command(remove)

if __name__== '__main__':
    cli()
