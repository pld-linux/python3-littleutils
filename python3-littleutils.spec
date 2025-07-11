#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Small personal collection of Python utility functions
Summary(pl.UTF-8):	Mała osobista kolekcja funkcji narzędziowych dla Pythona
Name:		python3-littleutils
Version:	0.2.4
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/littleutils/
Source0:	https://files.pythonhosted.org/packages/source/l/littleutils/littleutils-%{version}.tar.gz
# Source0-md5:	7c626364bc34403cb12d685ea18306aa
URL:		https://pypi.org/project/littleutils/
BuildRequires:	python3-modules >= 1:3.8
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.8
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Small personal collection of Python utility functions.

%description -l pl.UTF-8
Mała osobista kolekcja funkcji narzędziowych dla Pythona.

%prep
%setup -q -n littleutils-%{version}

%build
%py3_build

%if %{with tests}
%{__python3} littleutils/__init__.py
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py3_sitescriptdir}/littleutils
%{py3_sitescriptdir}/littleutils-%{version}-py*.egg-info
