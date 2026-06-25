# Task Tracker App
This application serves to track and manage tasks that are input by the user using a command line interface. 

## CLI Sample Inputs
```
python task_cli.py add "Buy groceries"
python task_cli.py update 1 "Buy groceries and cook dinner"

python task_cli.py mark-in-progress 1
python task_cli.py mark-in-done 1

python task_cli.py list
python task_cli.py list todo
python task_cli.py list in-progress
python task_cli.py list done

python task_cli.py delete 1
```

## Supported task statuses:
```
todo
in-progress
done
```