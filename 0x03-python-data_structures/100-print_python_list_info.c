#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - print the information about python list
 * @p: a PyObject
 *
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	Py_ssize_t list_size, allocated_space, count;
	PyObject *item;

	list_size = PyList_Size(p);
	allocated_space = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %ld", list_size);
	printf("[*] Allocated = %ld", allocated_space);

	for (count = 0; count < size; count++)
	{
		item = PyList_GET_ITEM(p, count);
		printf("Element %ld: %s", count, Py_TYPE(item)->ob_type);
	}
}
