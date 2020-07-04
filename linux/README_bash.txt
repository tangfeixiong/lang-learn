hands-on: bash source build
===========================

Bash source
-----------

vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux$ git clone https://github.com/bminor/bash bminor/bash
Cloning into 'bminor/bash'...
remote: Enumerating objects: 1108, done.
remote: Counting objects: 100% (1108/1108), done.
remote: Compressing objects: 100% (815/815), done.
remote: Total 33427 (delta 693), reused 504 (delta 291), pack-reused 32319
Receiving objects: 100% (33427/33427), 228.20 MiB | 95.00 KiB/s, done.
Resolving deltas: 100% (28367/28367), done.
Checking out files: 100% (1307/1307), done.

Build
------

__configure__


vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash$ ./configure 
checking build system type... x86_64-pc-linux-gnu
checking host system type... x86_64-pc-linux-gnu

Beginning configuration for bash-5.0-release for x86_64-pc-linux-gnu

checking for gcc... gcc
checking whether the C compiler works... yes
checking for C compiler default output file name... a.out
checking for suffix of executables... 
checking whether we are cross compiling... no
checking for suffix of object files... o
checking whether we are using the GNU C compiler... yes
checking whether gcc accepts -g... yes
checking for gcc option to accept ISO C89... none needed
checking for strerror in -lcposix... no
checking how to run the C preprocessor... gcc -E
checking for grep that handles long lines and -e... /bin/grep
checking for egrep... /bin/grep -E
checking for ANSI C header files... yes
checking for sys/types.h... yes
checking for sys/stat.h... yes
checking for stdlib.h... yes
checking for string.h... yes
checking for memory.h... yes
checking for strings.h... yes
checking for inttypes.h... yes
checking for stdint.h... yes
checking for unistd.h... yes
checking minix/config.h usability... no
checking minix/config.h presence... no
checking for minix/config.h... no
checking whether it is safe to define __EXTENSIONS__... yes
checking for special C compiler options needed for large files... no
checking for _FILE_OFFSET_BITS value needed for large files... no
checking whether gcc needs -traditional... no
checking for a BSD-compatible install... /usr/bin/install -c
checking for ar... ar
checking for ranlib... ranlib
checking for bison... bison -y
checking whether make sets $(MAKE)... yes
checking for an ANSI C-conforming const... yes
checking for inline... inline
checking whether byte ordering is bigendian... no
checking for preprocessor stringizing operator... yes
checking for long double with more range or precision than double... yes
checking for function prototypes... yes
checking whether char is unsigned... no
checking for working volatile... yes
checking for C/C++ restrict keyword... __restrict
checking whether NLS is requested... yes
checking for msgfmt... /usr/bin/msgfmt
checking for gmsgfmt... /usr/bin/msgfmt
checking for xgettext... /usr/bin/xgettext
checking for msgmerge... /usr/bin/msgmerge
checking for off_t... yes
checking for size_t... yes
checking for working alloca.h... yes
checking for alloca... yes
checking for stdlib.h... (cached) yes
checking for unistd.h... (cached) yes
checking for sys/param.h... yes
checking for sys/time.h... yes
checking for getpagesize... yes
checking for working mmap... no
checking whether we are using the GNU C Library 2.1 or newer... yes
checking whether integer division by zero raises SIGFPE... yes
checking for inttypes.h... yes
checking for stdint.h... yes
checking for unsigned long long... yes
checking for inttypes.h... yes
checking whether the inttypes.h PRIxNN macros are broken... no
checking for ld used by GCC... /usr/bin/ld
checking if the linker (/usr/bin/ld) is GNU ld... yes
checking for shared library run path origin... done
checking argz.h usability... yes
checking argz.h presence... yes
checking for argz.h... yes
checking limits.h usability... yes
checking limits.h presence... yes
checking for limits.h... yes
checking locale.h usability... yes
checking locale.h presence... yes
checking for locale.h... yes
checking nl_types.h usability... yes
checking nl_types.h presence... yes
checking for nl_types.h... yes
checking malloc.h usability... yes
checking malloc.h presence... yes
checking for malloc.h... yes
checking stddef.h usability... yes
checking stddef.h presence... yes
checking for stddef.h... yes
checking for stdlib.h... (cached) yes
checking for string.h... (cached) yes
checking for unistd.h... (cached) yes
checking for sys/param.h... (cached) yes
checking for feof_unlocked... yes
checking for fgets_unlocked... yes
checking for getc_unlocked... yes
checking for getcwd... yes
checking for getegid... yes
checking for geteuid... yes
checking for getgid... yes
checking for getuid... yes
checking for mempcpy... yes
checking for munmap... yes
checking for putenv... yes
checking for setenv... yes
checking for setlocale... yes
checking for localeconv... yes
checking for stpcpy... yes
checking for strcasecmp... yes
checking for strdup... yes
checking for strtoul... yes
checking for tsearch... yes
checking for __argz_count... yes
checking for __argz_stringify... yes
checking for __argz_next... yes
checking for __fsetlocking... yes
checking for iconv... yes
checking for iconv declaration... 
         extern size_t iconv (iconv_t cd, char * *inbuf, size_t *inbytesleft, char * *outbuf, size_t *outbytesleft);
