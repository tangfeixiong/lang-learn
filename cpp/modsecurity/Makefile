pkgincludedir = $(includedir)/modsecurity
pkglibdir = $(libdir)/modsecurity

am_dump_OBJECTS = dump.$(OBJEXT)
dump_OBJECTS = $(am_dump_OBJECTS)
am__DEPENDENCIES_1 =
dump_DEPENDENCIES =  \
	$(prefix)/lib/libmodsecurity.a \
	$(am__DEPENDENCIES_1) $(am__DEPENDENCIES_1) \
	$(am__DEPENDENCIES_1) $(am__DEPENDENCIES_1) \
	$(am__DEPENDENCIES_1) $(am__DEPENDENCIES_1) \
	$(am__DEPENDENCIES_1) $(am__DEPENDENCIES_1) \
	$(am__DEPENDENCIES_1) $(am__DEPENDENCIES_1)
AM_V_lt = $(am__v_lt_$(V))
am__v_lt_ = $(am__v_lt_$(AM_DEFAULT_VERBOSITY))
am__v_lt_0 = --silent
am__v_lt_1 = 
dump_LINK = $(LIBTOOL) $(AM_V_lt) --tag=CXX \
	$(AM_LIBTOOLFLAGS) $(LIBTOOLFLAGS) --mode=link $(CXXLD) \
	$(AM_CXXFLAGS) $(CXXFLAGS) $(dump_LDFLAGS) \
	$(LDFLAGS) -o $@
AM_V_P = $(am__v_P_$(V))
am__v_P_ = $(am__v_P_$(AM_DEFAULT_VERBOSITY))
am__v_P_0 = false
am__v_P_1 = :
AM_V_GEN = $(am__v_GEN_$(V))
am__v_GEN_ = $(am__v_GEN_$(AM_DEFAULT_VERBOSITY))
am__v_GEN_0 = @echo "  GEN     " $@;
am__v_GEN_1 = 
AM_V_at = $(am__v_at_$(V))
am__v_at_ = $(am__v_at_$(AM_DEFAULT_VERBOSITY))
am__v_at_0 = @
am__v_at_1 = 
DEFAULT_INCLUDES = -I. -I$(prefix)/include

am__mv = mv -f
CXXCOMPILE = $(CXX) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) \
	$(AM_CPPFLAGS) $(CPPFLAGS) $(AM_CXXFLAGS) $(CXXFLAGS)
LTCXXCOMPILE = $(LIBTOOL) $(AM_V_lt) --tag=CXX $(AM_LIBTOOLFLAGS) \
	$(LIBTOOLFLAGS) --mode=compile $(CXX) $(DEFS) \
	$(DEFAULT_INCLUDES) $(INCLUDES) $(AM_CPPFLAGS) $(CPPFLAGS) \
	$(AM_CXXFLAGS) $(CXXFLAGS)
AM_V_CXX = $(am__v_CXX_$(V))
am__v_CXX_ = $(am__v_CXX_$(AM_DEFAULT_VERBOSITY))
am__v_CXX_0 = @echo "  CXX     " $@;
am__v_CXX_1 = 
CXXLD = $(CXX)
CXXLINK = $(LIBTOOL) $(AM_V_lt) --tag=CXX $(AM_LIBTOOLFLAGS) \
	$(LIBTOOLFLAGS) --mode=link $(CXXLD) $(AM_CXXFLAGS) \
	$(CXXFLAGS) $(AM_LDFLAGS) $(LDFLAGS) -o $@
AM_V_CXXLD = $(am__v_CXXLD_$(V))
am__v_CXXLD_ = $(am__v_CXXLD_$(AM_DEFAULT_VERBOSITY))
am__v_CXXLD_0 = @echo "  CXXLD   " $@;
am__v_CXXLD_1 = 
SOURCES = $(dump_SOURCES)

AM_DEFAULT_VERBOSITY = 1

CPP = gcc -E
CPPFLAGS = 

