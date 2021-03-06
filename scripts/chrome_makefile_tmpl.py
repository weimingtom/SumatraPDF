MAKEFILE_TMPL = """
# FILE AUTOGENERATED BY import_chrome_sources.py !!!! Don't change manually.

# include this after mupdf\makefile.msvc

!if "$(O)"==""
!error Include mupdf\makefile.msvc first (or build ..\makefile.msvc instead)
!endif

OCH = $(O)\\chrome

CHROME_INC = %s

# /wd4244 - conversion from 'x' to 'y', possible loss of data
# /wd4530 - C++ exception handler used, but unwind semantics are not enabled. Specify /EHsc
# /wd4019 - signed/unsigned mismatch
# /wd4355 - 'this' : used in base member initializer list
# /D "NOMINMAX" - don't define min/max macros to not confuse 
CHROME_CFLAGS = $(CFLAGSOPT) /wd4244 /wd4530 /wd4018 /wd4355 /D "NO_TCMALLOC" /D "NOMINMAX" $(CHROME_INC)

CHROME_OBJS = \\
	%s

$(OCH): force
	@if not exist $(OCH) mkdir $(OCH)
%s
"""

DIR_TMPL = """
{$(EXTDIR)\\chrome\\%s}.cc{$(OCH)}.obj::
	$(CC) $(CHROME_CFLAGS) /Fo$(OCH)\\ /Fd$(O)\\vc80.pdb $<
"""