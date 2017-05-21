# clean-tex
Tool for cleaning directories of LaTeX log files


# Motivation
When you compile a LaTeX document the compiler generates a collection of log files (.aux, .log, .out, .synctex.gz) for use in future compilations. 

If you use an editor like TEX Maker you have the option to send all output files to a separate "build" directory but then your pdf gets sent there too and I haven't found that option to be much cleaner or more convenient.

Additionally, any code you've been working on will inevitably leave behind backup files (files ending in a tilde "~") and these wind up cluttering up my directories. "Why are you still using Emacs??" Hitting tab is easier than hitting backspace.

What I want is a command line utility to clean up my working directory or any arbitrarily specified directory with the option to clean sub-directories, i.e., "from here down".


# Usage
Convert this script to an executable and stick it in your /usr/local/bin/ or other directory in your shell PATH.


# Warning
I made this for Linux users. If you use Windows or MacOS, God help you.