checking for nl_langinfo and CODESET... yes
checking for LC_MESSAGES... yes
checking for bison... bison
checking version of bison... 3.0.4, ok
checking whether NLS is requested... yes
checking whether included gettext is requested... no
checking for GNU gettext in libc... yes
checking whether to use NLS... yes
checking where the gettext function comes from... libc
checking for dirent.h that defines DIR... yes
checking for library containing opendir... none required
checking whether time.h and sys/time.h may both be included... yes
checking for inttypes.h... (cached) yes
checking for unistd.h... (cached) yes
checking for stdlib.h... (cached) yes
checking stdarg.h usability... yes
checking stdarg.h presence... yes
checking for stdarg.h... yes
checking varargs.h usability... no
checking varargs.h presence... no
checking for varargs.h... no
checking for limits.h... (cached) yes
checking for string.h... (cached) yes
checking for memory.h... (cached) yes
checking for locale.h... (cached) yes
checking termcap.h usability... yes
checking termcap.h presence... yes
checking for termcap.h... yes
checking termio.h usability... yes
checking termio.h presence... yes
checking for termio.h... yes
checking termios.h usability... yes
checking termios.h presence... yes
checking for termios.h... yes
checking dlfcn.h usability... yes
checking dlfcn.h presence... yes
checking for dlfcn.h... yes
checking stdbool.h usability... yes
checking stdbool.h presence... yes
checking for stdbool.h... yes
checking for stddef.h... (cached) yes
checking for stdint.h... (cached) yes
checking netdb.h usability... yes
checking netdb.h presence... yes
checking for netdb.h... yes
checking pwd.h usability... yes
checking pwd.h presence... yes
checking for pwd.h... yes
checking grp.h usability... yes
checking grp.h presence... yes
checking for grp.h... yes
checking for strings.h... (cached) yes
checking regex.h usability... yes
checking regex.h presence... yes
checking for regex.h... yes
checking syslog.h usability... yes
checking syslog.h presence... yes
checking for syslog.h... yes
checking ulimit.h usability... yes
checking ulimit.h presence... yes
checking for ulimit.h... yes
checking sys/pte.h usability... no
checking sys/pte.h presence... no
checking for sys/pte.h... no
checking sys/stream.h usability... no
checking sys/stream.h presence... no
checking for sys/stream.h... no
checking sys/select.h usability... yes
checking sys/select.h presence... yes
checking for sys/select.h... yes
checking sys/file.h usability... yes
checking sys/file.h presence... yes
checking for sys/file.h... yes
checking sys/ioctl.h usability... yes
checking sys/ioctl.h presence... yes
checking for sys/ioctl.h... yes
checking sys/mman.h usability... yes
checking sys/mman.h presence... yes
checking for sys/mman.h... yes
checking for sys/param.h... (cached) yes
checking sys/socket.h usability... yes
checking sys/socket.h presence... yes
checking for sys/socket.h... yes
checking for sys/stat.h... (cached) yes
checking for sys/time.h... (cached) yes
checking sys/times.h usability... yes
checking sys/times.h presence... yes
checking for sys/times.h... yes
checking for sys/types.h... (cached) yes
checking sys/wait.h usability... yes
checking sys/wait.h presence... yes
checking for sys/wait.h... yes
checking netinet/in.h usability... yes
checking netinet/in.h presence... yes
checking for netinet/in.h... yes
checking arpa/inet.h usability... yes
checking arpa/inet.h presence... yes
checking for arpa/inet.h... yes
checking for sys/ptem.h... no
checking for sys/resource.h... yes
checking for working alloca.h... (cached) yes
checking for alloca... (cached) yes
checking for uid_t in sys/types.h... yes
checking for unistd.h... (cached) yes
checking for working chown... yes
checking whether getpgrp requires zero arguments... yes
checking for vprintf... yes
checking for _doprnt... no
checking for working strcoll... yes
checking return type of signal handlers... void
checking for __setostype... no
checking for wait3... yes
checking for mkfifo... yes
checking for dup2... yes
checking for eaccess... yes
checking for fcntl... yes
checking for getdtablesize... yes
checking for getgroups... yes
checking for gethostname... yes
checking for getpagesize... (cached) yes
checking for getpeername... yes
checking for getrlimit... yes
checking for getrusage... yes
checking for gettimeofday... yes
checking for kill... yes
checking for killpg... yes
checking for lstat... yes
checking for pselect... yes
checking for readlink... yes
checking for select... yes
checking for setdtablesize... no
checking for setitimer... yes
checking for tcgetpgrp... yes
checking for uname... yes
checking for ulimit... yes
checking for waitpid... yes
checking for rename... yes
checking for bcopy... yes
checking for bzero... yes
checking for confstr... yes
checking for faccessat... yes
checking for fnmatch... yes
checking for getaddrinfo... yes
checking for gethostbyname... yes
checking for getservbyname... yes
checking for getservent... yes
checking for inet_aton... yes
checking for imaxdiv... yes
checking for memmove... yes
checking for pathconf... yes
checking for putenv... (cached) yes
checking for raise... yes
checking for random... yes
checking for regcomp... yes
checking for regexec... yes
checking for setenv... (cached) yes
checking for setlinebuf... yes
checking for setlocale... (cached) yes
checking for setvbuf... yes
checking for siginterrupt... yes
checking for strchr... yes
checking for sysconf... yes
checking for syslog... yes
checking for tcgetattr... yes
checking for times... yes
checking for ttyname... yes
checking for tzset... yes
checking for unsetenv... yes
checking for vasprintf... yes
checking for asprintf... yes
checking for isascii... yes
checking for isblank... yes
checking for isgraph... yes
checking for isprint... yes
checking for isspace... yes
checking for isxdigit... yes
checking for getpwent... yes
checking for getpwnam... yes
checking for getpwuid... yes
checking for mkstemp... yes
checking for getcwd... (cached) yes
checking for memset... yes
checking for strcasecmp... (cached) yes
checking for strcasestr... yes
checking for strerror... yes
checking for strftime... yes
checking for strnlen... yes
checking for strpbrk... yes
checking for strstr... yes
checking for strtod... yes
checking for strtol... yes
checking for strtoul... (cached) yes
checking for strtoll... yes
checking for strtoull... yes
checking for strtoimax... yes
checking for strtoumax... yes
checking for dprintf... yes
checking for strchrnul... yes
checking for strdup... (cached) yes
checking libaudit.h usability... no
checking libaudit.h presence... no
checking for libaudit.h... no
checking whether AUDIT_USER_TTY is declared... yes
checking whether confstr is declared... yes
checking whether printf is declared... yes
checking whether sbrk is declared... yes
checking whether setregid is declared... yes
checking whether strcpy is declared... yes
checking whether strsignal is declared... yes
checking whether strtold is declared... yes
checking for broken strtold... no
checking for declaration of strtoimax... yes
checking for declaration of strtol... yes
checking for declaration of strtoll... yes
checking for declaration of strtoul... yes
checking for declaration of strtoull... yes
checking for declaration of strtoumax... yes
checking for alarm... yes
checking for sbrk... yes
checking for fpurge... no
checking for __fpurge... yes
checking for snprintf... yes
checking for vsnprintf... yes
checking for working mktime... yes
checking for argz.h... (cached) yes
checking errno.h usability... yes
checking errno.h presence... yes
checking for errno.h... yes
checking fcntl.h usability... yes
checking fcntl.h presence... yes
checking for fcntl.h... yes
checking for malloc.h... (cached) yes
checking stdio_ext.h usability... yes
checking stdio_ext.h presence... yes
checking for stdio_ext.h... yes
checking for getpagesize... (cached) yes
checking for working mmap... (cached) no
checking for __argz_count... (cached) yes
checking for __argz_next... (cached) yes
checking for __argz_stringify... (cached) yes
checking for dcgettext... yes
checking for mempcpy... (cached) yes
checking for munmap... (cached) yes
checking for mremap... yes
checking for stpcpy... (cached) yes
checking for strcspn... yes
checking wctype.h usability... yes
checking wctype.h presence... yes
checking for wctype.h... yes
checking wchar.h usability... yes
checking wchar.h presence... yes
checking for wchar.h... yes
checking langinfo.h usability... yes
checking langinfo.h presence... yes
checking for langinfo.h... yes
checking mbstr.h usability... no
checking mbstr.h presence... no
checking for mbstr.h... no
checking for mbrlen... yes
checking for mbscasecmp... no
checking for mbscmp... no
checking for mbsnrtowcs... yes
checking for mbsrtowcs... yes
checking for mbschr... no
checking for wcrtomb... yes
checking for wcscoll... yes
checking for wcsdup... yes
checking for wcwidth... yes
checking for wctype... yes
checking for wcswidth... yes
checking whether mbrtowc and mbstate_t are properly declared... yes
checking for iswlower... yes
checking for iswupper... yes
checking for towlower... yes
checking for towupper... yes
checking for iswctype... yes
checking for nl_langinfo and CODESET... yes
checking for wchar_t in wchar.h... yes
checking for wctype_t in wctype.h... yes
checking for wint_t in wctype.h... yes
checking for wcwidth broken with unicode combining characters... no
checking for locale_charset... no
checking size of wchar_t... 4
checking for dlopen in -ldl... yes
checking for dlopen... yes
checking for dlclose... yes
checking for dlsym... yes
checking whether sys_siglist is declared... yes
checking type of array argument to getgroups... gid_t
checking for off_t... (cached) yes
checking for mode_t... yes
checking for uid_t in sys/types.h... (cached) yes
checking for pid_t... yes
checking for size_t... (cached) yes
checking for uintptr_t... yes
checking for ssize_t... yes
checking for time_t... yes
checking for long long... long long
checking for unsigned long long... unsigned long long
checking return type of signal handlers... (cached) void
checking for sig_atomic_t in signal.h... yes
checking size of char... 1
checking size of short... 2
checking size of int... 4
checking size of long... 8
checking size of char *... 8
checking size of double... 8
checking size of long long... 8
checking for u_int... yes
checking for u_long... yes
checking for bits16_t... no
checking for u_bits16_t... no
checking for bits32_t... no
checking for u_bits32_t... no
checking for bits64_t... no
checking for ptrdiff_t... yes
checking whether stat file-mode macros are broken... no
checking whether #! works in shell scripts... yes
checking whether the ctype macros accept non-ascii characters... no
checking if dup2 fails to clear the close-on-exec flag... no
checking whether pgrps need synchronization... no
checking for type of signal functions... posix
checking for sys_errlist and sys_nerr... yes
checking for sys_siglist in system C library... yes
checking for _sys_siglist in signal.h or unistd.h... yes
checking for _sys_siglist in system C library... yes
checking whether signal handlers are of type void... yes
checking for clock_t... yes
checking for sigset_t... yes
checking for sig_atomic_t... yes
checking for quad_t... yes
checking for intmax_t... yes
checking for uintmax_t... yes
checking for socklen_t... yes
checking for size and type of struct rlimit fields... rlim_t
checking size of intmax_t... 8
checking for struct termios.c_line... yes
checking for struct termio.c_line... yes
checking for struct dirent.d_ino... yes
checking for struct dirent.d_fileno... yes
checking for struct dirent.d_namlen... no
checking for struct winsize in sys/ioctl.h and termios.h... sys/ioctl.h
checking for struct timeval in sys/time.h and time.h... yes
checking for struct stat.st_blocks... yes
checking whether struct tm is in sys/time.h or time.h... time.h
checking for struct tm.tm_zone... yes
checking for struct timezone in sys/time.h and time.h... yes
checking for offset of exit status in return status from wait... 8
checking for struct timespec in <time.h>... yes
checking for struct stat.st_atim.tv_nsec... yes
checking whether struct stat.st_atim is of type struct timespec... yes
checking for working sbrk... yes
checking for the existence of strsignal... yes
checking if opendir() opens non-directories... no
checking whether ulimit can substitute for getdtablesize... yes
checking whether fpurge is declared... no
checking to see if getenv can be redefined... yes
checking if getcwd() will dynamically allocate memory with 0 size... yes
checking for presence of POSIX-style sigsetjmp/siglongjmp... present
checking whether or not strcoll and strcmp differ... no
checking for standard-conformant snprintf... yes
checking for standard-conformant vsnprintf... yes
checking for standard-conformant putenv declaration... yes
checking for standard-conformant unsetenv declaration... yes
checking for printf floating point output in hex notation... yes
checking whether fnmatch can be used to check bracket equivalence classes... no
checking if signal handlers must be reinstalled when invoked... no
checking for presence of necessary job control definitions... present
checking for presence of named pipes... present
checking whether termios.h defines TIOCGWINSZ... no
checking whether sys/ioctl.h defines TIOCGWINSZ... yes
checking for TIOCSTAT in sys/ioctl.h... no
checking for FIONREAD in sys/ioctl.h... yes
checking whether WCONTINUED flag to waitpid is unavailable or available but broken... no
checking for speed_t in sys/types.h... no
checking whether getpw functions are declared in pwd.h... yes
checking for unusable real-time signals due to large values... no
checking for tgetent... no
checking for tgetent in -ltermcap... yes
checking which library has the termcap functions... using libtermcap
checking whether /dev/fd is available... standard
checking whether /dev/stdin stdout stderr are available... present
checking for default mail directory... /var/mail
checking shared object configuration for loadable builtins... supported
configure: creating ./config.status
config.status: creating Makefile
config.status: creating builtins/Makefile
config.status: creating lib/readline/Makefile
config.status: creating lib/glob/Makefile
config.status: creating lib/intl/Makefile
config.status: creating lib/malloc/Makefile
config.status: creating lib/sh/Makefile
config.status: creating lib/termcap/Makefile
config.status: creating lib/tilde/Makefile
config.status: creating doc/Makefile
config.status: creating support/Makefile
config.status: creating po/Makefile.in
config.status: creating examples/loadables/Makefile
config.status: creating examples/loadables/Makefile.inc
config.status: creating examples/loadables/perl/Makefile
config.status: creating support/bash.pc
config.status: creating support/bashbug.sh
config.status: creating config.h
config.status: executing default-1 commands
config.status: creating po/POTFILES
config.status: creating po/Makefile
config.status: executing default commands


