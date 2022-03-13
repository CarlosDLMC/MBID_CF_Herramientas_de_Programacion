with open("comentario.txt") as comment:
    todo = comment.read()
    print(len(todo.split()))