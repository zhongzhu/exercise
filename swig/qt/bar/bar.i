/* File : bar.i */
%module bar

%include "std_string.i"
using namespace std;

%{
#include "barbinding.h"
%}

/* Let's just grab the original header file here */
%include "barbinding.h"