__make__


vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash$ make
rm -f mksyntax
gcc -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib   -g -O2   -rdynamic -g -O2 -Wno-parentheses -Wno-format-security   -rdynamic -g -O2  -o mksyntax ./mksyntax.c 
rm -f syntax.c
./mksyntax -o syntax.c
/bin/sh ./support/mkversion.sh -b -S . -s release -d 5.0 -o newversion.h \
	&& mv newversion.h version.h
gcc -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib   -g -O2  -DBUILDTOOL -c -o buildversion.o ./version.c
gcc -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib   -g -O2   -rdynamic -g -O2 -Wno-parentheses -Wno-format-security   -rdynamic -g -O2  -o bashversion ./support/bashversion.c buildversion.o 

	  ***********************************************************
	  *                                                         *
	  * GNU bash, version 5.0.17(1)-release (x86_64-pc-linux-gnu)
	  *                                                         *
	  ***********************************************************

rm -f shell.o
gcc  -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib    -g -O2 -Wno-parentheses -Wno-format-security -c shell.c
rm -f eval.o
gcc  -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib    -g -O2 -Wno-parentheses -Wno-format-security -c eval.c
make[1]: Entering directory '/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash/builtins'
rm -f mkbuiltins.o
gcc -c  -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2  mkbuiltins.c
gcc -rdynamic -g -O2 -Wno-parentheses -Wno-format-security -rdynamic -g -O2  -o mkbuiltins mkbuiltins.o -ldl 
./mkbuiltins -externfile builtext.h -structfile builtins.c \
    -noproduction -D .   ./alias.def ./bind.def ./break.def ./builtin.def ./caller.def ./cd.def ./colon.def ./command.def ./declare.def ./echo.def ./enable.def ./eval.def ./getopts.def ./exec.def ./exit.def ./fc.def ./fg_bg.def ./hash.def ./help.def ./history.def ./jobs.def ./kill.def ./let.def ./read.def ./return.def ./set.def ./setattr.def ./shift.def ./source.def ./suspend.def ./test.def ./times.def ./trap.def ./type.def ./ulimit.def ./umask.def ./wait.def ./reserved.def ./pushd.def ./shopt.def ./printf.def ./complete.def ./mapfile.def
