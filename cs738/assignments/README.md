# CS738 Assignments

Assignment submissions for the Concepts, Algorithms, and Tools for Model Checking course for Fall 2020, by Sankalp Gambhir.

To add new submissions, create a corresponding `weekX` folder, and add the following base structure to a `.tex` file of choice in the folder:

```tex
% is draft? include comments and notes?
\newcounter{draft}
\setcounter{draft}{1}

\input{../macro}
```

This will generate the basic format with defaults as defined in `macro.tex`

To override defaults, after the first block, add one or more of the following:

```tex
\renewcommand{\hwname}{Authors}
\renewcommand{\hwemail}{Author email / details}
\renewcommand{\hwtype}{Title (eg: Assignment)}
\renewcommand{\hwnum}{Number} % defaults to 0 : **recommended**
\renewcommand{\hwdate}{February 29, 2000} % defaults to today : **recommended**
\renewcommand{\hwclass}{Course Number}
\renewcommand{\hwlecture}{Lecture corresponding to submission}
\renewcommand{\hwsection}{Section for Submission}
```

Followed by the (necessary) usual block:

```tex
\begin{document}
    \maketitle

    % content here
    % \question
    %   answer
    % \question*{Question Title}
    %   answer

\end{document}
```

Copyright © 2020.
This work is free. You can redistribute it and/or modify it under the
terms of the Do What The Fuck You Want To Public License, Version 2,
as published by Sam Hocevar. See the COPYING file for more details.
