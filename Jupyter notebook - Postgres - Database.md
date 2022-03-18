```python
! pip install ipython-sql
```

    Requirement already satisfied: ipython-sql in /Users/simonxu/opt/anaconda3/lib/python3.8/site-packages (0.3.9)
    Requirement already satisfied: prettytable in /Users/simonxu/opt/anaconda3/lib/python3.8/site-packages (from ipython-sql) (2.2.1)
    Requirement already satisfied: sqlparse in /Users/simonxu/opt/anaconda3/lib/python3.8/site-packages (from ipython-sql) (0.4.2)
    Requirement already satisfied: sqlalchemy>=0.6.7 in /Users/simonxu/opt/anaconda3/lib/python3.8/site-packages (from ipython-sql) (1.3.18)
    Requirement already satisfied: ipython>=1.0 in /Users/simonxu/opt/anaconda3/lib/python3.8/site-packages (from ipython-sql) (7.16.1)
    Requirement already satisfied: ipython-genutils>=0.1.0 in /Users/simonxu/opt/anaconda3/lib/python3.8/site-packages (from ipython-sql) (0.2.0)
    Requirement already satisfied: six in /Users/simonxu/opt/anaconda3/lib/python3.8/site-packages (from ipython-sql) (1.14.0)
    Requirement already satisfied: jedi>=0.10 in /Users/simonxu/opt/anaconda3/lib/python3.8/site-packages (from ipython>=1.0->ipython-sql) (0.17.1)
    Requirement already satisfied: prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0 in /Users/simonxu/opt/anaconda3/lib/python3.8/site-packages (from ipython>=1.0->ipython-sql) (3.0.5)
    Requirement already satisfied: traitlets>=4.2 in /Users/simonxu/opt/anaconda3/lib/python3.8/site-packages (from ipython>=1.0->ipython-sql) (4.3.3)
    Requirement already satisfied: pygments in /Users/simonxu/opt/anaconda3/lib/python3.8/site-packages (from ipython>=1.0->ipython-sql) (2.6.1)
    Requirement already satisfied: appnope in /Users/simonxu/opt/anaconda3/lib/python3.8/site-packages (from ipython>=1.0->ipython-sql) (0.1.0)
    Requirement already satisfied: decorator in /Users/simonxu/opt/anaconda3/lib/python3.8/site-packages (from ipython>=1.0->ipython-sql) (4.4.2)
    Requirement already satisfied: pickleshare in /Users/simonxu/opt/anaconda3/lib/python3.8/site-packages (from ipython>=1.0->ipython-sql) (0.7.5)
    Requirement already satisfied: setuptools>=18.5 in /Users/simonxu/opt/anaconda3/lib/python3.8/site-packages (from ipython>=1.0->ipython-sql) (54.2.0)
    Requirement already satisfied: backcall in /Users/simonxu/opt/anaconda3/lib/python3.8/site-packages (from ipython>=1.0->ipython-sql) (0.2.0)
    Requirement already satisfied: pexpect in /Users/simonxu/opt/anaconda3/lib/python3.8/site-packages (from ipython>=1.0->ipython-sql) (4.8.0)
    Requirement already satisfied: parso<0.8.0,>=0.7.0 in /Users/simonxu/opt/anaconda3/lib/python3.8/site-packages (from jedi>=0.10->ipython>=1.0->ipython-sql) (0.7.0)
    Requirement already satisfied: wcwidth in /Users/simonxu/opt/anaconda3/lib/python3.8/site-packages (from prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0->ipython>=1.0->ipython-sql) (0.1.9)
    Requirement already satisfied: ptyprocess>=0.5 in /Users/simonxu/opt/anaconda3/lib/python3.8/site-packages (from pexpect->ipython>=1.0->ipython-sql) (0.6.0)
    [33mWARNING: You are using pip version 21.1.2; however, version 21.3.1 is available.
    You should consider upgrading via the '/Users/simonxu/opt/anaconda3/bin/python -m pip install --upgrade pip' command.[0m



```python
!pip install sqlalchemy
```

    Requirement already satisfied: sqlalchemy in /Users/simonxu/opt/anaconda3/lib/python3.8/site-packages (1.3.18)
    [33mWARNING: You are using pip version 21.1.2; however, version 21.3.1 is available.
    You should consider upgrading via the '/Users/simonxu/opt/anaconda3/bin/python -m pip install --upgrade pip' command.[0m



```python
!pip install psycopg2
```

    Collecting psycopg2
      Downloading psycopg2-2.9.1.tar.gz (379 kB)
    [K     |████████████████████████████████| 379 kB 3.0 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_cbaa189c0105465498668d2ace897823/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_cbaa189c0105465498668d2ace897823/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-e5skf3ts
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_cbaa189c0105465498668d2ace897823/
        Complete output (23 lines):
        running egg_info
        creating /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-e5skf3ts/psycopg2.egg-info
        writing /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-e5skf3ts/psycopg2.egg-info/PKG-INFO
        writing dependency_links to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-e5skf3ts/psycopg2.egg-info/dependency_links.txt
        writing top-level names to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-e5skf3ts/psycopg2.egg-info/top_level.txt
        writing manifest file '/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-e5skf3ts/psycopg2.egg-info/SOURCES.txt'
        
        Error: pg_config executable not found.
        
        pg_config is required to build psycopg2 from source.  Please add the directory
        containing pg_config to the $PATH or specify the full executable path with the
        option:
        
            python setup.py build_ext --pg-config /path/to/pg_config build ...
        
        or with the pg_config option in 'setup.cfg'.
        
        If you prefer to avoid building psycopg2 from source, please install the PyPI
        'psycopg2-binary' package instead.
        
        For further information please check the 'doc/src/install.rst' file (also at
        <https://www.psycopg.org/docs/install.html>).
        
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/aa/8a/7c80e7e44fb1b4277e89bd9ca509aefdd4dd1b2c547c6f293afe9f7ffd04/psycopg2-2.9.1.tar.gz#sha256=de5303a6f1d0a7a34b9d40e4d3bef684ccc44a49bbe3eb85e3c0bffb4a131b7c (from https://pypi.org/simple/psycopg2/) (requires-python:>=3.6). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [?25h  Downloading psycopg2-2.9.tar.gz (379 kB)
    [K     |████████████████████████████████| 379 kB 21.8 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_d4bcdaf7cb6f4ada9cd245864eced445/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_d4bcdaf7cb6f4ada9cd245864eced445/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-34qzppo1
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_d4bcdaf7cb6f4ada9cd245864eced445/
        Complete output (23 lines):
        running egg_info
        creating /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-34qzppo1/psycopg2.egg-info
        writing /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-34qzppo1/psycopg2.egg-info/PKG-INFO
        writing dependency_links to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-34qzppo1/psycopg2.egg-info/dependency_links.txt
        writing top-level names to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-34qzppo1/psycopg2.egg-info/top_level.txt
        writing manifest file '/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-34qzppo1/psycopg2.egg-info/SOURCES.txt'
        
        Error: pg_config executable not found.
        
        pg_config is required to build psycopg2 from source.  Please add the directory
        containing pg_config to the $PATH or specify the full executable path with the
        option:
        
            python setup.py build_ext --pg-config /path/to/pg_config build ...
        
        or with the pg_config option in 'setup.cfg'.
        
        If you prefer to avoid building psycopg2 from source, please install the PyPI
        'psycopg2-binary' package instead.
        
        For further information please check the 'doc/src/install.rst' file (also at
        <https://www.psycopg.org/docs/install.html>).
        
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/6c/79/6df8af2405e2aa60732c47757453fc7fa4af5c90a1796b3392ef892d3a52/psycopg2-2.9.tar.gz#sha256=b12073fdf2002e828e5921be2c39ff9c6eab361c5c0bd6c529619fc23677accc (from https://pypi.org/simple/psycopg2/) (requires-python:>=3.6). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [?25h  Using cached psycopg2-2.8.6.tar.gz (383 kB)
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_65d8fdd520e6416583e04f47667d5ab8/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_65d8fdd520e6416583e04f47667d5ab8/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-l80niqoo
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_65d8fdd520e6416583e04f47667d5ab8/
        Complete output (23 lines):
        running egg_info
        creating /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-l80niqoo/psycopg2.egg-info
        writing /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-l80niqoo/psycopg2.egg-info/PKG-INFO
        writing dependency_links to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-l80niqoo/psycopg2.egg-info/dependency_links.txt
        writing top-level names to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-l80niqoo/psycopg2.egg-info/top_level.txt
        writing manifest file '/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-l80niqoo/psycopg2.egg-info/SOURCES.txt'
        
        Error: pg_config executable not found.
        
        pg_config is required to build psycopg2 from source.  Please add the directory
        containing pg_config to the $PATH or specify the full executable path with the
        option:
        
            python setup.py build_ext --pg-config /path/to/pg_config build ...
        
        or with the pg_config option in 'setup.cfg'.
        
        If you prefer to avoid building psycopg2 from source, please install the PyPI
        'psycopg2-binary' package instead.
        
        For further information please check the 'doc/src/install.rst' file (also at
        <https://www.psycopg.org/docs/install.html>).
        
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/fd/ae/98cb7a0cbb1d748ee547b058b14604bd0e9bf285a8e0cc5d148f8a8a952e/psycopg2-2.8.6.tar.gz#sha256=fb23f6c71107c37fd667cb4ea363ddeb936b348bbd6449278eb92c189699f543 (from https://pypi.org/simple/psycopg2/) (requires-python:>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
      Downloading psycopg2-2.8.5.tar.gz (380 kB)
    [K     |████████████████████████████████| 380 kB 21.5 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_c797425ae0fb443ea8a14e33a033c1f0/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_c797425ae0fb443ea8a14e33a033c1f0/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-emwd7wzm
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_c797425ae0fb443ea8a14e33a033c1f0/
        Complete output (23 lines):
        running egg_info
        creating /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-emwd7wzm/psycopg2.egg-info
        writing /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-emwd7wzm/psycopg2.egg-info/PKG-INFO
        writing dependency_links to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-emwd7wzm/psycopg2.egg-info/dependency_links.txt
        writing top-level names to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-emwd7wzm/psycopg2.egg-info/top_level.txt
        writing manifest file '/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-emwd7wzm/psycopg2.egg-info/SOURCES.txt'
        
        Error: pg_config executable not found.
        
        pg_config is required to build psycopg2 from source.  Please add the directory
        containing pg_config to the $PATH or specify the full executable path with the
        option:
        
            python setup.py build_ext --pg-config /path/to/pg_config build ...
        
        or with the pg_config option in 'setup.cfg'.
        
        If you prefer to avoid building psycopg2 from source, please install the PyPI
        'psycopg2-binary' package instead.
        
        For further information please check the 'doc/src/install.rst' file (also at
        <https://www.psycopg.org/docs/install.html>).
        
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/a8/8f/1c5690eebf148d1d1554fc00ccf9101e134636553dbb75bdfef4f85d7647/psycopg2-2.8.5.tar.gz#sha256=f7d46240f7a1ae1dd95aab38bd74f7428d46531f69219954266d669da60c0818 (from https://pypi.org/simple/psycopg2/) (requires-python:>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [?25h  Downloading psycopg2-2.8.4.tar.gz (377 kB)
    [K     |████████████████████████████████| 377 kB 23.8 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_0e8e3b3f6141459493d86547f5c7c64a/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_0e8e3b3f6141459493d86547f5c7c64a/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-0v6slzbn
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_0e8e3b3f6141459493d86547f5c7c64a/
        Complete output (23 lines):
        running egg_info
        creating /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-0v6slzbn/psycopg2.egg-info
        writing /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-0v6slzbn/psycopg2.egg-info/PKG-INFO
        writing dependency_links to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-0v6slzbn/psycopg2.egg-info/dependency_links.txt
        writing top-level names to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-0v6slzbn/psycopg2.egg-info/top_level.txt
        writing manifest file '/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-0v6slzbn/psycopg2.egg-info/SOURCES.txt'
        
        Error: pg_config executable not found.
        
        pg_config is required to build psycopg2 from source.  Please add the directory
        containing pg_config to the $PATH or specify the full executable path with the
        option:
        
            python setup.py build_ext --pg-config /path/to/pg_config build ...
        
        or with the pg_config option in 'setup.cfg'.
        
        If you prefer to avoid building psycopg2 from source, please install the PyPI
        'psycopg2-binary' package instead.
        
        For further information please check the 'doc/src/install.rst' file (also at
        <http://initd.org/psycopg/docs/install.html>).
        
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/84/d7/6a93c99b5ba4d4d22daa3928b983cec66df4536ca50b22ce5dcac65e4e71/psycopg2-2.8.4.tar.gz#sha256=f898e5cc0a662a9e12bde6f931263a1bbd350cfb18e1d5336a12927851825bb6 (from https://pypi.org/simple/psycopg2/) (requires-python:>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [?25h  Downloading psycopg2-2.8.3.tar.gz (377 kB)
    [K     |████████████████████████████████| 377 kB 14.8 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_64c248795d444817a70ef25ad5757fd6/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_64c248795d444817a70ef25ad5757fd6/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-c9w0ga0m
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_64c248795d444817a70ef25ad5757fd6/
        Complete output (23 lines):
        running egg_info
        creating /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-c9w0ga0m/psycopg2.egg-info
        writing /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-c9w0ga0m/psycopg2.egg-info/PKG-INFO
        writing dependency_links to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-c9w0ga0m/psycopg2.egg-info/dependency_links.txt
        writing top-level names to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-c9w0ga0m/psycopg2.egg-info/top_level.txt
        writing manifest file '/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-c9w0ga0m/psycopg2.egg-info/SOURCES.txt'
        
        Error: pg_config executable not found.
        
        pg_config is required to build psycopg2 from source.  Please add the directory
        containing pg_config to the $PATH or specify the full executable path with the
        option:
        
            python setup.py build_ext --pg-config /path/to/pg_config build ...
        
        or with the pg_config option in 'setup.cfg'.
        
        If you prefer to avoid building psycopg2 from source, please install the PyPI
        'psycopg2-binary' package instead.
        
        For further information please check the 'doc/src/install.rst' file (also at
        <http://initd.org/psycopg/docs/install.html>).
        
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/5c/1c/6997288da181277a0c29bc39a5f9143ff20b8c99f2a7d059cfb55163e165/psycopg2-2.8.3.tar.gz#sha256=897a6e838319b4bf648a574afb6cabcb17d0488f8c7195100d48d872419f4457 (from https://pypi.org/simple/psycopg2/) (requires-python:>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [?25h  Downloading psycopg2-2.8.2.tar.gz (368 kB)
    [K     |████████████████████████████████| 368 kB 24.3 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_d706a586e72a4f1b8f7354ef08eb01ed/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_d706a586e72a4f1b8f7354ef08eb01ed/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-b3fm62pk
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_d706a586e72a4f1b8f7354ef08eb01ed/
        Complete output (23 lines):
        running egg_info
        creating /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-b3fm62pk/psycopg2.egg-info
        writing /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-b3fm62pk/psycopg2.egg-info/PKG-INFO
        writing dependency_links to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-b3fm62pk/psycopg2.egg-info/dependency_links.txt
        writing top-level names to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-b3fm62pk/psycopg2.egg-info/top_level.txt
        writing manifest file '/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-b3fm62pk/psycopg2.egg-info/SOURCES.txt'
        
        Error: pg_config executable not found.
        
        pg_config is required to build psycopg2 from source.  Please add the directory
        containing pg_config to the $PATH or specify the full executable path with the
        option:
        
            python setup.py build_ext --pg-config /path/to/pg_config build ...
        
        or with the pg_config option in 'setup.cfg'.
        
        If you prefer to avoid building psycopg2 from source, please install the PyPI
        'psycopg2-binary' package instead.
        
        For further information please check the 'doc/src/install.rst' file (also at
        <http://initd.org/psycopg/docs/install.html>).
        
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/23/7e/93c325482c328619870b6cd09370f6dbe1148283daca65115cd63642e60f/psycopg2-2.8.2.tar.gz#sha256=5cacf21b6f813c239f100ef78a4132056f93a5940219ec25d2ef833cbeb05588 (from https://pypi.org/simple/psycopg2/) (requires-python:>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [?25h  Downloading psycopg2-2.8.1.tar.gz (367 kB)
    [K     |████████████████████████████████| 367 kB 18.4 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_7d3fc17f9ce74d9496ce257da7e8e971/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_7d3fc17f9ce74d9496ce257da7e8e971/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-8tsmbwqc
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_7d3fc17f9ce74d9496ce257da7e8e971/
        Complete output (23 lines):
        running egg_info
        creating /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-8tsmbwqc/psycopg2.egg-info
        writing /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-8tsmbwqc/psycopg2.egg-info/PKG-INFO
        writing dependency_links to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-8tsmbwqc/psycopg2.egg-info/dependency_links.txt
        writing top-level names to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-8tsmbwqc/psycopg2.egg-info/top_level.txt
        writing manifest file '/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-8tsmbwqc/psycopg2.egg-info/SOURCES.txt'
        
        Error: pg_config executable not found.
        
        pg_config is required to build psycopg2 from source.  Please add the directory
        containing pg_config to the $PATH or specify the full executable path with the
        option:
        
            python setup.py build_ext --pg-config /path/to/pg_config build ...
        
        or with the pg_config option in 'setup.cfg'.
        
        If you prefer to avoid building psycopg2 from source, please install the PyPI
        'psycopg2-binary' package instead.
        
        For further information please check the 'doc/src/install.rst' file (also at
        <http://initd.org/psycopg/docs/install.html>).
        
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/52/be/f898e712f5f08131d651a62754fca82a1deb42e4e9889ad01932f770a2be/psycopg2-2.8.1.tar.gz#sha256=b4a475ce87eabc0607e068a3c704d0aa0820237ed78d493b8e2d880eb73cd7fe (from https://pypi.org/simple/psycopg2/) (requires-python:>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [?25h  Downloading psycopg2-2.8.tar.gz (367 kB)
    [K     |████████████████████████████████| 367 kB 14.7 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_ecea9379a1004b569bcafb508094ebd0/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_ecea9379a1004b569bcafb508094ebd0/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-_z2o4wkh
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_ecea9379a1004b569bcafb508094ebd0/
        Complete output (23 lines):
        running egg_info
        creating /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-_z2o4wkh/psycopg2.egg-info
        writing /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-_z2o4wkh/psycopg2.egg-info/PKG-INFO
        writing dependency_links to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-_z2o4wkh/psycopg2.egg-info/dependency_links.txt
        writing top-level names to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-_z2o4wkh/psycopg2.egg-info/top_level.txt
        writing manifest file '/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-_z2o4wkh/psycopg2.egg-info/SOURCES.txt'
        
        Error: pg_config executable not found.
        
        pg_config is required to build psycopg2 from source.  Please add the directory
        containing pg_config to the $PATH or specify the full executable path with the
        option:
        
            python setup.py build_ext --pg-config /path/to/pg_config build ...
        
        or with the pg_config option in 'setup.cfg'.
        
        If you prefer to avoid building psycopg2 from source, please install the PyPI
        'psycopg2-binary' package instead.
        
        For further information please check the 'doc/src/install.rst' file (also at
        <http://initd.org/psycopg/docs/install.html>).
        
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/c7/ca/75236b17f1b951950ffc55d657c5aa408d3d0327a1b6c4c0f7cb16ef7e7b/psycopg2-2.8.tar.gz#sha256=49c5838d90e83217909db3789d30a105385b5e696ec5168cda645546c542f35a (from https://pypi.org/simple/psycopg2/) (requires-python:>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [?25h  Downloading psycopg2-2.7.7.tar.gz (427 kB)
    [K     |████████████████████████████████| 427 kB 18.9 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_013cbd4c559d4e1b98127aac285fb460/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_013cbd4c559d4e1b98127aac285fb460/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-rfvo0bec
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_013cbd4c559d4e1b98127aac285fb460/
        Complete output (23 lines):
        running egg_info
        creating /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-rfvo0bec/psycopg2.egg-info
        writing /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-rfvo0bec/psycopg2.egg-info/PKG-INFO
        writing dependency_links to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-rfvo0bec/psycopg2.egg-info/dependency_links.txt
        writing top-level names to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-rfvo0bec/psycopg2.egg-info/top_level.txt
        writing manifest file '/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-rfvo0bec/psycopg2.egg-info/SOURCES.txt'
        
        Error: pg_config executable not found.
        
        pg_config is required to build psycopg2 from source.  Please add the directory
        containing pg_config to the $PATH or specify the full executable path with the
        option:
        
            python setup.py build_ext --pg-config /path/to/pg_config build ...
        
        or with the pg_config option in 'setup.cfg'.
        
        If you prefer to avoid building psycopg2 from source, please install the PyPI
        'psycopg2-binary' package instead.
        
        For further information please check the 'doc/src/install.rst' file (also at
        <http://initd.org/psycopg/docs/install.html>).
        
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/63/54/c039eb0f46f9a9406b59a638415c2012ad7be9b4b97bfddb1f48c280df3a/psycopg2-2.7.7.tar.gz#sha256=f4526d078aedd5187d0508aa5f9a01eae6a48a470ed678406da94b4cd6524b7e (from https://pypi.org/simple/psycopg2/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [?25h  Downloading psycopg2-2.7.6.1.tar.gz (427 kB)
    [K     |████████████████████████████████| 427 kB 19.3 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_59c75910289f49d182eb2337bf9d3e75/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_59c75910289f49d182eb2337bf9d3e75/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-b43dc7ed
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_59c75910289f49d182eb2337bf9d3e75/
        Complete output (23 lines):
        running egg_info
        creating /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-b43dc7ed/psycopg2.egg-info
        writing /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-b43dc7ed/psycopg2.egg-info/PKG-INFO
        writing dependency_links to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-b43dc7ed/psycopg2.egg-info/dependency_links.txt
        writing top-level names to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-b43dc7ed/psycopg2.egg-info/top_level.txt
        writing manifest file '/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-b43dc7ed/psycopg2.egg-info/SOURCES.txt'
        
        Error: pg_config executable not found.
        
        pg_config is required to build psycopg2 from source.  Please add the directory
        containing pg_config to the $PATH or specify the full executable path with the
        option:
        
            python setup.py build_ext --pg-config /path/to/pg_config build ...
        
        or with the pg_config option in 'setup.cfg'.
        
        If you prefer to avoid building psycopg2 from source, please install the PyPI
        'psycopg2-binary' package instead.
        
        For further information please check the 'doc/src/install.rst' file (also at
        <http://initd.org/psycopg/docs/install.html>).
        
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/c0/07/93573b97ed61b6fb907c8439bf58f09957564cf7c39612cef36c547e68c6/psycopg2-2.7.6.1.tar.gz#sha256=27959abe64ca1fc6d8cd11a71a1f421d8287831a3262bd4cacd43bbf43cc3c82 (from https://pypi.org/simple/psycopg2/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [?25h  Downloading psycopg2-2.7.6.tar.gz (427 kB)
    [K     |████████████████████████████████| 427 kB 21.5 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_3434b065de5243a798d863be7bdfc9a5/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_3434b065de5243a798d863be7bdfc9a5/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-5s1kjal_
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_3434b065de5243a798d863be7bdfc9a5/
        Complete output (23 lines):
        running egg_info
        creating /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-5s1kjal_/psycopg2.egg-info
        writing /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-5s1kjal_/psycopg2.egg-info/PKG-INFO
        writing dependency_links to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-5s1kjal_/psycopg2.egg-info/dependency_links.txt
        writing top-level names to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-5s1kjal_/psycopg2.egg-info/top_level.txt
        writing manifest file '/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-5s1kjal_/psycopg2.egg-info/SOURCES.txt'
        
        Error: pg_config executable not found.
        
        pg_config is required to build psycopg2 from source.  Please add the directory
        containing pg_config to the $PATH or specify the full executable path with the
        option:
        
            python setup.py build_ext --pg-config /path/to/pg_config build ...
        
        or with the pg_config option in 'setup.cfg'.
        
        If you prefer to avoid building psycopg2 from source, please install the PyPI
        'psycopg2-binary' package instead.
        
        For further information please check the 'doc/src/install.rst' file (also at
        <http://initd.org/psycopg/docs/install.html>).
        
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/94/09/2f1fae36d83e2315b90ee91738d01baf8af8c945726bf4b4708fcec3256d/psycopg2-2.7.6.tar.gz#sha256=4a658550b0bcb259e97f77f2dc93ed6b108fe2eda963a9e6fc8b48040d542ec2 (from https://pypi.org/simple/psycopg2/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [?25h  Downloading psycopg2-2.7.5.tar.gz (426 kB)
    [K     |████████████████████████████████| 426 kB 17.9 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_1a4a7f768e01493fbbaa6e29bf309853/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_1a4a7f768e01493fbbaa6e29bf309853/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-acm11auo
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_1a4a7f768e01493fbbaa6e29bf309853/
        Complete output (23 lines):
        running egg_info
        creating /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-acm11auo/psycopg2.egg-info
        writing /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-acm11auo/psycopg2.egg-info/PKG-INFO
        writing dependency_links to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-acm11auo/psycopg2.egg-info/dependency_links.txt
        writing top-level names to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-acm11auo/psycopg2.egg-info/top_level.txt
        writing manifest file '/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-acm11auo/psycopg2.egg-info/SOURCES.txt'
        
        Error: pg_config executable not found.
        
        pg_config is required to build psycopg2 from source.  Please add the directory
        containing pg_config to the $PATH or specify the full executable path with the
        option:
        
            python setup.py build_ext --pg-config /path/to/pg_config build ...
        
        or with the pg_config option in 'setup.cfg'.
        
        If you prefer to avoid building psycopg2 from source, please install the PyPI
        'psycopg2-binary' package instead.
        
        For further information please check the 'doc/src/install.rst' file (also at
        <http://initd.org/psycopg/docs/install.html>).
        
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/b2/c1/7bf6c464e903ffc4f3f5907c389e5a4199666bf57f6cd6bf46c17912a1f9/psycopg2-2.7.5.tar.gz#sha256=eccf962d41ca46e6326b97c8fe0a6687b58dfc1a5f6540ed071ff1474cea749e (from https://pypi.org/simple/psycopg2/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [?25h  Downloading psycopg2-2.7.4.tar.gz (425 kB)
    [K     |████████████████████████████████| 425 kB 14.5 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_16dd41fa903b4b6999e8f1dacaa1dad5/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_16dd41fa903b4b6999e8f1dacaa1dad5/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-z0yr48kq
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_16dd41fa903b4b6999e8f1dacaa1dad5/
        Complete output (23 lines):
        running egg_info
        creating /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-z0yr48kq/psycopg2.egg-info
        writing /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-z0yr48kq/psycopg2.egg-info/PKG-INFO
        writing dependency_links to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-z0yr48kq/psycopg2.egg-info/dependency_links.txt
        writing top-level names to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-z0yr48kq/psycopg2.egg-info/top_level.txt
        writing manifest file '/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-z0yr48kq/psycopg2.egg-info/SOURCES.txt'
        
        Error: pg_config executable not found.
        
        pg_config is required to build psycopg2 from source.  Please add the directory
        containing pg_config to the $PATH or specify the full executable path with the
        option:
        
            python setup.py build_ext --pg-config /path/to/pg_config build ...
        
        or with the pg_config option in 'setup.cfg'.
        
        If you prefer to avoid building psycopg2 from source, please install the PyPI
        'psycopg2-binary' package instead.
        
        For further information please check the 'doc/src/install.rst' file (also at
        <http://initd.org/psycopg/docs/install.html>).
        
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/74/83/51580322ed0e82cba7ad8e0af590b8fb2cf11bd5aaa1ed872661bd36f462/psycopg2-2.7.4.tar.gz#sha256=8bf51191d60f6987482ef0cfe8511bbf4877a5aa7f313d7b488b53189cf26209 (from https://pypi.org/simple/psycopg2/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [?25h  Downloading psycopg2-2.7.3.2.tar.gz (425 kB)
    [K     |████████████████████████████████| 425 kB 19.4 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_f0284a3e5b684d6398d6f3f134194112/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_f0284a3e5b684d6398d6f3f134194112/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-8ifx0v0h
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_f0284a3e5b684d6398d6f3f134194112/
        Complete output (14 lines):
        running egg_info
        creating /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-8ifx0v0h/psycopg2.egg-info
        writing /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-8ifx0v0h/psycopg2.egg-info/PKG-INFO
        writing dependency_links to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-8ifx0v0h/psycopg2.egg-info/dependency_links.txt
        writing top-level names to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-8ifx0v0h/psycopg2.egg-info/top_level.txt
        writing manifest file '/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-8ifx0v0h/psycopg2.egg-info/SOURCES.txt'
        Error: pg_config executable not found.
        
        Please add the directory containing pg_config to the PATH
        or specify the full executable path with the option:
        
            python setup.py build_ext --pg-config /path/to/pg_config build ...
        
        or with the pg_config option in 'setup.cfg'.
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/dd/47/000b405d73ca22980684fd7bd3318690cc03cfa3b2ae1c5b7fff8050b28a/psycopg2-2.7.3.2.tar.gz#sha256=5c3213be557d0468f9df8fe2487eaf2990d9799202c5ff5cb8d394d09fad9b2a (from https://pypi.org/simple/psycopg2/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [?25h  Downloading psycopg2-2.7.3.1.tar.gz (425 kB)
    [K     |████████████████████████████████| 425 kB 37.7 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_bcb501aed5e24359942a0db3e79472e4/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_bcb501aed5e24359942a0db3e79472e4/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-q2tzd0dl
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_bcb501aed5e24359942a0db3e79472e4/
        Complete output (14 lines):
        running egg_info
        creating /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-q2tzd0dl/psycopg2.egg-info
        writing /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-q2tzd0dl/psycopg2.egg-info/PKG-INFO
        writing dependency_links to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-q2tzd0dl/psycopg2.egg-info/dependency_links.txt
        writing top-level names to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-q2tzd0dl/psycopg2.egg-info/top_level.txt
        writing manifest file '/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-q2tzd0dl/psycopg2.egg-info/SOURCES.txt'
        Error: pg_config executable not found.
        
        Please add the directory containing pg_config to the PATH
        or specify the full executable path with the option:
        
            python setup.py build_ext --pg-config /path/to/pg_config build ...
        
        or with the pg_config option in 'setup.cfg'.
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/6b/fb/15c687eda2f925f0ff59373063fdb408471b4284714a7761daaa65c01f15/psycopg2-2.7.3.1.tar.gz#sha256=9b7b16e26448b43cf167f785d8b5345007731ebf153a510e12dae826800caa65 (from https://pypi.org/simple/psycopg2/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [?25h  Downloading psycopg2-2.7.3.tar.gz (425 kB)
    [K     |████████████████████████████████| 425 kB 7.2 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_04c24b1408d24a72ae686c4e17e7455d/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_04c24b1408d24a72ae686c4e17e7455d/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-5y53rsui
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_04c24b1408d24a72ae686c4e17e7455d/
        Complete output (14 lines):
        running egg_info
        creating /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-5y53rsui/psycopg2.egg-info
        writing /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-5y53rsui/psycopg2.egg-info/PKG-INFO
        writing dependency_links to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-5y53rsui/psycopg2.egg-info/dependency_links.txt
        writing top-level names to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-5y53rsui/psycopg2.egg-info/top_level.txt
        writing manifest file '/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-5y53rsui/psycopg2.egg-info/SOURCES.txt'
        Error: pg_config executable not found.
        
        Please add the directory containing pg_config to the PATH
        or specify the full executable path with the option:
        
            python setup.py build_ext --pg-config /path/to/pg_config build ...
        
        or with the pg_config option in 'setup.cfg'.
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/98/99/33ca02c4bc3ed1bd9ceab5614bda2e6d1d31e61ec58345b9feece238c38a/psycopg2-2.7.3.tar.gz#sha256=c9bd49848556d04093909faec017c3675efabf78c2b7f383bf7c43ba18324ac8 (from https://pypi.org/simple/psycopg2/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [?25h  Downloading psycopg2-2.7.2.tar.gz (424 kB)
    [K     |████████████████████████████████| 424 kB 17.2 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_7e5068aa697a43fabc52fc3a047cb975/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_7e5068aa697a43fabc52fc3a047cb975/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-5fjbxca8
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_7e5068aa697a43fabc52fc3a047cb975/
        Complete output (14 lines):
        running egg_info
        creating /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-5fjbxca8/psycopg2.egg-info
        writing /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-5fjbxca8/psycopg2.egg-info/PKG-INFO
        writing dependency_links to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-5fjbxca8/psycopg2.egg-info/dependency_links.txt
        writing top-level names to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-5fjbxca8/psycopg2.egg-info/top_level.txt
        writing manifest file '/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-5fjbxca8/psycopg2.egg-info/SOURCES.txt'
        Error: pg_config executable not found.
        
        Please add the directory containing pg_config to the PATH
        or specify the full executable path with the option:
        
            python setup.py build_ext --pg-config /path/to/pg_config build ...
        
        or with the pg_config option in 'setup.cfg'.
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/d0/66/61c1b34ea8da8f95d99676e6803ccad83abef3ac90df145b45033696f3d2/psycopg2-2.7.2.tar.gz#sha256=3767f40bb35713ccc75dbcff80bf228a75e080d6b98c78afd5fb9aa84682a9f4 (from https://pypi.org/simple/psycopg2/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [?25h  Downloading psycopg2-2.7.1.tar.gz (421 kB)
    [K     |████████████████████████████████| 421 kB 28.2 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_d609d303c8f54d368c1b293628076261/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_d609d303c8f54d368c1b293628076261/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-91povdnm
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_d609d303c8f54d368c1b293628076261/
        Complete output (14 lines):
        running egg_info
        creating /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-91povdnm/psycopg2.egg-info
        writing /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-91povdnm/psycopg2.egg-info/PKG-INFO
        writing dependency_links to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-91povdnm/psycopg2.egg-info/dependency_links.txt
        writing top-level names to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-91povdnm/psycopg2.egg-info/top_level.txt
        writing manifest file '/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-91povdnm/psycopg2.egg-info/SOURCES.txt'
        Error: pg_config executable not found.
        
        Please add the directory containing pg_config to the PATH
        or specify the full executable path with the option:
        
            python setup.py build_ext --pg-config /path/to/pg_config build ...
        
        or with the pg_config option in 'setup.cfg'.
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/f8/e9/5793369ce8a41bf5467623ded8d59a434dfef9c136351aca4e70c2657ba0/psycopg2-2.7.1.tar.gz#sha256=86c9355f5374b008c8479bc00023b295c07d508f7c3b91dbd2e74f8925b1d9c6 (from https://pypi.org/simple/psycopg2/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [?25h  Downloading psycopg2-2.7.tar.gz (421 kB)
    [K     |████████████████████████████████| 421 kB 21.9 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_f5566161fa3c4fe7836b9092831d6990/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_f5566161fa3c4fe7836b9092831d6990/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-qb2rs3cv
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_f5566161fa3c4fe7836b9092831d6990/
        Complete output (14 lines):
        running egg_info
        creating /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-qb2rs3cv/psycopg2.egg-info
        writing /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-qb2rs3cv/psycopg2.egg-info/PKG-INFO
        writing dependency_links to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-qb2rs3cv/psycopg2.egg-info/dependency_links.txt
        writing top-level names to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-qb2rs3cv/psycopg2.egg-info/top_level.txt
        writing manifest file '/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-qb2rs3cv/psycopg2.egg-info/SOURCES.txt'
        Error: pg_config executable not found.
        
        Please add the directory containing pg_config to the PATH
        or specify the full executable path with the option:
        
            python setup.py build_ext --pg-config /path/to/pg_config build ...
        
        or with the pg_config option in 'setup.cfg'.
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/62/ca/0a479c9664526e86c2913a7ad593586eeb86b428b7e629e7c7b6b69e3cb7/psycopg2-2.7.tar.gz#sha256=ceadecf660ad4f7a31ea5baef30a7351add8626f9fd3daaafabb9a9e549f3f9a (from https://pypi.org/simple/psycopg2/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [?25h  Downloading psycopg2-2.6.2.tar.gz (376 kB)
    [K     |████████████████████████████████| 376 kB 15.6 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_72dc4c0c76484a9d9543d727de2e602b/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_72dc4c0c76484a9d9543d727de2e602b/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-je7i6g0a
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_72dc4c0c76484a9d9543d727de2e602b/
        Complete output (14 lines):
        running egg_info
        creating /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-je7i6g0a/psycopg2.egg-info
        writing /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-je7i6g0a/psycopg2.egg-info/PKG-INFO
        writing dependency_links to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-je7i6g0a/psycopg2.egg-info/dependency_links.txt
        writing top-level names to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-je7i6g0a/psycopg2.egg-info/top_level.txt
        writing manifest file '/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-je7i6g0a/psycopg2.egg-info/SOURCES.txt'
        Error: pg_config executable not found.
        
        Please add the directory containing pg_config to the PATH
        or specify the full executable path with the option:
        
            python setup.py build_ext --pg-config /path/to/pg_config build ...
        
        or with the pg_config option in 'setup.cfg'.
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/7b/a8/dc2d50a6f37c157459cd18bab381c8e6134b9381b50fbe969997b2ae7dbc/psycopg2-2.6.2.tar.gz#sha256=70490e12ed9c5c818ecd85d185d363335cc8a8cbf7212e3c185431c79ff8c05c (from https://pypi.org/simple/psycopg2/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [?25h  Downloading psycopg2-2.6.1.tar.gz (371 kB)
    [K     |████████████████████████████████| 371 kB 23.0 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_54107274ac8d493eaccab17b0d2cbc23/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_54107274ac8d493eaccab17b0d2cbc23/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-rtn4k0d6
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_54107274ac8d493eaccab17b0d2cbc23/
        Complete output (14 lines):
        running egg_info
        creating /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-rtn4k0d6/psycopg2.egg-info
        writing /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-rtn4k0d6/psycopg2.egg-info/PKG-INFO
        writing dependency_links to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-rtn4k0d6/psycopg2.egg-info/dependency_links.txt
        writing top-level names to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-rtn4k0d6/psycopg2.egg-info/top_level.txt
        writing manifest file '/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-rtn4k0d6/psycopg2.egg-info/SOURCES.txt'
        Error: pg_config executable not found.
        
        Please add the directory containing pg_config to the PATH
        or specify the full executable path with the option:
        
            python setup.py build_ext --pg-config /path/to/pg_config build ...
        
        or with the pg_config option in 'setup.cfg'.
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/86/fd/cc8315be63a41fe000cce20482a917e874cdc1151e62cb0141f5e55f711e/psycopg2-2.6.1.tar.gz#sha256=6acf9abbbe757ef75dc2ecd9d91ba749547941abaffbe69ff2086a9e37d4904c (from https://pypi.org/simple/psycopg2/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [?25h  Downloading psycopg2-2.6.tar.gz (367 kB)
    [K     |████████████████████████████████| 367 kB 16.4 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_7e36fd87ad444f6baa88a43afbf0ffe6/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_7e36fd87ad444f6baa88a43afbf0ffe6/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-adzhy3nc
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_7e36fd87ad444f6baa88a43afbf0ffe6/
        Complete output (14 lines):
        running egg_info
        creating /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-adzhy3nc/psycopg2.egg-info
        writing /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-adzhy3nc/psycopg2.egg-info/PKG-INFO
        writing dependency_links to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-adzhy3nc/psycopg2.egg-info/dependency_links.txt
        writing top-level names to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-adzhy3nc/psycopg2.egg-info/top_level.txt
        writing manifest file '/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-adzhy3nc/psycopg2.egg-info/SOURCES.txt'
        Error: pg_config executable not found.
        
        Please add the directory containing pg_config to the PATH
        or specify the full executable path with the option:
        
            python setup.py build_ext --pg-config /path/to/pg_config build ...
        
        or with the pg_config option in 'setup.cfg'.
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/dd/c7/9016ff8ff69da269b1848276eebfb264af5badf6b38caad805426771f04d/psycopg2-2.6.tar.gz#sha256=c00afecb302a99a4f83dec9b055c4d1cc196926d62c8db015d68432df8118ca8 (from https://pypi.org/simple/psycopg2/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [?25h  Downloading psycopg2-2.5.5.tar.gz (779 kB)
    [K     |████████████████████████████████| 779 kB 13.2 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_e65e84200678444da9fbce9926476afa/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_e65e84200678444da9fbce9926476afa/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-m5xranbc
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_e65e84200678444da9fbce9926476afa/
        Complete output (14 lines):
        running egg_info
        creating /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-m5xranbc/psycopg2.egg-info
        writing /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-m5xranbc/psycopg2.egg-info/PKG-INFO
        writing dependency_links to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-m5xranbc/psycopg2.egg-info/dependency_links.txt
        writing top-level names to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-m5xranbc/psycopg2.egg-info/top_level.txt
        writing manifest file '/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-m5xranbc/psycopg2.egg-info/SOURCES.txt'
        Error: pg_config executable not found.
        
        Please add the directory containing pg_config to the PATH
        or specify the full executable path with the option:
        
            python setup.py build_ext --pg-config /path/to/pg_config build ...
        
        or with the pg_config option in 'setup.cfg'.
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/9b/60/f4c79e73a69ded145880bcf4f98eeed741af12c62c5ddc89b754602b1807/psycopg2-2.5.5.tar.gz#sha256=c6c330c98ab08c5639f0ccd7e211b82b3a39f001813dcea6bb824a99d2b34fe2 (from https://pypi.org/simple/psycopg2/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [?25h  Downloading psycopg2-2.5.4.tar.gz (682 kB)
    [K     |████████████████████████████████| 682 kB 21.4 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_a5a2ed026b3942909cd7c69617dabbc1/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_a5a2ed026b3942909cd7c69617dabbc1/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-_0jgtu5e
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_a5a2ed026b3942909cd7c69617dabbc1/
        Complete output (14 lines):
        running egg_info
        creating /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-_0jgtu5e/psycopg2.egg-info
        writing /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-_0jgtu5e/psycopg2.egg-info/PKG-INFO
        writing dependency_links to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-_0jgtu5e/psycopg2.egg-info/dependency_links.txt
        writing top-level names to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-_0jgtu5e/psycopg2.egg-info/top_level.txt
        writing manifest file '/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-_0jgtu5e/psycopg2.egg-info/SOURCES.txt'
        Error: pg_config executable not found.
        
        Please add the directory containing pg_config to the PATH
        or specify the full executable path with the option:
        
            python setup.py build_ext --pg-config /path/to/pg_config build ...
        
        or with the pg_config option in 'setup.cfg'.
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/63/c3/802668cb3cfc2880c2a8364623e7105a0257724a2612bb66ec733aaddb8c/psycopg2-2.5.4.tar.gz#sha256=24ba3f328aba08d8d505bc2a8f68a94ebe24a85e8483640b667221bc0efd3b1e (from https://pypi.org/simple/psycopg2/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [?25h  Downloading psycopg2-2.5.3.tar.gz (690 kB)
    [K     |████████████████████████████████| 690 kB 24.2 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_7f27ffeaf7fc46f888379b987b5f83db/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_7f27ffeaf7fc46f888379b987b5f83db/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-fdmuw3jt
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_7f27ffeaf7fc46f888379b987b5f83db/
        Complete output (14 lines):
        running egg_info
        creating /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-fdmuw3jt/psycopg2.egg-info
        writing /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-fdmuw3jt/psycopg2.egg-info/PKG-INFO
        writing dependency_links to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-fdmuw3jt/psycopg2.egg-info/dependency_links.txt
        writing top-level names to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-fdmuw3jt/psycopg2.egg-info/top_level.txt
        writing manifest file '/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-fdmuw3jt/psycopg2.egg-info/SOURCES.txt'
        Error: pg_config executable not found.
        
        Please add the directory containing pg_config to the PATH
        or specify the full executable path with the option:
        
            python setup.py build_ext --pg-config /path/to/pg_config build ...
        
        or with the pg_config option in 'setup.cfg'.
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/22/fa/5ddcafc7387c1534c59eb3ffcdb9ab2af106fd3b104e6df191b6c55718af/psycopg2-2.5.3.tar.gz#sha256=3a2df3bb113187227aa97d0dd3d06e0f26be3d50dcdeeaef67fac59ed51a030a (from https://pypi.org/simple/psycopg2/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [?25h  Downloading psycopg2-2.5.2.tar.gz (685 kB)
    [K     |████████████████████████████████| 685 kB 16.3 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_b7166bf73e1045c89751298e57295fb5/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_b7166bf73e1045c89751298e57295fb5/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-icvemh94
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_b7166bf73e1045c89751298e57295fb5/
        Complete output (14 lines):
        running egg_info
        creating /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-icvemh94/psycopg2.egg-info
        writing /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-icvemh94/psycopg2.egg-info/PKG-INFO
        writing dependency_links to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-icvemh94/psycopg2.egg-info/dependency_links.txt
        writing top-level names to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-icvemh94/psycopg2.egg-info/top_level.txt
        writing manifest file '/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-icvemh94/psycopg2.egg-info/SOURCES.txt'
        Error: pg_config executable not found.
        
        Please add the directory containing pg_config to the PATH
        or specify the full executable path with the option:
        
            python setup.py build_ext --pg-config /path/to/pg_config build ...
        
        or with the pg_config option in 'setup.cfg'.
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/c3/f3/5519551f02ae70fc51f4e608e7b44d59a408fe3264fec4afeea37b8ea317/psycopg2-2.5.2.tar.gz#sha256=50382d8703a16c3c615f328c2676f002787095925c99f0afb125a59962a5bd2e (from https://pypi.org/simple/psycopg2/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [?25h  Downloading psycopg2-2.5.1.tar.gz (684 kB)
    [K     |████████████████████████████████| 684 kB 18.8 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_6b598886636f42a18a2d23c627aced6c/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_6b598886636f42a18a2d23c627aced6c/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-7uueid_o
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_6b598886636f42a18a2d23c627aced6c/
        Complete output (14 lines):
        running egg_info
        creating /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-7uueid_o/psycopg2.egg-info
        writing /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-7uueid_o/psycopg2.egg-info/PKG-INFO
        writing dependency_links to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-7uueid_o/psycopg2.egg-info/dependency_links.txt
        writing top-level names to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-7uueid_o/psycopg2.egg-info/top_level.txt
        writing manifest file '/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-7uueid_o/psycopg2.egg-info/SOURCES.txt'
        Error: pg_config executable not found.
        
        Please add the directory containing pg_config to the PATH
        or specify the full executable path with the option:
        
            python setup.py build_ext --pg-config /path/to/pg_config build ...
        
        or with the pg_config option in 'setup.cfg'.
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/22/09/63d5da7375c267e208bbadf56b51699d85cb7b3a9096817eeea500a27b3b/psycopg2-2.5.1.tar.gz#sha256=65a70c88a7e02d8bef57aab8636b5795389674c3205fd88ec46a4dffffa7efec (from https://pypi.org/simple/psycopg2/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [?25h  Downloading psycopg2-2.5.tar.gz (703 kB)
    [K     |████████████████████████████████| 703 kB 22.5 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_0837584935ca486a8afb9ef358bb2e51/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_0837584935ca486a8afb9ef358bb2e51/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-ryplrjj0
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_0837584935ca486a8afb9ef358bb2e51/
        Complete output (14 lines):
        running egg_info
        creating /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-ryplrjj0/psycopg2.egg-info
        writing /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-ryplrjj0/psycopg2.egg-info/PKG-INFO
        writing dependency_links to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-ryplrjj0/psycopg2.egg-info/dependency_links.txt
        writing top-level names to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-ryplrjj0/psycopg2.egg-info/top_level.txt
        writing manifest file '/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-ryplrjj0/psycopg2.egg-info/SOURCES.txt'
        Error: pg_config executable not found.
        
        Please add the directory containing pg_config to the PATH
        or specify the full executable path with the option:
        
            python setup.py build_ext --pg-config /path/to/pg_config build ...
        
        or with the pg_config option in 'setup.cfg'.
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/84/7e/7256298bf7064238e63b9380cf424f776a4d2a87e387c9a9bd1bc5ea0fbc/psycopg2-2.5.tar.gz#sha256=6b2f0cc9199de9eaa53ba10ff69b2741e73484b24657e69bdae259561c23bde4 (from https://pypi.org/simple/psycopg2/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [?25h  Downloading psycopg2-2.4.6.tar.gz (667 kB)
    [K     |████████████████████████████████| 667 kB 27.5 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_0ea285d774cb42e8b5161a583e823185/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_0ea285d774cb42e8b5161a583e823185/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-x_76tog7
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_0ea285d774cb42e8b5161a583e823185/
        Complete output (14 lines):
        running egg_info
        creating /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-x_76tog7/psycopg2.egg-info
        writing /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-x_76tog7/psycopg2.egg-info/PKG-INFO
        writing dependency_links to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-x_76tog7/psycopg2.egg-info/dependency_links.txt
        writing top-level names to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-x_76tog7/psycopg2.egg-info/top_level.txt
        writing manifest file '/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-x_76tog7/psycopg2.egg-info/SOURCES.txt'
        Error: pg_config executable not found.
        
        Please add the directory containing pg_config to the PATH
        or specify the full executable path with the option:
        
            python setup.py build_ext --pg-config /path/to/pg_config build ...
        
        or with the pg_config option in 'setup.cfg'.
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/59/aa/4d74a5dc32a89d622c1fa896a86683b488ef255f06d4b27231e12e6076f7/psycopg2-2.4.6.tar.gz#sha256=4edcb40b0a039b4b559a6bc887b2155db8b6c53d0f55b00af8338c77b725621f (from https://pypi.org/simple/psycopg2/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [?25h  Downloading psycopg2-2.4.5.tar.gz (719 kB)
    [K     |████████████████████████████████| 719 kB 21.6 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_555dc3e3e99d4e4092a88827e29e12ea/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_555dc3e3e99d4e4092a88827e29e12ea/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-yac9x7bx
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_555dc3e3e99d4e4092a88827e29e12ea/
        Complete output (14 lines):
        running egg_info
        creating /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-yac9x7bx/psycopg2.egg-info
        writing /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-yac9x7bx/psycopg2.egg-info/PKG-INFO
        writing dependency_links to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-yac9x7bx/psycopg2.egg-info/dependency_links.txt
        writing top-level names to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-yac9x7bx/psycopg2.egg-info/top_level.txt
        writing manifest file '/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-yac9x7bx/psycopg2.egg-info/SOURCES.txt'
        Error: pg_config executable not found.
        
        Please add the directory containing pg_config to the PATH
        or specify the full executable path with the option:
        
            python setup.py build_ext --pg-config /path/to/pg_config build ...
        
        or with the pg_config option in 'setup.cfg'.
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/36/77/894a5dd9f3f55cfc85682d3e6473ee5103d8d418b95baf4019fad3ffa026/psycopg2-2.4.5.tar.gz#sha256=48b702a7ca479e1bc2c1a7b81875a07d474298132605993e2cb979f5e08277d7 (from https://pypi.org/simple/psycopg2/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [?25h  Downloading psycopg2-2.4.4.tar.gz (648 kB)
    [K     |████████████████████████████████| 648 kB 16.8 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_198f40161237412dad11f9b23965c9c7/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_198f40161237412dad11f9b23965c9c7/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-5b_2wzjn
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_198f40161237412dad11f9b23965c9c7/
        Complete output (14 lines):
        running egg_info
        creating /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-5b_2wzjn/psycopg2.egg-info
        writing /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-5b_2wzjn/psycopg2.egg-info/PKG-INFO
        writing dependency_links to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-5b_2wzjn/psycopg2.egg-info/dependency_links.txt
        writing top-level names to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-5b_2wzjn/psycopg2.egg-info/top_level.txt
        writing manifest file '/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-5b_2wzjn/psycopg2.egg-info/SOURCES.txt'
        Error: pg_config executable not found.
        
        Please add the directory containing pg_config to the PATH
        or specify the full executable path with the option:
        
            python setup.py build_ext --pg-config /path/to/pg_config build ...
        
        or with the pg_config option in 'setup.cfg'.
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/6f/91/890c6f954e2d09d26b266a24468570c6227de61ac6f64926c48000db0a6e/psycopg2-2.4.4.tar.gz#sha256=0c55b059d33f6b2cbb52f254320832c0ca30498ae06f4f4df2a2b38af989127e (from https://pypi.org/simple/psycopg2/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [?25h  Downloading psycopg2-2.4.3.tar.gz (647 kB)
    [K     |████████████████████████████████| 647 kB 20.1 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_c6570e5b5102427b82c984adf6781dc2/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_c6570e5b5102427b82c984adf6781dc2/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-_w7e212m
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_c6570e5b5102427b82c984adf6781dc2/
        Complete output (14 lines):
        running egg_info
        creating /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-_w7e212m/psycopg2.egg-info
        writing /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-_w7e212m/psycopg2.egg-info/PKG-INFO
        writing dependency_links to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-_w7e212m/psycopg2.egg-info/dependency_links.txt
        writing top-level names to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-_w7e212m/psycopg2.egg-info/top_level.txt
        writing manifest file '/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-_w7e212m/psycopg2.egg-info/SOURCES.txt'
        Error: pg_config executable not found.
        
        Please add the directory containing pg_config to the PATH
        or specify the full executable path with the option:
        
            python setup.py build_ext --pg-config /path/to/pg_config build ...
        
        or with the pg_config option in 'setup.cfg'.
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/1e/71/8929172068cbc3d3c7288bf888a7df5862a28d67ed61ad9b4c7aa5cf8be8/psycopg2-2.4.3.tar.gz#sha256=febd8e35ca9904bf4418e611f866a80639fbca7db2781e5b5cd20589b767af0b (from https://pypi.org/simple/psycopg2/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [?25h  Downloading psycopg2-2.4.2.tar.gz (667 kB)
    [K     |████████████████████████████████| 667 kB 21.3 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_5d51478c1aac4bc5a283075bfbe55b76/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_5d51478c1aac4bc5a283075bfbe55b76/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-dqrt7m54
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_5d51478c1aac4bc5a283075bfbe55b76/
        Complete output (14 lines):
        running egg_info
        creating /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-dqrt7m54/psycopg2.egg-info
        writing /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-dqrt7m54/psycopg2.egg-info/PKG-INFO
        writing dependency_links to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-dqrt7m54/psycopg2.egg-info/dependency_links.txt
        writing top-level names to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-dqrt7m54/psycopg2.egg-info/top_level.txt
        writing manifest file '/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-dqrt7m54/psycopg2.egg-info/SOURCES.txt'
        Error: pg_config executable not found.
        
        Please add the directory containing pg_config to the PATH
        or specify the full executable path with the option:
        
            python setup.py build_ext --pg-config /path/to/pg_config build ...
        
        or with the pg_config option in 'setup.cfg'.
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/70/91/345f8eb32dc333331510e1adad858f7a1478d3a1e4aae05ee188985c6b17/psycopg2-2.4.2.tar.gz#sha256=c5f0f853aeeefc7b2aa73b08579e5d74c4c32ad5fca87e058bf04e08273a41a1 (from https://pypi.org/simple/psycopg2/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [?25h  Downloading psycopg2-2.4.1.tar.gz (398 kB)
    [K     |████████████████████████████████| 398 kB 17.8 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_9aa21ae36208475ca0f4656361320cf5/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_9aa21ae36208475ca0f4656361320cf5/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-3zep36an
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_9aa21ae36208475ca0f4656361320cf5/
        Complete output (14 lines):
        running egg_info
        creating /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-3zep36an/psycopg2.egg-info
        writing /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-3zep36an/psycopg2.egg-info/PKG-INFO
        writing dependency_links to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-3zep36an/psycopg2.egg-info/dependency_links.txt
        writing top-level names to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-3zep36an/psycopg2.egg-info/top_level.txt
        writing manifest file '/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-3zep36an/psycopg2.egg-info/SOURCES.txt'
        Error: pg_config executable not found.
        
        Please add the directory containing pg_config to the PATH
        or specify the full executable path with the option:
        
            python setup.py build_ext --pg-config /path/to/pg_config build ...
        
        or with the pg_config option in 'setup.cfg'.
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/82/f8/6c80beb1b58f01f52dcdfa52bc1668caa4e3fc4927e9230edc40afa98c05/psycopg2-2.4.1.tar.gz#sha256=f8ee9a4004afbd1ff1a1db8df7910475d6ec26e102aa92c9214cbeb1ef39ff49 (from https://pypi.org/simple/psycopg2/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [?25h  Downloading psycopg2-2.4.tar.gz (607 kB)
    [K     |████████████████████████████████| 607 kB 18.3 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_52dd99e65aa04783b467a5c8a935121f/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_52dd99e65aa04783b467a5c8a935121f/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-me2zs450
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_52dd99e65aa04783b467a5c8a935121f/
        Complete output (14 lines):
        running egg_info
        creating /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-me2zs450/psycopg2.egg-info
        writing /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-me2zs450/psycopg2.egg-info/PKG-INFO
        writing dependency_links to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-me2zs450/psycopg2.egg-info/dependency_links.txt
        writing top-level names to /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-me2zs450/psycopg2.egg-info/top_level.txt
        writing manifest file '/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-me2zs450/psycopg2.egg-info/SOURCES.txt'
        Error: pg_config executable not found.
        
        Please add the directory containing pg_config to the PATH
        or specify the full executable path with the option:
        
            python setup.py build_ext --pg-config /path/to/pg_config build ...
        
        or with the pg_config option in 'setup.cfg'.
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/ce/2d/e9e65ee32ef2657028109bd5a1c1ece97e409ebf790b6ee286aae2c6b890/psycopg2-2.4.tar.gz#sha256=f41623c413283f101b61ba2356f92cc1890b00308aea970124ebd6178ac5c3a5 (from https://pypi.org/simple/psycopg2/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [?25h  Downloading psycopg2-2.3.2.tar.gz (568 kB)
    [K     |████████████████████████████████| 568 kB 15.5 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_2177c8cfa46444e399db7f6d3159be9a/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_2177c8cfa46444e399db7f6d3159be9a/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-4y5sbkld
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_2177c8cfa46444e399db7f6d3159be9a/
        Complete output (6 lines):
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
          File "/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_2177c8cfa46444e399db7f6d3159be9a/setup.py", line 247
            except Warning, w:
                          ^
        SyntaxError: invalid syntax
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/50/48/32927cbc99633613704950be5013fc144aa0f451a5e0616635a934d94a62/psycopg2-2.3.2.tar.gz#sha256=0ef1df428f5482c41885ee6d9a6975473fc83af5497801abd36dd150a3754c2c (from https://pypi.org/simple/psycopg2/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [?25h  Downloading psycopg2-2.3.1.tar.gz (567 kB)
    [K     |████████████████████████████████| 567 kB 20.0 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_5b947de40c7643b3bef35d2feba87f6f/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_5b947de40c7643b3bef35d2feba87f6f/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-ml6mlu4c
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_5b947de40c7643b3bef35d2feba87f6f/
        Complete output (6 lines):
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
          File "/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_5b947de40c7643b3bef35d2feba87f6f/setup.py", line 247
            except Warning, w:
                          ^
        SyntaxError: invalid syntax
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/cd/7c/6acf5aacd347f3dc1398eca0e2123c35a48efb07617d4d9578e9cd79a1a7/psycopg2-2.3.1.tar.gz#sha256=7aee74fb13f3b51571fa84cebeeeb29b4230e7553f554f228636c6754752c4e4 (from https://pypi.org/simple/psycopg2/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [?25h  Downloading psycopg2-2.3.0.tar.gz (588 kB)
    [K     |████████████████████████████████| 588 kB 13.6 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_60dbed207ecd4ad3b0d063c3c847528f/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_60dbed207ecd4ad3b0d063c3c847528f/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-9nw_nakv
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_60dbed207ecd4ad3b0d063c3c847528f/
        Complete output (6 lines):
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
          File "/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_60dbed207ecd4ad3b0d063c3c847528f/setup.py", line 247
            except Warning, w:
                          ^
        SyntaxError: invalid syntax
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/68/0a/459df8dcbcc118ca435e9567abceaab919706908d52139e503f6396c4935/psycopg2-2.3.0.tar.gz#sha256=c17a06b7468debba94fa151d3ad93cd885d9cbe9a751e54ceb87738d5f0478ea (from https://pypi.org/simple/psycopg2/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [?25h  Downloading psycopg2-2.2.2.tar.gz (530 kB)
    [K     |████████████████████████████████| 530 kB 17.5 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_2d6841499a4346bba282e0487206a701/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_2d6841499a4346bba282e0487206a701/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-73_8lnkg
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_2d6841499a4346bba282e0487206a701/
        Complete output (6 lines):
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
          File "/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_2d6841499a4346bba282e0487206a701/setup.py", line 245
            except Warning, w:
                          ^
        SyntaxError: invalid syntax
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/63/3e/a4a35761eb4595fff89e63347b4f8e79c2095782fa5bc016a6dfb18b21ac/psycopg2-2.2.2.tar.gz#sha256=21a33d5b2609103512748098a06249492cc294790e07638fadc68cf06eeac39d (from https://pypi.org/simple/psycopg2/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [?25h  Downloading psycopg2-2.2.1.tar.gz (529 kB)
    [K     |████████████████████████████████| 529 kB 25.2 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_0bf5de8ec5ca4d0c90fb852b54413704/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_0bf5de8ec5ca4d0c90fb852b54413704/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-kkkcfmj2
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_0bf5de8ec5ca4d0c90fb852b54413704/
        Complete output (6 lines):
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
          File "/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_0bf5de8ec5ca4d0c90fb852b54413704/setup.py", line 239
            except Warning, w:
                          ^
        SyntaxError: invalid syntax
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/de/c4/fdfb801035bd7da9e1ce98169d48ca2d6dee5b4361e349afbba40b3d7a5d/psycopg2-2.2.1.tar.gz#sha256=b0eca4e8438025dc57cacbea4e8ca2f5dc0554d41b1cdcc177757a5fc413f3d1 (from https://pypi.org/simple/psycopg2/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [?25h  Downloading psycopg2-2.2.0.tar.gz (528 kB)
    [K     |████████████████████████████████| 528 kB 48.7 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_3904ef08c8c84046be48700301ab94d7/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_3904ef08c8c84046be48700301ab94d7/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-iog8vajy
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_3904ef08c8c84046be48700301ab94d7/
        Complete output (6 lines):
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
          File "/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_3904ef08c8c84046be48700301ab94d7/setup.py", line 238
            except Warning, w:
                          ^
        SyntaxError: invalid syntax
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/32/0c/2f4da04ae2a66d71eff37f19fce67506ad28f887851cd1c1cca35ba08b36/psycopg2-2.2.0.tar.gz#sha256=e70a8eabc491318beef4cd9cd9245a4d8dc62ee31cb74e7988913a66bb33f858 (from https://pypi.org/simple/psycopg2/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [?25h  Downloading psycopg2-2.0.14.tar.gz (491 kB)
    [K     |████████████████████████████████| 491 kB 20.9 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_3e68d01b845048cf8d8541803e12fdb2/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_3e68d01b845048cf8d8541803e12fdb2/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-jc1hzxaf
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_3e68d01b845048cf8d8541803e12fdb2/
        Complete output (6 lines):
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
          File "/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_3e68d01b845048cf8d8541803e12fdb2/setup.py", line 238
            except Warning, w:
                          ^
        SyntaxError: invalid syntax
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/e0/1c/f0843f50a69fba3db880e9b267d36f6709bbf31a36fc46b82f75e8975ede/psycopg2-2.0.14.tar.gz#sha256=902607cdbe1195a00694d2b477eed8429eda433caaa0eb6ff7f80883e1c17ac7 (from https://pypi.org/simple/psycopg2/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [?25h  Downloading psycopg2-2.0.13.tar.gz (258 kB)
    [K     |████████████████████████████████| 258 kB 16.3 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_d610cded60a6463a80cd874d40abd1f1/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_d610cded60a6463a80cd874d40abd1f1/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-ja7qr95_
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_d610cded60a6463a80cd874d40abd1f1/
        Complete output (6 lines):
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
          File "/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_d610cded60a6463a80cd874d40abd1f1/setup.py", line 233
            except Warning, w:
                          ^
        SyntaxError: invalid syntax
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/3a/7a/968afcb86b1958ae963a3aaa42c561e3ed2c2d4a8b773622b03856a16248/psycopg2-2.0.13.tar.gz#sha256=a15e622e101b16aa8ad44813d8fb1eced91379396c054aacbfa3ad658352332b (from https://pypi.org/simple/psycopg2/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [?25h  Downloading psycopg2-2.0.12.tar.gz (256 kB)
    [K     |████████████████████████████████| 256 kB 10.9 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_7d33791ac7c8436eb5dbeb39dfe529e1/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_7d33791ac7c8436eb5dbeb39dfe529e1/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-h1a9l7ae
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_7d33791ac7c8436eb5dbeb39dfe529e1/
        Complete output (6 lines):
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
          File "/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_7d33791ac7c8436eb5dbeb39dfe529e1/setup.py", line 225
            except Warning, w:
                          ^
        SyntaxError: invalid syntax
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/6a/8d/ee5c330823d527a5cd14c833063f825211d7b5de6e4897f72e250c107d85/psycopg2-2.0.12.tar.gz#sha256=542c187531e756867fb60034c393b6f2beca34eeeb3ce2e0089a2b6fb8be1292 (from https://pypi.org/simple/psycopg2/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [?25h  Downloading psycopg2-2.0.11.tar.gz (255 kB)
    [K     |████████████████████████████████| 255 kB 17.9 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_a0f1c8e57ce443908f38f03e6218d438/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_a0f1c8e57ce443908f38f03e6218d438/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-5k_hbcdy
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_a0f1c8e57ce443908f38f03e6218d438/
        Complete output (6 lines):
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
          File "/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_a0f1c8e57ce443908f38f03e6218d438/setup.py", line 225
            except Warning, w:
                          ^
        SyntaxError: invalid syntax
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/2d/d7/496da11d7c81971870ddd36800419c4f84e8f6208aac5eabedf9f7748729/psycopg2-2.0.11.tar.gz#sha256=e6b4e0e41df97441eff34e00065376414da6488e0d55848a45cd77551dbae434 (from https://pypi.org/simple/psycopg2/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [?25h  Downloading psycopg2-2.0.10.tar.gz (255 kB)
    [K     |████████████████████████████████| 255 kB 20.7 MB/s eta 0:00:01
    [31m    ERROR: Command errored out with exit status 1:
         command: /Users/simonxu/opt/anaconda3/bin/python -c 'import io, os, sys, setuptools, tokenize; sys.argv[0] = '"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_5cef8a02ba2b4d129d7fba200647d7d5/setup.py'"'"'; __file__='"'"'/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_5cef8a02ba2b4d129d7fba200647d7d5/setup.py'"'"';f = getattr(tokenize, '"'"'open'"'"', open)(__file__) if os.path.exists(__file__) else io.StringIO('"'"'from setuptools import setup; setup()'"'"');code = f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-pip-egg-info-66a23wll
             cwd: /private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_5cef8a02ba2b4d129d7fba200647d7d5/
        Complete output (5 lines):
        Traceback (most recent call last):
          File "<string>", line 1, in <module>
          File "/private/var/folders/p4/bklxjxxj2sq59w13x2tmsz9h0000gn/T/pip-install-l2_6g4ui/psycopg2_5cef8a02ba2b4d129d7fba200647d7d5/setup.py", line 50, in <module>
            import ConfigParser
        ModuleNotFoundError: No module named 'ConfigParser'
        ----------------------------------------[0m
    [33mWARNING: Discarding https://files.pythonhosted.org/packages/19/79/35c7596bab4456f3610c12ec542a94d51c6781ced587d1d85127210b879b/psycopg2-2.0.10.tar.gz#sha256=e40cc04b43849085725076ae134bfef9e3b087f6dd7c964aeeb930e2f0bc14ab (from https://pypi.org/simple/psycopg2/). Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.[0m
    [31mERROR: Could not find a version that satisfies the requirement psycopg2 (from versions: 2.0.10, 2.0.11, 2.0.12, 2.0.13, 2.0.14, 2.2.0, 2.2.1, 2.2.2, 2.3.0, 2.3.1, 2.3.2, 2.4, 2.4.1, 2.4.2, 2.4.3, 2.4.4, 2.4.5, 2.4.6, 2.5, 2.5.1, 2.5.2, 2.5.3, 2.5.4, 2.5.5, 2.6, 2.6.1, 2.6.2, 2.7, 2.7.1, 2.7.2, 2.7.3, 2.7.3.1, 2.7.3.2, 2.7.4, 2.7.5, 2.7.6, 2.7.6.1, 2.7.7, 2.8, 2.8.1, 2.8.2, 2.8.3, 2.8.4, 2.8.5, 2.8.6, 2.9, 2.9.1)[0m
    [31mERROR: No matching distribution found for psycopg2[0m
    [33mWARNING: You are using pip version 21.1.2; however, version 21.3.1 is available.
    You should consider upgrading via the '/Users/simonxu/opt/anaconda3/bin/python -m pip install --upgrade pip' command.[0m
    [?25h


```python
%load_ext sql
```

    The sql extension is already loaded. To reload it, use:
      %reload_ext sql



```python
from sqlalchemy import create_engine
```


```python
# Format
# %sql dialect+driver://username:password@host:port/database
%sql postgresql://postgres:postgres@localhost/PH-EmployeeDB
```




    'Connected: postgres@PH-EmployeeDB'




```python
# Format
# engine = create_engine('dialect+driver://username:password@host:port/database')
# Example format
engine = create_engine('postgresql://postgres:password123@localhost/dvdrental')
```


```python
%%sql
SELECT *
FROM employees
LIMIT 100
```

     * postgresql://postgres:***@localhost/PH-EmployeeDB
    100 rows affected.





<table>
    <thead>
        <tr>
            <th>emp_no</th>
            <th>birth_date</th>
            <th>first_name</th>
            <th>last_name</th>
            <th>gender</th>
            <th>hire_date</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>10001</td>
            <td>1953-09-02</td>
            <td>Georgi</td>
            <td>Facello</td>
            <td>M</td>
            <td>1986-06-26</td>
        </tr>
        <tr>
            <td>10002</td>
            <td>1964-06-02</td>
            <td>Bezalel</td>
            <td>Simmel</td>
            <td>F</td>
            <td>1985-11-21</td>
        </tr>
        <tr>
            <td>10003</td>
            <td>1959-12-03</td>
            <td>Parto</td>
            <td>Bamford</td>
            <td>M</td>
            <td>1986-08-28</td>
        </tr>
        <tr>
            <td>10004</td>
            <td>1954-05-01</td>
            <td>Chirstian</td>
            <td>Koblick</td>
            <td>M</td>
            <td>1986-12-01</td>
        </tr>
        <tr>
            <td>10005</td>
            <td>1955-01-21</td>
            <td>Kyoichi</td>
            <td>Maliniak</td>
            <td>M</td>
            <td>1989-09-12</td>
        </tr>
        <tr>
            <td>10006</td>
            <td>1953-04-20</td>
            <td>Anneke</td>
            <td>Preusig</td>
            <td>F</td>
            <td>1989-06-02</td>
        </tr>
        <tr>
            <td>10007</td>
            <td>1957-05-23</td>
            <td>Tzvetan</td>
            <td>Zielinski</td>
            <td>F</td>
            <td>1989-02-10</td>
        </tr>
        <tr>
            <td>10008</td>
            <td>1958-02-19</td>
            <td>Saniya</td>
            <td>Kalloufi</td>
            <td>M</td>
            <td>1994-09-15</td>
        </tr>
        <tr>
            <td>10009</td>
            <td>1952-04-19</td>
            <td>Sumant</td>
            <td>Peac</td>
            <td>F</td>
            <td>1985-02-18</td>
        </tr>
        <tr>
            <td>10010</td>
            <td>1963-06-01</td>
            <td>Duangkaew</td>
            <td>Piveteau</td>
            <td>F</td>
            <td>1989-08-24</td>
        </tr>
        <tr>
            <td>10011</td>
            <td>1953-11-07</td>
            <td>Mary</td>
            <td>Sluis</td>
            <td>F</td>
            <td>1990-01-22</td>
        </tr>
        <tr>
            <td>10012</td>
            <td>1960-10-04</td>
            <td>Patricio</td>
            <td>Bridgland</td>
            <td>M</td>
            <td>1992-12-18</td>
        </tr>
        <tr>
            <td>10013</td>
            <td>1963-06-07</td>
            <td>Eberhardt</td>
            <td>Terkki</td>
            <td>M</td>
            <td>1985-10-20</td>
        </tr>
        <tr>
            <td>10014</td>
            <td>1956-02-12</td>
            <td>Berni</td>
            <td>Genin</td>
            <td>M</td>
            <td>1987-03-11</td>
        </tr>
        <tr>
            <td>10015</td>
            <td>1959-08-19</td>
            <td>Guoxiang</td>
            <td>Nooteboom</td>
            <td>M</td>
            <td>1987-07-02</td>
        </tr>
        <tr>
            <td>10016</td>
            <td>1961-05-02</td>
            <td>Kazuhito</td>
            <td>Cappelletti</td>
            <td>M</td>
            <td>1995-01-27</td>
        </tr>
        <tr>
            <td>10017</td>
            <td>1958-07-06</td>
            <td>Cristinel</td>
            <td>Bouloucos</td>
            <td>F</td>
            <td>1993-08-03</td>
        </tr>
        <tr>
            <td>10018</td>
            <td>1954-06-19</td>
            <td>Kazuhide</td>
            <td>Peha</td>
            <td>F</td>
            <td>1987-04-03</td>
        </tr>
        <tr>
            <td>10019</td>
            <td>1953-01-23</td>
            <td>Lillian</td>
            <td>Haddadi</td>
            <td>M</td>
            <td>1999-04-30</td>
        </tr>
        <tr>
            <td>10020</td>
            <td>1952-12-24</td>
            <td>Mayuko</td>
            <td>Warwick</td>
            <td>M</td>
            <td>1991-01-26</td>
        </tr>
        <tr>
            <td>10021</td>
            <td>1960-02-20</td>
            <td>Ramzi</td>
            <td>Erde</td>
            <td>M</td>
            <td>1988-02-10</td>
        </tr>
        <tr>
            <td>10022</td>
            <td>1952-07-08</td>
            <td>Shahaf</td>
            <td>Famili</td>
            <td>M</td>
            <td>1995-08-22</td>
        </tr>
        <tr>
            <td>10023</td>
            <td>1953-09-29</td>
            <td>Bojan</td>
            <td>Montemayor</td>
            <td>F</td>
            <td>1989-12-17</td>
        </tr>
        <tr>
            <td>10024</td>
            <td>1958-09-05</td>
            <td>Suzette</td>
            <td>Pettey</td>
            <td>F</td>
            <td>1997-05-19</td>
        </tr>
        <tr>
            <td>10025</td>
            <td>1958-10-31</td>
            <td>Prasadram</td>
            <td>Heyers</td>
            <td>M</td>
            <td>1987-08-17</td>
        </tr>
        <tr>
            <td>10026</td>
            <td>1953-04-03</td>
            <td>Yongqiao</td>
            <td>Berztiss</td>
            <td>M</td>
            <td>1995-03-20</td>
        </tr>
        <tr>
            <td>10027</td>
            <td>1962-07-10</td>
            <td>Divier</td>
            <td>Reistad</td>
            <td>F</td>
            <td>1989-07-07</td>
        </tr>
        <tr>
            <td>10028</td>
            <td>1963-11-26</td>
            <td>Domenick</td>
            <td>Tempesti</td>
            <td>M</td>
            <td>1991-10-22</td>
        </tr>
        <tr>
            <td>10029</td>
            <td>1956-12-13</td>
            <td>Otmar</td>
            <td>Herbst</td>
            <td>M</td>
            <td>1985-11-20</td>
        </tr>
        <tr>
            <td>10030</td>
            <td>1958-07-14</td>
            <td>Elvis</td>
            <td>Demeyer</td>
            <td>M</td>
            <td>1994-02-17</td>
        </tr>
        <tr>
            <td>10031</td>
            <td>1959-01-27</td>
            <td>Karsten</td>
            <td>Joslin</td>
            <td>M</td>
            <td>1991-09-01</td>
        </tr>
        <tr>
            <td>10032</td>
            <td>1960-08-09</td>
            <td>Jeong</td>
            <td>Reistad</td>
            <td>F</td>
            <td>1990-06-20</td>
        </tr>
        <tr>
            <td>10033</td>
            <td>1956-11-14</td>
            <td>Arif</td>
            <td>Merlo</td>
            <td>M</td>
            <td>1987-03-18</td>
        </tr>
        <tr>
            <td>10034</td>
            <td>1962-12-29</td>
            <td>Bader</td>
            <td>Swan</td>
            <td>M</td>
            <td>1988-09-21</td>
        </tr>
        <tr>
            <td>10035</td>
            <td>1953-02-08</td>
            <td>Alain</td>
            <td>Chappelet</td>
            <td>M</td>
            <td>1988-09-05</td>
        </tr>
        <tr>
            <td>10036</td>
            <td>1959-08-10</td>
            <td>Adamantios</td>
            <td>Portugali</td>
            <td>M</td>
            <td>1992-01-03</td>
        </tr>
        <tr>
            <td>10037</td>
            <td>1963-07-22</td>
            <td>Pradeep</td>
            <td>Makrucki</td>
            <td>M</td>
            <td>1990-12-05</td>
        </tr>
        <tr>
            <td>10038</td>
            <td>1960-07-20</td>
            <td>Huan</td>
            <td>Lortz</td>
            <td>M</td>
            <td>1989-09-20</td>
        </tr>
        <tr>
            <td>10039</td>
            <td>1959-10-01</td>
            <td>Alejandro</td>
            <td>Brender</td>
            <td>M</td>
            <td>1988-01-19</td>
        </tr>
        <tr>
            <td>10040</td>
            <td>1959-09-13</td>
            <td>Weiyi</td>
            <td>Meriste</td>
            <td>F</td>
            <td>1993-02-14</td>
        </tr>
        <tr>
            <td>10041</td>
            <td>1959-08-27</td>
            <td>Uri</td>
            <td>Lenart</td>
            <td>F</td>
            <td>1989-11-12</td>
        </tr>
        <tr>
            <td>10042</td>
            <td>1956-02-26</td>
            <td>Magy</td>
            <td>Stamatiou</td>
            <td>F</td>
            <td>1993-03-21</td>
        </tr>
        <tr>
            <td>10043</td>
            <td>1960-09-19</td>
            <td>Yishay</td>
            <td>Tzvieli</td>
            <td>M</td>
            <td>1990-10-20</td>
        </tr>
        <tr>
            <td>10044</td>
            <td>1961-09-21</td>
            <td>Mingsen</td>
            <td>Casley</td>
            <td>F</td>
            <td>1994-05-21</td>
        </tr>
        <tr>
            <td>10045</td>
            <td>1957-08-14</td>
            <td>Moss</td>
            <td>Shanbhogue</td>
            <td>M</td>
            <td>1989-09-02</td>
        </tr>
        <tr>
            <td>10046</td>
            <td>1960-07-23</td>
            <td>Lucien</td>
            <td>Rosenbaum</td>
            <td>M</td>
            <td>1992-06-20</td>
        </tr>
        <tr>
            <td>10047</td>
            <td>1952-06-29</td>
            <td>Zvonko</td>
            <td>Nyanchama</td>
            <td>M</td>
            <td>1989-03-31</td>
        </tr>
        <tr>
            <td>10048</td>
            <td>1963-07-11</td>
            <td>Florian</td>
            <td>Syrotiuk</td>
            <td>M</td>
            <td>1985-02-24</td>
        </tr>
        <tr>
            <td>10049</td>
            <td>1961-04-24</td>
            <td>Basil</td>
            <td>Tramer</td>
            <td>F</td>
            <td>1992-05-04</td>
        </tr>
        <tr>
            <td>10050</td>
            <td>1958-05-21</td>
            <td>Yinghua</td>
            <td>Dredge</td>
            <td>M</td>
            <td>1990-12-25</td>
        </tr>
        <tr>
            <td>10051</td>
            <td>1953-07-28</td>
            <td>Hidefumi</td>
            <td>Caine</td>
            <td>M</td>
            <td>1992-10-15</td>
        </tr>
        <tr>
            <td>10052</td>
            <td>1961-02-26</td>
            <td>Heping</td>
            <td>Nitsch</td>
            <td>M</td>
            <td>1988-05-21</td>
        </tr>
        <tr>
            <td>10053</td>
            <td>1954-09-13</td>
            <td>Sanjiv</td>
            <td>Zschoche</td>
            <td>F</td>
            <td>1986-02-04</td>
        </tr>
        <tr>
            <td>10054</td>
            <td>1957-04-04</td>
            <td>Mayumi</td>
            <td>Schueller</td>
            <td>M</td>
            <td>1995-03-13</td>
        </tr>
        <tr>
            <td>10055</td>
            <td>1956-06-06</td>
            <td>Georgy</td>
            <td>Dredge</td>
            <td>M</td>
            <td>1992-04-27</td>
        </tr>
        <tr>
            <td>10056</td>
            <td>1961-09-01</td>
            <td>Brendon</td>
            <td>Bernini</td>
            <td>F</td>
            <td>1990-02-01</td>
        </tr>
        <tr>
            <td>10057</td>
            <td>1954-05-30</td>
            <td>Ebbe</td>
            <td>Callaway</td>
            <td>F</td>
            <td>1992-01-15</td>
        </tr>
        <tr>
            <td>10058</td>
            <td>1954-10-01</td>
            <td>Berhard</td>
            <td>McFarlin</td>
            <td>M</td>
            <td>1987-04-13</td>
        </tr>
        <tr>
            <td>10059</td>
            <td>1953-09-19</td>
            <td>Alejandro</td>
            <td>McAlpine</td>
            <td>F</td>
            <td>1991-06-26</td>
        </tr>
        <tr>
            <td>10060</td>
            <td>1961-10-15</td>
            <td>Breannda</td>
            <td>Billingsley</td>
            <td>M</td>
            <td>1987-11-02</td>
        </tr>
        <tr>
            <td>10061</td>
            <td>1962-10-19</td>
            <td>Tse</td>
            <td>Herber</td>
            <td>M</td>
            <td>1985-09-17</td>
        </tr>
        <tr>
            <td>10062</td>
            <td>1961-11-02</td>
            <td>Anoosh</td>
            <td>Peyn</td>
            <td>M</td>
            <td>1991-08-30</td>
        </tr>
        <tr>
            <td>10063</td>
            <td>1952-08-06</td>
            <td>Gino</td>
            <td>Leonhardt</td>
            <td>F</td>
            <td>1989-04-08</td>
        </tr>
        <tr>
            <td>10064</td>
            <td>1959-04-07</td>
            <td>Udi</td>
            <td>Jansch</td>
            <td>M</td>
            <td>1985-11-20</td>
        </tr>
        <tr>
            <td>10065</td>
            <td>1963-04-14</td>
            <td>Satosi</td>
            <td>Awdeh</td>
            <td>M</td>
            <td>1988-05-18</td>
        </tr>
        <tr>
            <td>10066</td>
            <td>1952-11-13</td>
            <td>Kwee</td>
            <td>Schusler</td>
            <td>M</td>
            <td>1986-02-26</td>
        </tr>
        <tr>
            <td>10067</td>
            <td>1953-01-07</td>
            <td>Claudi</td>
            <td>Stavenow</td>
            <td>M</td>
            <td>1987-03-04</td>
        </tr>
        <tr>
            <td>10068</td>
            <td>1962-11-26</td>
            <td>Charlene</td>
            <td>Brattka</td>
            <td>M</td>
            <td>1987-08-07</td>
        </tr>
        <tr>
            <td>10069</td>
            <td>1960-09-06</td>
            <td>Margareta</td>
            <td>Bierman</td>
            <td>F</td>
            <td>1989-11-05</td>
        </tr>
        <tr>
            <td>10070</td>
            <td>1955-08-20</td>
            <td>Reuven</td>
            <td>Garigliano</td>
            <td>M</td>
            <td>1985-10-14</td>
        </tr>
        <tr>
            <td>10071</td>
            <td>1958-01-21</td>
            <td>Hisao</td>
            <td>Lipner</td>
            <td>M</td>
            <td>1987-10-01</td>
        </tr>
        <tr>
            <td>10072</td>
            <td>1952-05-15</td>
            <td>Hironoby</td>
            <td>Sidou</td>
            <td>F</td>
            <td>1988-07-21</td>
        </tr>
        <tr>
            <td>10073</td>
            <td>1954-02-23</td>
            <td>Shir</td>
            <td>McClurg</td>
            <td>M</td>
            <td>1991-12-01</td>
        </tr>
        <tr>
            <td>10074</td>
            <td>1955-08-28</td>
            <td>Mokhtar</td>
            <td>Bernatsky</td>
            <td>F</td>
            <td>1990-08-13</td>
        </tr>
        <tr>
            <td>10075</td>
            <td>1960-03-09</td>
            <td>Gao</td>
            <td>Dolinsky</td>
            <td>F</td>
            <td>1987-03-19</td>
        </tr>
        <tr>
            <td>10076</td>
            <td>1952-06-13</td>
            <td>Erez</td>
            <td>Ritzmann</td>
            <td>F</td>
            <td>1985-07-09</td>
        </tr>
        <tr>
            <td>10077</td>
            <td>1964-04-18</td>
            <td>Mona</td>
            <td>Azuma</td>
            <td>M</td>
            <td>1990-03-02</td>
        </tr>
        <tr>
            <td>10078</td>
            <td>1959-12-25</td>
            <td>Danel</td>
            <td>Mondadori</td>
            <td>F</td>
            <td>1987-05-26</td>
        </tr>
        <tr>
            <td>10079</td>
            <td>1961-10-05</td>
            <td>Kshitij</td>
            <td>Gils</td>
            <td>F</td>
            <td>1986-03-27</td>
        </tr>
        <tr>
            <td>10080</td>
            <td>1957-12-03</td>
            <td>Premal</td>
            <td>Baek</td>
            <td>M</td>
            <td>1985-11-19</td>
        </tr>
        <tr>
            <td>10081</td>
            <td>1960-12-17</td>
            <td>Zhongwei</td>
            <td>Rosen</td>
            <td>M</td>
            <td>1986-10-30</td>
        </tr>
        <tr>
            <td>10082</td>
            <td>1963-09-09</td>
            <td>Parviz</td>
            <td>Lortz</td>
            <td>M</td>
            <td>1990-01-03</td>
        </tr>
        <tr>
            <td>10083</td>
            <td>1959-07-23</td>
            <td>Vishv</td>
            <td>Zockler</td>
            <td>M</td>
            <td>1987-03-31</td>
        </tr>
        <tr>
            <td>10084</td>
            <td>1960-05-25</td>
            <td>Tuval</td>
            <td>Kalloufi</td>
            <td>M</td>
            <td>1995-12-15</td>
        </tr>
        <tr>
            <td>10085</td>
            <td>1962-11-07</td>
            <td>Kenroku</td>
            <td>Malabarba</td>
            <td>M</td>
            <td>1994-04-09</td>
        </tr>
        <tr>
            <td>10086</td>
            <td>1962-11-19</td>
            <td>Somnath</td>
            <td>Foote</td>
            <td>M</td>
            <td>1990-02-16</td>
        </tr>
        <tr>
            <td>10087</td>
            <td>1959-07-23</td>
            <td>Xinglin</td>
            <td>Eugenio</td>
            <td>F</td>
            <td>1986-09-08</td>
        </tr>
        <tr>
            <td>10088</td>
            <td>1954-02-25</td>
            <td>Jungsoon</td>
            <td>Syrzycki</td>
            <td>F</td>
            <td>1988-09-02</td>
        </tr>
        <tr>
            <td>10089</td>
            <td>1963-03-21</td>
            <td>Sudharsan</td>
            <td>Flasterstein</td>
            <td>F</td>
            <td>1986-08-12</td>
        </tr>
        <tr>
            <td>10090</td>
            <td>1961-05-30</td>
            <td>Kendra</td>
            <td>Hofting</td>
            <td>M</td>
            <td>1986-03-14</td>
        </tr>
        <tr>
            <td>10091</td>
            <td>1955-10-04</td>
            <td>Amabile</td>
            <td>Gomatam</td>
            <td>M</td>
            <td>1992-11-18</td>
        </tr>
        <tr>
            <td>10092</td>
            <td>1964-10-18</td>
            <td>Valdiodio</td>
            <td>Niizuma</td>
            <td>F</td>
            <td>1989-09-22</td>
        </tr>
        <tr>
            <td>10093</td>
            <td>1964-06-11</td>
            <td>Sailaja</td>
            <td>Desikan</td>
            <td>M</td>
            <td>1996-11-05</td>
        </tr>
        <tr>
            <td>10094</td>
            <td>1957-05-25</td>
            <td>Arumugam</td>
            <td>Ossenbruggen</td>
            <td>F</td>
            <td>1987-04-18</td>
        </tr>
        <tr>
            <td>10095</td>
            <td>1965-01-03</td>
            <td>Hilari</td>
            <td>Morton</td>
            <td>M</td>
            <td>1986-07-15</td>
        </tr>
        <tr>
            <td>10096</td>
            <td>1954-09-16</td>
            <td>Jayson</td>
            <td>Mandell</td>
            <td>M</td>
            <td>1990-01-14</td>
        </tr>
        <tr>
            <td>10097</td>
            <td>1952-02-27</td>
            <td>Remzi</td>
            <td>Waschkowski</td>
            <td>M</td>
            <td>1990-09-15</td>
        </tr>
        <tr>
            <td>10098</td>
            <td>1961-09-23</td>
            <td>Sreekrishna</td>
            <td>Servieres</td>
            <td>F</td>
            <td>1985-05-13</td>
        </tr>
        <tr>
            <td>10099</td>
            <td>1956-05-25</td>
            <td>Valter</td>
            <td>Sullins</td>
            <td>F</td>
            <td>1988-10-18</td>
        </tr>
        <tr>
            <td>10100</td>
            <td>1953-04-21</td>
            <td>Hironobu</td>
            <td>Haraldson</td>
            <td>F</td>
            <td>1987-09-21</td>
        </tr>
    </tbody>
</table>




```python

```