make[1]: Leaving directory '/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash/builtins'
rm -f execute_cmd.o
gcc  -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib    -g -O2 -Wno-parentheses -Wno-format-security -c execute_cmd.c
rm -f y.tab.o
gcc  -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib    -g -O2 -Wno-parentheses -Wno-format-security -c y.tab.c
rm -f general.o
gcc  -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib    -g -O2 -Wno-parentheses -Wno-format-security -c general.c
rm -f make_cmd.o
gcc  -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib    -g -O2 -Wno-parentheses -Wno-format-security -c make_cmd.c
rm -f print_cmd.o
gcc  -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib    -g -O2 -Wno-parentheses -Wno-format-security -c print_cmd.c
print_cmd.c: In function ‘make_command_string_internal’:
print_cmd.c:173:14: warning: zero-length gnu_printf format string [-Wformat-zero-length]
     cprintf ("");
              ^~
rm -f dispose_cmd.o
gcc  -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib    -g -O2 -Wno-parentheses -Wno-format-security -c dispose_cmd.c
rm -f variables.o
gcc  -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib    -g -O2 -Wno-parentheses -Wno-format-security -c variables.c
rm -f copy_cmd.o
gcc  -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib    -g -O2 -Wno-parentheses -Wno-format-security -c copy_cmd.c
rm -f error.o
gcc  -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib    -g -O2 -Wno-parentheses -Wno-format-security -c error.c
rm -f expr.o
gcc  -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib    -g -O2 -Wno-parentheses -Wno-format-security -c expr.c
rm -f flags.o
gcc  -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib    -g -O2 -Wno-parentheses -Wno-format-security -c flags.c
rm -f jobs.o
gcc  -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib    -g -O2 -Wno-parentheses -Wno-format-security -c jobs.c
rm -f subst.o
gcc  -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib    -g -O2 -Wno-parentheses -Wno-format-security -c subst.c
rm -f hashcmd.o
gcc  -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib    -g -O2 -Wno-parentheses -Wno-format-security -c hashcmd.c
rm -f hashlib.o
gcc  -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib    -g -O2 -Wno-parentheses -Wno-format-security -c hashlib.c
rm -f mailcheck.o
gcc  -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib    -g -O2 -Wno-parentheses -Wno-format-security -c mailcheck.c
rm -f mksignames.o
gcc -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib   -g -O2  -DBUILDTOOL -c ./support/mksignames.c
rm -f buildsignames.o
gcc -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib   -g -O2  -DBUILDTOOL -o buildsignames.o -c ./support/signames.c
rm -f mksignames
gcc -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib   -g -O2   -rdynamic -g -O2 -Wno-parentheses -Wno-format-security   -rdynamic -g -O2  -o mksignames mksignames.o buildsignames.o 
rm -f lsignames.h
./mksignames lsignames.h
if cmp -s lsignames.h signames.h ; then :; else rm -f signames.h ; cp lsignames.h signames.h ; fi
rm -f trap.o
gcc  -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib    -g -O2 -Wno-parentheses -Wno-format-security -c trap.c
rm -f input.o
gcc  -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib    -g -O2 -Wno-parentheses -Wno-format-security -c input.c
rm -f unwind_prot.o
gcc  -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib    -g -O2 -Wno-parentheses -Wno-format-security -c unwind_prot.c
rm -f pathexp.o
gcc  -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib    -g -O2 -Wno-parentheses -Wno-format-security -c pathexp.c
rm -f sig.o
gcc  -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib    -g -O2 -Wno-parentheses -Wno-format-security -c sig.c
rm -f test.o
gcc  -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib    -g -O2 -Wno-parentheses -Wno-format-security -c test.c
rm -f version.o
gcc  -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib    -g -O2 -Wno-parentheses -Wno-format-security -c version.c
rm -f alias.o
gcc  -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib    -g -O2 -Wno-parentheses -Wno-format-security -c alias.c
rm -f array.o
gcc  -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib    -g -O2 -Wno-parentheses -Wno-format-security -c array.c
rm -f arrayfunc.o
gcc  -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib    -g -O2 -Wno-parentheses -Wno-format-security -c arrayfunc.c
rm -f assoc.o
gcc  -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib    -g -O2 -Wno-parentheses -Wno-format-security -c assoc.c
rm -f braces.o
gcc  -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib    -g -O2 -Wno-parentheses -Wno-format-security -c braces.c
rm -f bracecomp.o
gcc  -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib    -g -O2 -Wno-parentheses -Wno-format-security -c bracecomp.c
rm -f bashhist.o
gcc  -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib    -g -O2 -Wno-parentheses -Wno-format-security -c bashhist.c
rm -f bashline.o
gcc  -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib    -g -O2 -Wno-parentheses -Wno-format-security -c bashline.c
rm -f list.o
gcc  -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib    -g -O2 -Wno-parentheses -Wno-format-security -c list.c
rm -f stringlib.o
gcc  -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib    -g -O2 -Wno-parentheses -Wno-format-security -c stringlib.c
rm -f locale.o
gcc  -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib    -g -O2 -Wno-parentheses -Wno-format-security -c locale.c
rm -f findcmd.o
gcc  -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib    -g -O2 -Wno-parentheses -Wno-format-security -c findcmd.c
rm -f redir.o
gcc  -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib    -g -O2 -Wno-parentheses -Wno-format-security -c redir.c
rm -f pcomplete.o
gcc  -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib    -g -O2 -Wno-parentheses -Wno-format-security -c pcomplete.c
rm -f pcomplib.o
gcc  -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib    -g -O2 -Wno-parentheses -Wno-format-security -c pcomplib.c
rm -f syntax.o
gcc  -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib    -g -O2 -Wno-parentheses -Wno-format-security -c syntax.c
rm -f xmalloc.o
gcc  -DPROGRAM='"bash"' -DCONF_HOSTTYPE='"x86_64"' -DCONF_OSTYPE='"linux-gnu"' -DCONF_MACHTYPE='"x86_64-pc-linux-gnu"' -DCONF_VENDOR='"pc"' -DLOCALEDIR='"/usr/local/share/locale"' -DPACKAGE='"bash"' -DSHELL -DHAVE_CONFIG_H   -I.  -I. -I./include -I./lib    -g -O2 -Wno-parentheses -Wno-format-security -c xmalloc.c
make[1]: Entering directory '/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash/builtins'
make[1]: Warning: File 'mkbuiltins' has modification time 332 s in the future
rm -f builtins.o
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security builtins.c
rm -f alias.o
./mkbuiltins -D . alias.def
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security alias.c || ( rm -f alias.c ; exit 1 )
rm -f alias.c
rm -f bind.o
./mkbuiltins -D . bind.def
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security bind.c || ( rm -f bind.c ; exit 1 )
rm -f bind.c
rm -f break.o
./mkbuiltins -D . break.def
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security break.c || ( rm -f break.c ; exit 1 )
rm -f break.c
rm -f builtin.o
./mkbuiltins -D . builtin.def
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security builtin.c || ( rm -f builtin.c ; exit 1 )
rm -f builtin.c
rm -f caller.o
./mkbuiltins -D . caller.def
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security caller.c || ( rm -f caller.c ; exit 1 )
rm -f caller.c
rm -f cd.o
./mkbuiltins -D . cd.def
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security cd.c || ( rm -f cd.c ; exit 1 )
rm -f cd.c
rm -f colon.o
./mkbuiltins -D . colon.def
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security colon.c || ( rm -f colon.c ; exit 1 )
rm -f colon.c
rm -f command.o
./mkbuiltins -D . command.def
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security command.c || ( rm -f command.c ; exit 1 )
rm -f command.c
rm -f common.o
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security common.c
rm -f declare.o
./mkbuiltins -D . declare.def
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security declare.c || ( rm -f declare.c ; exit 1 )
rm -f declare.c
rm -f echo.o
./mkbuiltins -D . echo.def
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security echo.c || ( rm -f echo.c ; exit 1 )
rm -f echo.c
rm -f enable.o
./mkbuiltins -D . enable.def
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security enable.c || ( rm -f enable.c ; exit 1 )
rm -f enable.c
rm -f eval.o
./mkbuiltins -D . eval.def
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security eval.c || ( rm -f eval.c ; exit 1 )
rm -f eval.c
rm -f evalfile.o
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security evalfile.c
rm -f evalstring.o
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security evalstring.c
rm -f exec.o
./mkbuiltins -D . exec.def
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security exec.c || ( rm -f exec.c ; exit 1 )
rm -f exec.c
rm -f exit.o
./mkbuiltins -D . exit.def
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security exit.c || ( rm -f exit.c ; exit 1 )
rm -f exit.c
rm -f fc.o
./mkbuiltins -D . fc.def
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security fc.c || ( rm -f fc.c ; exit 1 )
rm -f fc.c
rm -f fg_bg.o
./mkbuiltins -D . fg_bg.def
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security fg_bg.c || ( rm -f fg_bg.c ; exit 1 )
rm -f fg_bg.c
rm -f hash.o
./mkbuiltins -D . hash.def
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security hash.c || ( rm -f hash.c ; exit 1 )
rm -f hash.c
rm -f help.o
./mkbuiltins -D . help.def
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security help.c || ( rm -f help.c ; exit 1 )
rm -f help.c
rm -f history.o
./mkbuiltins -D . history.def
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security history.c || ( rm -f history.c ; exit 1 )
rm -f history.c
rm -f jobs.o
./mkbuiltins -D . jobs.def
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security jobs.c || ( rm -f jobs.c ; exit 1 )
rm -f jobs.c
rm -f kill.o
./mkbuiltins -D . kill.def
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security kill.c || ( rm -f kill.c ; exit 1 )
rm -f kill.c
rm -f let.o
./mkbuiltins -D . let.def
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security let.c || ( rm -f let.c ; exit 1 )
rm -f let.c
rm -f mapfile.o
./mkbuiltins -D . mapfile.def
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security mapfile.c || ( rm -f mapfile.c ; exit 1 )
rm -f mapfile.c
rm -f pushd.o
./mkbuiltins -D . pushd.def
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security pushd.c || ( rm -f pushd.c ; exit 1 )
rm -f pushd.c
rm -f read.o
./mkbuiltins -D . read.def
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security read.c || ( rm -f read.c ; exit 1 )
rm -f read.c
rm -f return.o
./mkbuiltins -D . return.def
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security return.c || ( rm -f return.c ; exit 1 )
rm -f return.c
rm -f set.o
./mkbuiltins -D . set.def
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security set.c || ( rm -f set.c ; exit 1 )
rm -f set.c
rm -f setattr.o
./mkbuiltins -D . setattr.def
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security setattr.c || ( rm -f setattr.c ; exit 1 )
rm -f setattr.c
rm -f shift.o
./mkbuiltins -D . shift.def
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security shift.c || ( rm -f shift.c ; exit 1 )
rm -f shift.c
rm -f source.o
./mkbuiltins -D . source.def
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security source.c || ( rm -f source.c ; exit 1 )
rm -f source.c
rm -f suspend.o
./mkbuiltins -D . suspend.def
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security suspend.c || ( rm -f suspend.c ; exit 1 )
rm -f suspend.c
rm -f test.o
./mkbuiltins -D . test.def
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security test.c || ( rm -f test.c ; exit 1 )
rm -f test.c
rm -f times.o
./mkbuiltins -D . times.def
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security times.c || ( rm -f times.c ; exit 1 )
rm -f times.c
rm -f trap.o
./mkbuiltins -D . trap.def
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security trap.c || ( rm -f trap.c ; exit 1 )
rm -f trap.c
rm -f type.o
./mkbuiltins -D . type.def
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security type.c || ( rm -f type.c ; exit 1 )
rm -f type.c
gcc  -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2  -rdynamic -g -O2 -Wno-parentheses -Wno-format-security -rdynamic -g -O2  -o psize.aux ./psize.c
/bin/sh ./psize.sh > pipesize.h
rm -f ulimit.o
./mkbuiltins -D . ulimit.def
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security ulimit.c || ( rm -f ulimit.c ; exit 1 )
rm -f ulimit.c
rm -f umask.o
./mkbuiltins -D . umask.def
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security umask.c || ( rm -f umask.c ; exit 1 )
rm -f umask.c
rm -f wait.o
./mkbuiltins -D . wait.def
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security wait.c || ( rm -f wait.c ; exit 1 )
rm -f wait.c
rm -f getopts.o
./mkbuiltins -D . getopts.def
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security getopts.c || ( rm -f getopts.c ; exit 1 )
rm -f getopts.c
rm -f shopt.o
./mkbuiltins -D . shopt.def
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security shopt.c || ( rm -f shopt.c ; exit 1 )
rm -f shopt.c
rm -f printf.o
./mkbuiltins -D . printf.def
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security printf.c || ( rm -f printf.c ; exit 1 )
rm -f printf.c
rm -f getopt.o
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security getopt.c
rm -f bashgetopt.o
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security bashgetopt.c
rm -f complete.o
./mkbuiltins -D . complete.def
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I..  -I.. -I../include -I../lib -I.    -g -O2 -Wno-parentheses -Wno-format-security complete.c || ( rm -f complete.c ; exit 1 )
rm -f complete.c
rm -f libbuiltins.a
ar cr libbuiltins.a builtins.o alias.o bind.o break.o builtin.o caller.o cd.o colon.o command.o common.o declare.o echo.o enable.o eval.o evalfile.o evalstring.o exec.o exit.o fc.o fg_bg.o hash.o help.o history.o jobs.o kill.o let.o mapfile.o pushd.o read.o return.o set.o setattr.o shift.o source.o suspend.o test.o times.o trap.o type.o ulimit.o umask.o wait.o getopts.o shopt.o printf.o getopt.o bashgetopt.o complete.o
ranlib libbuiltins.a
make[1]: warning:  Clock skew detected.  Your build may be incomplete.
make[1]: Leaving directory '/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash/builtins'
making lib/glob/libglob.a in ./lib/glob
make[1]: Entering directory '/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash/lib/glob'
make[1]: Warning: File '/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash/pathnames.h' has modification time 316 s in the future
rm -f glob.o
gcc -c  -DHAVE_CONFIG_H -DSHELL -I. -I../.. -I../.. -I../../include -I../../lib   -g -O2 -Wno-parentheses -Wno-format-security  glob.c
rm -f strmatch.o
gcc -c  -DHAVE_CONFIG_H -DSHELL -I. -I../.. -I../.. -I../../include -I../../lib   -g -O2 -Wno-parentheses -Wno-format-security  strmatch.c
rm -f smatch.o
gcc -c  -DHAVE_CONFIG_H -DSHELL -I. -I../.. -I../.. -I../../include -I../../lib   -g -O2 -Wno-parentheses -Wno-format-security  smatch.c
rm -f xmbsrtowcs.o
gcc -c  -DHAVE_CONFIG_H -DSHELL -I. -I../.. -I../.. -I../../include -I../../lib   -g -O2 -Wno-parentheses -Wno-format-security  xmbsrtowcs.c
rm -f gmisc.o
gcc -c  -DHAVE_CONFIG_H -DSHELL -I. -I../.. -I../.. -I../../include -I../../lib   -g -O2 -Wno-parentheses -Wno-format-security  gmisc.c
rm -f -f libglob.a
ar cr libglob.a glob.o strmatch.o smatch.o xmbsrtowcs.o gmisc.o
test -n "ranlib" && ranlib libglob.a
make[1]: warning:  Clock skew detected.  Your build may be incomplete.
make[1]: Leaving directory '/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash/lib/glob'
making lib/sh/libsh.a in ./lib/sh
make[1]: Entering directory '/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash/lib/sh'
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   clktck.c
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   clock.c
make[1]: Warning: File '/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash/pathnames.h' has modification time 314 s in the future
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   getenv.c
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   oslib.c
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   setlinebuf.c
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   strnlen.c
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   itos.c
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   zread.c
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   zwrite.c
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   shtty.c
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   shmatch.c
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   eaccess.c
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   netconn.c
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   netopen.c
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   timeval.c
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   makepath.c
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   pathcanon.c
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   pathphys.c
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   tmpfile.c
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   stringlist.c
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   stringvec.c
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   spell.c
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   shquote.c
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   strtrans.c
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   snprintf.c
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   mailstat.c
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   fmtulong.c
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   fmtullong.c
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   fmtumax.c
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   zcatfd.c
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   zmapfd.c
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   winsize.c
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   wcsdup.c
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   fpurge.c
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   zgetline.c
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   mbscmp.c
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   uconvert.c
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   ufuncs.c
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   casemod.c
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   input_avail.c
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   mbscasecmp.c
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   fnxform.c
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   unicode.c
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   shmbchar.c
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   utf8.c
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   wcsnwidth.c
gcc -c   -I. -I../.. -I../.. -I../../lib -I../../include -I.  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security   mbschr.c
rm -f libsh.a
ar cr libsh.a clktck.o clock.o getenv.o oslib.o setlinebuf.o strnlen.o itos.o zread.o zwrite.o shtty.o shmatch.o eaccess.o netconn.o netopen.o timeval.o makepath.o pathcanon.o pathphys.o tmpfile.o stringlist.o stringvec.o spell.o shquote.o strtrans.o snprintf.o mailstat.o fmtulong.o fmtullong.o fmtumax.o zcatfd.o zmapfd.o winsize.o wcsdup.o fpurge.o zgetline.o mbscmp.o uconvert.o ufuncs.o casemod.o input_avail.o mbscasecmp.o fnxform.o unicode.o shmbchar.o utf8.o wcsnwidth.o mbschr.o
test -n "ranlib" && ranlib libsh.a
make[1]: warning:  Clock skew detected.  Your build may be incomplete.
make[1]: Leaving directory '/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash/lib/sh'
making lib/readline/libreadline.a in ./lib/readline
make[1]: Entering directory '/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash/lib/readline'
rm -f readline.o
gcc -c -DHAVE_CONFIG_H -DSHELL   -I. -I/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash -I../.. -I../../lib  -g -O2 -Wno-parentheses -Wno-format-security  readline.c
rm -f vi_mode.o
gcc -c -DHAVE_CONFIG_H -DSHELL   -I. -I/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash -I../.. -I../../lib  -g -O2 -Wno-parentheses -Wno-format-security  vi_mode.c
rm -f funmap.o
gcc -c -DHAVE_CONFIG_H -DSHELL   -I. -I/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash -I../.. -I../../lib  -g -O2 -Wno-parentheses -Wno-format-security  funmap.c
rm -f keymaps.o
gcc -c -DHAVE_CONFIG_H -DSHELL   -I. -I/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash -I../.. -I../../lib  -g -O2 -Wno-parentheses -Wno-format-security  keymaps.c
rm -f parens.o
gcc -c -DHAVE_CONFIG_H -DSHELL   -I. -I/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash -I../.. -I../../lib  -g -O2 -Wno-parentheses -Wno-format-security  parens.c
rm -f search.o
gcc -c -DHAVE_CONFIG_H -DSHELL   -I. -I/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash -I../.. -I../../lib  -g -O2 -Wno-parentheses -Wno-format-security  search.c
rm -f rltty.o
gcc -c -DHAVE_CONFIG_H -DSHELL   -I. -I/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash -I../.. -I../../lib  -g -O2 -Wno-parentheses -Wno-format-security  rltty.c
rm -f complete.o
gcc -c -DHAVE_CONFIG_H -DSHELL   -I. -I/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash -I../.. -I../../lib  -g -O2 -Wno-parentheses -Wno-format-security  complete.c
rm -f bind.o
gcc -c -DHAVE_CONFIG_H -DSHELL   -I. -I/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash -I../.. -I../../lib  -g -O2 -Wno-parentheses -Wno-format-security  bind.c
rm -f isearch.o
gcc -c -DHAVE_CONFIG_H -DSHELL   -I. -I/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash -I../.. -I../../lib  -g -O2 -Wno-parentheses -Wno-format-security  isearch.c
rm -f display.o
gcc -c -DHAVE_CONFIG_H -DSHELL   -I. -I/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash -I../.. -I../../lib  -g -O2 -Wno-parentheses -Wno-format-security  display.c
rm -f signals.o
gcc -c -DHAVE_CONFIG_H -DSHELL   -I. -I/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash -I../.. -I../../lib  -g -O2 -Wno-parentheses -Wno-format-security  signals.c
rm -f util.o
gcc -c -DHAVE_CONFIG_H -DSHELL   -I. -I/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash -I../.. -I../../lib  -g -O2 -Wno-parentheses -Wno-format-security  util.c
rm -f kill.o
gcc -c -DHAVE_CONFIG_H -DSHELL   -I. -I/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash -I../.. -I../../lib  -g -O2 -Wno-parentheses -Wno-format-security  kill.c
rm -f undo.o
gcc -c -DHAVE_CONFIG_H -DSHELL   -I. -I/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash -I../.. -I../../lib  -g -O2 -Wno-parentheses -Wno-format-security  undo.c
rm -f macro.o
gcc -c -DHAVE_CONFIG_H -DSHELL   -I. -I/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash -I../.. -I../../lib  -g -O2 -Wno-parentheses -Wno-format-security  macro.c
rm -f input.o
gcc -c -DHAVE_CONFIG_H -DSHELL   -I. -I/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash -I../.. -I../../lib  -g -O2 -Wno-parentheses -Wno-format-security  input.c
rm -f callback.o
gcc -c -DHAVE_CONFIG_H -DSHELL   -I. -I/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash -I../.. -I../../lib  -g -O2 -Wno-parentheses -Wno-format-security  callback.c
rm -f terminal.o
gcc -c -DHAVE_CONFIG_H -DSHELL   -I. -I/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash -I../.. -I../../lib  -g -O2 -Wno-parentheses -Wno-format-security  terminal.c
rm -f text.o
gcc -c -DHAVE_CONFIG_H -DSHELL   -I. -I/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash -I../.. -I../../lib  -g -O2 -Wno-parentheses -Wno-format-security  text.c
rm -f nls.o
gcc -c -DHAVE_CONFIG_H -DSHELL   -I. -I/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash -I../.. -I../../lib  -g -O2 -Wno-parentheses -Wno-format-security  nls.c
rm -f misc.o
gcc -c -DHAVE_CONFIG_H -DSHELL   -I. -I/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash -I../.. -I../../lib  -g -O2 -Wno-parentheses -Wno-format-security  misc.c
rm -f history.o
gcc -c -DHAVE_CONFIG_H -DSHELL   -I. -I/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash -I../.. -I../../lib  -g -O2 -Wno-parentheses -Wno-format-security  history.c
rm -f histexpand.o
gcc -c -DHAVE_CONFIG_H -DSHELL   -I. -I/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash -I../.. -I../../lib  -g -O2 -Wno-parentheses -Wno-format-security  histexpand.c
rm -f histfile.o
gcc -c -DHAVE_CONFIG_H -DSHELL   -I. -I/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash -I../.. -I../../lib  -g -O2 -Wno-parentheses -Wno-format-security  histfile.c
rm -f histsearch.o
gcc -c -DHAVE_CONFIG_H -DSHELL   -I. -I/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash -I../.. -I../../lib  -g -O2 -Wno-parentheses -Wno-format-security  histsearch.c
rm -f shell.o
gcc -c -DHAVE_CONFIG_H -DSHELL   -I. -I/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash -I../.. -I../../lib  -g -O2 -Wno-parentheses -Wno-format-security  shell.c
rm -f savestring.o
gcc -c -DHAVE_CONFIG_H -DSHELL   -I. -I/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash -I../.. -I../../lib  -g -O2 -Wno-parentheses -Wno-format-security  savestring.c
rm -f mbutil.o
gcc -c -DHAVE_CONFIG_H -DSHELL   -I. -I/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash -I../.. -I../../lib  -g -O2 -Wno-parentheses -Wno-format-security  mbutil.c
rm -f tilde.o
gcc -DHAVE_CONFIG_H -DSHELL   -I. -I/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash -I../.. -I../../lib  -g -O2 -Wno-parentheses -Wno-format-security  -DREADLINE_LIBRARY -c ./tilde.c
rm -f colors.o
gcc -c -DHAVE_CONFIG_H -DSHELL   -I. -I/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash -I../.. -I../../lib  -g -O2 -Wno-parentheses -Wno-format-security  colors.c
rm -f parse-colors.o
gcc -c -DHAVE_CONFIG_H -DSHELL   -I. -I/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash -I../.. -I../../lib  -g -O2 -Wno-parentheses -Wno-format-security  parse-colors.c
rm -f xmalloc.o
gcc -c -DHAVE_CONFIG_H -DSHELL   -I. -I/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash -I../.. -I../../lib  -g -O2 -Wno-parentheses -Wno-format-security  xmalloc.c
rm -f xfree.o
gcc -c -DHAVE_CONFIG_H -DSHELL   -I. -I/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash -I../.. -I../../lib  -g -O2 -Wno-parentheses -Wno-format-security  xfree.c
rm -f compat.o
gcc -c -DHAVE_CONFIG_H -DSHELL   -I. -I/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash -I../.. -I../../lib  -g -O2 -Wno-parentheses -Wno-format-security  compat.c
rm -f libreadline.a
ar cr libreadline.a readline.o vi_mode.o funmap.o keymaps.o parens.o search.o rltty.o complete.o bind.o isearch.o display.o signals.o util.o kill.o undo.o macro.o input.o callback.o terminal.o text.o nls.o misc.o history.o histexpand.o histfile.o histsearch.o shell.o savestring.o mbutil.o tilde.o colors.o parse-colors.o xmalloc.o xfree.o compat.o 
test -n "ranlib" && ranlib libreadline.a
make[1]: Leaving directory '/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash/lib/readline'
making lib/readline/libhistory.a in ./lib/readline
make[1]: Entering directory '/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash/lib/readline'
make[1]: Warning: File 'history.o' has modification time 348 s in the future
rm -f libhistory.a
ar cr libhistory.a history.o histexpand.o histfile.o histsearch.o shell.o savestring.o mbutil.o xmalloc.o xfree.o
test -n "ranlib" && ranlib libhistory.a
make[1]: warning:  Clock skew detected.  Your build may be incomplete.
make[1]: Leaving directory '/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash/lib/readline'
making lib/tilde/libtilde.a in ./lib/tilde
make[1]: Entering directory '/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash/lib/tilde'
gcc -c   -DHAVE_CONFIG_H -DSHELL  -I. -I../.. -I../.. -I../../include -I../../lib  -g -O2 -Wno-parentheses -Wno-format-security tilde.c
rm -f libtilde.a
ar cr libtilde.a tilde.o
test -n "ranlib" && ranlib libtilde.a
make[1]: Leaving directory '/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash/lib/tilde'
make[1]: Entering directory '/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash/lib/malloc'
gcc  -I. -I../.. -I../.. -I../../include -I../../lib  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security -DRCHECK -Dbotch=programming_error   -c malloc.c
gcc  -I. -I../.. -I../.. -I../../include -I../../lib  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security -DRCHECK -Dbotch=programming_error   -c trace.c
gcc  -I. -I../.. -I../.. -I../../include -I../../lib  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security -DRCHECK -Dbotch=programming_error   -c stats.c
gcc  -I. -I../.. -I../.. -I../../include -I../../lib  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security -DRCHECK -Dbotch=programming_error   -c table.c
gcc  -I. -I../.. -I../.. -I../../include -I../../lib  -DHAVE_CONFIG_H -DSHELL  -g -O2 -Wno-parentheses -Wno-format-security -DRCHECK -Dbotch=programming_error   -c watch.c
rm -f libmalloc.a
ar cr libmalloc.a malloc.o  trace.o stats.o table.o watch.o
test -n "ranlib" && ranlib libmalloc.a
make[1]: Leaving directory '/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash/lib/malloc'
rm -f bash
gcc -L./builtins -L./lib/readline -L./lib/readline -L./lib/glob -L./lib/tilde -L./lib/malloc -L./lib/sh  -rdynamic -g -O2 -Wno-parentheses -Wno-format-security   -o bash shell.o eval.o y.tab.o general.o make_cmd.o print_cmd.o  dispose_cmd.o execute_cmd.o variables.o copy_cmd.o error.o expr.o flags.o jobs.o subst.o hashcmd.o hashlib.o mailcheck.o trap.o input.o unwind_prot.o pathexp.o sig.o test.o version.o alias.o array.o arrayfunc.o assoc.o braces.o bracecomp.o bashhist.o bashline.o  list.o stringlib.o locale.o findcmd.o redir.o pcomplete.o pcomplib.o syntax.o xmalloc.o  -lbuiltins -lglob -lsh -lreadline -lhistory -ltermcap -ltilde -lmalloc    -ldl 
./lib/sh/libsh.a(tmpfile.o): In function `sh_mktmpname':
/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash/lib/sh/tmpfile.c:152: warning: the use of `mktemp' is dangerous, better use `mkstemp' or `mkdtemp'
ls -l bash
-rwxr-xr-x 1 vagrant vagrant 4980144 Jul  3  2020 bash
size bash
   text	   data	    bss	    dec	    hex	filename
1145349	  47352	  40440	1233141	 12d0f5	bash
make[1]: Entering directory '/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash/support'
rm -f man2html.o
gcc -c  -DHAVE_CONFIG_H -DSHELL  -I/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash -I..   -g -O2 man2html.c
gcc  -DHAVE_CONFIG_H -DSHELL  -I/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash -I..   -g -O2 man2html.o -o man2html -ldl 		
make[1]: Leaving directory '/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash/support'


trial
-----

__this is original__

vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash$ which bash
/bin/bash
vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash$ bash --version
GNU bash, version 4.4.19(1)-release (x86_64-pc-linux-gnu)
Copyright (C) 2016 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>

This is free software; you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.


__this is just build__

vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash$ ./bash --version
GNU bash, version 5.0.17(1)-release (x86_64-pc-linux-gnu)
Copyright (C) 2019 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>

This is free software; you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.


vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash$ ./bash


vagrant@ubuntu-bionic:/Users/fanhongling/Downloads/workspace/src/github.com/tangfeixiong/lang-learn/linux/bminor/bash$ exit
exit
