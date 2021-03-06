import functools


def test(a, b=10):
    print("A:", a)
    print("B:", b)


def show_details(name, func, is_partial=False):
    print(name)
    if not is_partial:
        print("Not partial")
        print(func.__name__)
    else:
        print("Partial")
        try:
            print(func.__name__)
        except AttributeError as e:
            print("If we dont use update wrapper, partial does not get the properties of func name")
            print("No name")
        print(func.func)
        print(func.args)
        print(func.keywords)


# normal test show details
show_details("Normal", test)
test(3)

# Now we create a function with smaller args than the original test function.
test_with_fixed_a = functools.partial(test, 1)
test_with_fixed_a()

# Now we create a function with smaller args than the original test function.
test_with_fixed_a_and_update_wrapper = functools.partial(test, 100)
functools.update_wrapper(test_with_fixed_a_and_update_wrapper, test)
show_details("test_with_fixed_a_and_update_wrapper", test_with_fixed_a_and_update_wrapper, True)
test_with_fixed_a(b=1200)