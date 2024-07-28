---
tags:
- Type/Note
- Topic/Data_Science
- Class/DSC_20
date:
- 2024-01-31
---
Source: https://docs.google.com/presentation/d/14BU3Q3HhNa7iI7L1LXx7b0OdJwjh-fWzVReK5fsAFLI/edit#slide=id.g162b847a252_0_49  

> [!note] Environment Diagrams  
> visualize the interpreter process  

> [!definition] Execution procedure for def statement  
> ```Python  
> def function_name(formal_parameters):  
> 	function_body  
> 	return return_expression```  
> 1. Create a function with a given signature  
> 2. Set the body of that function to be everything indented after the first line  
> 3. Bind function_name to that function in the current frame  

> [!note] Calling user-defined functions  
> Procedure for calling/applying user-defined functions:  
> - Add a local frame, forming a new environment  
> - Bind the function's formal parameters to its arguments in that frame  
> - Execute the body of the function in that new environment  

> [!note] Looking up Names in Environments  
> - Every expression is evaluated in the context of an environment.  
> - Environments are the memory that keeps track of the correspondence between names and values.  
> - So far, the current environment is either:  
> 	- The global frame alone, or  
> 	- A local frame, followed by the global frame.  
> - Frame is a binding between names and values.  
> Important:  
> 1. An environment is a sequence of frames.  
> 2.   A name evaluates to the value bound to that name in the earliest frame of the current environment in which that name is found.  