CXX = g++
CXXCPP = g++ -E
CXXDEPMODE = depmode=gcc3
CXXFLAGS = -g -O2
CYGPATH_W = echo
DEFS = -DHAVE_CONFIG_H
DEPDIR = .
DLLTOOL = false
DOXYGEN_PAPER_SIZE = 
DSYMUTIL = 
DUMPBIN = 

ECHO_C = 
ECHO_N = -n
ECHO_T = 
EGREP = /bin/grep -E
ENABLE_VALGRIND_drd = no
ENABLE_VALGRIND_helgrind = no
ENABLE_VALGRIND_memcheck = no
ENABLE_VALGRIND_sgcheck = no
EXEEXT = 
FGREP = /bin/grep -F
FLEX = 

LD = /usr/bin/ld -m elf_x86_64
LDFLAGS =  -lpcre
LEX = 
LEXLIB = 
LEX_OUTPUT_ROOT = 
LIBOBJS = 
LIBS = 
LIBTOOL = $(SHELL) /usr/bin/libtool

OBJDUMP = objdump
OBJEXT = o

SHELL = /bin/bash

bindir = ${exec_prefix}/bin
build = x86_64-pc-linux-gnu
build_alias = 
build_cpu = x86_64
build_os = linux-gnu
build_vendor = pc
builddir = .
datadir = ${datarootdir}
datarootdir = ${prefix}/share
docdir = ${datarootdir}/doc/${PACKAGE_TARNAME}
dvidir = ${docdir}
exec_prefix = ${prefix}
host = x86_64-pc-linux-gnu
host_alias = 
host_cpu = x86_64
host_os = linux-gnu
host_vendor = pc
htmldir = ${docdir}
includedir = ${prefix}/include
infodir = ${datarootdir}/info
install_sh = 
libdir = ${exec_prefix}/lib
libexecdir = ${exec_prefix}/libexec
localedir = ${datarootdir}/locale
localstatedir = ${prefix}/var
mandir = ${datarootdir}/man
mkdir_p = $(MKDIR_P)
oldincludedir = /usr/include
pdfdir = ${docdir}
prefix = /usr/local/modsecurity
program_transform_name = s,x,x,
psdir = ${docdir}
runstatedir = ${localstatedir}/run
sbindir = ${exec_prefix}/sbin
sharedstatedir = ${prefix}/com
srcdir = .
sysconfdir = ${prefix}/etc
target_alias = 
#top_build_prefix = ../../
#top_builddir = ../..
#top_srcdir = ../..
valgrind_enabled_tools = 
valgrind_tools = memcheck helgrind drd sgcheck
dump_SOURCES = \
	dump.cc

dump_LDADD = \
	$(prefix)/lib/libmodsecurity.a

dump_LDFLAGS = \
	-lpthread

dump_CPPFLAGS = \
	$(GLOBAL_CFLAGS) \
	-std=c++11 \
	-g \
	-fPIC \
	-O3

.SUFFIXES:
.SUFFIXES: .cc .o


dump$(EXEEXT): $(dump_OBJECTS) $(dump_DEPENDENCIES) $(EXTRA_dump_DEPENDENCIES) 
	@rm -f dump$(EXEEXT)
	$(AM_V_CXXLD)$(dump_LINK) $(dump_OBJECTS) $(dump_LDADD) $(LIBS)


dump.o: dump.cc
	$(AM_V_CXX)$(CXX) $(DEFS) $(DEFAULT_INCLUDES) $(INCLUDES) $(dump_app_CPPFLAGS) $(CPPFLAGS) $(AM_CXXFLAGS) $(CXXFLAGS) -MT dump.o -MD -MP -MF $(DEPDIR)/dump.Tpo -c -o dump.o `test -f 'dump.cc' || echo '$(srcdir)/'`dump.cc
	$(AM_V_at)$(am__mv) $(DEPDIR)/dump.Tpo $(DEPDIR)/dump.Po

clean:
	rm dump.o dump.Tpo
