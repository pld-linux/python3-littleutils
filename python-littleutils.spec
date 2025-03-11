#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Small personal collection of Python utility functions
Summary(pl.UTF-8):	Mała osobista kolekcja funkcji narzędziowych dla Pythona
Name:		python-littleutils
# keep 0.2.2 here for python2 support
Version:	0.2.2
Release:	3
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/littleutils/
Source0:	https://files.pythonhosted.org/packages/source/l/littleutils/littleutils-%{version}.tar.gz
# Source0-md5:	e6199893c6d139c9d9dc1aeac7fa38e0
URL:		https://pypi.org/project/littleutils/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Small personal collection of Python utility functions.

%description -l pl.UTF-8
Mała osobista kolekcja funkcji narzędziowych dla Pythona.

%package -n python3-littleutils
Summary:	Small personal collection of Python utility functions
Summary(pl.UTF-8):	Mała osobista kolekcja funkcji narzędziowych dla Pythona
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-littleutils
Small personal collection of Python utility functions.

%description -n python3-littleutils -l pl.UTF-8
Mała osobista kolekcja funkcji narzędziowych dla Pythona.

%prep
%setup -q -n littleutils-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} littleutils/__init__.py
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} littleutils/__init__.py
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/littleutils
%{py_sitescriptdir}/littleutils-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-littleutils
%defattr(644,root,root,755)
%{py3_sitescriptdir}/littleutils
%{py3_sitescriptdir}/littleutils-%{version}-py*.egg-info
%endif
