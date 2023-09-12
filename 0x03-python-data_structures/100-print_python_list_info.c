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
	int list_size, allocated_space, count;
	PyObject *item;

	list_size = PyList_Size(p);
	allocated_space = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d", list_size);
	printf("[*] Allocated = %d", allocated_space);

	for (i = 0; i < size; i++)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %d: %s", i, py_TYPE(item)->ob_type);
	}
}
