# Comic book tracker 

##Frontend



##Backend



##MiddleWare (glue)



##Logging

* If you include date format in the log, it must be sortable. ISO-8601, ISO-3339 or a zero-padded timestamp. No exceptions.


* Always include filename and line number where possible. Makes it a lot easier to jump to parts of the project and set breakpoints. The format {filename}:{lineno}:message

* If a function returns something, try to avoid putting log statements in its body. Keep it as close to being a pure function as you can; logging is a side effect that could break the function if something breaks in logging.

* Don’t log irrelevant details.

