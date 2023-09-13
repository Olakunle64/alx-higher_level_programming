#include <stdio.h>
#include <python.h>

/**
 * print_python_list - print some basic info about python lists
 * @p: PyObject
 *
 * Return: void
 */

void print_python_list(PyObject *p)
{
	Pyssize_t allocated_space, list_size;
	Pyobject *item;

	allocated_space = ((PyListObject *)p)->allocated;
	list_size = PyList_Size(p);
	printf("[*] Python list info");
	printf("[*] Size of the Python List = %ld", list_size);
	printf("[*] Allocated = %ld", allocated_size);

	for (i = 0, (Pyssize_t)i < list_size, i++)
	{
		item = PyList_GET_ITEM(p, i);
		printf("Element %d: %s", i, PyObject_Type(item)->tp_name);
	}
}
/**
 * print_python_bytes - print some basic infor about python bytes
 * @p: PyObject
 *
 * Return: void.
 */

void print_python_bytes(PyObject *p)
{

}
