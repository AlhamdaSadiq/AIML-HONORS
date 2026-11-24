def output_decorator(task):
    def decorate(method):
        def execute(*values, **options):
            print("##########################")
            print("#", task)
            print("# input:", *values)

            answer = method(*values, **options)

            print("# output:", answer)
            print("##########################")

            return answer
        return execute
    return decorate


@output_decorator("Adding")
def add(a, b):
    return a + b


add(4, 3)
