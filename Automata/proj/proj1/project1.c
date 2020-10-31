#include <Python.h>
#include <stdio.h>

int main(int argc, char *argv[])
{
	Py_Initialize();
	PyRun_SimpleString("import sys");
	PyRun_SimpleString("sys.path.append('./')");

	PyObject * pModule = NULL;
	PyObject * pFunc = NULL;
	pModule = PyImport_ImportModule("stript");
	pFunc = PyObject_GetAttrString(pModule, "REMatchReadingStdin");
	PyEval_CallObject(pFunc, NULL);

	Py_Finalize();
	return 0;
}
